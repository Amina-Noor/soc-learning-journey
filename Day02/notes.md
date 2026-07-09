# SOC Roadmap - Day 2: Networking Fundamentals

## Assignment Answers

### 1. What is an IP address?

An IP (Internet Protocol) address is a unique numerical label assigned to every device connected to a computer network. It serves two main purposes: identifying the host or network interface, and providing the location of the device in the network so data can be routed to it. Think of it like a postal address — without it, data sent over the internet wouldn't know where to go. IP addresses come in two versions: IPv4 (e.g., 192.168.1.10) which uses 32-bit addressing, and IPv6 (e.g., 2001:0db8:85a3::8a2e:0370:7334) which uses 128-bit addressing to accommodate the growing number of internet-connected devices.

### 2. What is the difference between a public IP and a private IP?

A **private IP** is used within a local network (home, office, or internal network) and is not directly reachable from the internet. Private IP ranges are defined by RFC 1918: 10.0.0.0/8, 172.16.0.0/12, and 192.168.0.0/16. Multiple networks can use the same private IPs simultaneously because they are not globally unique. A **public IP** is assigned by an ISP and is globally unique — it's the address the entire internet uses to identify your network. Your router performs NAT (Network Address Translation) to map private IPs to the public IP when devices communicate externally. In a SOC context, a public IP in an alert often means the threat is external, while a private IP suggests internal lateral movement.

### 3. What is a MAC address?

A MAC (Media Access Control) address is a 48-bit (6-byte) hardware address permanently assigned to a network interface card (NIC) by the manufacturer. It's typically displayed in hexadecimal format like `00-1A-2B-3C-4D-5E`. Unlike an IP address which is logical and changes based on the network, a MAC address is burned into the hardware (though it can be spoofed). The first three octets (OUI — Organizationally Unique Identifier) identify the manufacturer, and the last three identify the specific device. In SOC work, MAC addresses are useful for identifying devices on a local network, detecting MAC spoofing attacks, and tracing activity to specific hardware.

### 4. What does a router do?

A router connects different networks together and directs (routes) data packets between them. It operates at Layer 3 (Network Layer) of the OSI model and uses IP addresses to make forwarding decisions. When you send data to a website, your router determines the best path for that data to reach its destination across the internet. Routers also perform NAT (translating private IPs to public IPs), run firewalls to filter traffic, and maintain routing tables that map network destinations. In a home setup, your Wi-Fi router connects your local network (LAN) to the ISP's network (WAN). For SOC analysts, routers are critical because they log traffic, enforce access controls, and their misconfigurations are common attack vectors.

### 5. What does a switch do?

A switch connects devices within the **same local network** (LAN) and forwards data frames to the correct device using MAC addresses. It operates at Layer 2 (Data Link Layer) of the OSI model. Unlike an old hub that broadcasts data to all ports, a switch maintains a MAC address table and only sends data to the specific port where the destination device is connected. This makes network communication efficient and reduces unnecessary traffic. In enterprise environments, managed switches also support VLANs (Virtual LANs), port security, and traffic monitoring — all of which are relevant to SOC analysts investigating internal network activity.

### 6. What is DNS?

DNS (Domain Name System) is the internet's phone book. It translates human-readable domain names (like `google.com`) into machine-readable IP addresses (like `142.250.190.14`). When you type a URL into your browser, a DNS query is sent to a DNS resolver (usually provided by your ISP or a service like Google's 8.8.8.8), which looks up the corresponding IP address. DNS uses a hierarchical system: root servers → TLD servers (like .com) → authoritative name servers for the specific domain. In a SOC, DNS is crucial because attackers use techniques like DNS tunneling (hiding data in DNS queries), DNS spoofing (redirecting traffic to malicious sites), and domain generation algorithms (DGAs) to evade detection. Monitoring DNS logs is a daily SOC task.

### 7. What is DHCP?

DHCP (Dynamic Host Configuration Protocol) automatically assigns network configuration to devices when they join a network. Without DHCP, you'd have to manually configure every device with an IP address, subnet mask, default gateway, and DNS server. When a device connects, it sends a DHCP Discover broadcast, a DHCP server responds with an Offer, the device sends a Request, and the server sends an Acknowledgment (this is called the DORA process). The lease is temporary — it expires and must be renewed. In security, DHCP spoofing is an attack where a rogue DHCP server assigns malicious configurations (like a fake DNS server) to redirect traffic. SOC analysts monitor DHCP logs to detect unauthorized devices, IP conflicts, and rogue DHCP servers on the network.

### 8. Why is networking important for a SOC Analyst?

Networking is the foundation of almost everything a SOC analyst does. More than 70% of security alerts involve network activity. When an alert fires — whether it's a failed login, suspicious outbound connection, or malware communication — you need networking knowledge to investigate it effectively. You need to understand IP addresses to determine if a threat is internal or external. You need to know ports and protocols to understand what kind of communication is happening. You need DNS knowledge to investigate phishing domains and DNS-based attacks. You need to read routing logs, firewall rules, and packet captures. Without networking fundamentals, you cannot triage alerts, write detection rules, or communicate findings to network engineers. It is the single most important technical skill for SOC work.

---

## Practical Lab Notes

### ipconfig Output

### getmac Output

### ping google.com Output

### tracert google.com Output

### nslookup github.com Output

### netstat -ano Output

All commands above, their screenshots are added to the Screenshot Folder.

---

## Optional Challenge: Common Ports

| Port | Service       | What It's Used For |
|------|---------------|--------------------|
| 20   | FTP (Data)    | Transfers file data between client and server in FTP sessions. |
| 21   | FTP (Control) | Sends FTP commands (login, directory listing, file requests) between client and server. |
| 22   | SSH           | Provides encrypted remote shell access and secure file transfers (SCP/SFTP). |
| 23   | Telnet        | Provides unencrypted remote terminal access — considered insecure and rarely used today. |
| 25   | SMTP          | Sends email between mail servers and from email clients to outgoing mail servers. |
| 53   | DNS           | Resolves domain names to IP addresses and handles DNS queries and responses. |
| 80   | HTTP          | Serves unencrypted web pages and web application traffic. |
| 110  | POP3          | Retrieves email from a mail server to a client (downloads and often deletes from server). |
| 143  | IMAP          | Retrieves and syncs email between client and server without deleting from the server. |
| 443  | HTTPS         | Serves encrypted web traffic using TLS/SSL — the secure version of HTTP. |

---

## Key Takeaways

- Every device on a network has both an IP address (logical, changes) and a MAC address (physical, usually fixed).
- Routers connect **different** networks; switches connect devices **within** the same network.
- DNS translates domain names to IPs; DHCP automatically assigns network settings.
- Over 70% of SOC alerts involve networking — this knowledge is non-negotiable for analysts.