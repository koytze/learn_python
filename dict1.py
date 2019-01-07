#!/usr/bin/python


'''#Dictionaries exercises'''


'''#1. AddItemToDict
#Given a dictionary and a tuple item as parameters,
#return a dictionary with the new item added.
#Example:
#Given dictionary: {2:10,3:9,4:8,5:7,6:5} and item (11,11)
#Return: {2: 10, 3: 9, 4: 8, 5: 7, 6: 5, 11: 11}'''

def AddItemToDict(dictionary, item):
    if len(item) > 0:
        dictionary[item[0]] = item[1]
    #fill in your code here
    return dictionary


'''#2. JoinDictionary
#Given three dictionaries, return a dictionary to concatenate all three 
#dictionaries into a new one.
#Example:
#Given dictionaries: {1: 10, 2: 20} {3: 30, 4: 40} {5: 50, 6: 60}
#Return: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''

def JoinDictionary(dict1, dict2, dict3):
    dictionary = {}
    dictionary.update(dict1)
    dictionary.update(dict2)
    dictionary.update(dict3)
    
       
    #fill in your code here
    return dictionary



'''#3. GenerateDictionary
#Given a number n as parameter, return a dictionary with pairs (x, x*x) where 
#x is in range(1,n).
#Example:
#Given number: 4
#Return: {1: 1, 2: 4, 3: 9, 4: 16}'''

def GenerateDictionary(n):
    x = 1
    dic = {}
    while x in range(1,n+1):
        dic[x] = x*x
        x += 1
    #fill in your code here
    return dic

'''#4. JoinSumDictionary
#Given two dictionaries, return a new dictionary which includes items 
#from dict1 and dict2.
#For keys which are common to both dictionaries, sum up the values
#Example:
#Given dictionaries: 
#dict1 = {'a': 100, 'b': 200, 'c': 300}
#dict2 = {'a': 300, 'b': 100, 'd': 500}
#Return: {'a': 400, 'b': 300, 'c': 300, 'd': 500}'''

# def JoinSumDictionary(dict1, dict2):
#     dictionary = {}
#     for k1,v1 in dict1.items():
#         if dict2.get(k1) == True:
#             print(dict1.get(k1),dict2.get(k1))
#     #fill in your code here
#     return dictionary

def JoinSumDictionary(dict1, dict2, fn:  = lambda x, y: x + y):
    res = dict1.copy()  # "= dict(d1)" for lists of tuples
    for key, val in dict2.iteritems():  # ".. in d2" for lists of tuples
        try:
            res[key] = fn(res[key], val)
        except KeyError:
            res[key] = val
    return res


'''#Below test() function is used in main() to print
#what each function returns vs. what it's supposed to return.'''

def test(in_data, returned, expected):
    if returned == expected:
        prefix = ' OK '
    else:
        prefix = 'NOK '
    print ('%s- Input data: %s. Returned: %s Expected: %s' % (prefix, in_data, repr(returned), repr(expected)))


'''# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.'''

def main():
    print('1. AddItemToDict')
    test(({2: 10, 3: 9, 4: 8, 5: 7, 6: 5}, (11, 11)), AddItemToDict({2: 10, 3: 9, 4: 8, 5: 7, 6: 5}, (11, 11)), {2: 10, 3: 9, 4: 8, 5: 7, 6: 5, 11: 11})
    test(({2: 10, 3: 9, 4: 8, 5: 7, 6: 5}, ()), AddItemToDict({2: 10, 3: 9, 4: 8, 5: 7, 6: 5}, ()), {2: 10, 3: 9, 4: 8, 5: 7, 6: 5})
    test(({2: 10, 3: 9, 4: 8, 5: 7, 6: 5}, ('a', 'c')), AddItemToDict({2: 10, 3: 9, 4: 8, 5: 7, 6: 5}, ('a', 'c')), {2: 10, 3: 9, 4: 8, 5: 7, 6: 5, 'a': 'c'})

    print()
    print('2. JoinDictionary')
    test(({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}), JoinDictionary({1: 10, 2: 20}, {3: 30, 4: 40}, {5: 50, 6: 60}), {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60})
    test(({}, {1: 2, 3: 'c', 4: 'b'}, {6: 'e', 7: 'h', 'z': 'z'}), JoinDictionary({}, {1: 2, 3: 'c', 4: 'b'}, {6: 'e', 7: 'h', 'z': 'z'}), {1: 2, 3: 'c', 4: 'b', 6: 'e', 7: 'h', 'z': 'z'})
    test(({}, {}, {}), JoinDictionary({}, {}, {}), {})
  
    print()
    print('3. GenerateDictionary')
    test(4, GenerateDictionary(4), {1: 1, 2: 4, 3: 9, 4: 16})
    test(5, GenerateDictionary(5), {1: 1, 2: 4, 3: 9, 4: 16, 5: 25})
    test(0, GenerateDictionary(0), {})

    print()
    print('4. JoinSumDictionary')
    test(({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 100, 'd': 500}), JoinSumDictionary({'a': 100, 'b': 200, 'c': 300}, {'a': 300, 'b': 100, 'd': 500}), {'a': 400, 'b': 300, 'c': 300, 'd': 500})
    test(({'a': 100, 'c': 200, 'd': 300}, {'a': 300, 'e': 100, 'f': 500}), JoinSumDictionary({'a': 100, 'c': 200, 'd': 300}, {'a': 300, 'e': 100, 'f': 500}), {'a': 400, 'c': 200, 'd': 300, 'e': 100,  'f': 500})
    test(({},{}), JoinSumDictionary({},{}), {})
    
'''# Standard boilerplate to call the main() function.'''
if __name__ == '__main__':
    main()

