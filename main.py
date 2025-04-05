import random
import string

len_str = int(input('Длина пароля'))

password = ''
for i in range(len_str):
    password += random.choice(string.printable)

print(password)
