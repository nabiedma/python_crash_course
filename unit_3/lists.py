names = ['Roberto', 'Franku', 'Ale']
print(names[2])

message = f"Hey there {names[1]}"
print(message)

print("//////////////")

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# append() adds an element to the end of the list
motorcycles.append('ducati')
print(motorcycles)

# insert(position, value) adds a value at the specified index
motorcycles.insert(0, 'kawasaki')
print(motorcycles)

# If we know the position of the item, we can use 'del' statement
del motorcycles[0]
print(motorcycles)

# 'pop' removes the last item in a list, but lets you work with that item after removing it
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# We can also use 'pop(x)' to remove an item from any position in a list by including the index

print("//////////////")
print(motorcycles)
first_owned = motorcycles.pop(2)
print(f"the first motorcycle I owned was a {first_owned.title()}.")
print(motorcycles)

# remove() to remove by value.
print("//////////////")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

# remove() algo works with a value that's being removed from a list.
print("//////////////")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

# The remove() method deletes only the frst occurrence of the value you specify. If there’s
# a possibility the value appears more than once in the list, you’ll need to use a loop
# to make sure all occurrences of the value are removed.
print("//////////////")
print("Exercises Chapter 3")
print("//////////////")

# Exercise 3-4
print("Ex 3-4")
guests = ['Ricardo Fort', 'Chapu Nocioni', 'Batman']
message = f"Hey {guests[0]}, would you like to have dinner tonight?"
print(message)

# Exercise 3-5
print("Ex 3-5")
guests = ['Ricardo Fort', 'Chapu Nocioni', 'Batman']
print(guests)
guests.remove('Batman')
guests.append('The Joker')
print(f"Hey {guests[0]}, would you like to have dinner tonight?")
print(f"Hey {guests[1]}, would you like to have dinner tonight?")
print(f"Hey {guests[2]}, would you like to have dinner tonight?")

print("//////////////")
