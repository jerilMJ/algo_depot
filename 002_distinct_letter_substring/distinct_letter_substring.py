import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import time_watch
import time
'''
    Let count = 0
    Let longest_string = 0
    Go through each character (Loop)
    append character to longest_string
    if a repeating character is encountered, 
    then:
        if length of string so far is greater than count,
            count = length
        else
            cut off substring upto the repeating character
'''
if __name__ == '__main__':
    input_string = input()

    start = time.time()
    watch = time_watch.TimeWatch()
    # watch.start_measuring()

    input_string = input_string.lower()
    longest_string = ''
    count = 0

    for index, character in enumerate(input_string):
        rem = len(input_string) - (index + 1)

        if count > rem:
            break

        if character not in longest_string:
            longest_string += character
        else:
            count = max(count, len(longest_string))
            pos = longest_string.find(character)
            longest_string = longest_string[pos + 1:]
            longest_string += character

    count = max(count, len(longest_string))
    print(count)
    print(time.time() - start)

    # watch.stop_measuring('distinct_letter_substring')
