#!/usr/bin/python


#Additional string exercises


#5. AddString
#Given a string, if its length is at least 3
#add 'ing' at the end.
#However, if the string already ends in 'ing', then add 'ly'.
#If the length is smaller than 3, leave it unchanged.
#Example:
#Given string: 'say'
#Return: 'saying'
#Given string: 'fishing'
#Output: 'fishingly'
#Given string: 'be'
#Output: 'be'
def AddString(text):
    #fill in your code here

    if len(text) >= 3:
        if text[-3:] == 'ing':
            text += 'ly'
        else:
            text += 'ing'
            
        return text
    
    else:
        return text


#6. NotBad
#Given a string text, find the first appearange of the substring 'not' and 'bad'.
#If 'bad' follows 'not', replace the whole 'not' .. 'bad' substring with 'good' 
#and return the resulting string.
#Example:
#Given text: 'The food is not so bad!'
#Return: 'The food is good!'
#Given text: 'The offer is not that bad'
#Return: 'The offer is good'
#Given text: 'Outside is not so cold'
#Return: 'Outside is not so cold'
def NotBad(text):
    #fill in your code here

    p_not = text.find('not')
    p_bad = text.find('bad')

    
    if p_not >= 0:
        r_not = text[p_not:p_not+3]
        
    elif p_bad >= 0:
        r_bad = text[p_bad:p_bad+3]
    
    else:
        return text

    if r_not < 0 or r_bad < 0:
        if r_not < r_bad:
            return text.replace('text[p_not:r_bad+1]','good')
    
    #return
    


#7. MultiplySuffix
#Given a string text, return a string made of 4 copies of last two characters of given string
#Example:
#Given string: 'Python'
#Return: 'onononon'
#Given string: 'Exercise'
#Return: 'sesesese'
def MultiplySuffix(text):
    #fill in your code here
    return


#8. FrontBack
#Consider dividing a string into two halves.
#If the length is even, the front and back halves are the same length.
#If the lenght is odd, we'll say that the extra char goes in the front half.
#Example: 'munte', the front half is 'mun', the second half is 'te'
#Given two strings, a and b, return a string of the form
#a-front+b-front+a-back+b-back
#Given strings: 'master' 'race'
#Return: 'masraterce'
#Given strings: 'micro' 'wave'
#Return: 'micwarove'
def FrontBack(text1, text2):
    #fill in your code here
    return


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
    print('5. AddString')
    test('say', AddString('say'), 'saying')
    test('fishing', AddString('fishing'), 'fishingly')
    test('sa', AddString('sa'), 'sa')
    test('testing', AddString('testing'), 'testingly')

    print()
    print('6. NotBad')
    test('The food is not so bad!', NotBad('The food is not so bad!'), 'The food is good!')
    test('The offer is not that bad', NotBad('The offer is not that bad'), 'The offer is good')
    test('Outside is not so cold', NotBad('Outside is not so cold'), 'Outside is not so cold')
    test('Smile and wave!', NotBad('Smile and wave!'), 'Smile and wave!')

  
    print()
    print('7. MultiplySuffix')
    test('Python', MultiplySuffix('Python'), 'onononon')
    test('Exercise', MultiplySuffix('Exercise'), 'sesesese')
    test('Trainee', MultiplySuffix('Trainee'), 'eeeeeeee')
    test('Hi!', MultiplySuffix('Hi!'), 'i!i!i!i!')

    print()
    print('8. MultiplySuffix')
    test(('master', 'race'), FrontBack('master', 'race'), 'masraterce')
    test(('micro', 'wave'), FrontBack('micro', 'wave'), 'micwarove')
    

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

