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
    
def check_answer(answer, num):
    if answer == questions[num]['answer']:
        return True
    return False
    
def init():
    score = 0
    q_index = 1
    return q_index
    
    
        
q_index = 1
question = ask_question(q_index)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global q_index
    global question
    
    if request.method == "POST":
        
        if request.form.get('start') == 'start':
            #POST request coming from landing page ie. start game
            
            return render_template('quiz.html', question=question, q_index=q_index)
        
        elif request.form['submit_btn'] == 'submit':
            #POST request from submit button. Check answer
            answer = str(request.form['user_answer']).lower()
            q_index = int(request.form.get('q_index'))
            if check_answer(answer, q_index) == True:
                flash('YES!')
            else:
                flash('Incorrect') 
               
            
            
        elif request.form['submit_btn'] == 'next':
            q_index += 1
            question = ask_question(q_index)
        return render_template('quiz.html', question=question, q_index=q_index)
            
         

    #if GET request show error and redirect to home page
    flash('Oops')
    return redirect('/')


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  