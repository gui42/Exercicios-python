import random

def dado(lados = 6):
    num = random.randint(1,int(lados))
    return num

print()

continua = True

while continua:
    num = input("Numero de dados: ")
    try:
        val = int(num)
        if val == 0:
            continua = False
        else:
            print(dado(val))
    except ValueError as e:
        print("Entrada não é um número\n")



