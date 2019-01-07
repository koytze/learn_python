#!/usr/bin/python


#More list exercises


#5. MergeLists
#Given two lists sorted in increasing order, return a merged list with elements sorted.
#Parse both input lists only once.
#Note: You may use pop(0)
#Example:
#Given list: ['aaa', 'ccc', 'ccc', 'zz'], ['bb', 'dd', 'mmm', 'zz']
#Return: ['aaa', 'bb', 'ccc', 'ccc', 'dd', 'mmm', 'zz', 'zz']
def MergeLists(lst1,lst2):
    #fill in your code here
    return


#6. RemoveAdjacent
#Given a list of numbers, return a list where all adjacent equal (==) elements are removed.
#Example:
#Given list: [1, 3, 4, 4, 5, 9, 9, 9]
#Return: [1, 3, 4, 5, 9]
def RemoveAdjacent(lst):
    #fill in your code here
    return



#7. MaxSum
#Given a list of lists. Return the sublist for which the sum of elements is the biggest.
#Example:
#Given list: [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]
#Return: [10, 11, 12]
def MaxSum(lst):
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
    print('5. MergeLists')
    test((['aaa', 'ccc', 'ccc', 'xx'], ['bb', 'dd', 'mmm', 'zz']), MergeLists(['aaa', 'ccc', 'ccc', 'xx'], ['bb', 'dd', 'mmm', 'zz']), ['aaa', 'bb', 'ccc', 'ccc', 'dd', 'mmm', 'xx', 'zz'])
    test((['a', 'x', 'z'], ['b', 'c', 'd']), MergeLists(['a', 'x', 'z'], ['b', 'c', 'd']), ['a', 'b', 'c', 'd', 'x', 'z'])
    test((['a', 'a'], ['a','b']), MergeLists(['a', 'a'], ['a','b']), ['a', 'a', 'a', 'b'])

    print()
    print('6. RemoveAdjacent')
    test([1, 3, 4, 4, 5, 9, 9, 9], RemoveAdjacent([1, 3, 4, 4, 5, 9, 9, 9]), [1, 3, 4, 5, 9])
    test([1, 2, 2, 2, 3, 2], RemoveAdjacent([1, 2, 2, 2, 3, 2]), [1, 2, 3, 2])
    test([], RemoveAdjacent([]), [])
  
    print()
    print('7. MaxSum')
    test([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]], MaxSum([[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]), [10, 11, 12])
    test([[1, 4], [1, 2, 3], [1, 2]], MaxSum([[1, 4], [1, 2, 3], [1, 2]]), [1, 2, 3])
    test([[1, 7], [3, 2], [1, 1]], MaxSum([[1, 7], [3, 2], [1, 1]]), [1, 7])


# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

