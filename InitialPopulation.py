from concurrent.futures import BrokenExecutor
import random
operators = ["+", "-", "*", "/", "^"]
operands = ["num", "x"]

def InitialPopulation():
    strAns = ""
    strWeigh = random.randint(1,10)
    varnumAdd = True
    operatorAdd = True
    for i in range(strWeigh):
        if i == 0 or (i == (strWeigh-1) and operatorAdd == False and varnumAdd == True):
            if random.randint(0,1) == 0 and varnumAdd == True:
                strAns += str(random.randint(1, 9))
                varnumAdd = False
                operatorAdd = True
            elif varnumAdd == True:
                strAns += "x"
                varnumAdd = False
                operatorAdd = True

        else:
            if (random.randint(0,1) == 0 and operatorAdd == True or varnumAdd == False) and i != (strWeigh-1):
                strAns += operators[random.randint(0,4)]
                operatorAdd = False
                varnumAdd = True
            elif varnumAdd == True:
                if random.randint(0,1) == 0 and varnumAdd == True:
                    strAns += str(random.randint(1, 9))
                    varnumAdd = False
                    operatorAdd = True
                else:
                    strAns += "x"
                    varnumAdd = False
                    operatorAdd = True
            else:
                break

    if strAns.find("x") == -1:
        strAns = InitialPopulation()
    return strAns