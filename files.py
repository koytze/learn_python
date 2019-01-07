#!/usr/bin/python


#Basic file i/o exercises
#You have to fill in the code for each function.



#1. Display top N lines of a file
#Your function receive as parameters: path of input file and n, the number of lines
#Write the rest of the code to display the top n lines from the input_file
#Append in front of each line, the line number.
def PrintLinesFromFile(input_file,n):
    #fill in your code here
    return

#2. Find longest word in the file
#Your function receives as parameter path of input file and should display the
#longest word found in the file. If multiple words have the same, maximum, length,
#display all of them.
def LongestWord(input_file):
    #fill in your code here
    return



#3. Copy content
#Your function receives as parameters path of input file and output file.
#Write the code as to copy the text from the input file and to write it to output file.
def CopyContent(input_file,output_file):
    #fill in your code here
    return


def main():
#call your functions from here
    PrintLinesFromFile('ceo.txt',10)
    LongestWord('ceo.txt')
    CopyContent('ceo.txt','ceo_copy.txt')

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
    main()

