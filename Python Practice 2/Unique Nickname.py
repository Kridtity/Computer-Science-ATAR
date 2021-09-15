#Unique Nickname
while True:
    online = input("Online now: ")
    nickname = input("Nickname: ")
    online_list = online.split(" ")

    if nickname not in online_list:
        print("Welcome, {}!".format(nickname))
    else:
        print("Sorry, that nickname is taken.")
