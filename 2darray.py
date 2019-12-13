#!/usr/bin/env python3

# Created by: Amir Mersad
# Created on: December 2019
# This program does unit6-04 ics3u

import random


def average(passed_array):
    total = 0
    counter = 0
    # Process
    for row_value in passed_array:
        for single_element in row_value:
            total += single_element
            counter += 1

    result = total / counter

    return result


def main():
    # This function gets the input and passes it to another function
    a_2d_array = []

    # Input and part of Process
    rows = input("enter how many rows you want: ")
    columns = input("enter how many columns you want: ")

    try:
        rows = int(rows)
        columns = int(columns)
    except(Exception):
        print("Wrong Input !!!")
        return

    if rows < 0 or columns < 0:
        print("Number must be more than 0!")
        return

    for counter in range(0, rows):
        temp_column = []
        for loop_counter_columns in range(0, columns):
            a_random_number = random.randint(0, 50)
            temp_column.append(a_random_number)
            print("{0} ".format(a_random_number), end="")
        a_2d_array.append(temp_column)
        print("")
    num_of_numbers = rows * columns

    # Passing to another function
    result = average(a_2d_array)

    # Output
    print("\n{0:.3f}".format(result))


if __name__ == "__main__":
    main()
