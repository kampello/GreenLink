import  os, getpass, msvcrt
from colorama import Fore, Back, Style, init

#limpar tela funcao
clear = lambda: os.system('clear')
#logo da greenLink
logo = lambda: print('''\033[92m
  _____                     _      _       _    
 / ____|                   | |    (_)     | |   
| |  __ _ __ ___  ___ _ __ | |     _ _ __ | | __
| | |_ | '__/ _ \/ _ \ '_ \| |    | | '_ \| |/ /
| |__| | | |  __/  __/ | | | |____| | | | |   < 
 \_____|_|  \___|\___|_| |_|______|_|_| |_|_|\_\\
\033[33m      we love broccoli™
\033[0m''')



#funcao feita pra que quando o utlizador escreva a senha apareca '*' em vez de a senha atual

def input_senha(prompt="Senha: "):
    print(prompt, end='', flush=True)
    senha = ''
    while True:
        ch = msvcrt.getch()
        if ch == b'\r':  # Enter
            print('')
            break
        elif ch == b'\x08':  # Backspace
            if len(senha) > 0:
                senha = senha[:-1]
                print('\b \b', end='', flush=True)
        elif ch == b'\x03':  # Ctrl+C
            raise KeyboardInterrupt
        else:
            senha += ch.decode('utf-8', errors='ignore')
            print('*', end='', flush=True)
    return senha


