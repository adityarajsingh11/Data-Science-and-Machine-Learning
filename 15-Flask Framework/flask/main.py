from flask import Flask,render_template

'''It creates an instance of the flask class,
which is the WSGI application.'''


## WSGI Application
app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define a route for the Home page 
def welcome():
    return "<html><h1>Welcome to Flask.This is amazing<h1></html>"  # Return a welcome message

@app.route("/index")  
def index():
    return render_template("index.html")  ## integrated html file with flask

@app.route("/about")  
def about():
    return render_template("about.html")





if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug 