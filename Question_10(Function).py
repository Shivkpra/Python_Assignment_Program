'''Football Points
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
wins get 3 points
draws get 1 point
losses get 0 points'''

def Points(win: object, draw: object, loss: object) -> object:
    wins=win*3
    draws=draw*1
    losses=0
    points=wins+draws+losses
    return points
win=int(input('Enter the  number of win'))
draw=int(input('Enter the  number of draws'))
loss=int(input('Enter the  number of loss'))
print('The points of the team is:',Points(win,draw,loss)) # function call print statement
