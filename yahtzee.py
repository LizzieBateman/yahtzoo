from random import randint
import time
import json
import collections
from scorecard import Scorecard
from turn import Turn
from turn import roll_a_dice
from gui_class import Yahtzee_gui
from Tkinter import *
import ttk

root = Tk()
root.geometry("700x500")

this_scorecard = Scorecard()
this_turn = Turn()
game_gui = Yahtzee_gui(root, this_scorecard, this_turn)

root.mainloop()
