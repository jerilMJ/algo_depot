import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time_watch

'''
    Idea is to find the first fizzbuzz line,
    i.e to find the fizzbuzz upto the max of 
    given numbers. The rest of the lines will
    be a repition of the first fizzbuzz line
    but the numbers changed (added by max).
'''
if __name__ == '__main__':
    watch = time_watch.TimeWatch()
    watch.start_measuring()

    fizzbuzz = []
    for i in range(1, 16):
        if i % 15 == 0:
            fizzbuzz.append('Fizz Buzz')
        elif i % 5 == 0:
            fizzbuzz.append('Buzz')
        elif i % 3 == 0:
            fizzbuzz.append('Fizz')
        else:
            fizzbuzz.append(str(i))

    fb = '\n'.join(fizzbuzz) + '\n'
    for _ in range((100 // 15) - 1):
        fizzbuzz = list(map(lambda x: str(int(x) + 15)
                            if x.isdigit() else x, fizzbuzz))
        fb += '\n'.join(fizzbuzz) + '\n'

    # Cutting down the overflow
    mult = 100 // 15
    overflow = abs(((mult + 1) * 15) - 100)
    fizzbuzz = list(map(lambda x: str(int(x) + 15)
                        if x.isdigit() else x, fizzbuzz))
    fizzbuzz = fizzbuzz[:-overflow]
    fb += '\n'.join(fizzbuzz) + '\n'

    print(fb)
    watch.stop_measuring('fizzbuzz_basic_better')
