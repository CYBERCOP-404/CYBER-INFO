# import section Start
import os 
from time import sleep
import sys
# import section end
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
# ANIMATION SECTION 
animation = ["[■□□□□□□□□□] 10%", "[■■□□□□□□□□] 20%", "[■■■□□□□□□□] 30%", "[■■■■□□□□□□] 40%", "[■■■■■□□□□□] 50%", "[■■■■■■□□□□] 60%", "[■■■■■■■□□□] 70%", "[■■■■■■■■□□] 80%", "[■■■■■■■■■□] 90%", "[■■■■■■■■■■] 100%"]
def anima(animation):
    for i in range(len(animation)):
        sleep(0.5)
        sys.stdout.write("\r[😊] PREPARING... " + animation[i % len(animation)])
        sys.stdout.flush()
BANNER='''\033[0;32m
 $$$$$$\ $$\     $$\ $$$$$$$\  $$$$$$$$\ $$$$$$$\ 
$$  __$$  $$\   $$  |$$  __$$\ $$  _____|$$  __$$\  
$$ /  \__|\$$\ $$  / $$ |  $$ |$$ |      $$ |  $$ | 
$$ |       \$$$$  /  $$$$$$$\ |$$$$$\    $$$$$$$  |
$$ |        \$$  /   $$  __$$\ $$  __|   $$  __$$< 
$$ |  $$\    $$ |    $$ |  $$ |$$ |      $$ |  $$ |  
\$$$$$$  |   $$ |    $$$$$$$  |$$$$$$$$\ $$ |  $$ |  
 \______/    \__|    \_______/ \033[0;31m PHONE VERSON >2.5.2
\033[1;39m ┏━━━━━━━━━━━━━━━━━━━\033[38;5;46m𝗞𝗜𝗡𝗚\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━━┓
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙉𝘼𝙈𝙀\033[1;34m       : [★]  CYBER COP BANGLADESH\033[1;39m ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[1;34m   : [★]  CYBER COP\033[1;39m            ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙂𝙄𝙏𝙃𝙐𝘽\033[1;34m     : [★]  CYBERCOP-404\033[1;39m         ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙍𝙄𝙇𝙄𝙂𝙀𝙎𝙃𝙊𝙉\033[1;34m : [★]  𝗕𝗔𝗡𝗚𝗟𝗔𝗗𝗘𝗦𝗛𝗜\033[1;39m          ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙒𝙃𝘼𝙏𝙎𝘼𝙋𝙋\033[1;34m   : [★]  +8809638223345\033[1;39m       ┃
\033[1;39m ┃ \x1b[1;95m[💉]😎\x1b[1;96m 𝙏𝙊𝙊𝙇𝙎 𝙉𝘼𝙈𝙀\033[1;31m : [★]  MAIN-ROOT-CYBER     \033[1;39m ┃
 \033[1;39m┗━━━━━━━━━━━━━━━━━━━━\033[1;32m𝙁𝙄𝙍𝙀\033[1;39m━━━━━━━━━━━━━━━━━━━━━━━┛
\033[0;32m
'''
command_list='''
[1] CYBER INFO BOX 
[2] PYTHON COLOR CODE  
'''
comm ='''\033[0;31m
LOGIN ERROR ....
'''
while True:
    clear_screen()
    anima(animation)
    print(BANNER)
    print(command_list)
    CHOICE = input('\033[1;34mENTER YOUR CHOICE : ')
    if CHOICE =='1':
        os.system('espeak opencyberinfo')
        os.system('python cyber_info.py')
    elif CHOICE=='2':
        os.system('python-color-code.txt')
    else:
        for i in range(10,0,-1):
            sleep(0.5)
            clear_screen()
            print(BANNER)
            print(comm)
            print(f'TRY AFTER {i} SECOND')
            sleep(0.5)
# Developed by CYBER COP BANGLADESH
