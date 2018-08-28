import os
from questions import questions
from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)

def ask_question(num):
    if num <= len(questions):
        return questions[num]['question']
    return "finished quiz"    
    
def get_answer(num):
    return questions[num]['answer']
    
def check_answer(answer):
    if answer == questions[1]['answer']:
        return True
    return False    


@app.route('/', methods=['GET', 'POST'])
def index():
    q_count = 1
    display_question = ask_question(q_count)
    if request.method == "POST":
        answer = str(request.form['user_answer']).lower()
        if check_answer(answer) == True:
            flash("correct")
        else:
            flash("false")
    
    return render_template('index.html',
    question=display_question)

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  