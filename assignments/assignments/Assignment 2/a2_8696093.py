import math
import random



def addi_test():
    score = 0
    n = int(input('How many questions would you like to solve? '))
    for i in range(n):
        num1 = random.randrange(0,9)
        num2 = random.randrange(0,9)
        question = input('What is the sum of'+ str(num1)+'+'+str(num2))
        if question == (num1 + num2):
            score = score + 1

        else:
            print('Sorry that is the incorrect value the correct answer was: '+ str(num1+num2))
    result = score/n *100
    if result >= 80:
        print('Well done! Congratulations.')
    elif result >= 60 and result < 80:
        print('Not too bad but please study and practice some more.')
    else:
        print('Please study more and ask your teacher for help.')

def multi_test():
    score = 0
    n = int(input('How many questions would you like to solve? '))
    for i in range(n):
        num1 = random.randrange(0,9)
        num2 = random.randrange(0,9)
        question = input('What is the multiple of'+ str(num1)+'*' +str(num2) + '?')
        if question == (num1*num2):
            score = score + 1

        else:
            print('Sorry that is the incorrect value the correct answer was: '+ str(num1*num2))
    result = int(score/n *100)
    if result >= 80:
        print('Well done! Congratulations.')
    elif result >= 60 and result < 80:
        print('Not too bad but please study and practice some more.')
    else:
        print('Please study more and ask your teacher for help.')
    
def perform_test(x):

    if x.upper() == 'M' :
        multi_test()
    elif x.upper() == 'A' :
        addi_test()
    else:
        print('Sorry that is not a valid input'

choice = input('Would you like to practice multiplication or addition? (M/A):
perform_test(choice)




