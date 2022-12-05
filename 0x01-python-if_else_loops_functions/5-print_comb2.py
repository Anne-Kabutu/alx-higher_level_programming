#!/usr/bin/python3
for number in range(0, 100):
    if number < 10:
        string = f"0{number:d}"
    else:
        string = f"{number:d}"
    if number == 99:
        print("{}".format(string))
    else:
        print("{}, ".format(string), end="")
