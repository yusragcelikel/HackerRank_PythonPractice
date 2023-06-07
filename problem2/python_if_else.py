import math
import os
import random
import re
import sys

if __name__ == '__main__':
    print("Enter a number in the inclusive range of 1 to 100.")
    n = int(input().strip())

    # check if the given number is in the inclusive range of 1 to 100.
    if n < 1:
        print("Not in the inclusive range of 1 to 100.")
    elif n > 100:
        print("Not in the inclusive range of 1 to 100.")

    # if the number is in range time to solve the problem
    else:
        if n % 2 == 0:
            if n > 20:
                print("Not Weird")
            elif n >= 6:
                print("Weird")
            elif n <= 5:
                print("Not Weird")
        else:
            print("Weird")
