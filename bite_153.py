import math
def round_up_or_down(transactions, up=True):
    """Round the list of transactions passed in.
       If up=True (default) round up, else round down.
       Return a new list of rounded values
    """
    rounded_list = []
    for x in transactions:
        rounded_list += [math.ceil(x) if up else math.floor(x)]  #ceil rounds up and floor down
    return (rounded_list)

round_up_or_down([2.05, 3.55, 4.50, 10.76, 100.25],True)
round_up_or_down([2.05, 3.55, 4.50, 10.76, 100.25],False)
round_up_or_down([1.55, 9.17, 5.67, 6.77, 2.33], True)
round_up_or_down([1.55, 9.17, 5.67, 6.77, 2.33], False)
