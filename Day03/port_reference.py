"""
Day 3 - SOC Roadmap
Network Port Reference Tool

This program asks the user to enter a port number and displays information about the service, protocol, and description.

"""

# Port database using a dictionary (Optional Challenge approach)
ports = {
    20: {
        "service": "FTP (Data)",
        "protocol": "TCP",
        "description": "File Transfer Protocol - Data transfer"
    },
    21: {
        "service": "FTP (Control)",
        "protocol": "TCP",
        "description": "File Transfer Protocol - Control commands"
    },
    22: {
        "service": "SSH",
        "protocol": "TCP",
        "description": "Secure Shell - Secure remote login"
    },
    23: {
        "service": "Telnet",
        "protocol": "TCP",
        "description": "Telnet - Unencrypted remote login (insecure)"
    },
    25: {
        "service": "SMTP",
        "protocol": "TCP",
        "description": "Simple Mail Transfer Protocol - Email sending"
    },
    53: {
        "service": "DNS",
        "protocol": "TCP/UDP",
        "description": "Domain Name System - Resolves domain names to IPs"
    },
    67: {
        "service": "DHCP Server",
        "protocol": "UDP",
        "description": "Dynamic Host Configuration Protocol - Server side"
    },
    68: {
        "service": "DHCP Client",
        "protocol": "UDP",
        "description": "Dynamic Host Configuration Protocol - Client side"
    },
    80: {
        "service": "HTTP",
        "protocol": "TCP",
        "description": "Hypertext Transfer Protocol - Web traffic (unencrypted)"
    },
    110: {
        "service": "POP3",
        "protocol": "TCP",
        "description": "Post Office Protocol v3 - Email retrieval"
    },
    143: {
        "service": "IMAP",
        "protocol": "TCP",
        "description": "Internet Message Access Protocol - Email access"
    },
    443: {
        "service": "HTTPS",
        "protocol": "TCP",
        "description": "Secure Web Traffic - Encrypted web browsing"
    },
    3389: {
        "service": "RDP",
        "protocol": "TCP",
        "description": "Remote Desktop Protocol - Remote Desktop connection"
    }
}


def lookup_port(port_number):
    """Look up a port number and return its information."""
    port_number = int(port_number)

    if port_number in ports:
        info = ports[port_number]
        print(f"\n{'=' * 40}")
        print(f"  Port {port_number}")
        print(f"{'=' * 40}")
        print(f"  Service:      {info['service']}")
        print(f"  Protocol:     {info['protocol']}")
        print(f"  Description:  {info['description']}")
        print(f"{'=' * 40}\n")
    else:
        print(f"\n  Unknown or custom port.\n")


def main():
    """Main program loop."""
    print("=" * 40)
    print("   Network Port Reference Tool")
    print("   SOC Roadmap - Day 3")
    print("=" * 40)
    print("\nType 'quit' or 'q' to exit.")
    print("Type 'list' or 'l' to show all known ports.\n")

    while True:
        user_input = input("Enter Port: ").strip()

        # Exit condition
        if user_input.lower() in ("quit", "q"):
            print("\nGoodbye!\n")
            break

        # List all ports
        if user_input.lower() in ("list", "l"):
            print(f"\n{'Port':<8} {'Service':<20} {'Protocol':<10} {'Description'}")
            print("-" * 75)
            for port_num, info in sorted(ports.items()):
                print(f"{port_num:<8} {info['service']:<20} {info['protocol']:<10} {info['description']}")
            print()
            continue

        # Validate input is a number
        try:
            port_num = int(user_input)
        except ValueError:
            print(f"\n  Invalid input. Please enter a number or 'quit'.\n")
            continue

        # Valid port range check
        if port_num < 0 or port_num > 65535:
            print(f"\n  Port number must be between 0 and 65535.\n")
            continue

        # Look up the port
        lookup_port(port_num)


if __name__ == "__main__":
    main()