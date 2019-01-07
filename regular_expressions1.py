#!/usr/bin/python


#Basic list exercises
#You have to fill in the code for each function and
#return a variable as described in the request
#Once you finished, you may proceed with the secondary exercise



#1. Findabbb
#Given a string, write a regular expressions to return the occurence of an a
#followed by three b. If no occurence if found return ''. 
#Example:
#Given string: 'one two three ab abb abbb abbba'
#Return: 'abbb'
import re

text = 'one two three ab abb abbb abbba'
def Findabbb(string):
    match = re.search(r'\babbb\b',string)
    if match:
        return match.group()
    else:
        return ''
##        if match.group():
##            return match.group()
##        else:
##      #print(match.group())
##    #fill in your code here
##            return ''


#2. zWord
#Given a string, return a list with words which contains letter 'z'.
#If no match is found, return [].
#Example:
#Given string: 'abc zap xyz aba smart zic'
#Return: ['zap', 'xyz', 'zic']
def zWord(string):

    match = re.search(r'\b\w*[z]\w*\b', string)
    if match:
        return re.findall(r'\b\w*[z]\w*\b', string)
    else:
        return []
    #fill in your code here
    



#3. zWordMiddle
#Given a string, return a list with words containing 'z',
#not at start or end of the word.
#If no match is found, return [].
#Example:
#Given string: 'abc azp xyz aba smart zic'
#Return: ['azp']
#Hint: You may use a custom key which uses a custom function to
#extract the last element from a tuple
def zWordMiddle(string):

    match = re.search(r'\b\w+z\w+\b',string)
    if match:
        return re.findall(r'\b\w+z\w+\b',string)
    else:
        return []
    


    
    #fill in your code here
    #return


#4. ConvertDate
#Given a string, return a new string where date of yyyy-mm-dd format was converted to dd-mm-yyyy format.
#Example:
#Given string: 'Next solar eclipse will occur on 2019-07-02. Next lunar eclipse will occur on 2018-07-27'
#Return: 'Next solar eclipse will occur on 02-07-2019. Next lunar eclipse will occur on 27-07-2018'
def ConvertDate(string):
    
    match = re.search(r'(\d{4})\-(\d{1,2})\-(\d{1,2})',string)
    if match:
        return re.sub(r' (\d{4})\-(\d{1,2})\-(\d{1,2})', r' \3-\2-\1', string)

    
    #fill in your code here
    #return


#Below test() function is used in main() to print
#what each function returns vs. what it's supposed to return.
def test(returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = 'NOK '
    print ('%s returned: %s expected: %s' % (prefix, repr(returned), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('1. Findabbb')
    test(Findabbb('one two three ab abb abbb abbba'), 'abbb')
    test(Findabbb('abc 12 23'), '')
    test(Findabbb('abb abbb abbba one two three ab'), 'abbb')

    print()
    print('2. zWord')
    test(zWord('abc zap xyz aba smart zic'), ['zap', 'xyz', 'zic'])
    test(zWord('abc xap xyx aba smart xic'), [])
    test(zWord('there is a zebra at the horizon'), ['zebra', 'horizon'])
  
    print()
    print('3. zWordMiddle')
    test(zWordMiddle('abc azp xyz aba smart zic'), ['azp'])
    test(zWordMiddle('there is a zebra at the horizon'), ['horizon'])
    test(zWordMiddle('there are a dozen of zebras at the horizon'), ['dozen', 'horizon'])
    test(zWordMiddle('no words can be found here'), [])

    print()
    print('4. ConvertDate')
    test(ConvertDate('Next solar eclipse will occur on 2019-07-02. Next lunar eclipse will occur on 2018-07-27'), 'Next solar eclipse will occur on 02-07-2019. Next lunar eclipse will occur on 27-07-2018')
    test(ConvertDate('Please return the book with IBAN 20-2019-03-12 until 2019-07-02.'), 'Please return the book with IBAN 20-2019-03-12 until 02-07-2019.')


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

