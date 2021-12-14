
from flask_app import app

from flask import render_template, redirect, session, request, flash

from flask_app.models import model_validation #import all model tables 

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/process', methods = ['POST'] )

@app.route('/create', methods=['POST'])
def create_survey():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not model_validation.Survey.validate_survey(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:


    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment'] = request.form['comment']
    return redirect ('/results')

@app.route('/results')
def display_results():
    return render_template('results.html')
