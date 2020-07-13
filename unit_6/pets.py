musika = {
    'type': 'dog',
    'name': 'musika',
    'owner': 'alejandro'
}

hebe = {
    'type': 'dog',
    'name': 'hebe',
    'owner': 'yepun'
}

ginshu = {
    'type': 'cat',
    'name': 'ginshu',
    'owner': 'nestor'
}

pets = [musika, hebe, ginshu]

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['type']}. The owner "
    f"is {pet['owner'].title()}")
