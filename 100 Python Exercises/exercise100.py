#Question:
'''
Create a web app with Flask that lets the user submit a username and a
password. The app then checks if the username exists in a text file, and it
also checks if the password contains at least one number, one uppercase
letter and it is at least 5 characters long.

Hint: You can use the code from exercise 81 and put it inside the function
that returns your HTML page.
'''
#Answer:
'''
from flask import Flask, render_template_string, request

app = Flask(__name__)

html = """
  		      <div class="form">
              <form action="{{url_for('sent')}}" method="POST">
  			        <input title="Your email address will be safe with us." placeholder="Enter username" type="text" name="username" required> <br>
  			        <input title="Your email address will be safe with us." placeholder="Enter password" type="text" name="password" required> <br>
                    {{message|safe}}
                <button class="go-button" type="submit"> Submit </button>
  		        </form>
          </div>
       """

@app.route("/")
def index():
    return render_template_string(html)

@app.route("/sent", methods=['GET', 'POST'])
def sent():
    line = None
    if request.method == 'POST':
        while True:
            usr = request.form['username']
            with open("users.txt", "r") as file:
                users = file.readlines()
                users = [i.strip("\n") for i in users]
            if usr in users:
                return render_template_string(html, message="Username exists!"+"<br>")
                continue
            else:
                print("Username is fine!")
                break
        while True:
            notes = []
            psw = request.form['password']
            if not any(i.isdigit() for i in psw):
                notes.append("You need at least one number")
            if not any(i.isupper() for i in psw):
                notes.append("You need at least one uppercase letter")
            if len(psw) < 5:
                notes.append("You need at least 5 characters")
            if len(notes) == 0:
                print("Password is fine"+"<br>")
                break
            else:
                return render_template_string(html, message="Please check password!")
        return render_template_string(html, message="Success"+"<br>")

if __name__ == "__main__":
    app.run(debug=True)

Explanation:

We have two while loops here which we got from exercise 81. The difference is
instead of getting input through an input function, we're getting input from
the html form with usr = request.form['username']. Then, if that user exists
in the text file, we insert the message "Username exists" in the HTML page and
we render the HTML form again. The same goes for the password.
'''
