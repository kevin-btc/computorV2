#!/usr/bin/env python
# -*- coding:utf-8 -*-

from re import *
from os import *
from constante import *
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
    match_assign = search(IS_ASSIGN, data)

    if match_assign is None:
        return None
    elif match_assign.group(0).lower() == "i":
        print("Error : `i` is reserved word.")
        return None
    return True


def is_calculation(data):
    return match(IS_CALCUL, data)


def is_error(data, nbr):
    if match_full(IS_NUMBER, data):
        print(data)
    else:
        print("assign: parse error: ", data, " \nError code: ", nbr)


def match_full(reg, val):
    resMatch = match(reg, val)

    if resMatch is not None:
        lenMatch = len(resMatch.group(0))
        if lenMatch == len(val):
            return True
    return False


def split_assign(data):
    data = data.split("=")

    if len(data) != 2 or not data[0] or not data[1]:
        return None, None
    var = sub("\s+", "", data[0].lower())
    val = sub("\s+", "", data[1].lower())
    rpl = sub(r"(\],\[)+", "];[", val)
    if not match_full(MATRICES, rpl):
        val = replace_var_to_val(val)
    return (var, val)


def are_brackets_valid(data):
    buffer = 0
    for char in data:
        try:
            if char == BRACKET_LEFT:
                buffer = buffer + 1
            elif char == BRACKET_RGTH:
                buffer = buffer - 1
            assert buffer >= 0
        except:
            print("Error: closing parenthesis must be behind the opening parenthesis.")
            return False

    if buffer != 0:
        print("Error: a closing parenthesis is missing.")
        return False
    return True


def del_var(assign_type, var_name):
    for type_name, vars in datas.items():
        for name, var_value in list(vars.items()):
            if name.lower() == var_name.lower() and assign_type != type_name:
                del datas[type_name][var_name]


def check_var_exist(assign_type, var_name):
    for type_name, vars in datas.items():
        for name, var_value in list(vars.items()):
            if name.lower() == var_name.lower() and assign_type != type_name:
                return True
    return False


def search_var(data):
    var_name = split_assign(data)[0]
    ret = "Error: no variable with this name."
    for type_name, vars in datas.items():
        for name, var_value in list(vars.items()):
            if name.lower() == var_name.lower():
                ret = var_value
    print(ret)


def nbr_to_str(eq):
    return str(eval(eq))


def add_forgot_star(val, name):
    name_if_exist = r"(?<=[a-zA-Z0-9]){}|{}(?=[a-zA-Z0-9])".format(name, name)

    lname = len(name)

    reg_both_star = "(?<=[a-zA-Z0-9]{{{}}}){}(?=[a-zA-Z0-9])".format(lname, name)
    reg_left_star = "(?<=[a-zA-Z0-9]{{{}}}){}".format(lname, name)
    reg_rght_star = "{}(?=[a-zA-Z0-9]{{{}}})".format(name, lname)

    str_both_star = "*" + name + "*"
    str_left_star = "*" + name
    str_rght_star = name + "*"

    while search(name_if_exist, val):
        val = sub(reg_left_star, str_left_star, val, 1)
        val = sub(reg_rght_star, str_rght_star, val, 1)
        val = sub(reg_both_star, str_both_star, val, 1)

    return val


def replace_var_to_val(val):
    match_var = findall(PARSE_PARAM, val)
    for type_name, vars in datas.items():
        for name, var_value in reversed(list(vars.items())):
            if name.lower() in "".join(match_var):
                if type_name == "function":
                    func_var = findall(PARAM_FUNCT, val)
                    for i in range(0, len(func_var)):
                        try:
                            search_func = name + "(" + func_var[i] + ")"
                            new_var_value = sub(IS_LETTER, func_var[i], var_value)
                            val = val.replace(search_func, nbr_to_str(new_var_value))
                        except:
                            is_error(val)
                else:
                    val = add_forgot_star(val, name)
                    val = val.replace(name, str(var_value))
    return val


def eval_assign(val):
    if are_brackets_valid(val):
        val = nbr_to_str(val)
        val = sub(STRIP_SPACE, "", val)
        return val
    return None


def parse_function(var, val):
    func_name = sub(CONTAIN_LTR, "", var)
    func_var = findall(PARSE_FUNCT, var)
    handle_val = findall(func_var[0], val)

    if func_name == func_var[0]:
        print("ERROR: Function and argument must have different name.")
        return False, func_name, val
    elif check_var_exist("function", func_var[0]):
        print("ERROR: Variable and parameter must have different name.")
        return False, func_name, val
    elif search(r"[a-zA-Z]", val):
        handle_val = sub(func_var[0], "", val)
        handle_val = findall(r"[a-zA-Z]+", handle_val)
        if len(handle_val) != 0:
            print("ERROR: Unknown argument, use `{}`".format(func_var[0]))
            return False, func_name, val
        try:
            val = add_forgot_star(val, func_var[0])
            eval(val.replace(func_var[0], "1"))
        except:
            return False, func_name, val
    elif len(handle_val) == 0:
        try:
            val = nbr_to_str(val)
        except:
            return False, func_name, val

    return "function", func_name, val


def check_assign_type(data):
    var, val = split_assign(data)

    if var is None and val is None:
        return False, var, val
    elif match(FUNCTION, data):
        return parse_function(var, val)
    elif match_full(RATIONAL, val):
        return "rational", var, val
    elif match_full(MATRICES, sub(r"(\],\[)+", "];[", val)):
        return "matrices", var, sub(r"(\];\[)+", "],[", val)
    # elif match_full(POLYNOME, val):
    #     return "polynome", data
    # elif match_full(COMPLEXE, val):
    #     return "complexe", data
    return False, var, val


def assign_var(data):
    assign_type, var_name, var_data = check_assign_type(data)
    if assign_type and assign_type == "function":
        del_var(assign_type, var_name)
        datas[assign_type][var_name] = var_data
        print(var_data)
    elif assign_type:
        try:
            var_data = eval_assign(var_data)
            assert var_data != None
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


def show_var(data):
    return match_full(r"\s*[a-zA-Z]+\s*=\s*\?", data)


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
        elif data.upper() == "CLEAR":
            copyright()
        elif data.upper() == "":
            continue
        elif show_var(data):
            search_var(data)
        elif is_assign(data):
            assign_var(data)
        elif is_calculation(data):
            print("i am an calculation")
        else:
            is_error(data, "3")


if __name__ == "__main__":
    copyright()
    # try:
    computor_v2()
    # except:
    # print("ooups")
