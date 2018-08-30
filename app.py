import os, json

from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)


########## Functions #############

def get_question_data(index):
    with open('data/questions.json') as json_questions:
        questions = json.loads(json_questions.read())
        return questions[index]

def get_question(index):
    data = get_question_data(index)
    question = data['question']
    return question
    
def get_answer(index):
    data = get_question_data(index)
    answer = data['answer']
    return answer
    
def get_image(index):
    data = get_question_data(index)
    image = data['image']
    return image
   
def check_answer(user_answer, index):
    if user_answer == get_answer(index):
        return True
    return False

######## Routes ############

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')    


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    
   
    if request.method == "POST":
        
        if "q_index" not in session:
        #start of game - set up first question
            session["q_index"] = 0
            session["correct_count"] = 0
            session["guess_num"] = 2
            question = get_question(session['q_index'])
            image = get_image(session['q_index'])
       
        if request.form.get('submit_btn', None) == "submit":
            user_answer = str(request.form['user_answer']).lower()
            answer = check_answer(user_answer, session['q_index'])
            if answer == True:
                flash('Correct')
            else:
                flash('Incorrect')
        
        if request.form.get('submit_btn', None) == "next":  
            session["q_index"] += 1
            return redirect(url_for('quiz'))
            
    q_index = session["q_index"]
    question = get_question(session['q_index'])
    image = get_image(session['q_index'])    
         
    return render_template('quiz.html', question=question, q_index=q_index, image=image) 
    


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  
