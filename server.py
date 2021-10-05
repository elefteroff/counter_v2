from typing import Counter
from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = 'its a secret'

@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 1
    else:
        session['counter'] += 1
    return render_template('index.html')

# @app.route('/plus_two')
# def plus_two():
#     if 'counter' not in session:
#         session['counter'] = 1
#     else:
#         session['counter'] += 2
#     return render_template('index.html')

@app.route('/destroy_session')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

