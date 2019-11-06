

################################################################### 
#Question 1
################################################################### 
def lbs2kg(w):
    x=w/2.2046226218
    return(x)
################################################################### 
#Question 2
################################################################### 
def id_formater(fn, ln, appelation, city, year):
    x='' + appelation +'. ' + ln+', '+fn +' ('+ city+ ', ' + str(year) +')'
    return(x)
################################################################### 
#Question 3
################################################################### 
def limerick_maker():
    x = input('What is your name: ')
    y = input('What is your city of birth: ')
    print ('There once was a computer named pie \nWho '+ x + ' would always make cry \n' +y+ ' was his home \nNow',
           x,'is alone \nNow pie is', x+'\'s only main guy')
    return
################################################################### 
#Question 4
################################################################### 
def id_formater_display():
    a = input('What is your first name? ')
    b = input('What is your last name? ')
    c = input('What is your appelation? ')
    d = input('What is your city name? ')
    e = input('What is the year:')
    return(str(id_formater(a,b,c,d,e)))
################################################################### 
#Question 5
################################################################### 
def l2loz(w):
    o = w % 1
    l =  w - o
    o = o * 16
    return (int(l),o)

################################################################### 
#Question 6
################################################################### 
def convert_days_to_YY_MM_DD(days):
    days =  days
    months = days//30
    years = days //360
    months = months - (12*years)
    days = days -(30*months)-(360*years)
    print(("Year: " + str(years)+', '+ "Month: " + str(months)+', '+ "Day: " + str(days)))
    return

################################################################### 
#Question 7
################################################################### 
def median3(num1,num2,num3):
    print(str(num1)+ ' is a median. That is '+ str(num2 >= num1 >= num3 or num3 >= num1 >= num2))
    print(str(num2)+' is a median. That is ' + str(num1 >= num2 >= num3 or num3 >= num2 >= num1))
    print(str(num3)+' is a median. That is ' + str(num1 >= num3 >= num2 or num2 >= num3 >= num1))
    return 

################################################################### 
#Question 8
################################################################### 
def below_parabola(a,b,p,q):
    
    return(q <= a*(p**2)+ b)
################################################################### 
#Question 9
################################################################### 
def projected_grade(a1,A1,a2,A2,m,M):
    x = a1/A1
    y = a2/A2
    z = (x+y)/2
    p = m/M
    F = p
    PG = ((x*5)+ (y *5)+ (z*5)+( p*35) + (p*50))
    return(PG)

################################################################### 
#Question 10
################################################################### 
def projected_grade_v2():
    a1= int(input('How many points did you get in Assignment 1? '))
    A1 = int(input('What was the maximum possible number of points for Assignment 1? '))
    a2 = int(input('How many points did you get in Assignment 2? '))
    A2 = int(input('What was the maximum possible number of points for Assignment 2? '))
    m = int(input('How many points did you get on the midterm? '))
    M = int(input('What was the maximum possible number of points for the midterm? '))



    
    x = (a1/A1)
    y = (a2/A2)
    z = ((x+y)/2)
    p = (m/M)
    F = p
    PG = ((x*5)+ (y *5)+ (z*5)+( p*35) + (p*50))
    if p < 0.50 and p < (PG/100):
        print('Your predicted final grade is '+ str(p*100)+'%')
    elif p < 0.50 and p > (PG/100):
        print('Your predicted final grade is '+ str(PG)+'%')
    else:
        print('Your predicted final grade is '+ str(PG)+'%')
    return
################################################################### 
#Question 11
###################################################################
import math
def change_to_coins(x):
    a= math.ceil(x*100)
    q = a//25
    y = a - (q*25)
    d = y//10
    b = y - (10*d)
    n = b//5
    p = b - (n*5)
    return((q,d,n,p))

    

    
    
    
