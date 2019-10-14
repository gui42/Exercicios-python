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
    letterL =[] 
    size = len(word)
    for x in range (0,size):
        letter = str(word[x])
        letterA = {letter: False}
        letterL.append(letterA)
 #       letterL[letter] = False
    
   
    print(letterL)
    return letterL

def printWord(letterL):
    wword = ""
    for x in letterL:
        if letterL[x]:
            wword = str(wword)+str(x.upper())
        else:
            wword = str(wword)+"*"
    print(wword)

def checkLetter(letter, letterL):
    for x in letterL:
        if x == letter:
            letterL[x] = True 
    return letterL

def checkVictory(letterL):
    for x in letterL:
        if not letterL[x]:
            return False

    return True
            
