#!/usr/bin/python3
for num in range(0, 100):
    if num < 10:
        string = f"0{num:d}"
    else:
        string = f"{num:d}"
    if num == 99:
        print("{}".format(string))
    else:
        print("{}, ".format(string), end="")
