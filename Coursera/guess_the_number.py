# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import random
import math
import simplegui

secret_number = 0
limit = 0
count = 0
#indicate the range is up to 100 or 1000
flag = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global flag
    secret_number = 0
    
    if(flag == 0):
        range100()
    else:
        range1000() 

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    global limit
    global count
    global flag
    
    flag = 0
    count = 0
    limit = int(math.ceil(math.log(101,2)))
    secret_number = random.randrange(0,100)
    
    print 'New game. Range is [0,100)'
    print 'Number of remaining guesses is ' + str(limit) + '\n'

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global limit
    global count
    global flag
    
    flag = 1
    count = 0
    limit = int(math.ceil(math.log(1001,2)))
    secret_number = random.randrange(0,1000)

    print 'New game. Range is [0,1000)'
    print 'Number of remaining guesses is ' + str(limit) + '\n'
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global count
    global limit
    player_number = int(guess)
    
    print 'Guess was '+ str(player_number)
    
    #compare the number of tryout
    count = count+1
    if(count >= limit):
        print 'You ran out of guesses. The number was ' + str(secret_number) + '\n'
        new_game()
        return
    else:
        left = limit - count
        print 'Number of remaining guesses is ' + str(left)

    if(player_number < secret_number):
        print 'Higher!\n'
    elif(player_number > secret_number):
        print 'Lower!\n'
    else:
        print 'Correct!\n'
        new_game()
        return
    

# create frame
frame = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
frame.add_button("Rnage is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter",input_guess,200)
frame.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
