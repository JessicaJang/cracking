# implementation of card game - Memory

import simplegui
import random

turn_str = "Turns = 0"
# helper function to initialize globals
def new_game():
    global deck, deck2, exposed, state, turn, before_1, before_2
    before_1 = 0
    before_2 = 0
    state = 0
    count = 0
    turn = 0
    deck = range(0, 8)
    deck2 = range(0, 8)

    deck.extend(deck2)
    random.shuffle(deck)
    
    exposed = []
    for count in range(16):
        exposed.append(False)

# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, deck, before_1, before_2, turn, turn_str
    check = pos[0] / 50

    if(exposed[check] == False):
        if state == 0:
            exposed[check] = True
            before_1 = check
            state = 1
            turn = turn + 1
        elif state == 1:
            exposed[check] = True
            before_2 = check
            state = 2
        else:
            if(deck[before_1] != deck[before_2]):
                exposed[before_1] = False
                exposed[before_2] = False
            turn = turn + 1
            state = 1
            exposed[check] = True
            before_1 = check

    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global deck, exposed, turn_str, turn
    global exposed
    i = 0
    
    for num in deck:
        canvas.draw_text(str(num), [10 + i, 70], 75, 'White')
        i = i + 50
        
    for count in range(16):
        if(exposed[count] == False):
            canvas.draw_polygon([[0 + 50 * count, 0], [0 + 50 * count, 100], [50 + 50 * count, 100], [50 + 50 * count, 0]], 1, 'Black', 'Green')
        
    turn_str = 'Turns = ' + str(turn)
    label.set_text(turn_str)


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label(turn_str)

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric