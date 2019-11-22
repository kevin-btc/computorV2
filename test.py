from computor import *
global failure
global success
failure = 0
success = 0

def test(str, type):
    print("\x1b[36mTesting -> {} :\x1b[0m".format(str))
    ret = computorV2Test(str)
    if ret == type:
        global success
        print('\x1b[32mSUCCESS\x1b[0m')
        success = success + 1
    else:
        global failure
        print('\x1b[31mFAIL\x1b[0m')
        failure =  failure + 1

def testName(str, ret):
    print("\x1b[36mTesting -> {} :\x1b[0m".format(str))
    ret = True if isAssignation(str) else False
    if ret == ret:
        global success
        print('\x1b[32mSUCCESS\x1b[0m')
        success = success + 1
    else:
        global failure
        print('\x1b[31mFAIL\x1b[0m')
        failure =  failure + 1

print("TEST NAME VARIABLE : ".center(50))
print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
testName('v=', True)
testName("f(x)=", True)
testName('var=', True)
testName('1v=', False)
testName('v1v=', False)
testName('fail5 - 5 ', False)
testName('=', False)
testName('', False)
print("\x1b[33m\n----------------------------------------------\n\x1b[0m")


print("TEST RATIONAL NUMBERS : ".center(50))
print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
test('v = 5 - 5', 'rational')
test('v = (5 - 5)', 'rational')
test('v = 5 -5 % 3 * 5 - 5/9', 'rational')
test('v = -5 -5', 'rational')
test('v = 5 -- 5', 'rational')
test('v = 4+3+(2*5)', 'rational')
test('v = 5 - 5 + ', False)
test('v = fail5 - 5 ', False)
test('v = 5 - 5a', False)
test('v = -%5 -5 % 3 * 5 - 5/9', False)
test('v = ', False)
print("\x1b[33m\n----------------------------------------------\n\x1b[0m")


print("TEST MATRIX : ".center(50))
print("\x1b[33m\n----------------------------------------------\n\x1b[0m")
test('v = [[23,1]]', 'matrices')
test('v = [[23,1];[7]]', 'matrices')
test('v = [[23,1];[7,14]] ', 'matrices')
test('v = [[1];[7,14];[8]] ', 'matrices')
test('v = [1];[7,14];[8]]', False)
test('v = [[1];[7,14]:[8]]', False)
test('v = [[1];[7,14][8]]', False)
test('v = [[1];7,14][8]]', False)
test('v = [[1];[7,14][8]]j', False)
test('v = [[1];[7,14][8,]]', False)
test('v = [[1];[7,14][8,];]', False)
test('v = []', False)
print("\x1b[33m\n----------------------------------------------\n\x1b[0m\n")

print("Result :")
print("\x1b[31mFail -> {} \x1b[0m\n\x1b[32mSuccess -> {}\x1b[0m".format(failure, success))
