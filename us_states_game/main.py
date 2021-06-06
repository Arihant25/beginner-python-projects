import pandas
import turtle

# Creates a screen with the U.S. map as the background
screen = turtle.Screen()
screen.title("U.S. States Game by Arihant")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
writer = turtle.Turtle()
writer.penup()
writer.hideturtle()

# Imports the CSV file containing the states and their coordinates on the map
states = pandas.read_csv('50_states.csv')

states_list = states.state.to_list()
missed_states = states_list

correct_states = []
answer_state = screen.textinput(title="Guess the State", prompt="Enter a state's name:").title()

while True:
    if answer_state == "Exit":
        break

    if answer_state in states_list:
        # Gets the X and Y position of the state from the states DataFrame
        position = (states[states.state == answer_state].x.to_list()[0],
                    states[states.state == answer_state].y.to_list()[0])
        writer.goto(position)
        writer.write(arg=answer_state, font=("Corbel", 10, 'normal'))
        missed_states.remove(answer_state)
        correct_states.append(answer_state)
    if len(correct_states) == 50:
        break

    answer_state = screen.textinput(title=f"{len(correct_states)}/50 States correct",
                                        prompt="Enter a state's name:").title()

# Exports the missed states to a separate CSV file
pandas.DataFrame(missed_states).to_csv('states-to-learn.csv')

screen.exitonclick()
