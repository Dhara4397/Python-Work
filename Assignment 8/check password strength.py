def validate_password(password):
    if len(username)>=6 and username.isalnum() and not username[0].isdigit():
        return True
    else:
        return False


usernames=["dharaprajapati403","hello","bhavin145","012hello"]

for username in usernames :
     print(username," -> ",validate_username(username))


