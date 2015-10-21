'''
Created on Oct 14, 2015

@author: scott.kilker
'''
import sys
from random import randint
from os import rename
from os import remove

def getUserPoint(userName):
   
    try:
        f = open('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.txt','r')
    except IOError as e:
        print ("File does not exist.  Creating new file to use")
        f = open('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.txt','w')
        return -1
        
    content = []
    
    for line in f:
        content.append(line.split(','))
    
    found = None
    scoreToReturn = -1
    for x in content:
        if (x[0] == userName) :
            found = True
            scoreToReturn = x[1]
                
    f.close()
    return scoreToReturn

def updateUserPoint(newUser, userName, score):
    if newUser == True:
        try:
            f = open('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.txt','a')
            f.write('\n' + userName + ',' + str(score))
        except IOError as e:
            print("File error occurred in updateUserPoint: " + e)
    else:
        try:
            f = open('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.txt','r')
            
            content = []
            for line in f:
                oldName,oldScore = line.split(',')
                print("oldName: " + oldName)
                print("oldScore: " + oldScore)
                newLine = []
                newLine.append(oldName)
                if oldName != userName:
                    newLine.append(oldScore)
                else:
                    newLine.append(str(score) +'\n')
                content.append(newLine)
            temp = open('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.tmp','w')
            for newLine in content:
                temp.write(newLine[0] + ',' + str(newLine[1]))
            f.close()
            temp.close()
            remove('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.txt')
            rename('C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.tmp','C:\\Users\\scott.kilker\\workspace\\Learning Python\\TestSource\\userScores.txt')
        except IOError as e:           
            print("File error occurred in updateUserPoint: " + e)
                    
        
        
def generateQuestion():
    operandList = [0,0,0,0,0]
    operatorList = ['','','','']
    operatorDict = {1:'+',2:'-',3:'*',4:'**'}
        
    # populate operandList with random numbers
    for i in range(0,5):
        operandList[i] = randint(1,9)
    print (operandList)
        
    previousOperator = ''
    for i in range(0,4):
        if previousOperator == '**':
            operatorList[i] = operatorDict[randint(1,3)]
        else:
            operatorList[i] = operatorDict[randint(1,4)]
        previousOperator = operatorList[i]
    print(operatorList)
    
    questionString = ''        
    for i in range(0,4):
        questionString += str(operandList[i]) + operatorList[i]
    questionString += str(operandList[4])
    print(questionString)
    
    result = eval(questionString)
    print(result)
        
    questionString = questionString.replace("**", "^")
    print("Question: " + questionString)

    answer = input("Enter answer: ")
    
    while True:
        try:
            if int(answer) == result:
                print("Correct!")
                return 1
            else:
                print("Incorrect!")
                return 0
        except:
            print("You did not enter an integer - please try again")
            answer = input("Enter answer: ")   
