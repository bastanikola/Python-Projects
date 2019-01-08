#Question:
'''
Create a scrip that doesn't lets a user submit a password until they have
satisfied three conditions:
1. Password contains at least one number
2. Contains one uppercase letter
3. It is at least 5 characters long

Give the exact reason why the user has not created a correct password.
Before asking for password, ask for username.

Hint: Here you would need two loops, one for checking for username and one that
checks for the password.
'''
#Answer:
'''
while True:
    usr = input("Enter username: ")
    #open already created text file
    with open("users.txt", "r") as file:
        users = file.readlines()
        users = [i.strip("\n") for i in users]
    if usr in users:
        print("Username exists")
    else:
        print("Username is fine")
        break

while True:
    notes = []
    psw = input("Enter password: ")
    if not any(i.isdigit() for i in psw):
        notes.append("You need at least one number")
    if not any(i.isupper() for i in psw):
        notes.append("You need at least one uppercase letter")
    if len(psw) < 5:
        notes.append("You need at least 5 characters")
    if len(notes) == 0:
        print("Password is fine")
        break
    else:
        print("Please check the following: ")
        for note in notes:
            print(note)
'''
