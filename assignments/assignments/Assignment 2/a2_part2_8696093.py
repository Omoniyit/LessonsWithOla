###################################################################
 # Question 1
###################################################################
import math 

def size_format(b):
    '''(integer) -> number
    Returns a readable string representation of this number of bytes. 
    The representation uses the metric units of bytes (B), kilobytes (KB), megabytes (MB)
    gigabytes (GB), and terrabytes (TB) and includes 1 significant decimal place

    >>> size_format(623) 
    '623B'
    >>> size_format(1500)
    '1.5KB'


    '''
    b = float(b)

    if b < 0:
        print('buy a new a hard disk')

    elif b > 0 and b < 1000.00:
        print ( '%d B' % (b))

    elif b > 1000.00 and b < 10.00**6:
        print ('%.1f KB' % ( (b/10.00**3)))

    elif b > 10**6 and b < 10**9:
        print('%.1f MB' % ( (b/10.00**6)))

    elif b > 10**9 and b < 10**12:
        print('%.1f GB' % ( (b/10.00**9)))
    
    elif b > 10**12: 
        print('%.1f TB' % ( (b/10.00**12)))

###################################################################
 # Question 2
###################################################################

def add_article(s):
    '''(string) -> string

    Takes as input a string s containing a name of a country
    and returns a string with article added.

    >>> add_article("Canada")
    'le Canada'
    >>> add_article("Cambodge")
    'le Cambodge'
    >>> add_article("Belgique")
    'la Belgique'

    '''
    length = len(s)
    e_or_no = s[length-1]
    a = s[0]
    if s[0].lower() == 'a' or s[0].lower() == 'e' or s[0].lower() == 'i' or s[0].lower() == 'o' or s[0].lower() == 'u':
        print('l\'' + s)
    elif s.lower() == 'canada' or s.lower() == 'cambodge':
        print('le ' + s)
    elif s.lower() == 'belgique':
        print('la ' + s)
    elif s.lower() == 'etas-unis' or s.lower() == 'pay-bas':
        print('les ' + s)
    elif e_or_no == 'e':
        print('la ' + s)
    else:
        print('le ' + (s))

###################################################################
 # Question 3
###################################################################

def factorial(n):
    '''(integer) -> integer
    Takes as input one number, n,
    and returns the value n*(n-1)*(n-2)*…*2*1

    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120

    '''
    score = 1
    while(n>0):
        score = score*n
        n = n - 1
    return score
###################################################################
 # Question 4
###################################################################
def special(x):

    count = 0
    if x <0:
        count =+ 0
    elif x%100 == 0 and x%400 == 0:
        count += 1

    elif x%100 == 0 and x%400 != 0:
        count += 0
    
    elif x >= 0 and x%4 == 0:
        count += 1
    
    else:
        count += 0
        

    return count
def special_count(a):
    '''(list) -> integer
    
    Takes as input a non-empty a of integers and returns the number of special
    numbersit contains (* A special number is non-negative and divisible by four,
    except that anynone-negative integer divisible by 100 is not special unless it
    is also divisible by 400)

    >>> special_count([2020, 600, 800, 22])
    2
    
    >>> special_count([44,-1200,100, 0])
    2


    '''
    score = 0
    length = len(a)
    for i in range(length):
        if special(a[i]) >= 1:
            score = score + 1
        

    print (score)
###################################################################
 # Question 5
###################################################################    
def vote():
    '''(string) -> string

    Takes input values of Yes, no or abstained and tallies them in order
    to decide whether or not the proposal passes.

    >>> vote()
    Enter the yes, no, abstained votes one by one and then press enter:
    yes Yes yes yes Y abstained abstained y yes yes yes
    proposal passes unanimously
    
    >>> vote()
    Enter the yes, no, abstained votes one by one and then press enter:
    abstained no abstained yes no yes no yes yes yes no
    proposal passes with simple majority
    
    >>> vote()
    Enter the yes, no, abstain votes one by one and then press enter:
    no yes no no no, yes yes yes no
    proposal fails

    
    
    '''
    a = str(input('Enter the yes, no, abstained votes one by one and then press enter:\n'))
    length = len(a)
     #To find out the number of Yes' and Nos in the string
    a = a.lower()
    count_y = a.count("y")
    count_a = a.count("abstained")
    count_n = a.count("n")
    n = count_y + count_n - count_a
    #since count_a includes count_n
    if ((count_n -count_a)/n) > (count_y/n):
        print('proposal fails')
    elif (count_y/n) == 1:
        print('proposal passes unanimously')
    elif (count_y/n) >= (2/3):
        print('proposal passes with super majority')
    elif(count_y/n) > (1/2):
        print('proposal passes with simple majority')

