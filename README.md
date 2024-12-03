### 🚀 DDoS Simulation Script (Educational Purpose)

A Python-based script to simulate Denial-of-Service (DoS) attacks in a controlled environment such as a home lab. This tool is designed to help understand the effects of network stress testing and improve your knowledge of network programming.
⚠️ Disclaimer

This script is strictly for educational purposes. Misuse of this tool to attack servers without authorization is illegal and unethical. The author is not responsible for any misuse or consequences arising from unauthorized use.
📋 Features

    🌐 Customizable Target: Specify the target IP address and port.
    🧵 Multi-threaded: Simulates concurrent requests using threads.
    🛠️ Configurable Settings: Adjust the number of threads for testing.
    📂 Easy-to-Understand: Clean and modular Python code with helpful comments.

### 🛠️ Requirements

    Python 3.6 or higher
    Basic understanding of Python and networking
    A controlled testing environment (e.g., a local server or home lab)

📦 Installation

    Clone this repository:

git clone https://github.com/your-username/ddos-simulation.git
cd ddos-simulation

Ensure Python is installed:

python --version

Install any required libraries (though none are needed for this script):

    pip install -r requirements.txt

### 🚀 Usage

    Run the script:

python ddos_simulation.py

Provide inputs:

    Enter the target IP address (e.g., 192.168.1.1).
    Enter the target port (e.g., 80 for HTTP, 443 for HTTPS).
    Specify the number of threads (e.g., 10).

Example Input:

Enter the IP address of the target (e.g., 192.168.1.1): 192.168.1.100
Enter the port number of the target (e.g., 80): 80
Enter the number of threads: 10

Monitor Output: Observe the logs as threads send requests to the target.