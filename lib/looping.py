# 1. Happy New Year Countdown using while loop
def happy_new_year():
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")


# 2. Square integers in a list
def square_integers(numbers):
    return [num ** 2 for num in numbers]


# 3. FizzBuzz from 1 to 100
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
