#!/bin/bash

user=$1
music=$2

isInFile=$(ls /home/aymn/Music | grep -c -i "$music")
echo $isInFile
if [[ $isInFile -eq 0 ]] 
then
   cd /home/$user/Music
   down=$(spotdl "$music")
   echo "Music $music Dowloaded"
   echo "$down" > /home/$user/Music/file2
   #cat file2
   track=$(cat file2 | head -n2 | tail -n1 | cut -d'"' -f2)
   track="$track".mp3
   echo "$track" > file
   #echo "$track"
   
elif [[ $isInFile -eq 1 ]] 
then
   echo "################"
   track=$(ls /home/aymn/Music | grep -i "$music")
   echo "$track" > /home/aymn/Music/file
   exit 2
fi

