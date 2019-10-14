#o usuário tem de adivinhar o número que é gerado pelo programa

import random

numero = random.randint(0,100)

cont  = True

while cont: 
    try:
        num = input("Entre com um número: ")
        val = int(num)
        if val == numero:
            print("Acertou!")
            cont = False
        elif val > numero:
            print("O número é maior que a entrada!")
        elif val < numero:
            print("O número é menor que a entrada!")

    except ValueError as e:
        print("Entrada não é um número")
