def count_pos(lst1):
    ''' (list) -> integer

    Takes a list of numbers as input and returns positive
    elements.

    Precondition: lst1 must be a list of integers

    >>> count_pos([1,4,-3,2])
    3
    >>> count_pos([-3,4-2,36])
    2
    '''
    
    count = 0
    for i in range(len(lst1)):
        if int(lst1[i]) > 0:
            count += 1
    print("Your list has ",count, 'positive numbers')

main = input(' Please input a list of numbers seperated by commas: ')
main=main.split(",")
for i in  range(len(main)):
    main[i] = int(main[i])


count_pos(main) 

            
            
            

        
