# Organizing a List

cars = ['bmw', 'audi', 'toyota', 'subaru']
# cars.sort()
# print(cars)

# cars.sort(reverse=True)
# print(cars)

# To maintain the original order of a list but present it in a sorted order,
# you can use the sorted() function.
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# reverse() doesn't sort backward alphabetically; it simply reverses the order
# of the list:
cars.reverse()
print(cars)

# To find the length of a list, use len() function
print(len(cars))

print("////////////")
print("/// EXERCISE 3-8")
# Exercise 3-8
places = ['Madrid', 'Arizona', 'Liverpool', 'Tokyo', 'Philadelphia']
print(places)

print("List in alphabetical order:")
print(sorted(places))
print("List in its original order:")
print(places)
print("List in reversed alphabetical order:")
print(sorted(places, reverse=True))
print("List in its original order, once again:")
print(places)
places.reverse()
print(places)
places.reverse()
print(places)
places.sort()
print("List in alphabetical order:")
print(places)
places.sort(reverse=True)
print("List in reverse alphabetical order:")
print(places)

# The index -1 always returns the last item in a list
print(places[-1])
