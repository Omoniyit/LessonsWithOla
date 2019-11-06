#Question 2
def two_length_run(lst1):
    '''(list) -> bool

    Takes a list of numbers and returns whether or not
    a single consecutive run of equal values occurs.

    Precondition: lst1 must be a list of integers

    >>> two_length_run([1,2,3,3,4,5])
    True
    >>> two_length_run([1,2,3,4,5])
    False

    '''

    length = len (lst1)
    for i in range(length):
        if i == (length-1):
            
            print(False)
    
        elif lst1[i] == lst1[i+1]:
            print(lst1[i] == lst1[i+1])
            break
main = input(' Please input a list of numbers seperated by commas: ')
main=main.split(",")
for i in  range(len(main)):
    main[i] = int(main[i])
two_length_run(main)
