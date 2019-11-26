#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re import *
from os import *
from regex import *
from sys import *
import gnureadline as readline


def copyright():
    system("clear")
    print(
        "                                 _                     ____\n\
   ___ ___  _ __ ___  _ __  _   _| |_ ___  _ __  __   _|___ \ \n\
  / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \| '__| \ \ / / __) |\n\
 | (_| (_) | | | | | | |_) | |_| | || (_) | |     \ V / / __/ \n\
  \___\___/|_| |_| |_| .__/ \__,_|\__\___/|_|      \_/ |_____| v0.1\n\
                     |_|                                      \n\
    "
    )
    print("Copyright 2019-2020, 2019 Free Software Foundation, Inc.".center(65))
    print("This is free software with ABSOLUTELY NO WARRANTY.\n\n".center(65))


def init_datas():
    global datas
    datas = {"rational": {}, "matrices": {}, "function": {}, "complexe": {}}


def show_datas():
    print(datas)


def exit_progs():
    exit("Bye !")


def is_assign(str):
    var = split_assign(str, 1)
    if var == "i":
        print("Error : `i` is reserved word.")
        return None
    return match(reg.IS_ASSIGN, str)


def is_calculation(str):
    return match(reg.IS_CALCUL, str)


def is_error(str, nbr):
    if match_full(reg.IS_NUMBER, str):
        print(str)
    else:
        print("assign: parse error", nbr)


def match_full(reg, val):
    resMatch = match(reg, val)
    if resMatch is not None:
        lenMatch = len(resMatch.group(0))
        if lenMatch == len(val):
            return True
    return False


def split_assign(str, mode=0):
    str = str.split("=")
    var = str[0].lower()
    val = find_var(str[1].lower())
    if mode == 1:
        return var
    if mode == 2:
        return val
    return (var, val)


def check_assign_type(str):
    var, val = split_assign(str)
    str = var + "=" + val

    if match_full(reg.RATIONAL, val):
        return "rational", str
    elif match_full(reg.MATRICES, sub(r"(\],\[)+", "];[", val)):
        return "matrices", str.replace(";", ",")
    elif match_full(reg.POLYNOME, val):
        return "polynome", str
    elif match_full(reg.COMPLEXE, val):
        return "complexe", str
    return False, val


def are_brackets_valid(str):
    buf = 0
    for char in str:
        if char == "(":
            buf += 1
        elif char == ")":
            buf -= 1
        if buf < 0:
            print("Error: wrong format ().")
            break
    return True if buf == 0 else False


def parse_assign(val, assign_type):
    var_rational = datas["rational"]
    var_matrices = datas["matrices"]
    var_name, var_calc = split_assign(val)
    if are_brackets_valid(val):
        var_calc = str(eval(var_calc, None, var_matrices))
        var_calc = sub(reg.STRIP_SPACE, "", var_calc)
        return var_name, var_calc


def del_datas_type(type_name, vars, assign_type, var_name):
    for name, var_value in list(vars.items()):
        if name.lower() == var_name.lower() and assign_type != type_name:
            del datas[type_name][var_name]


def del_datas(assign_type, var_name):
    for type_name, vars in datas.items():
        del_datas_type(type_name, vars, assign_type, var_name)


def replace_var(type_name, vars, assign_type, var_name):
    for name, var_value in list(vars.items()):
        if name.lower() == var_name.lower() and assign_type != type_name:
            del datas[type_name][var_name]


def find_var(val):
    test = findall(r"((?:^|(?<=[*/%+-]))[a-zA-Z]+(?=[*/%+-]|$))", val)
    for type_name, vars in datas.items():
        for name, var_value in list(vars.items()):
            if name.lower() in map(str.lower, test):
                return val.replace(name.lower(), str(var_value))
    return val


def assign_var(str):
    assign_type, str = check_assign_type(str)
    if assign_type:
        try:
            var_name, var_calc = parse_assign(str, assign_type)
            del_datas(assign_type, var_name)
            datas[assign_type][var_name] = var_calc
            print(var_calc)
        except:
            is_error(str, "1")
    else:
        is_error(str, "2")


def strip_input():
    try:
        return sub(reg.STRIP_SPACE, "", input("> "))
    except:
        exit("Oops! Something went wrong.")


def computor_v2():
    init_datas()

    while True:
        str = strip_input()
        if str.upper() == "QUIT":
            exit_progs()
        elif str.upper() == "PRINT":
            show_datas()
        elif str.upper() == "RESET":
            init_datas()
        elif str.upper() == "":
            continue
        elif is_assign(str):
            assign_var(str)
        elif is_calculation(str):
            print("i am an calculation")
        else:
            is_error(str, "3")


if __name__ == "__main__":
    copyright()
    computor_v2()
