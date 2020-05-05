from Tkinter import *
import ttk
from functools import partial
from collections import Counter

class Yahtzee_gui:

    tree_item_id = {"1s": "I00D", "2s": "I00C", "3s": "I00B", "4s":"I00A", "5s": "I009", "6s": "I008", "3 of a kind": "I007", "4 of a kind": "I006", "low run": "I005", "high run" : "I004", "full house": "I003", "sum" : "I002", "yahtzee": "I001"}
    
    def __init__(self, master, a_scorecard, a_turn):
        self.master = master
        master.title("Yahtzee!")

        self.label = Label(master, text="Welcome to Yahtzee!")
        self.label.pack()

        #create 2 frames side by side, one for the a_scorecard and the other for the throw of the dice

        self.scorecard_frame = Frame(master)
        self.scorecard_frame.pack(side = 'right')
        self.game_frame = Frame(master)
        self.game_frame.pack(side = 'left', fill = BOTH, expand = YES)
        self.close_button = Button(master, text="Close", command=master.quit)
        self.close_button.pack(side = 'bottom')


        self.take_selection_button = Button(self.scorecard_frame, text = "Take Selection", command=partial(self.take_selection_modify_scorecard, a_scorecard, a_turn))
        self.b_roll_dice = Button(self.game_frame, text = "Roll dice!", command = partial(self.roll_dice_and_display_numbers, a_turn))
        self.b_roll_dice.pack(side= "top", expand = YES)

        self.make_scorecard()

    #initialise the a_scorecard table
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

        while True:
                
            the_option = self.tree.item(selected, option='values')[0]
                
            if the_option == "1s" and a_scorecard.values["1s"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 1s")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "1s":
                a_scorecard.take_1s(a_turn.dice_values)
                break

            if the_option == "2s" and a_scorecard.values["2s"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 2s")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "2s":
                a_scorecard.take_2s(a_turn.dice_values)
                break

            if the_option == "3s" and a_scorecard.values["3s"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 3s")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "3s":
                a_scorecard.take_3s(a_turn.dice_values)
                break

            if the_option == "4s" and a_scorecard.values["4s"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 4s")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "4s":
                a_scorecard.take_4s(a_turn.dice_values)
                break

            if the_option == "5s" and a_scorecard.values["5s"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 5s")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "5s":
                a_scorecard.take_5s(a_turn.dice_values)
                break

            if the_option == "6s" and a_scorecard.values["6s"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 6s")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "6s":
                a_scorecard.take_6s(a_turn.dice_values)
                break

            if the_option == "3 of a kind" and a_scorecard.values["3 of a kind"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 3 of a kind")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "3 of a kind":

                #find if there is a number with 3 or 4 occurences and then if there are 3 or 4 of a certain number, then perform 3 of a kind on a the scorecard, if not, then perform no 3 of a kind

                check_values = dict(Counter(a_turn.dice_values).most_common(1))

                if check_values.values()[0] >= 3:
                    a_scorecard.three_of_kind(a_turn.dice_values)
                    break
                else:
                    a_scorecard.no_three_of_a_kind()
                    break

            if the_option == "4 of a kind" and a_scorecard.values["4 of a kind"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 4 of a kind")
                self.warning_label.pack(side="bottom") 
                break
            
            if the_option == "4 of a kind":

                #find if there is a number with 3 or 4 occurences and then if there are 3 or 4 of a certain number, then perform 3 of a kind on a the scorecard, if not, then perform no 3 of a kind

                check_values = dict(Counter(a_turn.dice_values).most_common(1))

                if check_values.values()[0] >= 4:
                    a_scorecard.four_of_kind(a_turn.dice_values)
                    break
                else:
                    a_scorecard.no_four_of_a_kind()
                    break

            if the_option == "low run" and a_scorecard.values["low run"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken low run")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "low run" and Counter(a_turn.dice_values) == Counter([1,2,4,5,3]):
                a_scorecard.low_run(a_turn.dice_values)
                break

            if the_option == "low run" and Counter(a_turn.dice_values) != Counter([2,3,4,5,1]):
                a_scorecard.no_low_run(a_turn.dice_values)
                break

            if the_option == "high run" and a_scorecard.values["high run"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken high")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "high run" and Counter(a_turn.dice_values) == Counter([2,3,4,5,6]):
                a_scorecard.high_run(a_turn.dice_values)
                break

            if the_option == "high run" and Counter(a_turn.dice_values) != Counter([2,3,4,5,6]):
                a_scorecard.no_high_run(a_turn.dice_values)
                break

            if the_option == "full house" and a_scorecard.values["full house"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken 4 of a kind")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "full house":
                countvalues = Counter(a_turn.dice_values)
                if countvalues.values() == [2,3] or countvalues.values() == [3,2] or countvalues.values() == [5]:
                    a_scorecard.full_house(a_turn.dice_values)
                    break
                else: a_scorecard.no_full_house()
                break

            if the_option == "sum" and a_scorecard.values["sum"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken sum")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "sum":
                a_scorecard.sum_of(a_turn.dice_values)
                break

            if the_option == "yahtzee" and a_scorecard.values["yahtzee"] != 'empty':
                self.warning_label = Label(self.scorecard_frame,text = "You have already taken yahtzee")
                self.warning_label.pack(side="bottom") 
                break

            if the_option == "yahtzee" and Counter(a_turn.dice_values) == Counter([6,6,6,6,6]):
                a_scorecard.yahtzee(a_turn.dice_values)
                break

            if the_option == "yahtzee" and Counter(a_turn.dice_values) != Counter([6,6,6,6,6]):
                a_scorecard.noyahtzee(a_turn.dice_values)
                break

           
        self.tree.item(self.tree_item_id[the_option], values = (the_option, a_scorecard.values[the_option]))

        self.take_selection_button.pack_forget()

        a_turn.dice_values = []
    
        self.b_roll_dice.pack(side= "top", expand = YES)
        
        if a_turn.throw_number == 0:
            self.dice_label2.pack_forget()

        elif a_turn.throw_number == 1:
            self.dice_label4.pack_forget()

        elif a_turn.throw_number == 2:
            self.dice_label5.pack_forget()
        
        a_turn.throw_number = 0

    def roll_dice_and_display_numbers(self, a_turn):
        
        a_turn.throw_number = 0
        
        a_turn.throw_multiple_dice(5)

        self.dice_label1 = Label(self.game_frame, text = "Your dice values are :  %s  " % a_turn.dice_values)
        self.dice_label1.pack(side = "top", expand = YES)
        self.b_roll_dice.pack_forget()

        self.choice_label = Label(self.game_frame, text = "Would you like to re-roll any dices?")
        self.choice_label.pack(side = "top")
        self.choice_button_y = Button(self.game_frame, text = "Yes", command = partial(self.yes_to_re_roll, a_turn))
        self.choice_button_y.pack()
        self.choice_button_n = Button(self.game_frame, text = "No", command = partial(self.no_to_re_roll, a_turn))
        self.choice_button_n.pack()

    def yes_to_re_roll(self, a_turn):

        a_turn.throw_number += 1

        self.choice_label.pack_forget()
        self.choice_button_n.pack_forget()
        self.choice_button_y.pack_forget()
        self.which_dice = Label(self.game_frame, text = "Select the dice values that you would like to re-roll.")
        self.which_dice.pack()
        self.listbox = Listbox(self.game_frame, selectmode = MULTIPLE)

        self.listbox.insert(END)
        
        for item in a_turn.dice_values:
            self.listbox.insert(END, item)

        self.listbox.pack()

        self.take_dices = Button(self.game_frame, text = "OK", command = partial(self.dice_to_re_roll_selected, a_turn))
        self.take_dices.pack()

    def dice_to_re_roll_selected(self, a_turn):
        #method to return the dice values that have been selected
        index_of_dice_selected = self.listbox.curselection()

        dices_to_re_roll = []

        for index in index_of_dice_selected:
            dices_to_re_roll.append(self.listbox.get(index))

        for value in dices_to_re_roll:
            if value in (a_turn.dice_values):
                a_turn.dice_values.remove(value)
            else:
                pass
        
        a_turn.throw_multiple_dice(len(dices_to_re_roll))

        #self.throw_number_label = Label(self.game_frame, text = "Throw number =  %s " % a_turn.throw_number)
        #self.throw_number_label.pack()

        if a_turn.throw_number == 1:

            self.listbox.pack_forget()
            self.dice_label1.pack_forget()
            self.which_dice.pack_forget()
            self.take_dices.pack_forget()
            self.dice_label3 = Label(self.game_frame, text = "Your dice values are now :  %s " % a_turn.dice_values)
            self.dice_label3.pack(side = "top", expand = YES)
            self.choice_label = Label(self.game_frame, text = "Would you like to re-roll any dices?")
            self.choice_label.pack(side = "top")
            self.choice_button_y = Button(self.game_frame, text = "Yes", command = partial(self.yes_to_re_roll, a_turn))
            self.choice_button_y.pack()
            self.choice_button_n = Button(self.game_frame, text = "No", command = partial(self.no_to_re_roll, a_turn))
            self.choice_button_n.pack()
  
        elif a_turn.throw_number == 2:

            self.listbox.pack_forget()
            self.dice_label3.pack_forget()
            self.which_dice.pack_forget()
            self.take_dices.pack_forget()
            self.dice_label5 = Label(self.game_frame, text = "Your final dice values are :  %s. \n Please take your selection. " % a_turn.dice_values)
            self.dice_label5.pack(side = "top", expand = YES)
            self.take_selection_button.pack(side = 'top')

    def no_to_re_roll(self, a_turn):
        self.take_selection_button.pack(side = 'top')

        #self.throw_number_label1 = Label(self.game_frame, text = "Throw number =  %s " % a_turn.throw_number)
        #self.throw_number_label1.pack()


        if a_turn.throw_number == 0:
            
            self.dice_label2 = Label(self.game_frame, text = "Your final dice values for this throw are %s. \n Please take your selection." % a_turn.dice_values)
            self.dice_label2.pack()
            self.dice_label1.pack_forget()
            self.take_selection_button.pack(side = 'top')
        
        elif a_turn.throw_number == 1:

            self.dice_label4 = Label(self.game_frame, text = "Your final dice values for this throw are %s. \n Please take your selection." % a_turn.dice_values)
            self.dice_label4.pack()
            self.dice_label3.pack_forget()
            self.take_selection_button.pack(side = 'top')
        
        self.choice_label.pack_forget()
        self.choice_button_n.pack_forget()
        self.choice_button_y.pack_forget()







        

        


        





