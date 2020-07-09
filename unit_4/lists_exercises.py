# Ex 4-3 Counting to Twenty
print("Counting to Twenty")
for value in range(1,21):
    print(value)

# Ex 4-4 Counting to Ten Thousands
print("Counting to Ten Thousands")
for value in range(1,10001):
    print(value)

# Ex 4-5 Summing a million
millions = []
for value in range(1, 1000001):
    millions.append(value)

print(f"El mínimo es: {min(millions)}")
print(f"El máximo es: {max(millions)}")
print(f"La suma de todos los números desde 1 a 1.000.000 es: {sum(millions)}.\n")

# Ex 4-6 Odd Numbers
print("Odd Numbers from 1 to 20")
odds = [value for value in range(1,20,2)]
print(odds)

# Ex 4-7 Threes
print("Multiples of 3 from 3 to 30")
threes = [value for value in range(3,31,3)]
print(threes)

# Ex 4-8 Cubes
print("Cubes from 1 to 10")
cubes = [value**3 for value in range(1,11)]
print(cubes)