#!/usr/bin/python
import re

#Please write the program which will open the file httperr1.log,
#will identify the lines with Timer_ConnectionIdle error only for
#IPv4 connections and will print:
#HH:MM:SS IPv4:port IPv4:port

#Hint:
#1. You will need to import re module
#2. You may need to parse the file line by line .readlines()
#3. You may use groups to separate time,IPv4 and port values

f = open(r'C:\Users\eionepe\__DOCS\Personal\Python\exercises\httperr1.log','r')
g = open(r'C:\Users\eionepe\__DOCS\Personal\Python\exercises\ouutput.log','w')

text = f.readlines()

#regex = r'(\d\d\d\d-\d\d-\d\d) (\d\d:\d\d:\d\d) (\d+?\.\d+?\.\d+?\.\d+?) (\d+?) (\d+?\.\d+?\.\d+?\.\d+?) (\d+?) .+? Timer_ConnectionIdle'

#matches = re.finditer(regex, text, re.MULTILINE)

##for matchNum, match in enumerate(matches):
##    matchNum = matchNum + 1
##    
##    print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
##    
##    for groupNum in range(0, len(match.groups())):
##        groupNum = groupNum + 1
##        
##        print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

for line in text:
      if 'Timer_ConnectionIdle' in line:
            #print(line)
            match = re.search(r'(\d\d:\d\d:\d\d) (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) (\d{1,5}) (\d+?\.\d+?\.\d+?\.\d+?) (\d+? )',line)
            if match:
                  print(match.group(1),' ', match.group(2),':',match.group(3),' ', match.group(4),':',match.group(5),sep='',file=g)
f.close()
g.close()
