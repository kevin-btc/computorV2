from re import *
from regex import *
import gnureadline as readline

def copyright():
    print("computorV2 0.1")
    print("Copyright 2019-2020, 2019 Free Software Foundation, Inc.")
    print("This is free software with ABSOLUTELY NO WARRANTY.")

def isAssignation(str):
    var = splitAssignation(str, 1)
    if var == 'i':
        print("Error : `i` is reserved word.")
        return None
    return match(reg.ASSIGNATION, str)

def isCalculation(str):
    return match(reg.CALCULATION, str)

def isError(str):
    if matchFull(reg.IS_NUMBER, str):
        print(str)
    else:
        print('Assignation: parse error')

def matchFull(reg, val):
    resMatch = match(reg, val)
    if resMatch != None:
        lenMatch = len(resMatch.group(0))
        if lenMatch == len(val):
            return True
    return False

def splitAssignation(str , mode = 0):
    str = str.split('=')
    if mode == 1:
        return str[0].lower()
    if mode == 2:
        return str[1].lower()
    return (str[0], str[1])

def checkAssignationType(str):
    val = splitAssignation(str, 2)

    if matchFull(reg.RATIONAL, val):
        return 'rational'
    elif matchFull(reg.MATRICES, val):
        return 'matrices'
    elif matchFull(reg.POLYNOME, val):
        return 'polynome'
    elif matchFull(reg.COMPLEXE, val):
        return 'complexe'
    else:
        return False

def parseAssignation(str, assignationType):
    nbr = 0
    global datas
    varRational = datas['rational']
    varName, varCalc = splitAssignation(str)
    for c in str:
        if c == '(': nbr += 1
        elif c == ')': nbr -= 1
        if nbr < 0:
            print('Error: wrong format ().')
            break
    if nbr == 0:
        return varName, eval(varCalc, None, varRational)

def computorV2():
    global datas
    datas = {
    "rational": {},
    "matrices": {},
    "function": {},
    "complexe": {}
    }

    while True:
        str = sub(reg.STRIP_SPACE, "", input("> "))
        if str == 'quit': break
        if str == 'look': print(datas)
        if str == '': continue
        elif isAssignation(str):
            assignationType = checkAssignationType(str)
            if assignationType:
                try:
                    varName, varCalc = parseAssignation(str, assignationType)
                    for key, value in datas.items():
                        for k, v in list(value.items()):
                            if k == varName and assignationType != key:
                                del datas[key][k]
                    datas[assignationType][varName] = varCalc
                    print(varCalc)
                except:
                    isError(str)
            else: isError(str)
        elif isCalculation(str):
            print('i am an calculation')
        else: isError(str)

def computorV2Test(argv):
    var = dict()
    str = sub(reg.STRIP_SPACE, "", argv)
    if isAssignation(str):
        return checkAssignationType(str)
    elif isCalculation(str):
        print('i am an calculation')
    else: isError(str)

if __name__ == "__main__":
    copyright()
    computorV2()
