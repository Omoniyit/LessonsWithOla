def main():
    '''(None) -> 2D_list
    Opens the file fromthe NYT-bestsellers.txt and converts it into
    a 2D_list.

>>> main()
...,['"W" Is For Wasted ', ' Sue Grafton ', ' Marian Wood/Putnam ', ' 9/29/2013 ', ' Fiction\n'],
['The Longest Ride ', ' Nicolas Sparks ', ' Grand Central ', ' 10/6/2013 ', ' Fiction\n'],
['Doctor Sleep ', ' Stephen King ', ' Scribner ', ' 10/13/2013 ', ' Fiction\n']]

'''
    
    text = open ('NYT-bestsellers.txt').readlines()
    list_of_all = []
    titles = []
    authors = []
    publishers = []
    dates = []
    genres = []

    for line in text:
        values = line.split('\t')
        list_of_all.append(values)
    return list_of_all

    

def print_list(l):
    '''(2D_list) -> None
    Takes a 2D_list and prints the value of the title, author and date given by
    the 2D_list
>>> print_list([['Never Go Back ', ' Lee Child ', ' Delacorte ', ' 9/22/2013 ', ' Fiction\n'], ['"W" Is For Wasted ', ' Sue Grafton ', ' Marian Wood/Putnam ', ' 9/29/2013 ', ' Fiction\n'],
['The Longest Ride ', ' Nicolas Sparks ', ' Grand Central ', ' 10/6/2013 ', ' Fiction\n'], ['Doctor Sleep ', ' Stephen King ', ' Scribner ', ' 10/13/2013 ', ' Fiction\n']])
Never Go Back , by  Lee Child  ( 9/22/2013 )
"W" Is For Wasted , by  Sue Grafton  ( 9/29/2013 )
The Longest Ride , by  Nicolas Sparks  ( 10/6/2013 )
Doctor Sleep , by  Stephen King  ( 10/13/2013 )
'''
    
    for val in l:
        print('%s, by %s (%s)' % (val[0],val[1],val[3]))
def sort_list(l):
    '''(2D_list) -> 2D_list
    Takes a 2D_list and sorts the years and returns the new sorted list.
    
'''
    
    dates = []
    dates2 = []
    sorted_list = []
    c = 0
    
    for val in l:
        dates.append(val[3])
    
    for day in dates:
        days = day.split('/')
        for num in days:
            num = int(num)
        days.reverse()
        days.append(c)
        days.reverse()
        days.reverse()
        dates2.append(days)
        c += 1
    dates2.sort()
    for val in dates2:
        sorted_list.append(l[val[3]])

    return sorted_list
        
    
        
        
        
#To seperate each line of the text document into a list
#Question 1:

def lookup_y(a,b):
    '''(int,int) -> None
    Takes a starting year a and ending year (b) as parameters and prints the values
    of all the bestsellers that occured in that range.

>>> lookup_y(1998,2011)
...
Dead Reckoning, by Charlaine Harris (5/22/2011)
Shock Wave, by John Sandford (10/23/2011)
The Fifth Witness, by Michael Connelly (4/24/2011)
Bossypants, by Tina Fey (4/24/2011)
Hit List, by Laurell K. Hamilton (6/26/2011)
23337, by Stephen King (11/27/2011)
Known and Unknown, by Donald Rumsfeld (2/27/2011)
The Jungle, by Clive Cussler (3/27/2011)
The Social Animal, by David Brooks (3/27/2011)
Lies That Chelsea Handler Told Me, by Chelsea Handler (5/29/2011)
Toys, by James Patterson (4/3/2011)
Red, by Sammy Hagar (4/3/2011)
Against All Enemies, by Tom Clancy (7/3/2011)
The Inner Circle, by Brad Melzer (1/30/2011)
The Best of Me, by Nicolas Sparks (10/30/2011)
A Dance With Dragons, by George R. R. Martin (7/31/2011)
A Stolen Life, by Jayce Dugard (7/31/2011)
Kill Alex Cross, by James Patterson (12/4/2011)
The Omen Machine, by Terry Goodkind (9/4/2011)
In the Garden of Beasts, by Erik Larson (6/5/2011)
Shadowfever, by Karen Marie Moning (2/6/2011)
The Sixth Man, by David Baldacci (5/8/2011)
Heat Rises, by Richard Castle (10/9/2011)
...


    
'''
    
    list_of_all = main()
    dates = []


    for item in list_of_all:
        dates.append(item[3])
        
    
        
    
    a = int(a)
    b = int(b)

    c = 0
    unsort= []
    

    for day in dates:
        days = day.split('/')
        for i in range(len(days)):
            days[i] = int(days[i])
            
        if days[2] in range(a,b+1):
            unsort.append(list_of_all[c])
            c += 1
        else:
            c += 1
    a = sort_list(unsort)
    print_list(a)
    
