

from re import *

# Regex Matrice : ((\[|^\[\[)([-+]?[0-9]*\.?[0-9]+([\^][-+]?[0-9]+)?\,?)+(\]\;|\]\]))
# Regex rational number : [-]?[0-9]+[,.]?[0-9]*([\/][0-9]+[,.]?[0-9]*)*
# Regex is Assignation : ^([a-zA-Z]+|[a-zA-Z]+\([a-zA-Z]{1}\))\={1}

class rationalNumber():
    print("I am a rational Number !")

def isAssignation(str):
    regex = r"^([a-zA-Z]+|[a-zA-Z]+\([a-zA-Z]{1}\))\={1}"
    return search(regex, str)

def isCalculation(str):
    regex = r"[a-zA-Z\+\-\*\/\^0-9]+=\?{1}"
    return search(regex, str)

def main():
    while True:
        str = sub(r"[\s]{1,}", "", input("> "))
        if str == 'quit':
            break
        elif isAssignation(str):
            print('i am an assignation')
        elif isCalculation(str):
            print('i am an calculation')

print("computorV2 0.1 \n\
Copyright 2019-2020, 2019 Free Software Foundation, Inc. \n\
This is free software with ABSOLUTELY NO WARRANTY.")

if __name__ == "__main__":
    main();
