import turtle
import pandas as pd 


screen = turtle.Screen()
screen.title('U.S. State Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv('50_states.csv')
new_data = data.state.to_list()
guesses_taken = []

while len(guesses_taken) < 50:
    
    player_guess = screen.textinput(title='Guess a State', prompt='Please, enter your guess.').title()

    if player_guess in new_data:
        guesses_taken.append(player_guess)
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.penup()
        location = data[data.state == player_guess]
        pen.goto(x= location.x.item(),y= location.y.item())
        pen.write(location.state.item())
    



screen.mainloop()
