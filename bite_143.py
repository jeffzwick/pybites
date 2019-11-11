NOT_FOUND = "Not found"

group1 = {'tim': 30, 'bob': 17, 'ana': 24}
group2 = {'ana': 26, 'thomas': 64, 'helen': 26}
group3 = {'brenda': 17, 'otto': 44, 'thomas': 46}


def get_person_age(name):
    """Look up name (case insensitive search) and return age.
       If name in > 1 dict, return the match of the group with
       greatest N (so group3 > group2 > group1)
    """
    if type(name) != str:
        return NOT_FOUND
    name = name.lower()
    if name in group3:
        return group3.get(name)
    elif name in group2:
        return group2.get(name)
    elif name in group1:
        return group1.get(name)
    else:
        return NOT_FOUND

print(get_person_age('tim'))
print(get_person_age('helen'))
print(get_person_age('otto'))
print(get_person_age('Tim'))
print(get_person_age('BOB'))
print(get_person_age('BrEnDa'))
print(get_person_age('timothy'))
print(get_person_age(None))
print(get_person_age(False))
print(get_person_age(-1))
print(get_person_age('thomas'))

"""
***SOLUTION***

name = str(name).lower()
# search goes in order of addition so as per requirements
# we insert groups from gt (#3) to lt (#1)
m = ChainMap(group3, group2, group1)    #chainmap combines all dict into one
return m.get(name, NOT_FOUND)
"""