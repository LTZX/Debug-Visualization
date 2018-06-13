
import sys

with open("terminalout1.txt") as f:
   word=[line.split() for line in f]
#ff=open("terminalout1.txt","r")
#flines=ff.readlines()
#linecount=len(flines)
testnum=0
bugnum=0
for i in range(len(word)):
   if(word[i]!=[]):
      if(word[i][0] == 'Tests'):
         if(word[i][1] == 'run:'):
            testnum=int(word[i][2].strip(','))
            bugnum=int(word[i][4].strip(','))

index=0
failureinfo=[None]*bugnum
failurecontent=[None]*bugnum
j=0
k=0
if(bugnum>0):
   for i in range(len(word)):
      if(word[i]!=[]):
         if(word[i][0] == 'Failed'):
            if(word[i][1] == 'tests:'):
               index=i+1
   for i in range(index,index+bugnum): #failureinfo[][0]:file name; [][1]:method name; [][2]:line number 
      failureinfo[j]=[word[i][0][:word[i][0].find("Test.test")]]
      methodname=word[i][0][word[i][0].find("Test.test"):word[i][0].find("Search")].strip("Test.test")
      failureinfo[j].append(methodname)
      failureinfo[j].append(word[i][0][word[i][0].find(":"):].strip(':'))
      j=j+1

   for i in range(index,index+bugnum):
      failurecontent[k]=" ".join(word[i]) #get failure content
      k=k+1
#print(testnum)
#print(bugnum)
"""
for i in range(bugnum):
   print(failureinfo[i])
   print(failurecontent[i])
"""
project={}
project['number-of-tests']=testnum
project['number-of-bugs']=bugnum
bug={}
#for i in range(bugnum):
#   bug[str(i)]={}
e1={}
e2={}
e1['file-name']=failureinfo[0][0]
e1['method-name']=failureinfo[0][1]
e1['line-number']=failureinfo[0][2]
e1['bug-detail']=failurecontent[0]
e2['file-name']=failureinfo[1][0]
e2['method-name']=failureinfo[1][1]
e2['line-number']=failureinfo[1][2]
e2['bug-detail']=failurecontent[1] 
bug['0']=e1
bug['1']=e2
print("project=")
print(project)
print("bug=")
print(bug)
