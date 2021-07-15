#!/usr/bin/env python

import sys
import random
import copy


def second_choice_greater(first, second):
    result = None
    while result is None:
        prompt = f"Is {second} better than {first}? (y/n): "
        response = input(prompt)
        if len(response) == 1:
            if response[0] == 'y':
                result = True
            elif response[0] == 'n':
                result = False
    return result

def merge_sorted(main_list, work_list, left_start, right_start, end):
    i = left_start
    j = right_start
    x = left_start
    while x < end:
        if i < right_start and (
            j >= end
            or second_choice_greater(main_list[i], main_list[j])
        ):
            work_list[x] = main_list[i]
            i += 1
        else:
            work_list[x] = main_list[j]
            j += 1
        x += 1

def merge_sort(main_list):
    work_list = [None] * len(main_list)
    sorted_width = 1
    while sorted_width < len(main_list):
        for i in range(0, len(main_list), 2 * sorted_width):
            merge_sorted(
                main_list,
                work_list,
                i,
                min(i + sorted_width, len(main_list)),
                min(i + 2 * sorted_width, len(main_list))
            )
        main_list = copy.copy(work_list)
        sorted_width *= 2
    return main_list

def main():
    collection = ["apple", "orange", "pear", "banana"]
    result = merge_sort(collection)
    with open("output.txt", "w") as f:
        print("From worst to best:", file=f)
        for item in result:
            print(item, file=f)

if __name__ == '__main__':
    main()

sys.exit()
