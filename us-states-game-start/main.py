import turtle
import pandas






screen = turtle.Screen()

screen.setup(725, 491)
screen.bgpic("blank_states_img.gif")

player = turtle.Turtle()
player.penup()


data = pandas.read_csv("50_states.csv")
states = data["state"]
states = states.tolist()
correct_ans = 0
screen.title("Name the state")


game = True
while game:
    guess = screen.textinput(title=f"{correct_ans}/50  states correct", prompt="State Name").title()

    if guess == "Exit":
        break

    if len(states) > 0:
        for i in states:
            if guess == i:
                correct_ans += 1
                required = data[data.state == guess]
                player.goto(x = int(required.x), y = int(required.y))
                player.write(arg=guess, align="center", font=('Arial', 8, 'normal'))
                states.remove(guess)
    else:
        print("u guessed all the states")

missed_states={
    "states": states
}

#generate csv
file = pandas.DataFrame(missed_states)
file.to_csv("States u didn't guess")


turtle.mainloop()


##rough
# data = pandas.read_csv("50_states.csv")
# required = data[data.state == "Alabama"]
# y = required.x
# print(y)
