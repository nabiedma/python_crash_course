favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print("\n")

for name in favorite_languages.keys():
    print(name.title())

# If you want to loop through the keys, you can avoid using
# keys() method, since is the default behavior when
# looping through a dictionary

print("\n")

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

print("\n")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

print("\n*** SORTED KEYS ***")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

# if you want to loop through the values of a dictionary, you should
# use the values() method to return a list of values without 
# any keys.

print("\n*** PRINTING ONLY VALUES ***")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print("\n*** PRINTING VALUES WITHOUT REPETITION ***")

# too see each language chosen without repetition, we can
# use a set. A set is a collection in which each item
# must be unique.

for language in set(favorite_languages.values()):
    print(language.title())

print("\n*** PRINTING LISTS INSIDE DICTIONARY ***")

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(f"\t{language.title()}")