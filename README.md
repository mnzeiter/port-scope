
# 🔍 PortScope – Python Port Scanner

A Python-based tool that scans all TCP ports on a target IP address and identifies open ports and their services using socket and nmap.

## 🔧 Features
- Full TCP port scan (1–65535)
- Fast socket-based connection check
- Service detection using nmap
- Console output of open ports and services

## 🛠 Tech Stack
- Python 3.x
- socket (built-in)
- python-nmap (library)
- nmap (system dependency)

## 🚀 Usage
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install python-nmap
   ```
3. Make sure `nmap` is installed on your system
4. Run the script:
   ```bash
   python scanner.py
   ```

## 📁 File Structure
```
scanner.py
requirements.txt
README.md
```

## ⚠️ Disclaimer
This tool is for educational and authorized testing purposes only. Do not scan networks without permission.
