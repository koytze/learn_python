#!/usr/bin/python


#Basic string exercises
#You have to fill in the code for each function and
#return a string variable as described in the request
#Once you finished, you may proceed with the secondary exercise



#1. Apples
#You will receive as int parameter a number of apples.
#Your function needs to return a string of the form: 'Anna has <count> apples'
#However, if number of apples is 5 or higher, the use the word 'lots of' instead.
#Example:
#Given number: 2
#Return: 'Anna has 2 apples'
#Given number: 5
#Return: 'Anna has lots of apples'
def Apples(number):
    if number < 5:
          return 'Anna has ' +str(number)+ ' apples'

    else:
          return 'Anna has lots of apples'


#2. Both ends
#Given a string text, return a string made of the first 2 and
#the last 2 chars of the original string. If the string length is less than 2,
#return the empty string.
#Example:
#Given text: 'testare'
#Return: 'tere'
#Given text: 'SA'
#Return: 'SASA'
#Given text: 'E'
#Return: ''
def BothEnds(text):
      if len(text) < 2:
            return ''
      else:
            x = text[:2]
            x += text[-2:]
      return x
    #fill in your code here
    #return



#3. Fix start
#Given a string text, return a string where all occurrences of its first char
#have been changed to '#', except the first char itself.
#Example:
#Given string: 'adamantium'
#Return: 'ad#m#ntium'
def FixStart(text):
      c = text[0]

      return c+text[1:].replace(c,'#')


#4. MixStrings
#Given two strings a and b, return a single string where a and b are separated by space
#and the first two characters of a and b are swapped.
#Example:
#Given Strings: 'abc','xyz'
#Return: 'xyc abz'
def MixStrings(a,b):
      ca=a[:2]
      cb=b[:2]
      text = cb+a[2:]+' '+ca+b[2:]
    #fill in your code here
      return text


#Below test() function is used in main() to print
#what each function returns vs. what it's supposed to return.
def test(in_data, returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = 'NOK '
    print ('%s- Input data: %s. Returned: %s Expected: %s' % (prefix, in_data, repr(returned), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('1. Apples')
    # Each line calls Apples(<number>), compares its result to the expected for that call.
    test(2, Apples(2), 'Anna has 2 apples')
    test(5, Apples(5), 'Anna has lots of apples')
    test(4, Apples(4), 'Anna has 4 apples')
    test(30, Apples(30), 'Anna has lots of apples')

    print()
    print('2. Both ends')
    # Each line calls BothEnds('text'), compares its result to the expected for that call.
    test('testare', BothEnds('testare'), 'tere')
    test('SA', BothEnds('SA'), 'SASA')
    test('E', BothEnds('E'), '')
    test('xyz', BothEnds('xyz'), 'xyyz')

  
    print()
    print('3. Fix start')
    test('adamantium', FixStart('adamantium'), 'ad#m#ntium')
    test('cctv recording', FixStart('cctv recording'), 'c#tv re#ording')
    test('ericsson', FixStart('ericsson'), 'ericsson')
    test('calc', FixStart('calc'), 'cal#')

    print()
    print('4. MixStrings')
    test(('abc', 'xyz'), MixStrings('abc', 'xyz'), 'xyc abz')
    test(('cash', 'infusion'), MixStrings('cash', 'infusion'), 'insh cafusion')
    test(('just', 'restart'), MixStrings('just', 'restart'), 'rest justart')
    test(('follow', 'him'), MixStrings('follow', 'him'), 'hillow fom')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

