#arquivo que controla o jogo de madlibs
import helper

userin=[]

#só abre o arquivo mesmo
mad = helper.openMad()
#cria a lista de variaveis
varList = helper.readMad(mad)

for x in varList:
        end = (len(x)-1)
        visual = x[1:end].lower()
        y = input("please enter a\\n "+visual+" ")
        userin.append(y.lower())

print()
helper.changeMad(userin, varList, mad)
