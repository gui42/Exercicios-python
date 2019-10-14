import random

def dado(lados = 6):
    num = random.randint(1,int(lados))
    return num

print()

continua = True

while continua:
    num = input("Numero de lados: ")
    if int(num) == 0:
        continua = False
    else:
        print(dado(num))



