squares = []

for value in range(1,11):
    square = value ** 2
    squares.append(square)

print(squares)

# Same result, but using LISTS COMPREHENSIONS

sqrs = [value**2 for value in range(1,11)]
print(sqrs)