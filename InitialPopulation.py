import random
operators = ["+", "-", "*", "/", "^"]
operands = ["num", "x"]

def InitialPopulation():
    strAns = ""
    strWeigh = random.randint(1,10)
    varAdd = True
    operatorAdd = True
    for i in range(strWeigh):
        if i == 0 or i == (strWeigh-1):
            if random.randint(0,1) == 0 or varAdd == False:
                strAns += str(random.randint(1, 9))
                varAdd = True
            else:
                strAns += "x"
                varAdd = False
        else:
            if random.randint(0,1) == 0 and operatorAdd == True:
                strAns += operators[random.randint(0,3)]
                operatorAdd = False
            else:
                if random.randint(0,1) == 0 or varAdd == False:
                    strAns += str(random.randint(1, 9))
                else:
                    strAns += "x"
                    varAdd = False
    return strAns