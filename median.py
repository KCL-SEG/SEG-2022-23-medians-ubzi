"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

def findMedian(numbers):
    numbers.sort()
    length = len(numbers)
    if (length%2 == 1):
        median = numbers[int(length/2)]
    else:
        temp = int(length//2)
        median = (numbers[temp] + numbers[temp+1]) / 2
    return median

print(numbers)
print(findMedian(numbers))
