def sum_numbers(numbers=None):
    if numbers == []:
        return 0
    elif numbers:
        return sum([x for x in numbers])
    else:
        return sum(range(1,101))

"""
Write a function that can sum up numbers:

It should receive a list of n numbers.
If no argument is provided, return sum of numbers 1..100.
Look closely to the type of the function's default argument
"""