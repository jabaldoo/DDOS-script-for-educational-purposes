import socket
import threading
import time
import argparse
import logging
import os
import sys
import random

# Configure logging
logging.basicConfig(
    filename='network_test.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filemode='w'
)

def display_banner():
    """Display ASCII art banner with clearing screen"""
    banner = r"""
    ░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░ ░▒▓███████▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
    ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░      ░▒▓█▓▒░
    ░▒▓███████▓▒░░▒▓███████▓▒░ ░▒▓██████▓▒░░▒▓███████▓▒░
    """
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)

def generate_fake_headers():
    """Generate random HTTP headers for traffic simulation"""
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
    ]
    return (
        f"GET /{random.randint(0, 1000)} HTTP/1.1\r\n"
        f"Host: {random.choice(['google.com', 'example.com', 'test.org'])}\r\n"
        f"User-Agent: {random.choice(user_agents)}\r\n"
        "Connection: keep-alive\r\n\r\n"
    ).encode('utf-8')

def network_test(target_ip, target_port, duration):
    """Simulate network traffic with timeout handling"""
    end_time = time.time() + duration
    try:
        while time.time() < end_time:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(3)
                s.connect((target_ip, target_port))
                s.sendall(generate_fake_headers())
                logging.info(f"Connection established to {target_ip}:{target_port}")
                time.sleep(0.5)  # Maintain connection briefly

    except (socket.timeout, ConnectionRefusedError) as e:
        logging.warning(f"Connection error: {str(e)}")
    except Exception as e:
        logging.error(f"Unexpected error: {str(e)}")

def start_test(target_ip, target_port, num_threads, duration=60):
    """Manage test threads with controlled execution time"""
    threads = []
    print(f"\nStarting network test on {target_ip}:{target_port}")
    print(f"Threads: {num_threads} | Duration: {duration}s")
    print("Press Ctrl+C to stop the test\n")

    try:
        for _ in range(num_threads):
            thread = threading.Thread(
                target=network_test,
                args=(target_ip, target_port, duration)
            )
            thread.daemon = True
            thread.start()
            threads.append(thread)

        for thread in threads:
            thread.join()

    except KeyboardInterrupt:
        print("\nTest interrupted by user")
        sys.exit(0)

def validate_input(target_ip, target_port):
    """Validate user input parameters"""
    try:
        socket.inet_aton(target_ip)
        if not (1 <= target_port <= 65535):
            raise ValueError("Invalid port number")
    except socket.error:
        raise ValueError("Invalid IP address format")
        
def main():
    display_banner()
    
    print("""
    NETWORK TESTING TOOL [EDUCATIONAL USE ONLY]
    ------------------------------------------
    This tool simulates network traffic for testing purposes.
    Use only on systems you have explicit permission to test.
    Improper use may violate laws and network policies.
    """)

    try:
        target_ip = input("Target IP: ").strip()
        target_port = int(input("Target port: ").strip())
        validate_input(target_ip, target_port)
        
        num_threads = int(input("Threads (1-1000): ").strip() or 10)
        num_threads = max(1, min(num_threads, 1000))  # Limit threads
        
        duration = int(input("Test duration (seconds): ").strip() or 60)

        start_test(target_ip, target_port, num_threads, duration)
        print("\nTest completed successfully")

    except ValueError as e:
        print(f"\nError: {str(e)}")
        sys.exit(1)
    except Exception as e:
        print(f"\nCritical error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
