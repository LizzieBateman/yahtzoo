from random import randint
import time
import json
import collections



def roll_a_dice():

    return randint(1,6)


class Turn(object):
   
    def __init__(self):

        self.dice_values = []
        self.throw_number = 0


    def throw_multiple_dice(self, number_of_dice):

        for i in range(0,number_of_dice):

            self.dice_values.append(roll_a_dice())
            #order the list?

        return    
       

    def take_turn(self):
        
        #A turn is up to and including 3 individual throws of 5 or less dice
        self.throw_multiple_dice(5)
        self.throw_number += 1

        #Print result and throw number
        def show_throw_and_dices():
            print "This is throw number %s" % (self.throw_number)
            time.sleep(1.0)
            print "Your dice values are %s" % (self.dice_values)
            time.sleep(1.0)
        
        show_throw_and_dices()

        #Ask whether to throw again
        choice = raw_input("Would you like to roll again (you can re-roll a maximum of 5 dice?) [Y/N] ")

        time.sleep(1.0)

        if choice == "n":
            print ("End of your turn. Your dice values are %s" % self.dice_values)
            return
        
        #Ask which numbers to re-roll
        def additional_throw():
            dices_to_re_roll = raw_input("Which dice do you want to re-roll? ")
            
            time.sleep(1.0)

            numbers_to_re_roll = map(int, dices_to_re_roll.split()) 

            print "You want to re-roll %s ? " % numbers_to_re_roll + ""

            time.sleep(1.0)

            for value in numbers_to_re_roll:
                if value in (self.dice_values):
                    self.dice_values.remove(value)
                else:
                    pass
            print "Your remaining dice are %s " % self.dice_values +""
            time.sleep(1.0)

                          
                #Throw replacement dices
            self.throw_multiple_dice(len(numbers_to_re_roll))

            self.throw_number += 1

        additional_throw()
        
        #Print result and throw number
        show_throw_and_dices()

        #Ask whether to throw again
        choice = raw_input("Would you like to roll again (you can re-roll a maximum of 5 dice?) [Y/N] ")

        time.sleep(1.0)

        if choice == "n":
            print ("End of your turn. Your dice values are %s" % self.dice_values)
            return     

        additional_throw()
        #Print result and throw number

        show_throw_and_dices()

        print "This is the end of your turn. Your dices values are %s" % self.dice_values