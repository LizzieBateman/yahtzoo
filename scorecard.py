from random import randint
import time
import json
import collections
from collections import Counter

class Scorecard(object):

    def __init__(self):

        self.values = {"1s":"empty" , "2s":"empty" , "3s":"empty" , "4s":"empty" , "5s": "empty" , "6s": "empty" , "3 of a kind" : "empty" , "4 of a kind" : "empty" , "low run" : "empty" , "high run" : "empty" , "full house" : "empty", "sum" : "empty" , "yahtzee" : "empty"}
        
    def show_scorecard(self):    
        
        print(json.dumps(self.values, indent=4, sort_keys=True))
    
    def take_1s(self, dices):
        
        sum_of_1s = 0
        
        for dice in dices:
            if dice == 1:
                sum_of_1s +=1
        
        self.values["1s"] = sum_of_1s
    
    def take_2s(self, dices):

        sum_of_2s = 0

        for dice in dices:
            if dice == 2:
                sum_of_2s +=2
        
        self.values["2s"] = sum_of_2s
    
    def take_3s(self, dices):
        
        sum_of_3s = 0
        
        for dice in dices:
            if dice == 3:
                sum_of_3s +=3
        
        self.values["3s"] = sum_of_3s
    
    def take_4s(self, dices):
        
        sum_of_4s = 0
        
        for dice in dices:
            if dice == 4:
                sum_of_4s +=4
        
        self.values["4s"] = sum_of_4s

    def take_5s(self, dices):
        
        sum_of_5s = 0
        
        for dice in dices:
            if dice == 5:
                sum_of_5s +=5
        
        self.values["5s"] = sum_of_5s

    def take_6s(self, dices):
        
        sum_of_6s = 0
        
        for dice in dices:
            if dice == 6:
                sum_of_6s +=6
        
        self.values["6s"] = sum_of_6s    

    def three_of_kind(self, dices):

        check_values = dict(Counter(dices).most_common(1))

        value = check_values.keys()[0]

        three_of_a_kind = 3*value
        
        self.values["3 of a kind"] = three_of_a_kind

    def no_three_of_a_kind(self):

        self.values["3 of a kind"] = "x"        

    def four_of_kind(self, dices, chosen_value):

        check_values = dict(Counter(dices).most_common(1))

        value = check_values.keys()[0]

        four_of_a_kind = 4*value

        self.values["4 of a kind"] = four_of_a_kind  
    
    def no_four_of_a_kind(self):

        self.values["4 of a kind"] = "x"

    def low_run(self, dices):

        self.values["low run"] = 40

    def no_low_run(self, dices):

        self.values["low run"] = "x"
    
    def high_run(self, dices):
        
        self.values["high run"] = 40

    def no_high_run(self, dices):
        
        self.values["high run"] = "x"

    def no_full_house(self):

        self.values["full house"] = "x"
    
    def full_house(self, dices):

        self.values["full house"] = 30    
    
    def sum_of(self,dices):
        
        total = 0

        for dice in dices:
            total += dice
        
        self.values["sum"] = total

    def yahtzee(self,dices):
        
        self.values["yahtzee"] = 100

    def noyahtzee(self, dices):

        self.values["yahtzee"] = "x"

    def total_score(self):

        totalscore = 0

        for key in self.values:
            if self.values[key] == "x":
                totalscore += 0
            else: totalscore += int(self.values[key])
         
        print totalscore