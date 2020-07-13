favorite_places = {
    'san martin de los andes': 'ale',
    'cordoba': 'luis',
    'madrid': 'victor',
    'hong kong': 'sontiog'
}

for place, person in favorite_places.items():
    if person == 'luis':
        print(f"{person.title()}' favorite place is {place.title()}")
    else:
        print(f"{person.title()}'s favorite place is {place.title()}")
