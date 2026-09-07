
import re
from collections import defaultdict

LOG_FILE = "scan_log.txt"
PORT_THRESHOLD = 5

HIGH_RISK_PORTS = {"21": "FTP", "22": "SSH", "23":  "Telnet", "3389": "RDP", "445": "SMB"}

pattern = re.compile(r"(\d+\.\d+\.\d+\.\d+) -> port (\d+)")

ip_ports = defaultdict(set)

with open(LOG_FILE, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            port = match.group(2)
            ip_ports[ip].add(port)

print("POrt scan detection summary:")
for ip, ports in ip_ports.items():
    flag = " <- POSSIBLE PORT SCAN" if len(ports) >= PORT_THRESHOLD else ""
    print(f"{ip}: contacted {len(ports)} distinct ports{flag}")
    if len(ports) >=PORT_THRESHOLD:
        print(f" ports: {', '.join(sorted(ports))}")
        risky_hit = [f"{p} ({HIGH_RISK_PORTS[p]})" for p in ports if p in  HIGH_RISK_PORTS]
        if risky_hit:
            print(f" High-risk ports connected: {', '.join(risky_hit)}")


