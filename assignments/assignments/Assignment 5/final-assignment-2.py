def digit_sum(n):
    '''
    (int)-> int
    Calculates the sum of all digits of the given non-negative integer n
    '''

    if n == 0:
        return 0
    else:
        return (n%10) + digit_sum(n//10)

def digital_root (n):
    '''
    (int)->
    calculates by taking the sum of all of the digits in a number,
    and repeating the process with the resulting sum until only a single digit remains
    '''
    ap = 0
    n = abs(int(n))
    while n >= 10:
        n = digit_sum(n)
        ap += 1
    return n