#Question 2
def lookup_my(m,y):
    '''(int,int) -> None
    Takes a first number as month (m) and second number as a year(y) and prints all the bestsellers in that specific month and year.

>>> lookup_my(3,1998)
The Millionaire Next Door, by Thomas J. Stanley (5/3/1998)

>>> lookup_my(8,2002)
Four Blind Mice, by James Patterson (12/8/2002)
Let's Roll!, by Lisa Beamer (9/8/2002)


'''

    list_of_all = main()
    dates = []
    for item in list_of_all:
        dates.append(item[3])
    
        
    
    m = int(m)
    y = int(y)

    c = 0
    unsort= []
    

    for day in dates:
        days = day.split('/')
        for i in range(len(days)):
            days[i] = int(days[i])
        if days[1] == m and days[2] == y:
            unsort.append(list_of_all[c])
            c+=1
        else:
            c += 1
    a = sort_list(unsort)
    print_list(a)
#Question 3    
def search_aut(s):
    ''' (string) -> None
    Takes a string and returns all the authors which containt that name.

>>> search_aut('trump')
Trump: The Art of the Deal, by Donald Trump (1/17/1988)
Trump: Surviving at the Top, by Donald Trump (9/9/1990)


'''

    name = s.lower()

    list_of_all = main()
    authors = []
    unsort = []
    c = 0

    for item in list_of_all:
        authors.append(item[1])

    for author in authors:
        if author.lower().find(name) != -1:
            unsort.append(list_of_all[c])
            c += 1
        else:
            c += 1
    a = sort_list(unsort)
    print_list(a)
#question 4
def search_tit(s):
    '''(str) -> None
    Takes a string as a parameter and searches and returns for its occurence in all the titles of the list.
>>> search_tit('Harry')
Harry S. Truman, by Margaret Truman (1/14/1973)
Harry Potter and the Sorcerer's Stone, by J. K. Rowling (8/15/1999)
Harry Potter and the Chamber of Secrets, by J. K. Rowling (6/20/1999)
Harry Potter and the Prisoner of Azkaban, by J. K. Rowling (9/26/1999)



'''


    name = s.lower()
    list_of_all = main()
    titles = []
    unsort = []
    c = 0
    for item in list_of_all:
        titles.append(item[0])

    for title in titles:
        if title.lower().find(name) != -1:
            unsort.append(list_of_all[c])
            c += 1
        else:
            c += 1
    a = sort_list(unsort)
    print_list(a)




def frequency(books):
    '''(2D_List) -> 2D_List
    Takes a 2D _list searches for the frequency of authors in the list. Returns a set of independent lists with author name
    and frequency.
>>> frequency([['Never Go Back ', ' Lee Child ', ' Delacorte ', ' 9/22/2013 ', ' Fiction\n'], ['"W" Is For Wasted ', ' Sue Grafton ', ' Marian Wood/Putnam ', ' 9/29/2013 ', ' Fiction\n'],
['The Longest Ride ', ' Nicolas Sparks ', ' Grand Central ', ' 10/6/2013 ', ' Fiction\n']])
[[1, ' Sue Grafton '], [1, ' Nicolas Sparks '], [1, ' Lee Child ']]


'''
    list_of_all = books
    authors = []
    blnk = []
    List_name = []
    
    c = 0
    for item in list_of_all:
        authors.append(item[1])
    for author in authors:
        blnk.append(author)
        blnk.append(authors.count(author))
        List_name.append(blnk)
        blnk = []
    names = []
    f = []
    final = []
    List_name.sort()
    for item in List_name:
        if item[0] not in names:
            names.append(item[0])
            f.append(item[1])
    for i in range(len(names)):
        bk = []
        bk.append(f[i])
        bk.append(names[i])
        final.append(bk)
    final.sort()
    final.reverse()
    
    return final 
    
#Question 5
def num_bestsellers(n):
    '''(int) -> None
    Takes a positive integer then displays authors who have at least n best sellers.
>>> num_bestsellers(8)
1. James Patterson with 41 bestsellers.
 2. Stephen King with 32 bestsellers.
 3. Danielle Steel with 27 bestsellers.
 4. John Grisham with 23 bestsellers.
 5. Patricia Cornwell with 17 bestsellers.
 6. Janet Evanovich with 17 bestsellers.
 7. Tom Clancy with 16 bestsellers.
 8. Mary Higgins Clark with 16 bestsellers.
 9. Bob Woodward with 12 bestsellers.
 10. Nora Roberts with 10 bestsellers.
 11. Dean R. Koontz with 10 bestsellers.
 12. David Baldacci with 10 bestsellers.
 13. James Michener with 9 bestsellers.
 14. Sue Grafton with 8 bestsellers.
 15. Sidney Sheldon with 8 bestsellers.
 16. Robert Ludlum with 8 bestsellers.

'''
    
    blnk = []
    a = main()
    values = frequency(a)
    for val in values:
        if val[0] >= n:
            blnk.append(val)
    if len(blnk) == 0:
        print('Sorry there are no authors with that many bestsellers.')
    else:
        print('The list of authors with at least %d NYT bestsellers is: ' % (n))
        for i in range(len(blnk)):
            print(' %d. '%(i+1), end='')
            print('%s with %d bestsellers.' %(blnk[i][1],blnk[i][0]))
        
            
        
