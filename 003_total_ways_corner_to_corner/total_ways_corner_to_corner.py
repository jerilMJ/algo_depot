import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time_watch
import math


def calculate_ways(r, c):
    tot = r + c

    if r != c:
        num = math.factorial(tot)
        den = math.factorial(r) * math.factorial(c)
    else:
        num = math.factorial(tot)
        den = math.factorial(tot - r) * math.factorial(r)

    return num // den


'''
    Simply find the total number of combinations
    we can make using each right and down movements.
'''
if (__name__ == '__main__'):
    print("Enter the no. of rows and columns: ")
    r, c = map(int, input().split())

    watch = time_watch.TimeWatch()
    watch.start_measuring()

    print(calculate_ways(r, c))

    watch.stop_measuring('total_ways_corner_to_corner')
