#Question:
'''
Create a scrip that doesn't lets a user submit a password until they have
satisfied three conditions:
1. Password contains at least one number
2. Contains one uppercase letter
3. It is at least 5 characters long

Give the exact reason why the user has not created a correct password

Hint: Here you could need to append the messages to a list.
'''
#Answer:
'''
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

Explanation:

Again, we're using a while loop. In the first if condition we check if there is
any number in the submitted password and if there is we append a message
string to the notes  list. Then, we check the next conditions in the next two
if  conditionals and keep adding messages to notes. We also check if the length
of notes  is zero, because it if is that means there were no message added
there which means the password is fine. Lastly, under else , we iterate through
the constructed list and print out its items (i.e messages).
'''
