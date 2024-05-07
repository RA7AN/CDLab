# Importing the time module to measure execution time
import time

# Function to calculate factorial recursively without optimization
def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n-1)

# Function to calculate factorial using memoization
def factorial_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 1
    memo[n] = n * factorial_memoization(n-1)
    return memo[n]

# Function to calculate factorial using loop unrolling
def factorial_loop_unrolling(n):
    result = 1
    while n >= 4:
        result *= n * (n-1) * (n-2) * (n-3)
        n -= 4
    while n > 0:
        result *= n
        n -= 1
    return result

# Main function to test and compare the execution time of different approaches
def main():
    num = 10  # Change the number to calculate factorial for a different input

    # Calculate factorial using recursive approach
    start_time = time.time()
    result_recursive = factorial_recursive(num)
    end_time = time.time()
    print("Factorial (Recursive):", result_recursive)
    print("Execution Time (Recursive):", end_time - start_time, "seconds")

    # Calculate factorial using memoization approach
    start_time = time.time()
    result_memoization = factorial_memoization(num)
    end_time = time.time()
    print("Factorial (Memoization):", result_memoization)
    print("Execution Time (Memoization):", end_time - start_time, "seconds")

    # Calculate factorial using loop unrolling approach
    start_time = time.time()
    result_loop_unrolling = factorial_loop_unrolling(num)
    end_time = time.time()
    print("Factorial (Loop Unrolling):", result_loop_unrolling)
    print("Execution Time (Loop Unrolling):", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()
