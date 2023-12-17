from turtle import Turtle
from brazil_states import br_states_game
import pandas as pd


ALIGNMENT = 'center'
FONT = ('Courier', 24, 'bold')
STATES = br_states_game["states"].tolist()

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(280, 220)
        self.score = 0
        self.highest_score = 27
        self.chance = 27
        self.screen_board()
        self.list_states = STATES

    def screen_board(self):
        self.clear()
        self.write(f"Score: {self.score}/{self.highest_score}", align=ALIGNMENT,
                   font=FONT)

    def right_answer(self):
        self.score += 1
        self.screen_board()

    def chances(self):
        self.chance = self.chance - 1

    def check_answer(self, answer):
        for state in self.list_states:
            if state == answer:
                self.list_states.remove(state)
                self.right_answer()

    def states_to_learn(self):
        data = pd.DataFrame({
            "states_to_learn": self.list_states
        })
        data.to_csv("states_to_learn.csv")
