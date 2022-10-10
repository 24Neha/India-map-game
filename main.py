# importing turtle and pandas module
import turtle
import pandas

screen = turtle.Screen()
screen.title("India States Game")
image = "India_map_img.gif"
screen.addshape(image)
turtle.shape(image)

# Reading csv file
data = pandas.read_csv("states-&-UT-of-india.csv")
# extracting state name and making a list
state_list = data.state.to_list()
# empty list
guessed_state = []

while len(guessed_state) < 35:
    answer = screen.textinput(title=f"{len(guessed_state)}/37 Correct",
                              prompt="What's another state's name?").title()

    # if answer is exit then create a file that contain all un-guessed names.
    if answer == "Exit":

        # for state in state_list:
        #     if answer != state:
        #         missed_state.append(state)
        # INSTEAD OF ABOVE CODE 1 LINE OF CODE
        missed_state = [state for state in state_list if state not in guessed_state]
        new_data = pandas.DataFrame(missed_state)
        print(new_data.to_csv("States-to-learn.csv"))
        break

    # guessed answer is right
        # take the turtle to the position of the state
    if answer in state_list:
        guessed_state.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer)


