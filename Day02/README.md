# Day 2: Networking Fundamentals — The Language of the Internet

## Overview

Learned the core networking concepts that form the foundation of SOC analysis: IP addresses, MAC addresses, DNS, DHCP, routers, switches, and essential command-line network tools.

## Topics Covered

- What a computer network is
- IP Addresses (Private vs. Public)
- MAC Addresses
- Routers vs. Switches
- DNS (Domain Name System)
- DHCP (Dynamic Host Configuration Protocol)
- Why networking matters for SOC analysts

## Practical Lab

| Command | Purpose |
|---------|---------|
| `ipconfig` | View network configuration (IP, gateway, subnet mask) |
| `getmac` | View MAC address |
| `ping google.com` | Test connectivity and measure response time |
| `tracert google.com` | Trace the route packets take to reach a destination |
| `nslookup github.com` | Perform DNS lookup to resolve domain to IP |
| `netstat -ano` | View all active network connections and listening ports |

## Mini Project

`network_info.py` — A Python script that displays:
- Computer hostname
- Local IP address
- MAC address
- Current date and time
- Operating system info

## Files

```
Day02/
├── README.md           <-- You are here
├── notes.md            <-- Assignment answers & lab notes
├── network_info.py     <-- Mini project script
└── Screenshots       <-- Command output screenshots
```

## Key Takeaway

> Over 70% of SOC alerts involve networking. Understanding how devices communicate is not optional — it's the single most important technical skill for a SOC analyst.
