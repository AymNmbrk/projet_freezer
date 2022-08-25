#import ftplib
from ftplib import FTP
import os
import socket             
import glob
import sys
import re




titre= sys.argv[1]

titre = titre.capitalize()

print("je n'ai pas la musique localement")

s = socket.socket()         

port = 12136


s.connect(('10.125.24.53', port)) 

firstmsg=s.recv(1024).decode()
print(firstmsg)

s.send(str("GET "+titre).encode())

rep=s.recv(1024).decode()


results=re.search("OK (.*)",rep)

music=results.groups()[0]

print("################")

print(rep)

ftp = FTP('10.125.24.53')


username="aymn"
password='1234'
ftp.login(user=username, passwd=password)

os.chdir("/home/waleed/Music/")
with open(music, 'wb') as fp:
    ftp.retrbinary('RETR '+str(music), fp.write)

os.system(f"vlc '/home/waleed/Music/"+music+"'")

ftp.quit()

s.close()
# revoir la condition, elle ne fonctionne pas
#liste_musiques = glob.glob(f"/home/waleed/Music/*{titre}*")
#
#print(liste_musiques)
#if len(liste_musiques) != 0 :
#    print(liste_musiques[0])
#    os.system(f"vlc '"+liste_musiques[0]+"'")
#    sys.exit()
    

# si tu l'as pas localement
  


# il faut demander au serveur ayman si il a la musique

## attendre la reponse du serveur ayman

## le serveur va forcement te dire OK c'est bon
## tu "OK"+"chemin musique"
#
## on se connecte en FTP au serveur ayman


##
##
### en fonction du "chemin musique" on recupere en FTP la musqiue voulue
#ftp.retriv(titre)
##
##
### la musique est téléchargée dans ~/Musics/
#filename = titre
##
#with open(filename, "wb") as file:
##
#ftp.retrbinary(f"RETR {filename}", file.write)
##
### ensuite elle est lue avec VLC
#os.system(f"vlc /home/waleed/Music/*{titre}*")
##
