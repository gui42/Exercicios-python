import helper
#uma palavra aleatória do arquivo lista.txt é escolhida
word =  helper.randomWord()
#word = input()
#imprimindo o tamanho da palavra:
print("The word has "+str(len(word))+" letters")

#cria um dicionario com cada das letras da palavra
letterL = helper.letterList(word)

#essa função imprimi a palavra, substituindo as letras desconhecidas por X
helper.printWord(letterL)
hp = 20
victory = False
allletters = ""
while not victory and hp > 0 :
    print("You have "+str(hp)+ " guesses left")
    print("You've tried this letters so far:"+allletters)
    letter = input("Enter a guess: ")
   
   #lista as tentativas
    allletters=allletters+" "+letter
    
   #funções verificam se a letra esta na palavra, depois imprimi a palavra com as alterações se necessário e verifica se a condição de vitória foi atingida
    letterL = helper.checkLetter(letter, letterL)
    helper.printWord(letterL)
    victory = helper.checkVictory(letterL)
    
    #verifica se a tentativa deve ou não ser descontada do total
    if helper.checkHP(letter, letterL):
        hp = hp
    else:
        hp -= 1

if victory:
    print("Victory!")
else:
    print("You loose, the word was "+str(word))
