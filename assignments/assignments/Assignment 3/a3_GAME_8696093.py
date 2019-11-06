# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     
     for card in range(0,26):
         dealer.append(deck[card])

     for card in range(26,51):
         other.append(deck[card])
    
     

     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    l.sort()
    a = l
    b =[]

    
    for itm in a:
        cur_val = ''.join(list(itm)[:-1])
        b.append(cur_val)

    for itm in b:
        if itm == 0:
            continue
        elif b.count(itm) == 3:
            b [b.index(itm)] = 0
            b[b.index(itm)] = 0

            no_pairs.append(l[b.index(itm)])

        elif b.count(itm) == 1:
            no_pairs.append(l[b.index(itm)])

    no_pairs.sort()

    for i in range(len(no_pairs)):
        if i < len(no_pairs) - 1:
            if no_pairs[i] == no_pairs[i+1]:
                no_pairs.remove(no_pairs[i])
        
                
        
        
        
        
            
            
        



    
                   
        
            
            

    random.shuffle(no_pairs)
    return( no_pairs)

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    for card in deck:
        print(card,end=' ')
        

    
def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     

     value = input('Give me an integer between 1 and ' + str(n) +': ' )
     
     if int(value) in range(1,n+1):
         return (int(value))
     else:
         while int(value) not in range(1,n+1):

             value = input('Invalid number. Give me an integer between 1 and ' +str(n) +': ')
    
         return (int(value))


    

def play_game():
     '''()->None
     This function plays the game'''
    
     deck = make_deck()
     
     shuffle_deck(deck)
     tmp = deal_cards(deck)

     dealer = tmp[0]
     human = tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("\nDo not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     while len(dealer) > 0 :
         print('***********************************************************')
         print('Your Turn')
         print('Your current deck of cards is: ')
         print_deck(human)
         print('\nI have ',len(dealer),' cards. If 1 stands for my first card and\n'+str(len(dealer))+'for my last card, which of my cards would you like?')
         a = get_valid_input(len(dealer))
         if a == 1:
             print('You asked for my 1st card')
         elif a == 2:
             print('You asked for my 2nd card')
         elif a == 3:
             print('You asked for my 3rd card')
         else:
             print('You asked for my %dth card' %(get_valid_input(len(dealer))))


         value = dealer[a-1]

         print('Here it is %s' % (value))

         human.append(value)
         dealer.remove(value)
         print('With %s added, your current deck of card is:' % (value))

         print_deck(human)

         print('\nAnd after discarding pairs and shuffling, your deck is:')
         human=remove_pairs(human)

         print_deck(human)
         wait_for_player()
         if len(human) == 0:
             break
         else:
             continue
     
         print('***********************************************************')
         print('My Turn')
         a = random.randrange(0,len(human))
         if a == 0:
             print('I took your 1st card')
         if a == 1:
             print('I took your 2nd card')
         if a == 2:
             print('I took your 3rd card')
         else:
             print('I took your %dth card' % (a +1))

         dealer.append(human[a])
         del human[a]
         dealer = remove_pairs(dealer)
         wait_for_player()
     if len(human) == 0:
         print('***********************************************************')
         print('Ups. You do not have any more cards')
         print('Congratulations! You, Human, win')
     else:
         print('***********************************************************')
         print('Ups. I do not have any more cards')
         print('Congratulations! I, Robot, win')
         
    
         
    
    
play_game()































         
     
     

     
     
    
     
	
	 

# main

