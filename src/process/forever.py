#!/usr/bin/python
from subprocess import Popen
from colorama import init, Fore
init()

while True:
    print(Fore.MAGENTA + 'Iniciando o bot em loop infinito!' + Fore.RESET)
    p = Popen("cd - && cd - && python3 index.py", shell=True)
    p.wait()
