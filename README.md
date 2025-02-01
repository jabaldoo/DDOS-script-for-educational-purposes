# DDOS Script for Educational Purposes

This is a simple Python script designed to simulate a **Distributed Denial of Service (DDOS)** attack for **educational purposes only**. It demonstrates how a basic DDOS attack works by sending multiple TCP connections to a target IP and port.

**Disclaimer**: This script is intended for educational and ethical use only. Do not use it for illegal or malicious activities. The author is not responsible for any misuse of this script.

# Preview💻

[Screenshot] 
---

## Features
- **Multi-threading**: Simulates multiple connections simultaneously.
- **Rate Limiting**: Controls the number of requests per second.
- **Logging**: Logs connection attempts and errors to a file (`ddos.log`).
- **User Input**: Prompts the user for target IP, port, number of threads, and rate limit.
- **Banner Display**: Displays a custom banner when the script is launched.

---

## Prerequisites
- Python 3.x
- `argparse`, `logging`, `socket`, `threading`, and `time` modules (included in Python's standard library).

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/jabaldoo/DDOS-script-for-educational-purposes.git
   cd DDOS-script-for-educational-purposes