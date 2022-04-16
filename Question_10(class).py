'''Football Points
Create a function that takes the number of wins, draws and losses and calculates the number of points a football team has obtained so far.
wins get 3 points
draws get 1 point
losses get 0 points'''
class total_points:                                                                         # creating class
    def __init__(self,win,draw,loss):                                                       #Constructor
        self.win=win
        self.draw=draw
        self.loss=loss

    def Points(self,win: object, draw: object, loss: object) -> object:                     #Function declaration
        wins = win * 3
        draws = draw * 1
        losses = 0
        points = wins + draws + losses                                                      #calculate total points of the teams
        return points

win = int(input('Enter the  number of win'))
draw = int(input('Enter the  number of draws'))
loss = int(input('Enter the  number of loss'))
obj=total_points(win,draw,loss)                                                             # creating object for class
print('The points of the team is:',obj.Points(win, draw, loss))

