"""
Assignment 2.2: Problem 2 - Prime Logarithm and Convergence
July 15, 2025
Johnpaul Nnaji
"""

from math import log # Import log from math module

# Define a function that checks if a number is prime
def is_prime(num):
    if num < 2: # 0 and 1 are not prime
        return False
    # Check divisibility from 2 up to square root of num
    for i in range(2, int(num**0.5) + 1):  # or use math.sqrt(num)
        if num % i == 0: # If divisible, it's not prime
            return False
    return True # If no divisors found, it's prime

# Define a function to sum the logarithms of all primes between 2 and n
def sum_prime_logs(n):
    total = 0 # Start with a total of 0
    for i in range (2, n +1): # Loop through numbers from 2 to n
        if is_prime(i): # If it's a prime number
            total += log(i) # Add its natural logarithm to the total
    return total # Return the final sum

# Define values of n we want to test
test_values = [ 5000, 10000, 15000, 20000]

# Loop through each test value
for n in test_values:
    log_sum = sum_prime_logs(n) # Calculate sum of log(primes) up to n
    ratio = log_sum /n # Calculate the ratio of sum/n
    # Print the results with clean formatting
    print(f"n = {n} | Sum of log(primes) = {log_sum:.2f} | {ratio:.5f}")

