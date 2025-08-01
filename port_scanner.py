import socket
host = "localhost"
for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.1)
    if s.connect_ex((host, port)) == 0:
        print(f"✅ Open port: {port}")
    s.close()

# Run with "python port_scanner.py"
