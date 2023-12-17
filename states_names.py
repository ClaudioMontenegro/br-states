from turtle import Turtle
from brazil_states import br_states_game

STATES = br_states_game["states"].tolist()
FONT = ('Courier', 10, 'bold')


class States(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.penup()
        self.ht()

    def point_state(self, answer):
        for state in br_states_game["states"]:
            if answer == state:
                self.new_state = self
                new_x = br_states_game.loc[br_states_game["states"] == state, "x"]
                new_y = br_states_game.loc[br_states_game["states"] == state, "y"]
                x_list = new_x.index.tolist()
                y_list = new_y.index.tolist()
                print(new_x[x_list[0]], new_y[y_list[0]])
                self.new_state.goto(new_x[x_list[0]]-10, new_y[y_list[0]])
                self.new_state.write(f"{state}", align="center", font=FONT)