###################################################################
 # Question 6
###################################################################
import random
def stats_v1(n):
    '''(integer) -> integer

    Takes as input a positive integer n, produces n random integers in the
    range [-100, 100], and prints all those integers, the minimum of all those
    integers and the average of all those integers.

    >>> stats_v1(3)
    The minimum and the average of the following numbers:
    72 12 33 
    is 12 and 39

    >>> stats_v1(3)
    The minimum and the average of the following numbers:
    92 -87 16 
    is -87 and 7.0
    
    


    '''
    list_n = [ ]
    for i in range(n):
        a = random.randint(-100,100)
        list_n = list_n + [a]
    length = len(list_n)    
    print('The minimum and the average of the following numbers:')
    for i in range(length):
        print(list_n[i],end=' ')
        
    print('\nis ' + str(min(list_n))+ ' and ' + str((sum(list_n))/(len(list_n))))
def stats_v2(n):
    '''(integer) -> integer

    Takes as input a positive integer n, produces n random integers in the
    range [-100, 100], and prints all those integers, the minimum of all those
    integers and the average of all those integers without using lists.

    >>> stats_v2(4)
    The minimum value and average for the following numbers:
    -78 19 -81 -72
    is -81 and -53.0

    >>> stats_v2(4)
    The minimum value and average for the following numbers:
    99 59 -65 -53
    is -65 and 10.0

    '''
    print('The minimum value and average for the following numbers:')
    min = 200
    sum = 0
    for i in range(n):
        randnum = random.randint(-100,100)
        sum += randnum
        if randnum < min:
            min = randnum
        if i < n-1:
            print(randnum, end=' ')
        else:
            print(randnum)
    print('is',min, 'and',(sum/n))        
###################################################################
 # Question 7
###################################################################    
def emphasize(s):
    '''(string) -> string
    Takes as an input a string s and returns a string with a blank space
    inserted between every pair of consecutive characters in s

    >>> emphasize('v')
    'v'
    >>> emphasize('  song ?  tr a ')
    '    s o n g   ?     t r   a  '
    >>> emphasize('')
    ''
    >>> emphasize('very important')
    'v e r y   i m p o r t a n t'
    >>> emphasize(' really?')
    '  r e a l l y ?'


    '''
    
    newword = ""
    
    for i in range (len(s)):
        newword = newword + s[i] + ' '
        
    return(newword)
###################################################################
 # Question 8
###################################################################      
def crypto(s): 
    '''(string) -> string
    
    Takes a string s and returns an encrypted string which is the
    last term of the string then first looping until the middle.
    
    >>> crypto('Good Day')
    'yGaoDo d'
    >>> crypto('Good Days')
    'sGyoaoDd '
    >>> crypto(',4?tr')
    'r,t4?'

    '''
  
    if len(s)%2 == 0:
        n = len(s) - 1
        i = -1
        a = ''
        while n!= i:
            i = i + 1
            a += s[n]
            a= a+ s[i]
            n = n -1
        return a
    else:

        n = len(s)-1
        middle = (len(s)//2)
        i = 0
        a = ''
        while n!= i :
        
            a = a +  s[n]
            a = a + s[i]
            n = n-1
            i = i +1
        a = a + s[middle]
    return a
    
###################################################################
 # Question 9
###################################################################          
def stranger_things(l1,l2):
    '''(list,list) -> bool
    Takes two non-empty equal lists(l1,l2) and compares the even and odd indexes
    of the list.If the even positions are equal and all odd positions are
    not equal the function returns True or else the function returns False. 

    >>> stranger_things([1],[2,"aha"])
    False
    >>> stranger_things([1,2,True, '7'],[1,False,True,5])
    True
    '''
    n_l1 = len(l1)
    n_l2 = len(l2)
    if n_l1 != n_l2:
        return(n_l1 == n_l2)
    elif n_l1==0 or n_l2 ==0:
        return 
    else:
        
        for i in range(0,n_l1,2):
            

            if l1[i] != l2[i]:
                
                return l1[i] == l2[i]
            

                

        for i in range(1,n_l1,2):
            if l1[i] == l2[i]:
                return(l1[i] != l2[i])

        return(n_l1 == n_l2)
   
    
        
        
     
         
