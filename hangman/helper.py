import random

def openList():
    with open('lista.txt') as f:
        lines = f.read().splitlines()
    return lines

def randomWord():
    lines = openList()
    i = len(lines)
    a =random.randint(0,i)
    return lines[a].lower()

def letterList(word):
    x = 0
    letterL = {}
    for x in range (0,len(word)):
        letter = str(word[x])
        letterL[letter] = False
        x = x +1
    
    return letterL

def printWord(letterL):
    wword = ""
    for x in letterL:
        if letterL[x]:
            wword = str(wword)+str(x.upper())
        else:
            wword = str(wword)+"X"
    print(wword)

def checkLetter(letter, letterL):
    for x in letterL:
        if x == letter:
            letterL[x] = True
    return letterL

    
