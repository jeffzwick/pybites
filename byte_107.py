def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    return [x for x in numbers if (x % 2 == 0 and x > 0)]


print (filter_positive_even_numbers([-4,-3,-2,-1,0,1,2,3,4]))