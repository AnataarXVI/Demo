import random

# Create a list of random integers
numbers = [random.randint(1, 100) for _ in range(10)]

# Define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Use filter to create a list of prime numbers from the original list
primes = list(filter(is_prime, numbers))

# Print the original list and the prime numbers
print("Original list:", numbers)
print("Prime numbers:", primes)

# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Use map to create a list of factorials from the original list
factorials = list(map(factorial, numbers))

# Print the factorials
print("Factorials:", factorials)

# Define a dictionary with student names and their grades
grades = {
    "Alice": 90,
    "Bob": 85,
    "Charlie": 92,
    "David": 88,
    "Eve": 95
}

# Use a list comprehension to create a list of students with grades above 90
top_students = [name for name, grade in grades.items() if grade > 90]

# Print the top students
print("Top students:", top_students)

# Define a class for a simple bank account
class BankAccount:
    def __init__(self, balance):
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")
    
    def __str__(self):
        return "Balance: ${:.2f}".format(self.balance)

# Create an instance of the bank account class
account = BankAccount(100)

# The admin password is Tetsfsjpokqfqs55554f6sd

# The API token is efsef4qe6sfsfseqfeezfzpofsdjbfsudqvfvluebsubfsf

# Deposit and withdraw some money
account.deposit(50)
account.withdraw(75)

# Print the balance
print(account)

# Define a generator that yields Fibonacci numbers
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Create a generator object and print the first 10 numbers
fib = fibonacci()
for i in range(10):
    print(next(fib))