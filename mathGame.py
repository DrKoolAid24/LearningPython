'''
Created on Oct 14, 2015

@author: scott.kilker
'''
from myPythonFunctions import getUserPoint, generateQuestion
from myPythonFunctions import updateUserPoint

try:
    userName = input("Enter User Name: ")
    userScore = int(getUserPoint(userName))
    print(userScore)
    
    newUser = False
    if userScore == -1:
        newUser = True
        userScore = 0

    userChoice = 0
    while userChoice != "Quit":
        userScore += generateQuestion()
        print(userScore)
        userChoice = input("Enter 'Quit' to quit")
    updateUserPoint(newUser,userName,userScore)
except: 
    print("An Exception occurred and program will now terminate")
    

