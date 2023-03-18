#!/bin/bash

curl https://www.vulnhub.com/ > log.log 2>/dev/null

echo "Estas son las máquinas más recientes: "

cat log.log | grep 'href="/entry/' | tr -d '#' | sed 's/entry/ /' | awk '{print $3}' | tr -d '/' | sed 's/download/ /' | sed 's/"/ /' | tr -d '>' | tr -d ' ' | uniq

cat log.log | grep noob >/dev/null

if [ "$(echo $?)" == "0" ]; then 
   echo "No hay máquinas nuevas"
else
   echo "Se ha encontrado una máquina nueva"
fi

rm log.log