#Question 6    
def num_authors(n):
    '''(int) -> None
    Takes an integer (n) as a parameter and reeturns the n amount of authors with the most bestsellers.
>>> num_authors(21)
Top 21 authors by the number of NYT bestsellers are: 
1. James Patterson
2. Stephen King
3. Danielle Steel
4. John Grisham
5. Patricia Cornwell
6. Janet Evanovich
7. Tom Clancy
8. Mary Higgins Clark
9. Bob Woodward
10. Nora Roberts
11. Dean R. Koontz
12. David Baldacci
13. James Michener
14. Sue Grafton
15. Sidney Sheldon
16. Robert Ludlum
17. Tim LaHaye
18. Nicholas Sparks
19. Michael Connelly
20. John le Carre
21. Robert Jordan



    
'''
    a = main()
    values = frequency(a)
    print('Top %d authors by the number of NYT bestsellers are: ' % (n))
    for i in range(0,n):
        print('%d. ' % (i+1), end='')
        print(values[i][1])
        
    
        
        
        
    
    
def Run_program():
    '''(None) -> None
    Runs the program which offers a combination of options for users to interact with the data from NYT-bestsellers.txtx in an organised fashion.
>>> Run_program()
===============================================================
What would you like to do? Enter 1,2,3,4,5,6 or Q for answer.
1: look up year range
2: Look up month/year/
3: Search for author
4: Search for title
5: Number of authors with at least x bestsellers
6: List y authors with the most bestsellers
Q: Quit
===============================================================
Answer (1,2,3,4,5,6, Q or q): 
'''
    a = 0
    p = 1
    

    while a != p:
            print('===============================================================')
            print('What would you like to do? Enter 1,2,3,4,5,6 or Q for answer.')
            print('1: look up year range')
            print('2: Look up month/year/')
            print('3: Search for author')
            print('4: Search for title')
            print('5: Number of authors with at least x bestsellers')
            print('6: List y authors with the most bestsellers')
            print('Q: Quit')
            print('===============================================================')
            a = input('Answer (1,2,3,4,5,6, Q or q): ')
            if a.lower() == 'q':
                print('Thank you, goodbye.')
                
                break
       
                    
            if a == '1':
                a = input ('Please enter the starting year: ')
                while a.isnumeric() != True:
                    print('Sorry that is not a valid input: ')
                    a = input ('Please enter the starting year: ')
                b = input ('Please enter ending year: ' )
                while b.isnumeric() != True:
                    print('Sorry that is not valid input')
                    b = input('Please enter ending year: ')
                a = int(a)
                b = int(b)
                while a > b:
                    print('Sorry the values you have entered for your starting year is not correct')
                    a = input ('Please enter the starting year: ')
                    while a.isnumeric() != True:
                        print('Sorry that is not a valid input: ')
                        a = input ('Please enter the starting year: ')
                    b = input ('Please enter ending year: ' )
                    while b.isnumeric() != True:
                        print('Sorry that is not valid input: ')
                        b = input('Please enter ending year: ')
                lookup_y(a,b)
            elif a == '2':
                a = input('Give a month as integer 1-12: ')
                while a.isnumeric() != True:
                    print('Sorry that is not valid')
                    a = input('Give a month as integer 1-12: ')
                while int(a) not in range(1,13):
                    print('Sorry that is not valid')
                    a = input('Give a month as integer 1-12: ')
                b = input('Give a four digit year: ')
                while b.isnumeric() != True:
                    print('Sorry that is not a valid year: ')
                    b = input('Give a four digit year: ')
                a = int(a)
                b = int(b)
                lookup_my(a,b)
            elif a == '3':
                s = input('Provide the author you would like to search for: ')
                search_aut(s)
            elif a == '4':
                s = input('Provide the name of the title you would like to search for: ')
                search_tit(s)
            elif a == '5':
                a = input('Provide the least number of bestsellers: ')
                while a.isnumeric() != True:
                    print('Sorry that is not valid input')
                    a = input('Provide the least number of bestsellers: ')
                a = int(a)
                num_bestsellers(a)
            elif a == '6':
                a = input('Provide the number of authors you would like to seach for: ')
                while a.isnumeric() != True:
                    print('Sorry that is not valid input')
                    a = input('Provide the number of authors you would like to seach for: ')
                a= int(a)

                num_authors(a)
            else:
                print('Sorry Invalid input')
                continue
        
    
Run_program()            
        
        
        
            
            
        
        
    
    
    
    
    
        
    


            
    
