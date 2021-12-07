from flask import Flask, render_template, session, request,redirect
app = Flask(__name__)
app.secret_key = "rootroot"

@app.route('/')
def home_page():
    return render_template("index.html")

@app.route('/process', methods = ['post'] )
def process():
    session['name']=request.form['name']
    session['location']=request.form['location']
    session['language']=request.form['language']
    session['comment'] = request.form['comment']
    return redirect ('/results')

@app.route('/results')
def display_results():
    return render_template('results.html')




if __name__=="__main__":
    app.run(debug=True)

