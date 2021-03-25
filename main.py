from os import system
from os import name
from sys import stdout
from time import sleep
from sys import exit
from platform import system as osname

def clear():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

lintest = osname()
if lintest == 'Linux':
    pkgin = input('pkg manger example (apt install "space!!!!") : ')
else:
    pass
clear()
print('remember stay at the good directory ')
sleep(6)
clear()
def slowprint(s):
    for c in s + '\n':
        stdout.write(c)
        stdout.flush()
        sleep(10. / 100)


with open('name.txt', 'r') as f:
    lines = f.read().splitlines()

print('''                                              ___    ___     _          
 / / _  o  _ ) _   _  _)_ o _(_ o  _   _ )    )     )_     /_)    )\/) 
(_/ ) ) ( (_( )_) ) ) (_  (   ) ( )_) (_(    (     (__    / /    (  (  
             (_                  (_                                    
''')
slowprint('starting project . . . .')


clear()


try :
    clear()
    system('git')
    clear()
except:
    platformname = osname()
    if platformname == 'Windows':
        print('install git at ( https://git-scm.com/download/win ) ')
    if platformname == 'Linux':
        system(f'{pkgin} git')
    if platformname == 'Darwin':
        system('brew install git')
    try:
        system('git')
    except:
        print('please install git ...')
        exit()

for i in lines:
    try:
        system(f"git clone {i}")
    except:
        print(f'error for {i}')
        pass