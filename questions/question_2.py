"""
2) Write an async python function that writes every item in any given array with 1, 2, 4,
8, ... seconds apart. ex: for [“a”,” b, “c, “d”], “a” is printed in 1 sec, “b” is printed in 2
seconds, “c” is printed in 4 seconds, ...

>>> async_array(["a", "b", "c", "d"])
“a” is printed in 1 seconds
“b” is printed in 2 seconds
“c” is printed in 4 seconds
"d" is printed in 8 seconds
"""

import time


def async_array(array):
    time_0 = time.time()

    for i, value in enumerate(array):
        sleep_time = 2 ** i
        time.sleep(sleep_time)
        print(f'“{value}” is printed in {sleep_time} seconds')


if __name__ == '__main__':
    input_array = ["a", "b", "c", "d"]
    print(f'input = {input_array}')
    print("Result: async_array(input_array)")
    async_array(input_array)
