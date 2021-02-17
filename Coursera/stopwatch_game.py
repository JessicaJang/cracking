# template for "Stopwatch: The Game"
import simplegui
import time

# define global variables
increment = 0
total = 0
score = 0
status = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global tenthsOf 
    
    tenthsOf = t % 10
    rest = t / 10   
    second = rest % 60
    minute = rest / 60
    
    if second >= 0 and second <= 9:
        return str(minute) + ':' + '0' + str(second) + '.' + str(tenthsOf)
    else:
        return str(minute) + ':' + str(second) + '.' + str(tenthsOf)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def click_start():
    global status
    
    status = False
    timer.start()
   
    return

def click_stop():
    global total
    global score
    global tenthsOf
    global status
    
    timer.stop()
    if tenthsOf == 0 and status == False:
        score = score + 1
        total = total + 1
        status = True
    elif tenthsOf != 0 and status == False:    
        total = total + 1
        status = True
    else:
        pass

def click_reset():
    global increment
    global total
    global score
    global status
    
    increment = 0
    total = 0
    score = 0
    status = True
    
# define event handler for timer with 0.1 sec interval
def increment_number():
    global increment

    if increment > 360000:
        timer.stop()
        increment = 0
    else:
        increment = increment + 1
   
# define draw handler
def draw(canvas):
    global increment
    global score
    global total
    
    stringOfnum = format(increment)
    stringOfscore = str(score) + '/' + str(total)
    canvas.draw_text(stringOfnum, [70, 110], 60, 'White')
    canvas.draw_text(stringOfscore, [210,40], 40, 'White')
    
# create frame
frame = simplegui.create_frame("Timer: Game", 300, 200)

# register event handlers
frame.add_button("Start", click_start, 200)
frame.add_button("Stop", click_stop, 200)
frame.add_button("Reset", click_reset, 200)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, increment_number)

# start frame
frame.start()

# Please remember to review the grading rubric
