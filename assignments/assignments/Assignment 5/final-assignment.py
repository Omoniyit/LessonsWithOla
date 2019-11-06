#######################################
# Question 1a
#######################################
def largest_34(a):
    '''
    (list)-> int
    Returns the sum of the 3rd and 4th largest values in the list a
    '''
    a.sort()
    x= a[2] + a[3]
    return x

#########################################
# Question 1b
#########################################
def largest_third(a):
    '''
    (list)-> int
    Computes the sum of the len(a)//3 of the largest values in the list a
    '''
    a.sort()
    a.reverse()
    x=len(a)//3
    print (sum(a [:x]))

###########################################
# Question 1c
###########################################
def third_at_least(a):
    '''
    (list)-> int
    Returns a value that occurs at least len(a)//3 of the largest values in the list a
    '''
    for i in a:
        if a.count(i)== len(a)//3:
            return i
        else:
            return None
          
#############################################
# Question 1d
#############################################
import itertools
def sum_tri(a,x):
    '''
    (list)-> bool
    Returns True if there exists indices i, j and k (where i and j and k are not necessarily distinct) such that a[i]+a[j]+a[k]=x
    '''
    uniquelist=set(a)
    for n in itertools.combinations(uniquelist, 3):
        if n[0] + n[1] + n[2] == x:
           return True
    else:
        return False
        
            
            
        
   
