#!/usr/bin/python


#Basic list exercises
#You have to fill in the code for each function and
#return a variable as described in the request
#Once you finished, you may proceed with the secondary exercise



#1. SameEnds
#Given a list o strings, return the number of strings where the lenght is 2 or more and
#first and last characters are same.
#Example:
#Given list: ['abc', 'xyz', 'aba', '1221']
#Return: 2
def SameEnds(lst):
    #fill in your code here
    count = 0
    for element in lst:
        if len(element) >= 2 and element[0] == element[-1]:
            count += 1
    return count


#2. StartZ
#Given a list of strigs, return a list with the strings in sorded order, except group
#all the strings that start with 'z' first.
#Hint: You may concatenate two sorted lists.
#Example:
#Given list: ['abc', 'zap', 'xyz', 'aba', 'mars', 'zic']
#Return: ['zap', 'zic', 'aba', 'abc', 'mars', 'xyz']
def StartZ(lst):
    lst1 = []
    lst2 = []
    for element in lst:
        if element[0] == 'z':
            lst1.append(element)
            lst1.sort()

        else:
            lst2.append(element)
            lst2.sort()
    lst = lst1+lst2
    #fill in your code here
    return lst



#3. SortLast
#Given a list with non-empty tuples, return a list sorted in increasing order by the last element in 
#each tuple.
#Example:
#Given list: [(1, 4), (3, 1), (1, 7), (2, 6), (4, 9, 2)]
#Return: [(3, 1), (4, 9, 2), (1, 4), (2, 6), (1, 7)]
#Hint: You may use a custom key which uses a custom function to extract the last element from a tuple
def SortLast(lst):
    #fill in your code here
    return


#4. RemoveDuplicates
#Given a list with string elements, write a program to return a list without duplicates, sorted.
#Hint: You may use set(), list() and sort() function
#Example:
#Given List: ['a', 'ab', 'bbb', 'a', 'ab', 'zzz']
#Return: ['a', 'ab', 'bbb', 'zzz']
def RemoveDuplicates(lst):
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
    print('1. SameEnds')
    test(['abc', 'xyz', 'aba', '1221'], SameEnds(['abc', 'xyz', 'aba', '1221']), 2)
    test(['abc', 'xyz', '1223'], SameEnds(['abc', 'xyz', '1223']), 0)
    test(['', 'aaaa', 'xxxxxx', 'test'], SameEnds(['', 'aaaa', 'xxxxxx', 'test']), 3)

    print()
    print('2. StartZ')
    test(['abc', 'zap', 'xyz', 'aba', 'mars', 'zic'], StartZ(['abc', 'zap', 'xyz', 'aba', 'mars', 'zic']), ['zap', 'zic', 'aba', 'abc', 'mars', 'xyz'])
    test(['ccc', 'bbb', 'aaa', 'zac', 'zzz', 'ddd'], StartZ(['ccc', 'bbb', 'aaa', 'zac', 'zzz', 'ddd']), ['zac', 'zzz', 'aaa', 'bbb', 'ccc', 'ddd'])
    test(['caz', 'zzz', 'zaa', 'aaa', 'ccc', 'dad'], StartZ(['caz', 'zzz', 'zaa', 'aaa', 'ccc', 'dad']), ['zaa', 'zzz', 'aaa', 'caz', 'ccc', 'dad'])
  
    print()
    print('3. SortLast')
    test([(1, 4), (3, 1), (1, 7), (2, 6), (4, 9, 2)], SortLast([(1, 4), (3, 1), (1, 7), (2, 6), (4, 9, 2)]), [(3, 1), (4, 9, 2), (1, 4), (2, 6), (1, 7)])
    test([(1, 4), (3, 1), (1, 7)], SortLast([(1, 4), (3, 1), (1, 7)]), [(3, 1), (1, 4), (1, 7)])
    test([(1, 7), (3, 2), (1, 1)], SortLast([(1, 7), (3, 2), (1, 1)]), [(1, 1), (3, 2), (1, 7)])

    print()
    print('4. RemoveDuplicates')
    test(['a', 'ab', 'bbb', 'a', 'ab', 'zzz'], RemoveDuplicates(['a', 'ab', 'bbb', 'a', 'ab', 'zzz']), ['a', 'ab', 'bbb', 'zzz'])
    test(['zz', 'aa', 'bbb', 'a', 'bbb', 'zzz'], RemoveDuplicates(['zz', 'aa', 'bbb', 'a', 'bbb', 'zzz']), ['a', 'aa', 'bbb', 'zz', 'zzz'])
    test(['aaa', 'zz', 'aa', 'zz', 'z', 'zzz'], RemoveDuplicates(['aaa', 'zz', 'aa', 'zz', 'z', 'zzz']), ['aa', 'aaa', 'z','zz', 'zzz'])


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

