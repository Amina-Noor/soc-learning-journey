# Day 3 - TCP, UDP, Ports & Network Port Reference Tool

## Overview

Day 3 of the SOC Roadmap focuses on understanding the fundamental networking concepts that form the backbone of Security Operations Center work: how data travels across networks, the TCP and UDP transport protocols, port numbers, and the TCP three-way handshake.

## Files

| File               | Description                                                        |
| ------------------ | ------------------------------------------------------------------ |
| `port_reference.py` | Interactive CLI tool to look up port numbers and their services    |
| `notes.md`         | Detailed study notes covering all Day 3 topics                     |
| `assignment_answers.md` | Answers to all 10 assignment questions                        |
| `interview_answers.md`  | Answers to all 8 interview questions                          |
| `README.md`        | This file                                                          |

## Topics Covered

- How data travels from your computer to a website (packets, routing)
- What TCP is (reliable, connection-oriented, ordered delivery)
- What UDP is (fast, connectionless, no delivery guarantee)
- TCP vs UDP comparison
- What ports are and why they matter
- Common port numbers every SOC analyst must know
- The TCP three-way handshake (SYN → SYN-ACK → ACK)

## How to Use port_reference.py

Run the script:

```bash
python port_reference.py
```

### Features

- Enter any port number (0-65535) to see its service, protocol, and description
- Type `list` to display all known ports in a table
- Type `quit` to exit the program
- Handles invalid input gracefully (non-numbers, out-of-range ports)

### Example

```
Enter Port: 443

========================================
  Port 443
========================================
  Service:      HTTPS
  Protocol:     TCP
  Description:  Secure Web Traffic - Encrypted web browsing
========================================
```

## Technologies

- Python 3
- No external dependencies required
```
