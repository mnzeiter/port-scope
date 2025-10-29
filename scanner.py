
import socket
import nmap

target = '127.0.0.1'
ports = range(1, 65536)
open_ports = []

for port in ports : 
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREM)
	sock.settimeout(1)
	result = sock.connect_ex((target, port))
	if result == 0:
		open_ports.append(port)
	sock.close()

nm = nmap.PortScanner()
for port in open_ports:
	nm.scan(target, str(port))
	service = nm[target]['tcp'][port]['name']
	print(f"Port {port} is open. Service : {service} ")
