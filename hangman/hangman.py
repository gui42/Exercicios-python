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

victory = False

while not victory :
    letter = input("Enter a guess: ")
    letterL = helper.checkLetter(letter, letterL)
    helper.printWord(letterL)
    victory = helper.checkVictory(letterL)
    if victory:
        print("Victory!")
        
