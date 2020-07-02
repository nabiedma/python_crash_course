# You can also work with a specific group of items in a list, which Python calls
# a slice.

players = ['charles', 'martina', 'michael', 'florence', 'eli']

# print("here are the first 3 players of my team:")
# for player in players[:3]:
#     print(player.title())

print("The first three items in the list are:")
print(players[:3])

print("Three items from the middle list are:")
print(players[1:4])

print("The last three items in the list are:")
print(players[-3:])