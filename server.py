import socket
import os 
import re

s = socket.socket()
ip = '10.125.24.53'
port = 12136
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((ip, port))
s.listen(5)
c, addr = s.accept()
print("Connexion from:", addr)

msg = "WE ARE CONNECTED"
c.send(msg.encode())


#os.system("bash mainscript.sh")
#if c.recv(1024) == "2":
#    os.system("ftp -inv '"+ip+"'")
#    os.system("user $user")
#    os.system("cd Music")
#    os.system("ls -c")
#    os.system("lcd /home/aymn/Music")
#    os.system("mget *") 
#    os.system("quit")

msg = c.recv(1024).decode()

# GET kiki

results=re.search("GET (.*)",msg)


music=results.groups()[0]
print(music)


print("CALLING MAINSCRIPT")
os.system("bash mainscript.sh aymn "+music+"")


with open("/home/aymn/Music/file",'r') as f:
    data=f.readlines()

lastfile=data[-1]

c.send(str("OK "+lastfile).encode())

c.close()
s.close()

# ok = "OK"
# chemin = "/home/aymn/Music"
# c.send(ok.encode())
# c.send(chemin.encode())
