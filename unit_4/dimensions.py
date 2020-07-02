# Tuples are immutable lists. This means that are
# made of items that cannot change (immutable items)

dimensions = (200, 50)

print("original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)