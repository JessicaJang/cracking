# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
end_game = False

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.card_list = []

    def __str__(self):
        string = "Hand contains"
        for temp in self.card_list:
            string = string + ' ' + str(temp)
        return string

    def add_card(self, card):
        self.card_list.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, 
        # then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        flag = False
        for card in self.card_list:
            if card.get_rank() == 'A' and flag == True:
                if value + 10 <= 21:
                    value += 10
            elif card.get_rank() == 'A':
                flag = True
            value += VALUES[card.get_rank()]
        return value

    def draw(self, canvas, pos):
        i = 0
        for temp in self.card_list:
            temp.draw(canvas, [pos[0] + i, pos[1]])
            i += 92
        
# define deck class 
class Deck:
    def __init__(self):
        self.card_list = []
        for suit in SUITS: 
            for rank in RANKS:
                cards = Card(suit, rank)
                self.card_list.append(cards)

    def shuffle(self):
        random.shuffle(self.card_list)

    def deal_card(self):
        return self.card_list.pop()
    
    def __str__(self):
        string = 'Deck contains '
        for cards in self.card_list:
            string = string + ' ' + str(cards)
        return string

#define event handlers for buttons
def deal():
    global outcome, in_play, deck_shuffled, player_hand, dealer_hand, score, end_game
    
    outcome = ""
    end_game = False
    if in_play == True:
        score -= 1
        outcome = "Dealer win"

    deck_shuffled = Deck()
    deck_shuffled.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck_shuffled.deal_card())
    player_hand.add_card(deck_shuffled.deal_card())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck_shuffled.deal_card())
    dealer_hand.add_card(deck_shuffled.deal_card())
    
    in_play = True


def hit():
    global deck_shuffled, in_play, player_hand, dealer_hand, score, outcome, end_game

    if in_play == True and end_game == False:
        player_hand.add_card(deck_shuffled.deal_card())
        if player_hand.get_value() > 21:
            outcome = "You have busted and lose"
            in_play = False
            end_game = True
            score -= 1
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global deck_shuffled, in_play, player_hand, dealer_hand, score, outcome, end_game
    
    if in_play == True and end_game == False:
        in_play = False
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck_shuffled.deal_card())
        if dealer_hand.get_value() > 21:
            outcome = 'Dealer busted. Player win'
            score += 1
            end_game = True
            
            
    if in_play == False and end_game == False:
        if dealer_hand.get_value() >= player_hand.get_value():
            outcome = 'Dealer win'
            score -= 1
        else:
            outcome = 'Player win'
            score += 1
        end_game = True

    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global score, outcome, in_play, player_hand, dealer_hand

    canvas.draw_text('Blackjack', [100, 70], 50, 'Aqua', 'sans-serif')
    canvas.draw_text('Score', [380, 70], 25, 'Black', 'sans-serif')
    canvas.draw_text(str(score), [480, 70], 25, 'Black', 'sans-serif')
    
    canvas.draw_text('Dealer', [80, 140], 25, 'Black', 'sans-serif')
    canvas.draw_text(outcome, [250, 140], 25, 'Black', 'sans-serif')
    
    canvas.draw_text('Player', [80, 330], 25, 'Black', 'sans-serif')
    dealer_hand.draw(canvas, (80, 150))
    player_hand.draw(canvas, (80, 350))
    if in_play == True:
        canvas.draw_text('Hit or Stand?', [250, 330], 25, 'Black', 'sans-serif')
        card_loc = (CARD_CENTER[0] + 80, CARD_CENTER[1] + 150)
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, card_loc, CARD_BACK_SIZE)
    else:
        canvas.draw_text('New deal?', [250, 330], 25, 'Black', 'sans-serif')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric