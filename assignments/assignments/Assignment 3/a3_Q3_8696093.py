def longest_run(lst1):
    '''(list) -> integer

    Takes a list and returns the longest consecutive run
    of equal values and the value of that run.

    Precondition: lst1 must be a list of integers
    
    >>> longest_run([1,2,3,4,5])
    1
    >>> longest_run([1,2,3,3,4,5])
    2

    '''
    count = 0
    blank_lst = []
    blank_lst2= []
    old_item = lst1[0]
    if len(lst1)== 1:
        print([1])
        print([lst1[0]])
    else:
        for new_item in lst1:
            if old_item == new_item:
                count += 1

            else:
                blank_lst.append(count)
                blank_lst2.append(old_item)
                count = 1
                old_item = new_item
        blank_lst.append(count)
        blank_lst2.append(new_item)
        run = max(blank_lst)
    print( run)
main = input(' Please input a list of numbers seperated by commas: ')

main = main.split(",")

for i in  range(len(main)):

    main[i] = int(main[i])

longest_run(main)














def longest_run_v2(lst1):
    '''(list) -> integer
    Takes a list and returns the longest consecutive run
    of equal values and the value of that run.
    
>>> longest_run_v2([1,1,2,3,4,5,5,5,2,1])
The longest run is: 3
The value of the Run is: 5

>>> longest_run_v2([1,1,2,3,4,5,5,5,2,1,2,3,4,5,6,7,7,7,7,7])
The longest run is: 5
The value of the Run is: 7

    '''
    count = 0
    blank_lst = []
    blank_lst2= []
    old_item = lst1[0]
    if len(lst1)== 1:
        print([1])
        print([lst1[0]])
    else:
        for new_item in lst1:
            if old_item == new_item:
                count += 1

            else:
                blank_lst.append(count)
                blank_lst2.append(old_item)
                count = 1
                old_item = new_item
        blank_lst.append(count)
        blank_lst2.append(new_item)
        run = max(blank_lst)
        if run == 1:
            print('There is no Longest run')
        else:
            value = blank_lst2[(blank_lst.index(max(blank_lst)))]

            print('The longest run is: %d\nThe value of the Run is: %d' % (run,value))



