#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            string = "FizzBuzz"
        elif num % 5 == 0:
            string = "Buzz"
        elif num % 3 == 0:
            string = "Fizz"
        else:
            string = num
        print("{} ".format(string), end="")
