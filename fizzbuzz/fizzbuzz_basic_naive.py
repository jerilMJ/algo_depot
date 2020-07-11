import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from time_watch import TimeWatch

'''
    Fizzbuzz naive way. Nothing much to explain,
    just the modulus way.
'''
if __name__ == '__main__':
    watch = TimeWatch()
    watch.start_measuring()

    fizzbuzz = ''
    for i in range(1, 101):
        if i % 15 == 0:
            fizzbuzz += 'Fizz Buzz'
        elif i % 5 == 0:
            fizzbuzz += 'Buzz'
        elif i % 3 == 0:
            fizzbuzz += 'Fizz'
        else:
            fizzbuzz += str(i)

        fizzbuzz += ' '

    print(fizzbuzz)
    watch.stop_measuring('fizzbuzz_basic_naive')
