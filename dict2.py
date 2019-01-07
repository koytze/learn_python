#!/usr/bin/python


#More dictionary exercises


#5. StrToDict
#Given a string, return a dictionary where key is each unique letter in the string
#and value is the occurance number of the letter in the string.
#Example:
#Given string: 'Ericsson'
#Return: {'E': 1, 'r': 1, 'i': 1, 'c': 1, 's': 2, 'o': 1, 'n': 1}
string = 'Ericsson'
def StrToDict(dictionary):
    final_dictionary = {}
    for letter in set(string):
        final_dictionary[letter] = string.count(letter)
    #fill in your code here
    return final_dictionary


#6. CombineDictValues
#Given a list of dictionary values combine data into one dictionary.
#Example:
#Given list: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
#Return: {'item1': 1150, 'item2': 300}
def CombineDictValues(dictionary):
    final_d = {}
    for d in input_list:
        k_,v_ = None,None
        for k,v in d.items():
            if type(v) is str:
                k_ = v
            if type(v) is int:
                v_ = v
        if k_ in final_d:
            final_d[k_] = v_+final_d[k_]
        else:
            final_d[k_] = v_
    
    #fill in your code here
    return final_d



#Below test() function is used in main() to print
#what each function returns vs. what it's supposed to return.
def test(in_data, returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = 'NOK '
    print ('%s- Input data: %s.\nReturned: %s Expected: %s' % (prefix, in_data, repr(returned), repr(expected)))


# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
    print('5. StrToDict')
    test('Ericsson', StrToDict('Ericsson'), {'E': 1, 'r': 1, 'i': 1, 'c': 1, 's': 2, 'o': 1, 'n': 1})
    test('This is a Python Class', StrToDict('This is a Python Class'), {'T': 1, 'h': 2, 'i': 2, 's': 4, ' ': 4, 'a': 2, 'P': 1, 'y': 1, 't': 1, 'o': 1, 'n': 1, 'C': 1, 'l': 1})
    test('dictionary', StrToDict('dictionary'), {'d': 1, 'i': 2, 'c': 1, 't': 1, 'o': 1, 'n': 1, 'a': 1, 'r': 1, 'y': 1})

    print()
    print('6. CombineDictValues')
    test([{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}], CombineDictValues([{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]), {'item1': 1150, 'item2': 300})
    test([{'type': 'phone', 'price': 300}, {'type': 'laptop', 'price': 1300}, {'type': 'phone', 'price': 700}], CombineDictValues([{'type': 'phone', 'price': 300}, {'type': 'laptop', 'price': 1300}, {'type': 'phone', 'price': 700}]), {'phone': 1000, 'laptop': 1300})
  
    
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

