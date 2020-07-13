rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yenisei': 'russia'
}

print("\n*** THE KEY-VALUE PAIR ***")
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}")

print("\n*** THE KEYS ***")
for river in rivers.keys():
    print(f"The {river.title()} river.")

print("\n*** THE KEYS ***")
for country in rivers.values():
    print(f"A river runs through {country.title()}.")