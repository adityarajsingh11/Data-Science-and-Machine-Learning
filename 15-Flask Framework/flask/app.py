from flask import Flask

'''It creates an instance of the flask class,
which is the WSGI application.'''


## WSGI Application
app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define a route for the Home page 
def welcome():
    return "Welcome to Flask.This is amazing"  # Return a welcome message

@app.route("/index")  
def index():
    return "Welcome to index Page"





if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug 