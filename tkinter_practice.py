from Tkinter import *

class Selection(object):

    def __init__(self):

        self.current_selection = ""

master = Tk()

var = StringVar(master)
var.set("What would you like to take?") # initial value

option = OptionMenu(master, var, "1s", "2s", "3s", "4s", "5s", "6s", "3 of a kind", "4 of a kind", "low run", "high run", "full house", "sum", "yahtzee")
option.pack()

selection = Selection()

def ok():
    selection.current_selection = var.get()
    print selection.current_selection
    master.quit()

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()

print selection.current_selection




