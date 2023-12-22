# functions that accept input

def greet(name): #parameter
    print(f'Hello {name}')
    print("I'm learning how to code")
    print("And to we are dealing with functions that accepts input and i think we are also going to have a look at arguments and parameters, don't know how to sleep tho. smile.")

greet('Angela')  #argument

#program to check if a number is prime or not
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number")
    else:
        print("it's not a prime number")

n = int(input("Enter a number: "))
prime_checker(number=n)
