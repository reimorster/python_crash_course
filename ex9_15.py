#!/usr/bin/env python3

"""
 ex9_15: use a loop to see how hard might be to win the previous exercise lottery
 use a my_ticket variable with your guess
 count the number of attempts until winning
"""

from ex9_14 import Lottery

my_ticket = [1,2,3,'a']

lot = Lottery()

times=0

while lot.result() != my_ticket:
    times += 1

print(f"It took {times} tries before winning")


