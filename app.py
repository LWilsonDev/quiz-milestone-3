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
    
def question_count():
    q_count = 1
    return q_count
    
def check_answer(answer):
    #answer = str(request.form['user_answer']).lower()
    if answer == questions[1]['answer']:
        return "correct"
    return "false"    


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  