import os

def clear():
    os_type = os.name
    if os_type == 'nt':
        os.system('cls')
    elif os_type == 'posix':
        os.system('clear')