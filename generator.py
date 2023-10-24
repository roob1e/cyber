from random import *

base_alpha_l=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
base_alpha_U=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
base_num=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
base_spec=['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '/', '?']

password=[]

def generate():
    amount = int(input('Введите количество символов в пароле'))
    for i in range(0, amount):
        base = randint(1,3)
        if base == 1:
            password.append(base_alpha_l[randint(0, 25)])
        elif base == 2:
            password.append(base_alpha_U[randint(0, 25)])
        elif base == 3:
            password.append(base_num[randint(0, 9)])

def generate_spec():
    amount = int(input('Введите количество символов в пароле'))
    for i in range(0, amount):
        base = randint(1,4)
        if base == 1:
            password.append(base_alpha_l[randint(0, 25)])
        elif base == 2:
            password.append(base_alpha_U[randint(0, 25)])
        elif base == 3:
            password.append(base_num[randint(0, 9)])
        elif base == 4:
            password.append(base_spec[randint(0, 25)])

a = str(input('В пароле допустимы спец. символы? \n'))

if a.lower() == 'да' or 'yes':
    generate_spec()
elif a.lower() == 'нет' or 'no':
    generate()

print(''.join(password))

