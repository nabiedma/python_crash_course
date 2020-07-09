users = ['admin', 'robert', 'nabiedma', 'benny', 'yepu']

if users:
    for user in users:
        if user == 'admin':
            print("Hello Admin. Would you like to see a report?")
        else:
            print(f"Hello there {user}. Welcome back.")
else:
    print("There are still no users registered!")
