------------------------------
### PROJECT: DAILY PLANNER ###
------------------------------
'''
Creating a day planner for a student

    - we need a username and password from a user, grant or deny access
    - once access is granted, the system requests to get the time of the
      day from a user
    - the system then provides the user with details on the lecture
      title and location
    - the program then provides the student with previous lecture notes,
      the notes are contained in the provided file name 'Lecture notes.txt'
'''
import getpass

def day_planner(time_h_now):
    daily_task = { 10 : 'Programming Lecture, Room A',
                   12 : 'Computere Vision Lecture, Room C',
                   13 : 'Lunch TIme, Cafeteria',
                   15 : 'Project Meeting, Room E'}

    for task_time in daily_task.keys():
        if time_h_now <= task_time:
            print('You should attend: ', daily_task[task_time])
            break
            
    myfile = open(r'C:\Users\Nikola\Desktop\Git\PythonPojects\Day Planner\Lecture_Notes.txt')
    print(myfile.read())

username = 'nikola'
password = 'python$123'

input_username = input('Enter Username: ').lower()
input_password = getpass.getpass('Enter your password: ')

if username == input_username and password == input_password:
    print('Access granted. Welcome to the system!')
    
    time_h_now = float(input("what's the time now? Please use 24h format [8:00 AM and 3:00 PM][8:00 - 15:00]"))
    day_planner(time_h_now)
    
else:
    print('Username or password is not correct, access denied!')
