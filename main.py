import turtle
from PIL import Image, ImageTk
from scoreboard import Score
from states_names import States

screen = turtle.Screen()
screen.title("BR States Game")
screen.setup(width=800, height=750)
screen.bgcolor("black")
image = Image.open("image/1.intro-to-geobr_15_1.gif")
score = Score()
states = States()

w = int(image.width * 0.24)
h = int(image.height * 0.24)
image = image.resize((w, h))
pic = ImageTk.PhotoImage(image)


screen.addshape('pic', turtle.Shape("image", pic))

br = turtle.Turtle("pic")


def get_state_click(x, y):
    print(x, y)


turtle.onscreenclick(get_state_click)

game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"Chances left: {score.chance}", prompt="What's the state's name?").title()
    print(answer_state)
    states.point_state(answer_state)
    score.check_answer(answer_state)
    score.chances()
    if score.chance == 0:
        score.states_to_learn()
        game_is_on = False
turtle.mainloop()
