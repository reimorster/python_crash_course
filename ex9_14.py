#!/usr/bin/env python3

"""
 Lottery:  make a list or tuple containing 10 numbers and 5 letters
 Randomly select 4 elements from it and say any ticket with these 
 4 numbers or letters wins a prize
"""

from random import choice

class Lottery:
    def __init__(self, mylist=[0,1,2,3,4,5,6,7,8,9,"a","b","c","d","e"]):
        self.list=mylist

    def result(self):
        res = []
        for i in range(4):
            res.append(choice(self.list))

        return res

