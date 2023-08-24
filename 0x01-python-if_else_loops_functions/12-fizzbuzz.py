#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        value = number
        if number % 15 == 0:
            value = "FizzBuzz"
        elif number % 3 == 0:
            value = "Fizz"
        elif number % 5 == 0:
            value = "Buzz"
        print(value, end=" ")
