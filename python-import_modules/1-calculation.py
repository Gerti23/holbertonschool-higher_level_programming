#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))

    from calculator_1 import sub
    print("{} - {} = {}".format(a, b, sub(a, b)))

    from calculator_1 import mul
    print("{} * {} = {}".format(a, b, mul(a, b)))