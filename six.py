# Write a program in python, that iterates from 1 through 100. Every time a number is divisible by 3, print the word Fizz. Every time a number is divisible by 5, print the word Buzz. Every time a number is divisible by both 3 and 5, print FizzBuzz.
# Output should look something like:
# 1
# 2
# Fizz
# 4
# Buzz
# 6
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz

def fizz_buzz(n):
    return ((not n % 3) * 'Fizz' + (not n % 5) * 'Buzz' or n )
for n in range(1,101):
    print(fizz_buzz(n))