import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """Attempts to connect to the specified port on the target IP address."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(1)  # Set timeout for socket connection
        result = sock.connect_ex((ip, port))
        return port, result == 0  # Return port and whether it's open

def port_scanner(ip, start_port, end_port):
    """Scans a range of ports on the given IP address."""
    print(f"Scanning {ip} from port {start_port} to {end_port}...")
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, ip, port): port for port in range(start_port, end_port + 1)}
        for future in futures:
            port, is_open = future.result()
            if is_open:
                print(f"Port {port} is open!")

if __name__ == "__main__":
    target_ip = input("Enter target IP address: ")
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    
    port_scanner(target_ip, start_port, end_port)
