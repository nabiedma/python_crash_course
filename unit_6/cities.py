cities = {
    'san martin de los andes': {
        'country': 'argentina',
        'population': 9000,
        'fact': 'best food in patagonia'
    },
    'madrid': {
        'country': 'spain',
        'population': 6600000,
        'fact': 'best tapas in the world'
    },
    'tokyo': {
        'country': 'japan',
        'population': 9200000,
        'fact': 'largest metropolitan area in the world'
    }
}

print("Information about cities")

for city, info in cities.items():
    print(f"{city.title()}:")
    print(f"\tCountry: {info['country'].title()}")
    print(f"\tPopulation: {info['population']} citizens")
    print(f"\tInteresting Fact: it is the {info['fact']}")