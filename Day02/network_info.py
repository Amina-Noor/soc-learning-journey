"""
SOC Roadmap - Day 2: Network Information Collector
Displays hostname, local IP, MAC address, and current date/time.
"""

import socket
import datetime
import uuid
import platform


def get_hostname():
    """Returns the computer's hostname."""
    return socket.gethostname()


def get_local_ip():
    """Returns the local IP address by creating a dummy socket connection."""
    try:
        # Creates a socket to determine the local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # Connect to a public DNS server (doesn't actually send data)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception as e:
        return f"Could not determine local IP: {e}"


def get_mac_address():
    """Returns the MAC address of the primary network interface."""
    mac = uuid.getnode()
    # Format as AA-BB-CC-DD-EE-FF
    mac_formatted = "-".join(
        f"{(mac >> elements) & 0xFF:02X}" for elements in range(0, 8 * 6, 8)[::-1]
    )
    return mac_formatted


def get_current_datetime():
    """Returns the current date and time."""
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_os_info():
    """Returns the operating system information."""
    return f"{platform.system()} {platform.release()}"


def main():
    print("=" * 45)
    print("   NETWORK INFORMATION COLLECTOR")
    print("   SOC Roadmap - Day 2")
    print("=" * 45)

    print(f"\n  Hostname     : {get_hostname()}")
    print(f"  Local IP     : {get_local_ip()}")
    print(f"  MAC Address  : {get_mac_address()}")
    print(f"  Date & Time  : {get_current_datetime()}")
    print(f"  OS           : {get_os_info()}")

    print("\n" + "=" * 45)


if __name__ == "__main__":
    main()