cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    jeeps = str(cars.get('Jeep'))
    return jeeps.strip("[]").replace("'", "")


def get_first_model_each_manufacturer(cars=cars):
    """return a list of matching models (original ordering)"""
    return [v[0] for v in cars.values()]


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    model_match = []
    for models in cars.values():
        for model in models:
            if grep.lower() in model.lower():
                model_match.append(model)
    return sorted(model_match)

def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    return {k:sorted(v) for k,v in cars.items()}

print(get_all_jeeps(cars))
print(get_first_model_each_manufacturer(cars))
print(get_all_matching_models(cars,"trail"))
print(sort_car_models(cars))