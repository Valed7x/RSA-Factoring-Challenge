#!/usr/bin/python3

import time
import math
import sys

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def find_prime_factors(n):
    for p in range(2, n + 1):
        if n % p == 0 and is_prime(p):
            q = n // p
            if is_prime(q):
                return p, q

def main(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                number = int(line.strip())
                p, q = find_prime_factors(number)
                print(f"{number}={p}*{q}")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except ValueError:
        print("Error: Invalid input in the file. The line must be a valid natural number.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: rsa.py <file>")
        sys.exit(1)

    filename = sys.argv[1]
    main(filename)
