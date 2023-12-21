# loops in python

# fruits = ["Apple", "Peach", "Pear"]
# for fruit in fruits:
#     print(fruit)

# for loop with range 
# for number in range(1, 11):
#     print(number)

# fizz buzz game
target = 100
for num in range(1, target + 1):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)