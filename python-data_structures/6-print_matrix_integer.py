#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i, elem in enumerate(row):
            if i < len(row) - 1:
                print("{:d}".format(elem), end=" ")
            else:
                print("{:d}".format(elem))
        if not row:
            print()


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print_matrix_integer(matrix)
    print("--")
    print_matrix_integer()
