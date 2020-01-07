#!/usr/bin/python
# -*- coding:UTF-8 -*-
from computor import *
from regex import *

from io import StringIO
import sys

init_datas()


def failure_success():
    global failure
    global success

    failure = 0
    success = 0


def is_assign_test(data, expect):
    global failure
    global success
    sys.stdout = StringIO()

    if is_assign(data) == expect:
        print("\x1b[32mSUCCESS\x1b[0m")
        success = success + 1
    else:
        print("\x1b[31mFAIL\x1b[0m")
        failure = failure + 1

    s = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("\x1b[36mTesting -> {} :\x1b[0m".format(data))
    print(s)


def is_calculation_test(data, expect):
    global failure
    global success
    sys.stdout = StringIO()
    print(is_calculation(data))
    if is_calculation(data) is not None:
        print("\x1b[32mSUCCESS\x1b[0m")
        success = success + 1
    else:
        print("\x1b[31mFAIL\x1b[0m")
        failure = failure + 1

    s = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("\x1b[36mTesting -> {} :\x1b[0m".format(data))
    print(s)


def match_full_test(data, expect, reg):
    global failure
    global success
    sys.stdout = StringIO()

    if match_full(reg, data) is True:
        print("\x1b[32mSUCCESS\x1b[0m")
        success = success + 1
    else:
        print("\x1b[31mFAIL\x1b[0m")
        failure = failure + 1

    s = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("\x1b[36mTesting -> {} :\x1b[0m".format(data))
    print(s)


def split_assign_test(data, expect):
    global failure
    global success
    sys.stdout = StringIO()

    ret = split_assign(data)
    if ret[0] is not None and ret[1] is not None or expect is None:
        print("\x1b[32mSUCCESS\x1b[0m")
        print(ret)
        success = success + 1
    else:
        print("\x1b[31mFAIL\x1b[0m")
        failure = failure + 1

    s = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("\x1b[36mTesting -> {} :\x1b[0m".format(data))
    print(s)


def are_brackets_valid_test(data, expect):
    global failure
    global success
    sys.stdout = StringIO()

    if are_brackets_valid(data) is expect:
        print("\x1b[32mSUCCESS\x1b[0m")
        success = success + 1
    else:
        print("\x1b[31mFAIL\x1b[0m")
        failure = failure + 1

    s = sys.stdout.getvalue()
    sys.stdout.close()
    sys.stdout = sys.__stdout__
    print("\x1b[36mTesting -> {} :\x1b[0m".format(data))
    print(s)


failure_success()
while True:
    print("\n\nTEST IS_ASSIGN FUNCTION : ".center(50))
    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    is_assign_test("v=", True)
    is_assign_test("f(x)=", True)
    is_assign_test("f()=", None)
    is_assign_test("f(=", None)
    is_assign_test("()=", None)
    is_assign_test("()f=", None)
    is_assign_test("() f =", None)
    is_assign_test("var=", True)
    is_assign_test("1v=", None)
    is_assign_test("v1v=", None)
    is_assign_test("fail5 - 5 ", None)
    is_assign_test("=", None)
    is_assign_test("", None)
    is_assign_test("g   =   ", True)
    is_assign_test("i = ", None)
    is_assign_test("I = ", None)
    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    #
    #

    print("TEST MATCH_FULL FUNCTION : ".center(50))
    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    match_full_test("5-5", True, RATIONAL)
    match_full_test("(5-5)", True, RATIONAL)
    match_full_test("(5-5+5*8/(4*5))", True, RATIONAL)
    match_full_test("5+5-", True, RATIONAL)

    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")

    print("TEST SPLIT_ASSIGN FUNCTION : ".center(50))
    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    split_assign_test("5-5=5", None)
    split_assign_test("A=7-J", None)
    split_assign_test("a=", None)
    split_assign_test("a", None)
    split_assign_test("f-=8", True)
    split_assign_test("f(x)=5x", True)
    split_assign_test("f(x) 5x", None)
    split_assign_test("f(x) 5x", None)
    split_assign_test("f(x) 5x", None)
    split_assign_test("f=[[1,2]]", True)
    split_assign_test("f=[[a,2]]", None)
    split_assign_test("f==5", None)
    split_assign_test("f         =                        5", True)

    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")

    print("TEST ARE_BRACKETS_VALID FUNCTION : ".center(50))
    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    are_brackets_valid_test("(((((())))))", True)
    are_brackets_valid_test("(((((()))))", False)
    are_brackets_valid_test("((((())))))", False)
    are_brackets_valid_test("(a+5 *(a - 5))", True)
    are_brackets_valid_test("(a+5 *(a - 5)", False)
    are_brackets_valid_test("((7 - 7) * 7)", True)
    are_brackets_valid_test("((7 - (7)) * 7)", True)

    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")

    print("TEST IS_CALCULATION FUNCTION : ".center(50))
    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    is_calculation_test("5-5=?", True)
    is_calculation_test("(5-5)=?", True)
    is_calculation_test("(5-5)=", False)
    is_calculation_test("5-=?", False)
    is_calculation_test("f(x)=?", True)

    print("\x1b[33m\n----------------------------------------------\n\x1b[0m")

    # print("TEST RATIONAL NUMBERS : ".center(50))
    # print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    # cmp_input_test("v = 5 - 5")
    # cmp_input_test("v = (5 - 5)")
    # cmp_input_test("v = 5 -5 % 3 * 5 - 5/9")
    # cmp_input_test("v = -5 -5")
    # cmp_input_test("v = 5 -- 5")
    # cmp_input_test("v = 4+3+(2*5)")
    # cmp_input_test("v = 5 - 5 + ")
    # cmp_input_test("v = fail5 - 5 ")
    # cmp_input_test("v = 5 - 5a")
    # cmp_input_test("v = -%5 -5 % 3 * 5 - 5/9")
    # cmp_input_test("v = ")
    # print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    #
    #
    # print("TEST MATRIX : ".center(50))
    # print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
    # cmp_input_test("v = [[23,1]]")
    # cmp_input_test("v = [[23,1];[7]]")
    # cmp_input_test("v = [[23,1];[7,14]] ")
    # cmp_input_test("v = [[1];[7,14];[8]] ")
    # cmp_input_test("v = [1];[7,14];[8]]")
    # cmp_input_test("v = [[1];[7,14]:[8]]")
    # cmp_input_test("v = [[1];[7,14][8]]")
    # cmp_input_test("v = [[1];7,14][8]]")
    # cmp_input_test("v = [[1];[7,14][8]]j")
    # cmp_input_test("v = [[1];[7,14][8,]]")
    # cmp_input_test("v = [[1];[7,14][8,];]")
    # cmp_input_test("v = []")
    # print("\x1b[33m\n----------------------------------------------\n\x1b[0m\n")
    #
    print("Result :")
    print(
        "\x1b[31mFail -> {} \x1b[0m\n\x1b[32mSuccess -> {}\x1b[0m".format(
            failure, success
        )
    )
    key = input("'R' for Retry.\n Other key for quit ")
    if key is not "R":
        break
