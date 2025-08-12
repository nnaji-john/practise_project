"""
Assignment 2.1: Problem 1 - Find the 450th Prime number
July 15, 2025
Johnpaul Nnaji
"""

import math # Import the math module to use square root

# Define a function that checks if a number is prime number
def is_prime(num):
    if num < 2: # 0 and 1 are not prime numbers
        return False
    # Check divisibility from 2 up to square root of num
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0: # If divisible, it's not prime number
            return False
    return True # If no divisors found, it's prime number

# Loop unith the 450th Prime number is found
# Initialize prime counter
prime_count = 0
num = 2 # start from the first prime number
primes = [] # Create a list to store prime numbers found

# Keep running until we find 450 prime numbers
while prime_count < 450:
    if is_prime(num) : # Check if current number is prime
        primes.append(num) # Store the prime number
        prime_count += 1 # Increase the count
        if prime_count % 50 == 0: # Print progress every 50 primes found
            print(f"{prime_count} prime numbers found so far,")
    num += 1 # Move to the next number


# Print The Final Result
print(f"\nThe 450th prime number is: {primes[-1]}")