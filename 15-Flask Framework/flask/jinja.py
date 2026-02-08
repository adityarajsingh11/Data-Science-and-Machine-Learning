## Building URL Dynamicallly with Flask
## Variable Rules
## Jinja 2 Template Engine

## Jinja2 Template Engine
'''
{{ }} expressions to print output in html
{%...%} conditions , for loops
{#...#} this ia for comments in jinja2
'''

from flask import Flask,render_template,request,redirect,url_for

'''It creates an instance of the flask class,
which is the WSGI application.'''


## WSGI Application
app = Flask(__name__)  # Create a Flask application instance

@app.route("/")  # Define a route for the Home page 
def welcome():
    return "<html><h1>Welcome to Flask.This is amazing<h1></html>"  # Return a welcome message

@app.route("/index",methods=["GET"])  
def index():
    return render_template("index.html")  ## integrated html file with flask

@app.route("/about")  
def about():
    return render_template("about.html")

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name=request.form['name']
        return f"Hello, {name}! Form submitted successfully."
    return render_template('form.html')
        
## Variable Rules
@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    return render_template("result.html",result=res)

## Variable Rules
@app.route('/successres/<int:score>')
def successres(score):
    res=""
    if score>=50:
        res="Passed"
    else:
        res="Failed"
    exp = {'score': score, 'result': res}
        
    return render_template("result1.html",result=exp)

## if condition in jinja2
@app.route('/successif/<int:score>')
def successif(score):
    return render_template("result.html",result=score)

## Variable Rules
@app.route('/fail/<int:score>')
def fail(score):
    return render_template("result.html",result=score)

@app.route('/getresults' , methods=['GET','POST'])
def getresults():
    total_score=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])

        total_score=(science+maths+c+data_science)/4
    else:
        return render_template('getresults.html')
    return redirect(url_for('successres',score=total_score))



if __name__ == "__main__":
    app.run(debug=True) # Run the application in debug 