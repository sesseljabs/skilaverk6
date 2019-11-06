import pygame
import random

# Fastar fyrir location og nafnið á myndunum
img_location = "img/"
img_name = "Dice-%s.png"

class Dice:
    def __init__(self):
        self.number = 0
        self.image = ""

    def __str__(self):
        return f"{self.number}"

    def throw(self):
        self.number = random.randint(1,6)
        self.image = img_name % self.number
        return self.number

class DiceThrower:
    def __init__(self, total=5):
        self.dice_count = total
        self.dice = Dice()
        self.dice_list = [Dice() for i in range(self.dice_count)]

    def __str__(self):
        li = [i.number for i in self.dice_list]
        return str(li)

    def throw(self, howmany=5): # full throw = 5,  all but one throw = 4
        if howmany > len(self.dice_list): # if this is bullshit make it the length of dice list
            howmany = len(self.dice_list)

        for i in range(0, howmany):
            self.dice_list[i].throw()

    def throwlast(self):
        self.dice_list[-1].throw()

    def counttotal(self):
        total = 0
        for i in self.dice_list:
            total += i.number

        return total


uwu = DiceThrower()
print(uwu)

uwu.throw(4)
print(uwu)
uwu.throwlast()
print(uwu)
print(uwu.counttotal())