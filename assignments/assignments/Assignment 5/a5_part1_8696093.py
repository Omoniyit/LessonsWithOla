#############################################
# Question 1a
#############################################
def largest_34(a):
    '''
    (list)-> int
    Returns the sum of the 3rd and 4th largest values in the list a
    '''
    a.sort()
    a.reverse()
    print (a[2] + a[3])
#############################################
# Question 1b
#############################################
def largest_third(a):
    '''
    (list)-> int
    Computes the sum of the len(a)//3 of the largest values in the list a
    '''
    a.sort()
    a.reverse()
    val = 0
    for i in range((len(a)//3)):
        val+= a[i]

    print(val)
#############################################    
# Question 1c
#############################################
def third_at_least(a):
    '''
    (list)-> int
    Returns a value that occurs at least len(a)//3 of the largest values in the list a
    '''
    for val in a:
        l = []
        if a.count(val) == len(a)//3 + 1:
            break
            l.append(val)
        else:
            break
            return val
    if len(l) == 0:
        print('None')
    else:
        print(l[0])
#############################################
# Question 1d
#############################################
def sum_tri(a,x):
    '''
    (list)-> bool
    Returns True if there exists indices i, j and k (where i and j and k are not necessarily distinct) such that a[i]+a[j]+a[k]=x
    '''
    for i in range(len(a)):
        for j in range(len(a)):
            for k in range(len(a)):
                if a[i]+ a[j] + a[k] == x:
                    break 
                    return True
    else:
        return False 
