import turtle
import pandas as pd 


screen = turtle.Screen()
screen.title('U.S. State Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)




player_guess = screen.textinput(title='Guess a State', prompt='Please, enter your guess.').capitalize()

data = pd.read_csv('50_states.csv')
new_data = data.state.to_list()

if player_guess in new_data:
    pen = turtle.Turtle()
    pen.hideturtle()
    pen.penup()
    location = data[data.state == player_guess]
    pen.goto(x= location.x.item(),y= location.y.item())
    pen.write(location.state.item())
    



turtle.mainloop()
