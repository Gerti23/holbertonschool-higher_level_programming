#!/usr/bin/python3
print("".join("{}".format(chr(i)) for i in range(97, 105) if chr(i) not in ['b', 'f']), end="")