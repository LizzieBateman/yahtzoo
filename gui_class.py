from Tkinter import *
import ttk

class Yahtzee_gui:

    tree_item_id = {"1s": "I00D", "2s": "I00C", "3s": "I00B", "I00A": "4s", "I009": "5s", "I008": "6s", "I007": "3 of a kind", "I006": "4 of a kind", "I005": "low run", "I004" : "high run", "I003": "full house", "I002" : "sum", "I001": "yahtzee"}
    
    def __init__(self, master):
        self.master = master
        master.title("Yahtzee!")

        self.label = Label(master, text="Welcome to Yahtzee!")
        self.label.pack()

        #create 2 frames side by side, one for the scorecard and the other for the throw of the dice

        self.scorecard_frame = Frame(master)
        self.scorecard_frame.pack(side = 'right')
        #self.scorecard_frame.label = Label(self.scorecard_frame, text="This is a frame on the right")
        #self.scorecard_frame.label.pack()

        self.game_frame = Frame(master, bg = 'blue')
        self.game_frame.pack(side = 'left')
        self.game_frame.label = Label(self.game_frame, text = "This is a frame on the left")
        self.game_frame.label.pack()

        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = 'bottom')

        self.make_scorecard()

        b = Button(self.scorecard_frame, text = "Take Selection", command=self.take_selection)
        b.pack(side = 'top')

    #initialise the scorecard table
    def make_scorecard(self):
        self.tree = ttk.Treeview(self.scorecard_frame, selectmode='browse')
        self.tree.pack(side='left')

        vsb = ttk.Scrollbar(orient="vertical",command=self.tree.yview)
        vsb.pack(side='right',fill='y')

        self.tree.configure(yscrollcommand=vsb.set)
        self.tree["columns"] = ("1","2")
        self.tree['show'] = 'headings'
        self.tree.column("1", width=100, anchor='c')
        self.tree.column("2", width=100, anchor='c')
        self.tree.heading("1", text="Options")
        self.tree.heading("2", text="Score")
        self.tree.insert("" , 0, text="LL13", values=("yahtzee","empty"))
        self.tree.insert("" , 0, text="L12", values=("sum","empty"))
        self.tree.insert("" , 0, text="L11", values=("full house","empty"))
        self.tree.insert("" , 0, text="L10", values=("high run","empty"))
        self.tree.insert("" , 0, text="L9", values=("low run","empty"))
        self.tree.insert("" , 0, text="L8", values=("4 of a kind","empty"))
        self.tree.insert("" , 0, text="L7", values=("3 of a kind","empty"))
        self.tree.insert("" , 0, text="L6", values=("6s","empty"))
        self.tree.insert("" , 0, text="L5", values=("5s","empty"))
        self.tree.insert("" , 0, text="L4", values=("4s","empty"))
        self.tree.insert("" , 0, text="L3", values=("3s","empty"))
        self.tree.insert("" , 0, text="L2", values=("2s","empty"))
        self.tree.insert("" , 0, text="L1", values=("1s","empty"))

    def update_scorecard(self,option, new_string):
        self.tree.item(item_id, values = (game_gui.tree_item_id[item_id], new_string))

    def take_selection(self, currentScore):
        selected = self.tree.focus()
        an_option = self.tree.item(selected, option='values')[0]
        self.tree.item(self.tree_item_id[an_option], values = (an_option, int(currentScore)))
        


root = Tk()
root.geometry("500x300")
game_gui = Yahtzee_gui(root)


root.mainloop()




# root = Tk()
# my_gui = Yahtzee_gui(root)
# root.mainloop()

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
