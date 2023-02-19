#!/bin/bash

if command -v python3 &> /dev/null; then
    echo "Python 3 já está instalado"
else
    echo "Python 3 não está instalado. Instalando..."
    sudo apt update
    sudo apt install -y python3
fi

python3 net_py_tools.py