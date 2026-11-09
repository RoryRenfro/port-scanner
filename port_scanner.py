import socket
import ipaddress

COMMON_PORTS = {
    21: "FTP", 22: "SSH", 23: "Telnet", 25: "SMTP (email)", 53: "DNS",
    80: "HTTP", 110: "POP3 (email)", 135: "Windows RPC", 139: "NetBIOS",
    143: "IMAP (email)", 443: "HTTPS", 445: "SMB (file sharing)",
    3306: "MySQL", 3389: "Remote Desktop", 8000: "HTTP (alternate)",
    8080: "HTTP (alternate)",
}


def scan_port(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(0.5)
        result = s.connect_ex((host, port))
        return result == 0

def get_target():
    while True:

        target =  input("What IP or website would you like to scan... ").strip()
        try:
            ipaddress.ip_address(target)
            host = target
            return target
        except ValueError:
            try:
                host = socket.gethostbyname(target)
                print(f"{target} resovles to {host}")
                return host
            except socket.gaierror:
                print("That's not a valid IP adress or website. Please try again (example: 192.168.1.50).")
def run_scan(host):
    print(f"Scanning {host}...\n")

    open_ports = []
    for port, service in COMMON_PORTS.items():
        if scan_port(host, port):
            print(f"Port {port:<5} OPEN     {service}")
            open_ports.append(port)

    print(f"\nScan Complete. {len(open_ports)} open port(s) found.")

while True:
    host = get_target()
    run_scan(host)

    again = input("Scan another target? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break