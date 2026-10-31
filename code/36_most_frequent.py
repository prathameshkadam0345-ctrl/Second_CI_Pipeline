# Program 36: Find the Most Frequent Element in a List

def most_frequent(numbers):
    if not numbers:
        return None

    return max(numbers, key=numbers.count)