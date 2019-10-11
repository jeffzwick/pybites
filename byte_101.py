MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if int(f"{age}") >= MIN_DRIVING_AGE:
        print(f"{name} is allowed to drive")
    else:
        print(f"{name} is not allowed to drive")

"""
In this Bite we'll get you to calculate whether a person is able to drive or 
not based on their minimum age which is stored in the constant MIN_DRIVING_AGE.

Print (not return) name is allowed to drive or name is not allowed to drive 
(note there is no period (.) at the end), based on the age being equal or 
greater than MIN_DRIVING_AGE.
"""