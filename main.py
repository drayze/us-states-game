import turtle

screen = turtle.Screen()
screen.title('U.S. State Game')

image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)


player_guess = screen.textinput(title='Guess a State', prompt='Please, enter your guess.')



turtle.mainloop()
