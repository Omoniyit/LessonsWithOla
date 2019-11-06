def digit_sum(n):
    '''(int)->int
    Precondition: n >=0'''
    if n==0: 
      return 0
    
    return n%10 + digit_sum(n//10)

def digital_root(n):
    '''(int)->int
    Precondition: n >=0'''
    if n < 10:
        return n

    digsum = digit_sum(n)
    return digital_root(digsum)

    # alternatively the last two lines can be replaced by one line:
    # return digital_root(digital_sum(n))
