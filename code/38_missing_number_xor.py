# Program 38: Find Missing Number Using XOR

def find_missing_number(numbers):
    n = len(numbers) + 1

    result = 0

    for i in range(1, n + 1):
        result ^= i

    for num in numbers:
        result ^= num

    return result