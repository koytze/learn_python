def Hello():
    print('This is my first Python function!')


def AddIt(Value1, Value2):
    print(Value1, " + ", Value2, " = ", (Value1 + Value2))

def Hello3(Greeting = 'No Value Supplied'):
    print(Greeting)


def Hello4(ArgCount, *VarArgs):
    print("You passed ", ArgCount, " arguments.")
    for Arg in VarArgs:
        print(Arg)

def DoAdd(Value1, Value2):
    return Value1 + Value2


print('The sum of 3 + 4 is ', DoAdd(3, 4))

print('3 + 4 equals 2 + 5 is ', (DoAdd(3, 4) == DoAdd(2, 5)))


