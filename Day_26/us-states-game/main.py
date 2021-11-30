import turtle
import pandas

screen = turtle.Screen()
screen.title('U.S States Game')

image = 'blank_states_img.gif'

screen.addshape(image)
turtle.shape(image)

board = turtle.Turtle()
board.penup()
board.hideturtle()

data = pandas.read_csv('./50_states.csv')

states_list = data.state.tolist()

print(states_list)

guessed_states = []

while len(guessed_states) < 50:
    answer = screen.textinput(
        title=f'{len(guessed_states)}/50 States Correct', prompt='Guess a State Name').title()
    if answer == 'Exit':
        break

    if answer in states_list and answer not in guessed_states:
        state_row = data[data.state == answer]
        x_pos = int(state_row.x)
        y_pos = int(state_row.y)
        board.goto(x_pos, y_pos)
        board.write(answer, font=('Arial', 8, 'bold'))
        guessed_states.append(answer)


# for state in states_list:
#     if state not in guessed_states:
#         states_to_learn.append(state)

states_to_learn = [
    state for state in states_list if state not in guessed_states]

df = pandas.DataFrame(states_to_learn)
df.to_csv('states_to_lean.csv')
