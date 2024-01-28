import socket
for x in range(1,255):
    ip = "192.168.77.%d" % x
    print(ip)
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.05)
        s.connect((ip, 22))
        s.send("GET / HTTP/1.1\r\nHost:"+ip+"\r\n\r\n")
        data = s.recv(1024)
        print(data)
        s.close()
    except Exception as e:
        print(e)