from Tkinter import *
import ttk
from functools import partial

class Yahtzee_gui:

    tree_item_id = {"1s": "I00D", "2s": "I00C", "3s": "I00B", "4s":"I00A", "5s": "I009", "6s": "I008", "3 of a kind": "I007", "4 of a kind": "I006", "low run": "I005", "high run" : "I004", "full house": "I003", "sum" : "I002", "yahtzee": "I001"}
    
    def __init__(self, master, scorecard, turn):
        self.master = master
        master.title("Yahtzee!")

        self.label = Label(master, text="Welcome to Yahtzee!")
        self.label.pack()

        #create 2 frames side by side, one for the scorecard and the other for the throw of the dice

        self.scorecard_frame = Frame(master)
        self.scorecard_frame.pack(side = 'right')
        self.game_frame = Frame(master)
        self.game_frame.pack(side = 'left', fill = BOTH, expand = YES)
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = 'bottom')


        self.b_right = Button(self.scorecard_frame, text = "Take Selection", command=partial(self.take_selection_modify_scorecard, scorecard, turn))
        self.b_right.pack(side = 'top')
        self.b_roll_dice = Button(self.game_frame, text = "Roll dice!", command = partial(self.roll_dice_and_display_numbers, turn))
        self.b_roll_dice.pack(side= "top", expand = YES)

        self.make_scorecard()

    #initialise the scorecard table
    def make_scorecard(self):
        self.tree = ttk.Treeview(self.scorecard_frame, selectmode='browse')
        self.tree.pack(side='left')

        vsb = ttk.Scrollbar(orient="vertical",command=partial(self.tree.yview))
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

    def take_selection_modify_scorecard(self, a_scorecard, a_turn):
        selected = self.tree.focus()
        the_option = self.tree.item(selected, option='values')[0]

        if the_option == "1s":
            a_scorecard.take_1s(a_turn.dice_values)
        if the_option == "2s":
            a_scorecard.take_2s(a_turn.dice_values)
        if the_option == "3s":
            a_scorecard.take_3s(a_turn.dice_values)        
        if the_option == "4s":
            a_scorecard.take_4s(a_turn.dice_values)
        if the_option == "5s":
            a_scorecard.take_5s(a_turn.dice_values)
        if the_option == "6s":
            a_scorecard.take_6s(a_turn.dice_values)

        self.tree.item(self.tree_item_id[the_option], values = (the_option, a_scorecard.values[the_option]))

    def roll_dice_and_display_numbers(self, turn):
        if turn.throw_number == 1:
            turn.throw_multiple_dice(5)
        else:
            turn.throw_multiple_dice(3)        
        
        self.dice_label = Label(self.game_frame, text = "Your dice values are :  %s  " % turn.dice_values)
        self.dice_label.pack(side = "top", expand = YES)
        self.b_roll_dice.pack_forget()

        self.choice_label = Label(self.game_frame, text = "Would you like to re-roll any dices?")
        self.choice_label.pack(side = "top")
        self.choice_button_y = Button(self.game_frame, text = "Yes", command = partial(self.yes_to_re_roll, turn))
        self.choice_button_y.pack()
        self.choice_button_n = Button(self.game_frame, text = "No", command = partial(self.no_to_re_roll, turn))
        self.choice_button_n.pack()

    def yes_to_re_roll(self, turn):
        self.choice_label.pack_forget()
        self.choice_button_n.pack_forget()
        self.choice_button_y.pack_forget()
        self.which_dice = Label(self.game_frame, text = "Select the dice values that you would like to re-roll.")
        self.which_dice.pack()
        self.listbox = Listbox(self.game_frame, selectmode = MULTIPLE)

        self.listbox.insert(END)
        
        for item in turn.dice_values:
            self.listbox.insert(END, item)

        self.listbox.pack()

        self.take_dices = Button(self.game_frame, text = "OK", command = self.dice_to_re_roll_selected)
        self.take_dices.pack()

    def dice_to_re_roll_selected():
        #method to return the dice values that have been selected
        pass

    def no_to_re_roll(self, turn):
        self.choice_label.pack_forget()
        self.choice_button_n.pack_forget()
        self.choice_button_y.pack_forget()
        self.dice_label.pack_forget()
        self.final_dice_values = Label(self.game_frame, text = "Your final dice values for this throw are %s. Please take a selection from the right." % turn.dice_values)
        self.final_dice_values.pack(side = "top", expand = YES)
        



        

        


        





