#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)  # Using a set to store unique numbers
    return sum(unique_numbers)  # Summing up the unique numbers


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
