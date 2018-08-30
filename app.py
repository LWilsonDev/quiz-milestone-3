import os, json

from flask import Flask, redirect, render_template, request, session, url_for, flash

app = Flask(__name__)
app.secret_key = os.urandom(24)


########## Functions #############

def get_question_data(index):
    with open('data/questions.json') as json_questions:
        questions = json.loads(json_questions.read())
        return questions[index]

def how_many_questions(): 
    '''
    Function to find the number of questions in the json file.
    '''
    with open('data/questions.json') as json_questions:
        q_dict = json.loads(json_questions.read())
        return len(q_dict)

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
    #remove session incase same user is returning
    for key in session.keys():
        session.pop(key)
    return render_template('index.html')    


@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    
    if request.method == "POST":
        
        if "q_index" not in session:
        #start of game - set up first question
            session["q_index"] = 0
            session["score"] = 0
            session["guess"] = 0
            question = get_question(session['q_index'])
            image = get_image(session['q_index'])
       
        if request.form.get('submit_btn', None) == "submit":
            user_answer = str(request.form['user_answer']).lower()
            answer = check_answer(user_answer, session['q_index'])
            session['guess'] += 1
            
            if session['guess'] <= 2:
                if answer == True:
                    session["score"] += 1
                    session['guess'] = 3 #So that the same correct answer can't be entered again
                    flash('Correct')
                else:
                    if session['guess'] == 1:
                        flash('Incorrect, try again')
                    elif session['guess'] == 2:
                        answer = get_answer(session['q_index'])
                        flash('Incorrect. The answer is ' + answer.capitalize())
            else:
                flash('You are out of guesses! Click Next to continue')
                
        if request.form.get('submit_btn', None) == "next":
            num_qestions = how_many_questions()
            session['guess'] = 0
            if session["q_index"] < num_qestions-1:
                session["q_index"] += 1
                return redirect(url_for('quiz'))
            else:
                # Display different message if user has scored less than half correct)
                low_score = session["score"] < num_qestions/2
                    
               
                return render_template('result.html', total_questions=num_qestions, user_score=session["score"], low_score=low_score)
            
    q_index = session["q_index"]
    question = get_question(session['q_index'])
    image = get_image(session['q_index'])    
         
    return render_template('quiz.html', question=question, q_index=q_index, image=image) 
    


app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  
