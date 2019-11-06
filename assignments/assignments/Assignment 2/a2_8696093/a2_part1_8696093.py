import math
import random



def addi_test():
    score = 0
    n = int(input('\nHow many questions would you like to solve?\n\tEnter a non negative integer for the answer:  '))
    if n <= 0:
        print('\nGood Bye')
        return
    else:
        print('\nThis software will test you with %d questions.....'%(n))
        for i in range(n):
            num1 = random.randrange(0,9)
            num2 = random.randrange(0,9)
            question = int(input('What is the sum of '+ str(num1)+' + '+str(num2)+' ? '))
            if question == (num1 + num2):
                score = score + 1

            else:
                print('Incorrect - the answer is '+ str(num1+num2))
    result = score/n *100
    if result >= 80:
        print('\nWell done! Congratulations.\n\n Good bye')
    elif result >= 60 and result < 80:
        print('\nNot too bad but please study and practice some more.\n\nGood bye')
    else:
        print('\nPlease study more and ask your teacher for help.\n\nGood bye')

    

def multi_test():
    score = 0
    n = int(input('\nHow many questions would you like to solve?\n\tEnter a non negative integer for the answer:  '))
    if n <= 0:
        print('\nGood Bye')
        return 
    else:
        print('\nThis software will test you with %d questions.....'%(n))
        for i in range(n):
            num1 = random.randrange(0,9)
            num2 = random.randrange(0,9)
            question = int(input('What is the multiple of '+ str(num1)+' * ' +str(num2) + ' ? '))
            if question == (num1*num2):
                score = score + 1
            else:
                print('Incorrect - the answer is '+ str(num1*num2))
    result = int(score/n *100)
    if result >= 80:
        print('\nWell done! Congratulations. \n\nGood bye')
    elif result >= 60 and result < 80:
        print('\nNot too bad but please study and practice some more.\n\nGood bye')
    else:
        print('\nPlease study more and ask your teacher for help.\n\nGood bye')
    
    
def perform_test(x):

    if x.upper() == 'M' :
        multi_test()
    elif x.upper() == 'A' :
        addi_test()
    else:
        print('Sorry that is not a valid input')

choice = input('Welcome to addition / multiplication test \nPlease make a selection\nA or a for Addition\nM or m for multiplication\nMake a selection : ')
if choice == 'm' or choice == 'M' or choice == 'a' or choice == 'A':
    perform_test(choice)
else:
    
    print('WRONG OPERATION, PLEASE TRY AGAIN \n\nGood bye')




