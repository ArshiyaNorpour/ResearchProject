import random
operators = ["+", "-", "*", "/", "^"]
operands = ["num", "x"]

def InitialPopulation():
    strAns = ""
    strWeigh = random.randint(1,10)
    for i in range(strWeigh):
        if i == 0 or i == (strWeigh-1):
            if random.randint(0,1) == 0:
                strAns += str(random.randint(1, 100))
            else:
                strAns += "x"
        else:
            if random.randint(0,1) == 0:
                strAns += operators[random.randint(0,3)]
            else:
                if random.randint(0,1) == 0:
                    strAns += str(random.randint(1, 100))
                else:
                    strAns += "x"
    return strAns