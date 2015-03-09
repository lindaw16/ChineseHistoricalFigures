
import numpy as np
import Image
from random import randint
import sys



figures = ["yuanshikai", "jiangjieshi", "dengxiaoping", "huaguofeng",
           "huyaobang", "zhaoziyang", "jiangzemin", "hujintao",
           "xijinping", "jiangjinguo", "lidenghui", "chenshuibian"]

def openImage(name):
    image = Image.open(name + '.png')
    image.show()


# Run ReverseIndex instance
if __name__ == '__main__':
    while(True):
        x = randint(0,len(figures) -1)
        person = figures[x]

        image = openImage(person)

        guess = raw_input("What is this person's name?: ")

        while (guess.lower() != person):
            if (guess == ":("):
                print person
            guess = raw_input("wrong, guess again: ")

        print "yay!"

            
    
    
