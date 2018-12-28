'''Understanding Python’s one ternary operator'''

'''A ternary operator requires three elements.
Python supports just one such operator, and
you use it to determine the truth value of an
expression. This operator takes the following
form:
    TrueValue if Expression else
        FalseValue
'''

#Example1:

print("Hello" if True else "Goodbye")

#Will print "Hello"

#Example2:

print("Hello" if False else "Goodbye")
#will print "Goodbye"


'''Python has an alternative form of this ternary
operator — an even shorter shortcut. It takes
the following form:
    (FalseValue, TrueValue)
        [Expression]
'''

#Example3:

print(("Hello", "Goodbye")[True])

'''An operator accepts one or more inputs in the form of variables or expressions,
performs a task (such as comparison or addition), and then provides an output
consistent with that task. Operators are classified partially by their effect and
partially by the number of elements they require. For example, a unary opera-
tor works with a single variable or expression; a binary operator requires two.
The elements provided as input to an operator are called operands. The oper-
and on the left side of the operator is called the left operand, while the oper-
and on the right side of the operator is called the right operand. The following
list shows the categories of operators that you use within Python:
✓ Unary
✓ Arithmetic
✓ Relational
✓ Logical
✓ Bitwise
✓ Assignment
✓ Membership
✓ Identity'''

#Example 4:
'''Calculate the value of the string'''
#a = 'Ko Y Tze'
a = input('Input a string: ')

total = 0
for char in a:
    total += ord(char)
    print(char,' value is:', str(ord(char)))
print('Sum of:', a, 'is: ',total)




