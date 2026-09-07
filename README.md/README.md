
# Cyber Security Portfolio

A collection of Python-based security tools built while studying for CompTIA Security+ and preparing for a career in cyber security. Built and tested on Kali Linux, with two of the three projects validated against real attack traffic generated in a home lab (Kali attacker VM + Metasploitable2 target VM).

## Projects

### 1. Password Strength Checker
`password-checker/password_checker.py`

A password security analyser available as both a CLI tool and a Tkinter GUI. Checks a password against multiple security criteria and returns a strength rating with specific, actionable recommendations.

**Checks performed:**
- Minimum length requirement
- Uppercase and lowercase character presence
- Number presence
- Special character presence
- Common password detection (checked against known weak passwords)
- Predictable pattern detection (e.g. `Password123!`)
- Overall complexity score (X/5) and strength rating (Weak → Very Strong)

**Security relevance:** Demonstrates that character complexity alone doesn't guarantee a secure password — a password can satisfy every complexity rule while still being predictable and easy to guess.

### 2. SSH Brute-Force Detector
`brute-force-lab/brute-force-lab.py`

A log analysis tool that parses SSH authentication logs and flags source IPs responsible for excessive failed login attempts.

**How it was tested:** Ran a real brute-force attack using Medusa against SSH on a Metasploitable2 VM, targeting a single username against a 5-password wordlist. The script then parsed the target's own `auth.log`, independently confirming the failed attempts recorded by the system under attack — not just relying on the attacking tool's own output.

**Output:** Tallies failed attempts per source IP and flags any IP exceeding a configurable threshold as suspicious.

### 3. Port Scan Detector
`portscan-detector/portscan_detector.py`

A network traffic analysis tool that detects port scanning activity by identifying source IPs that contact an unusually high number of distinct destination ports.

**How it was tested:** Captured live network traffic with `tcpdump` while running an `nmap` scan from Kali against a Metasploitable2 target. Filtered the capture for SYN packets — the first packet of any TCP handshake, and the clearest signal of a port scan — using `tcpdump` and `awk`, then fed the result into the Python detector.

**Output:** Flags any IP contacting 5+ distinct ports as a possible port scan, lists the exact ports touched, and cross-references them against a list of high-risk services (SSH, FTP, Telnet, RDP, SMB).

## Tech stack
- Python 3
- Tkinter (GUI)
- tcpdump, nmap, Medusa (traffic generation and capture)
- Kali Linux, Metasploitable2 (VMware lab environment)
