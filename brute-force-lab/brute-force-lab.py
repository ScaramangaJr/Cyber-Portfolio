


import re
from collections import defaultdict


LOG_FILE = "target_auth.log"
THRESHOLD = 1

pattern = re.compile(r"Failed password for .* from (\d+\.\d+\.\d+\.\d+)")

attempts = defaultdict(int)

with open(LOG_FILE, "r") as f:
    for line in f:
        match = pattern.search(line)
        if match:
            ip = match.group(1)
            attempts[ip] += 1

print("Failed login summary:")
for ip, count in attempts.items():
    flag = " <-- SUSPICIOUS" if count >=THRESHOLD else ""
    print (f"{ip}: {count} failed attempts{flag}")
