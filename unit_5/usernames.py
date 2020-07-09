current_users = ['nabiedma', 'YEPU', 'benny', 'b0ss', 'Franku']

current_lowercase = [user.lower() for user in current_users]
print(current_lowercase)
new_users = ['nabiedma', 'Florinda', 'yepu', 'musi', 'nyes']

for user in new_users:
    if user in current_lowercase:
        print(f'We are sorry {user}, this username is already taken!.')
    else:
        print(f'Hey {user}, your name is available!')
