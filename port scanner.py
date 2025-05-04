import socket
import sys

def scan_ports(ip, start_port, end_port):
    print(f"\nScanning {ip} from port {start_port} to {end_port}...\n")
    open_ports = []

    for port in range(start_port, end_port + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                sock.settimeout(0.5)
                result = sock.connect_ex((ip, port))
                if result == 0:
                    open_ports.append(port)
        except socket.error as e:
            print(f"Error scanning port {port}: {e}")
            continue

    if open_ports:
        print("Open ports found:")
        for port in open_ports:
            print(f"Port {port} is open")
    else:
        print("No open ports found.")

def get_valid_ip():
    while True:
        ip = input("Enter target IP address: ")
        try:
            socket.inet_aton(ip)
            return ip
        except socket.error:
            print("Invalid IP address. Please try again.")

def get_valid_port(prompt):
    while True:
        try:
            port = int(input(prompt))
            if 1 <= port <= 65535:
                return port
            else:
                print("Port must be between 1 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    print("=== Simple Port Scanner ===")
    target_ip = get_valid_ip()
    start_port = get_valid_port("Enter start port: ")
    end_port = get_valid_port("Enter end port: ")

    if start_port > end_port:
        print("Start port cannot be greater than end port.")
        sys.exit(1)

    scan_ports(target_ip, start_port, end_port)
