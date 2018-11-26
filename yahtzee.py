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
root.geometry("500x300")
game_gui = Yahtzee_gui(root)

game_gui.take_selection()

def game():

    scorecard = Scorecard()

    
    while "empty" in scorecard.values.values():

        turn = Turn()
        turn.take_turn()
        scorecard.show_scorecard()

        while True:
                
                choice = game_gui.take_selection()

                if choice == "quit":
                    return
                
                if choice == "1s" and scorecard.values["1's"] != 'empty':
                    print "You have already taken 1's"
                    continue

                if choice == "1s":
                    scorecard.take_1s(turn.dice_values)
                    break

                if choice == "2s" and scorecard.values["2's"] != 'empty':
                    print "You have already taken 2's"
                    continue                      
  
                elif choice == "2s":
                    scorecard.take_2s(turn.dice_values)
                    break

                if choice == "3s" and scorecard.values["3's"] != 'empty':
                    print "You have already taken 3's"
                    continue

                elif choice == "3s":
                    scorecard.take_3s(turn.dice_values)
                    break


                if choice == "4s" and scorecard.values["4's"] != 'empty':
                    print "You have already taken 4's"
                    continue

                elif choice == "4s":
                    scorecard.take_4s(turn.dice_values)
                    break

                if choice == "5s" and scorecard.values["5's"] != 'empty':
                    print "You have already taken 5's"
                    continue

                elif choice == "5s":
                    scorecard.take_5s(turn.dice_values)
                    break

                if choice == "6s" and scorecard.values["6's"] != 'empty':
                    print "You have already taken 6's"
                    continue                
                
                elif choice == "6s":
                    scorecard.take_6s(turn.dice_values)
                    break

                if choice == "3 of a kind" and scorecard.values["3 of a kind"] != 'empty':
                    print "You have already taken 3 of a kind"
                    continue

                elif choice == "3 of a kind":
                    number = raw_input("Which number?")
                    number = int(number)

                    if turn.dice_values.count(number) < 3:
                        print "You don't have 3 of that number"
                        decision = raw_input("Do you still want to take 3 of a kind, [y/n]?")
                        if decision == "n":
                            continue
                        else: scorecard.no_three_of_a_kind()
                        break
                    else: 
                        scorecard.three_of_kind(turn.dice_values,number)
                        break

                if choice == "4 of a kind" and scorecard.values["4 of a kind"] != 'empty':
                    print "You have already taken 4 of a kind"
                    continue

                elif choice == "4 of a kind":
                    number = raw_input("Which number?")
                    number = int(number)
                    
                    if turn.dice_values.count(number) < 4:
                        print "You don't have 4 of that number"
                        decision = raw_input("Do you still want to take 4 of a kind, [y/n]?")
                        if decision == "n":
                            continue
                        else:
                            scorecard.no_four_of_a_kind()
                            break
                    
                    else:
                        scorecard.four_of_kind(turn.dice_values, number)
                        break


                if choice == "low run" and scorecard.values["low run"] != 'empty':
                    print "You have already taken low run"
                    continue

                elif choice == "low run":
                    scorecard.low_run(turn.dice_values)
                    break

                if choice == "low run" and collections.Counter(turn.dice_values) == collections.Counter([1,2,4,5,3]):
                    scorecard.low_run(turn.dice_values)
                    break

                elif choice == "low run" and collections.Counter(turn.dice_values) != collections.Counter([2,3,4,5,1]):
                    scorecard.no_low_run(turn.dice_values)
                    break

                if choice == "high run" and scorecard.values["high run"] != 'empty':
                    print "You have already taken high run"
                    continue

                if choice == "high run" and collections.Counter(turn.dice_values) == collections.Counter([2,3,4,5,6]):
                    scorecard.high_run(turn.dice_values)
                    break

                elif choice == "high run" and collections.Counter(turn.dice_values) != collections.Counter([2,3,4,5,6]):
                    scorecard.no_high_run(turn.dice_values)
                    break

                if choice == "full house" and scorecard.values["full house"] != 'empty':
                    print "You have already taken full house"
                    continue

                if choice == "full house":
                    countvalues = collections.Counter(turn.dice_values)
                    if countvalues.values() == [2,3] or countvalues.values() == [3,2] or countvalues.values() == [5]:
                        scorecard.full_house(turn.dice_values)
                        break
                    else: scorecard.no_full_house()
                    break

                if choice == "sum" and scorecard.values["sum"] != 'empty':
                    print "You have already taken sum"
                    continue

                elif choice == "sum":
                    scorecard.sum_of(turn.dice_values)
                    break

                if choice == "yahtzee" and scorecard.values["yahtzee"] != 'empty':
                    print "You have already taken yahtzee"
                    continue

                elif choice == "yahtzee" and collections.Counter(turn.dice_values) == collections.Counter([6,6,6,6,6]):
                    scorecard.yahtzee(turn.dice_values)
                    break

                elif choice == "yahtzee" and collections.Counter(turn.dice_values) != collections.Counter([6,6,6,6,6]):
                    scorecard.noyahtzee(turn.dice_values)
                    break

     

        scorecard.show_scorecard()

    print "End of Game. Your final score is %s" % scorecard.total_score()

root.mainloop()



