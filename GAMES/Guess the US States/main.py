import turtle
import pandas


df = pandas.read_csv("50_states.csv")
screen = turtle.Screen()
screen.title("U.S. States Game")
img_gif = "blank_states_img.gif"
screen.addshape(img_gif)
# register the shape
turtle.shape(img_gif)
state_list = df.state.to_list()
guessed_states = []


def reveal_state(x, y):
    name = turtle.Turtle()
    name.hideturtle()
    name.penup()
    name.goto(x, y)
    name.write(f"{ans}")


while len(guessed_states) < 50:
    ans = screen.textinput(title=f" Score: {len(guessed_states)}/50", prompt="Name a State: ").title()

    if ans == "exit".title():
        correction = [state for state in state_list if state not in guessed_states]
 
        ans_file = pandas.DataFrame(correction)
        ans_file.to_csv("correct_ans.")
        break
        
        # ALl the states you have missed will be written in the correct_ans.csv file

    if ans in state_list:
        guessed_states.append(ans)
        state_data = df[df.state == ans]
        x_cor = state_data.x
        y_cor = state_data.y
        reveal_state(int(x_cor), int(y_cor))


# def get_mouse_click_coordinate(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coordinate)
# Get turtle coordinates on image
# These co ordinates were inserted in 50_states.csv

screen.exitonclick()
