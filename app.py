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
    
def save_to_leaderboard(username, score):
    with open('data/leaderboard.txt', 'a') as file:
        file.writelines('{0}: {1}\n'.format(username, score))    


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
            session["guess"] = 2
            
       # SUBMIT Button
        if "submit" in request.form:
            #User submits answer
            user_answer = str(request.form['user_answer']).lower()
            answer = check_answer(user_answer, session['q_index'])
            
            #Check how many guesses left
            if session['guess'] > 0:
                if answer == True:
                    session["score"] += 1
                    session['guess'] = 0 #So that the same correct answer can't be entered again
                    flash('Correct')
                else:
                    if session['guess'] == 2:
                        session['guess'] -= 1
                        flash('Incorrect, try again or continue to next question')
                    elif session['guess'] == 1:
                        answer = get_answer(session['q_index'])
                        session['guess'] -= 1
                        flash('Incorrect. The answer is ' + answer.capitalize())
            else:
                flash('You are out of guesses! Click Next to continue')
        
        # NEXT Button        
        if "next" in request.form:
            # Onto next question or results page if out of questions. Reset guess count
            num_qestions = how_many_questions()
            session['guess'] = 2
            if session["q_index"] < num_qestions-1:
                session["q_index"] += 1
                return redirect(url_for('quiz'))
            else: 
                #Finished quiz - no more questions
                return redirect(url_for('result'))
            
    q_index = session["q_index"]
    question = get_question(session['q_index'])
    image = get_image(session['q_index'])    
         
    return render_template('quiz.html', 
                question=question, 
                q_index=q_index, 
                image=image, 
                guess_count=session['guess']) 


@app.route('/result', methods=['GET', 'POST'])
def result():
    num_qestions = how_many_questions()
    low_score = session["score"] < num_qestions/2
     # Display different message if user has scored less than half correct)
    
    if request.method == "POST":
        
        # Leaderboard button: add name to leaderboard and view leaders
        if "leaderboard" in request.form:
            username = str(request.form['username'])
            save_to_leaderboard(username, session['score'])
            return redirect(url_for('leaderboard'))
            
        # Again button: start quiz from beginning    
        if "again" in request.form:
            session["q_index"] = 0
            session["score"] = 0
            session["guess"] = 2
            return redirect(url_for('quiz'))  
        
        if "exit" in request.form:
            return redirect(url_for('index'))
    
    return render_template('result.html', 
                    total_questions=num_qestions, 
                    user_score=session["score"], 
                    low_score=low_score,
                    guess_count=session['guess'])
  
  
@app.route('/leaderboard', methods=['GET', 'POST'])
def leaderboard(): 
    with open('data/leaderboard.txt', 'r') as f:
        data=f.readlines()
        score_list=[]
    # Sorting data code (adapted to be reversed) from https://stackoverflow.com/questions/32631581/python-how-do-i-sort-integers-in-a-text-file-into-ascending-and-or-descending-o    
    for line in data:
        score_list.append(line)
        sorted_data = sorted(score_list, key=lambda item: int(item.rsplit(': ')[-1].strip()), reverse=True)
        
    return render_template('leaderboard.html',
                    sorted_data=sorted_data)
    
    
app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)  
