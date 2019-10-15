import random

def openList():
    with open('lista.txt') as f:
        lines = f.read().splitlines()
    return lines

def randomWord():
    lines = openList()
    i = len(lines)
    i = i-1
    a =random.randint(0,i)
    return lines[a].lower()

def letterList(word):
    x = 0
    letterL =[] 
    size = len(word)
    for x in range (0,size):
        letter = str(word[x])
        letterA = {letter: False}
        letterL.append(letterA)
    return letterL

def printWord(letterL):
    wword = ""
    for x in letterL:
        for y in x:
            if x[y]: 
                wword = str(wword)+str(y)
            else:
                wword = str(wword)+"*"
    print("\n"+wword+"\n")

           
def checkLetter(letter, letterL):
    for x in letterL:
        for y in x:
            if y.lower() == letter.lower():
                x[y] = True
    return letterL

def checkVictory(letterL):
    for x in letterL:
        for y in x:
            if not x[y]:
                return False
    return True

def checkHP(letter, letterL):
    for x in letterL:
        for y in x:
            if letter.lower() == y.lower():
                return True
    return False
