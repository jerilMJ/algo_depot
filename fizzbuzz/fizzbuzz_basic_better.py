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

    print(', '.join(fizzbuzz))
    for _ in range(100 // 15):
        fizzbuzz = list(map(lambda x: str(int(x) + 15)
                            if x.isdigit() else x, fizzbuzz))
        print(', '.join(fizzbuzz))

    watch.stop_measuring('fizzbuzz_basic_better')
