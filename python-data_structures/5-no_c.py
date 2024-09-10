#!/usr/bin/python3
def no_c(my_string):
    # Create a new string with all 'c' and 'C' characters removed
    new_string = ''.join([char for char in my_string if char not in 'cC'])
    return new_string


if __name__ == "__main__":
    print(no_c("Best School"))
    print(no_c("Chicago"))
    print(no_c("C is fun!"))
