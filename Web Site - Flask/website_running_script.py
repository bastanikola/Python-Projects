--------------------------------
### PROJECT: WEBSITE - FLASK ###
--------------------------------
#importing Flask class object from flask framework(library)
#importing render_template from flask framework(library)
from flask import Flask, render_template

#storing a Flask class object; Instantiating a Flask class object
#__name__ is a special variable
#when the script is executed, python assigned __main__ to __name__
    #__name__ = __main__
#when the script is imported, python assignes name of the script to __name__
    #__name__ = (name of the script)
app = Flask(__name__)

#creating a decorator with the url of the web page
#"/" means home page (localhost:5000)
#function will store the output to defined url
@app.route('/')
def home_page():
    #name of the render_template has to be created, edited and stored into templates folder
    #here we are just calling that template
    return render_template("home.html")

#python will create localhost:5000/about page
@app.route('/About')
def about_page():
    return render_template("about.html")

#if the script is imported, app.run(debug=True) won't be executed.
#This allow us to have control over this script
if __name__ == "__main__":
    app.run(debug=True)
