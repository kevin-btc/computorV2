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


def is_assign(data):
    match_assign = search(reg.IS_ASSIGN, data)

    if match_assign is None:
        return None
    elif match_assign.group(0) == 'i':
        print("Error : `i` is reserved word.")
        return None
    return True


def is_calculation(data):
    return match(reg.IS_CALCUL, data)


def is_error(data, nbr):
    if match_full(reg.IS_NUMBER, data):
        print(data)
    else:
        print("assign: parse error: ", data," \nError code: ", nbr)


def match_full(reg, val):
    resMatch = match(reg, val)

    if resMatch is not None:
        lenMatch = len(resMatch.group(0))
        if lenMatch == len(val):
            return True
    return False


def split_assign(data):
    data = data.split("=")
    if len(data) == 1:
        return None
    var = data[0].lower().replace(' ', '')
    val = data[1].lower().replace(' ', '')
    val = replace_var_to_val(val)
    return (var, val)


def are_brackets_valid(data):
    buf = 0
    for char in data:
        if char == "(":
            buf += 1
        elif char == ")":
            buf -= 1
        if buf < 0:
            print("Error: wrong format ().")
            break
    return True if buf == 0 else False


def del_var(assign_type, var_name):
    for type_name, vars in datas.items():
        for name, var_value in list(vars.items()):
            if name.lower() == var_name.lower() and assign_type != type_name:
                del datas[type_name][var_name]



def replace_var_to_val(val):
    match_var = findall(r"((?:^|(?<=[*/%+-\[\s]))[a-zA-Z]+(?=[*/%+-\]\s]|$))", val)
    for type_name, vars in datas.items():
        for name, var_value in list(vars.items()):
            if name.lower() in match_var:
                val = val.replace(name, var_value)
    return val


def eval_assign(val):
    if are_brackets_valid(val):
        val = str(eval(val))
        val = sub(reg.STRIP_SPACE, "", val)
        return val


def check_assign_type(data):
    var, val = split_assign(data)
    print(data)
    if match(reg.FUNCTION, data):
        print(var)
        var = sub(r"(\([a-z]\))+", "", var)
        print(var)
        return "function", var, val
    elif match_full(reg.RATIONAL, val):
        return "rational", var, val
    elif match_full(reg.MATRICES, sub(r"(\],\[)+", "];[", val)):
        return "matrices", var, val
    # elif match_full(reg.POLYNOME, val):
    #     return "polynome", data
    # elif match_full(reg.COMPLEXE, val):
    #     return "complexe", data
    return False, var, val

def assign_var(data):
    assign_type, var_name, var_data = check_assign_type(data)

    if assign_type:
        try:
            var_data = eval_assign(var_data)
            del_var(assign_type, var_name)
            datas[assign_type][var_name] = var_data
            print(var_data)
        except:
            is_error(data, "1")
    else:
        is_error(data, "2")


def strip_input():
    try:
        return input("> ").strip()
    except:
        exit("Oops! Something went wrong.")


def computor_v2():
    init_datas()

    while True:
        data = strip_input()
        if data.upper() == "QUIT":
            exit_progs()
        elif data.upper() == "PRINT":
            show_datas()
        elif data.upper() == "RESET":
            init_datas()
        elif data.upper() == "":
            continue
        elif is_assign(data):
            assign_var(data)
        elif is_calculation(data):
            print("i am an calculation")
        else:
            is_error(data, "3")


if __name__ == "__main__":
    copyright()
    computor_v2()
