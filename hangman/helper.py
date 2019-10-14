import random

def openList():
    with open('lista.txt') as f:
        lines = f.read().splitlines()
    return lines

def RandomWord():
    lines = openList()
    i = len(lines)
    a =random.randint(0,i)
    return lines[a].lower()


