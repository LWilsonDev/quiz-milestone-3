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
    ask_question(1)
    q_index= 1
    context = {
        'q_count': 1,
        'question': questions[q_index]['question'],
        'answer': questions[q_index]['answer'],
        
    }
    return context
    

@app.route('/', methods=['GET', 'POST'])
def index():
    
        
    #display_question = ask_question(q_count)
    
        #answer = str(request.form['user_answer']).lower()
   
    return render_template('index.html')    
#        if check_answer(answer, q_count) == True:
#            flash("correct")
#            q_count += 1
#        else:
#            flash("false")
#        if request.form['submit_btn'] == 'next':
#            
#            return redirect(url_for('index'))    
#    
#    return render_template('index.html',
#    question=display_question)

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == "POST":
        if request.form['start'] == 'start':
            context = init()
            return render_template('quiz.html', context=context)
        
#        
#    
#    return render_template('quiz.html', context=context)    
#        if check_answer(answer, q_count) == True:
#            flash("correct")
#            q_count += 1
#        else:
#            flash("false")
#        if request.form['submit_btn'] == 'next':
#            
#            return redirect(url_for('index'))    
#    
#    return render_template('index.html',
#    question=display_question)


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  