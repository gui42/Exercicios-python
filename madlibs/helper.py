#arquivo que contem funções do jogo madlib

def openMad():
    try:
        with open("puzzle.txt") as f:
            lines = f.read().splitlines()
            return lines
    except FileNotFoundError as e:
        print(":(")

def criaVar(mad):
    varList = []
    var = ""
    part_of_var = False
    for x in mad:
        if x == "[":
            part_of_var = True
        if x == "]":
            var += x
            varList.append(var)
            var = ""
            part_of_var = False
        if part_of_var:
            var += x
    return varList   

def readMad(lines):
    varL =[]
    for x in lines:
      varL += criaVar(x)
    return varL 


def changeMad(userin, varList, mad):
    for line in mad:
        for item in varList:
            if item in line:
                index = varList.index(item)
                line=(line.replace(item, userin[index]))
                varList[index] ="done"
        print(line)
