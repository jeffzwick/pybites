names = 'Julian Bob PyBites Dante Martin Rodolfo'.split()
countries = 'Australia Spain Global Argentina USA Mexico'.split()


def enumerate_names_countries():
    """Outputs:
       1. Julian     Australia
       2. Bob        Spain
       3. PyBites    Global
       4. Dante      Argentina
       5. Martin     USA
       6. Rodolfo    Mexico"""

    for x, (value1, value2) in enumerate(zip(names, countries), 1): #enumerate counts interations, add 1 at the end makes it start with 1 instead of 0
        match = f"{x}. {value1:11}{value2}"  # :11 allows to pad 11 characters (filled with spaces after word)
        print(match)                           # check out https://pyformat.info/ for more info
                                               # you can center, right-align and insert characters like _ or -

(enumerate_names_countries())