import socket

def scan_target(target, ports):
    print(f"\nScanning {target} for open ports...\n")
    
    for port in ports:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            
            if result == 0:
                print(f"[+] Port {port} is OPEN")
            else:
                print(f"[-] Port {port} is closed")

            sock.close()
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")

if __name__ == "__main__":
    target = input("Enter target IP or domain (e.g., scanme.nmap.org): ")
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080]  # Common ports
    scan_target(target, ports)
