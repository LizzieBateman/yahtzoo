from Tkinter import *

class Yahtzee_gui:

    def __init__(self, master):
        self.master = master
        master.title("Yahtzee!")

        self.label = Label(master, text="Welcome to Yahtzee!")
        self.label.pack()

        #create 2 frames side by side, one for the scorecard and the other for the throw of the dice

        self.scorecard_frame = Frame(master)
        self.scorecard_frame.pack(side = 'left')
        self.scorecard_frame.label = Label(self.scorecard_frame, text="This is a frame on the left")
        self.scorecard_frame.label.pack()

        self.game_frame = Frame(master, bg = 'blue')
        self.game_frame.pack(side = 'right')
        self.game_frame.label = Label(self.game_frame, text = "This is a frame on the right")
        self.game_frame.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = 'bottom')

        #initialise the scorecard table

    



root = Tk()
my_gui = Yahtzee_gui(root)
root.mainloop()

# from Tkinter import *

# class Selection(object):

#     def __init__(self):

#         self.current_selection = ""

# master = Tk()

# var = StringVar(master)
# var.set("What would you like to take?") # initial value

# option = OptionMenu(master, var, "1s", "2s", "3s", "4s", "5s", "6s", "3 of a kind", "4 of a kind", "low run", "high run", "full house", "sum", "yahtzee")
# option.pack()

# selection = Selection()

# def ok():
#     selection.current_selection = var.get()
#     print selection.current_selection
#     master.quit()

# button = Button(master, text="OK", command=ok)
# button.pack()

# mainloop()

# print selection.current_selection
