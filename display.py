#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import system
from setting import init_datas
def copyright():
    system("clear")
    print(
        "                                 _                     ____\n\
   ___ ___  _ __ ___  _ __  _   _| |_ ___  _ __  __   _|___ \ \n\
  / __/ _ \| '_ ` _ \| '_ \| | | | __/ _ \| '__| \ \ / / __) |\n\
 | (_| (_) | | | | | | |_) | |_| | || (_) | |     \ V / / __/ \n\
  \___\___/|_| |_| |_| .__/ \__,_|\__\___/|_|      \_/ |_____| v0.1\n\
                     |_|                                      \n\
    ")
    print("Copyright 2019-2020, 2019 Free Software Kevin Foundation, Inc.".center(65))
    print("This is free software with ABSOLUTELY NO WARRANTY.\n\n".center(65))


def colorText(value, color = '31'):
    return '\x1b[' + color + 'm' + value + '\x1b[0m'


def format_matrix(matrix, mode = 0):
    if mode == 1:
        matrix = matrix.replace("],[", "]\n\t [")
    else:
        matrix = matrix.replace("],[", "]\n[")
    matrix = matrix.replace("[[", "[")
    matrix = matrix.replace("]]", "]")
    return matrix


def show_datas():
    empty_data = 0
    for type_name, vars in datas.items():
        if len(vars) == 0:
            empty_data += 1
            continue
        print("-------------------------")
        print(colorText(type_name, "36"))
        for var_name, val in vars.items():
            if type_name == "matrices":
                print('\t' + var_name, "->\n\t", format_matrix(val, 1))
            else:
                print('\t' + var_name, "->", val)
    if empty_data == 4:
        print(colorText('No variable saved.\x1b[0m'))
    print("-------------------------")


def print_com(data):
    print(colorText(data, "33"))


def usage():
    print("usage: ")


