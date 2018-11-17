from random import randint
import time
import json
import collections
from scorecard import Scorecard
from turn import Turn
from turn import roll_a_dice

def game():

    scorecard1 = Scorecard()

    
    while "empty" in scorecard1.values.values():

        turn1 = Turn()
        turn1.take_turn()
        scorecard1.show_scorecard()

        while True:
                choice = raw_input("What would you like to take?")

                if choice == "quit":
                    return
                
                if choice == "1s" and scorecard1.values["1's"] != 'empty':
                    print "You have already taken 1's"
                    continue

                if choice == "1s":
                    scorecard1.take_1s(turn1.dice_values)
                    break

                if choice == "2s" and scorecard1.values["2's"] != 'empty':
                    print "You have already taken 2's"
                    continue                      
  
                elif choice == "2s":
                    scorecard1.take_2s(turn1.dice_values)
                    break

                if choice == "3s" and scorecard1.values["3's"] != 'empty':
                    print "You have already taken 3's"
                    continue

                elif choice == "3s":
                    scorecard1.take_3s(turn1.dice_values)
                    break


                if choice == "4s" and scorecard1.values["4's"] != 'empty':
                    print "You have already taken 4's"
                    continue

                elif choice == "4s":
                    scorecard1.take_4s(turn1.dice_values)
                    break

                if choice == "5s" and scorecard1.values["5's"] != 'empty':
                    print "You have already taken 5's"
                    continue

                elif choice == "5s":
                    scorecard1.take_5s(turn1.dice_values)
                    break

                if choice == "6s" and scorecard1.values["6's"] != 'empty':
                    print "You have already taken 6's"
                    continue                
                
                elif choice == "6s":
                    scorecard1.take_6s(turn1.dice_values)
                    break

                if choice == "3 of a kind" and scorecard1.values["3 of a kind"] != 'empty':
                    print "You have already taken 3 of a kind"
                    continue

                elif choice == "3 of a kind":
                    number = raw_input("Which number?")
                    number = int(number)

                    if turn1.dice_values.count(number) < 3:
                        print "You don't have 3 of that number"
                        decision = raw_input("Do you still want to take 3 of a kind, [y/n]?")
                        if decision == "n":
                            continue
                        else: scorecard1.no_three_of_a_kind
                        break
                    else: scorecard1.three_of_kind(turn1.dice_values,number)
                    break

                if choice == "4 of a kind" and scorecard1.values["4 of a kind"] != 'empty':
                    print "You have already taken 4 of a kind"
                    continue

                elif choice == "4 of a kind":
                    number = raw_input("Which number?")
                    number = int(number)
                    
                    if turn1.dice_values.count(number) < 4:
                        print "You don't have 4 of that number"
                        decision = raw_input("Do you still want to take 4 of a kind, [y/n]?")
                        if decision == "n":
                            continue
                        else:
                            scorecard1.no_four_of_a_kind()
                            break
                    
                    else:
                        scorecard1.four_of_kind(turn1.dice_values, number)
                        break


                if choice == "low run" and scorecard1.values["low run"] != 'empty':
                    print "You have already taken low run"
                    continue

                elif choice == "low run":
                    scorecard1.low_run(turn1.dice_values)
                    break

                if choice == "low run" and collections.Counter(turn1.dice_values) == collections.Counter([1,2,4,5,3]):
                    scorecard1.low_run(turn1.dice_values)
                    break

                elif choice == "low run" and collections.Counter(turn1.dice_values) != collections.Counter([2,3,4,5,1]):
                    scorecard1.no_low_run(turn1.dice_values)
                    break

                if choice == "high run" and scorecard1.values["high run"] != 'empty':
                    print "You have already taken high run"
                    continue

                if choice == "high run" and collections.Counter(turn1.dice_values) == collections.Counter([2,3,4,5,6]):
                    scorecard1.high_run(turn1.dice_values)
                    break

                elif choice == "high run" and collections.Counter(turn1.dice_values) != collections.Counter([2,3,4,5,6]):
                    scorecard1.no_high_run(turn1.dice_values)
                    break

                if choice == "full house" and scorecard1.values["full house"] != 'empty':
                    print "You have already taken full house"
                    continue

                if choice == "full house":
                    countvalues = collections.Counter(turn1.dice_values)
                    if countvalues.values() == [2,3] or countvalues.values() == [3,2] or countvalues.values() == [5]:
                        scorecard1.full_house(turn1.dice_values)
                        break
                    else: scorecard1.no_full_house()
                    break

                if choice == "sum" and scorecard1.values["sum"] != 'empty':
                    print "You have already taken sum"
                    continue

                elif choice == "sum":
                    scorecard1.sum_of(turn1.dice_values)
                    break

                if choice == "yahtzee" and scorecard1.values["yahtzee"] != 'empty':
                    print "You have already taken yahtzee"
                    continue

                elif choice == "yahtzee" and collections.Counter(turn1.dice_values) == collections.Counter([6,6,6,6,6]):
                    scorecard1.yahtzee(turn1.dice_values)
                    break

                elif choice == "yahtzee" and collections.Counter(turn1.dice_values) != collections.Counter([6,6,6,6,6]):
                    scorecard1.noyahtzee(turn1.dice_values)
                    break

     

        scorecard1.show_scorecard()

    print "End of Game. Your final score is %s" % scorecard1.total_score()
    
game()

