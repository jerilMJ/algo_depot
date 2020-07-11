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
    print('Enter fizzbuzz limit: ')
    limit = int(input())

    print('How many conditions?')
    total_conditions = int(input())

    print('Enter the numbers')
    nums = list(map(int, input().split(' ')))

    print('Enter the placeholders')
    names = input().split(' ')

    watch = time_watch.TimeWatch()
    watch.start_measuring()

    greatest = max(nums)

    num_name = {}

    for num, name in zip(nums, names):
        num_name[num] = name

    print()
    fizzbuzz = []
    nums.sort(reverse=True)
    for i in range(1, greatest + 1):
        div = False
        for num in nums:
            if i % num == 0:
                div = True
                fizzbuzz.append(num_name[num])
                break
        if not div:
            fizzbuzz.append(str(i))

    fb = ''
    fb += ', '.join(fizzbuzz) + ', '
    for _ in range((limit // greatest) - 1):
        fizzbuzz = list(map(lambda x: str(int(x) + greatest)
                            if x.isdigit() else x, fizzbuzz))
        fb += ', '.join(fizzbuzz) + ', '

    # Cutting down the overflow
    if limit % greatest != 0:
        mult = limit // greatest
        overflow = abs(((mult + 1) * greatest) - limit)
        fizzbuzz = list(map(lambda x: str(int(x) + greatest)
                            if x.isdigit() else x, fizzbuzz))
        fizzbuzz = fizzbuzz[:-overflow]
        fb += ', '.join(fizzbuzz) + ', '

    print(fb)
    watch.stop_measuring('fizzbuzz_advanced')
