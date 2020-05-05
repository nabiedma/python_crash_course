# Python’s range() function makes it easy to generate a series of numbers.
# For example, you can use the range() function to print a series of numbers
# like this:

for value in range(1,6):
    print(value)

# If you want to make a list of numbers, you can convert the results of range()
# directly into a list using the list() function. When you wrap list() around a
# call to the range() function, the output will be a list of numbers.

numbers = list(range(1, 6))
print(numbers)