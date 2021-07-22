from flask import Flask, render_template, redirect, request
import requests, random, html
app = Flask(__name__)


app.config['SECRET_KEY'] = '51'

@app.route("/quiz")
def quiz():

    return render_template("quiz.html")

question_list = []
@app.route("/user/input", methods = ["POST"])
def user_input():
    global question_list
    global correct_answers
    global final_answers
    global amount
    amount = request.form.get("amount")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    typeQ = request.form.get("type")
    
    url = getUrl(amount, category , difficulty, typeQ)
    Json = getJson(url)
    correct_answers, final_answers, question_list = toDict(Json)
    
    #session['correct_answers'] = correct_answers
    #session["final_answers"] = final_answers
    #session["question_list"] = question_list
    #print('INITIAL LIST: ', question_list)
    

    #next_que = [0]  
   # session["next_que"] = next_que
    #quiz(correct_answers,final_answers,question_list) 
    #next_question(correct_answers,final_answers,question_list)

    return quiz(correct_answers,final_answers,question_list)
   

def getUrl(amount, category, difficulty, typeQ):
    Base_url = 'https://opentdb.com/api.php?amount=' + str(amount)
    final_url = Base_url
   #categoryA
    if category != 'default_c':
        final_url =final_url + '&category=' + str(category) 
      
   #difficulty
    if difficulty != 'default_d':
        final_url = final_url + '&difficulty=' + str(difficulty) 
      
    #type  
    if typeQ != 'default_t':
        final_url = final_url + '&type=' + str(typeQ) 
      
    return final_url
   
   
def getJson(final_url):
    response = requests.get(final_url)
    data = response.json()
    return data

      
def toDict(json_data):
    question_list = {}
    correct_list = []
    correct = []
    answers = []
    final_answers = []
    for value in json_data['results']:
        #print(value)
        #questions.append(value['question'])
        question_list[value['question']] = value['type']
        correct_list.append(value['correct_answer'])
        correct = value['correct_answer']
        answers = value['incorrect_answers']
        answers.append(correct)
        random.shuffle(answers)
        final_answers.append(answers)
    print('q list ', question_list)
   # print('f answers ', final_answers)
    #print('c list' , correct_list)
    
    return correct_list, final_answers, question_list


@app.route("/")
@app.route("/home")
def home():
    global next_que
    global question_list
    global correct_answers
    global final_answers 
    global amount
    global score
    next_que = 0
    amount = 0
    score = 0
    question_list = []
    final_answers = []
    correct_answers = []
    return render_template("home.html")


@app.route("/quiz")
def quiz_2():
    return render_template("quiz.html")

@app.route("/nickname", methods = ["POST"])
def nickname_page():
    global nickname
    nickname = request.form.get("nickname")
    return render_template("info.html")

@app.route("/info")
def info():
    return render_template("info.html")


def quiz(correct_answers,final_answers,question_list):
    #redirect("/quiz")
    question_type = list(question_list.values())[0]
        #print(question_type)                     
       # print(next(iter(question_list)))                   
    question_name = list(question_list.keys())[0]                    
    
    if question_type == 'multiple':            
        return render_template('quiz.html', question = '1) ' + html.unescape(question_name), answer1 = html.unescape(final_answers[0][0]), answer2 = html.unescape(final_answers[0][1]), answer3 = html.unescape(final_answers[0][2]), answer4 = html.unescape(final_answers[0][3]))
              
                            
    if question_type == 'boolean':
        return render_template("quiz.html", question = '1) ' + html.unescape(question_name), answer1 = 'True', answer2 = 'False')
                            

next_que = 0
score = 0
@app.route('/next/question', methods = ["POST"])
def next_question():
    global next_que
    global question_list
    global correct_answers
    global final_answers 
    global amount
    global score

    answer = request.form.get("answers")
    
    #print('outside', final_answers[next_que][int(answer)])
    #print('outside', correct_answers[next_que])
    if(final_answers[next_que][int(answer)] == correct_answers[next_que]): 
        print(final_answers[next_que][int(answer)])
        print(correct_answers[next_que])
        score+=1

    if int(next_que + 1) == int(amount):
        print('\n\n\nLAST QUESTION\n\n\n\n')
        link = "/display_score/" + str(score) + str(amount)
        return redirect(link)
        #print(score)
        #return home()
    next_que += 1
    question_type = list(question_list.values())[next_que]
    question_name = list(question_list.keys())[next_que]                    
    #print(question_name) 

    
    #print(next_que)
    #print('AMT: ', amount)
    
    
      
    if question_type == 'multiple':
        print(final_answers)
        return render_template('quiz.html',  question = str(next_que + 1) + ") "+ html.unescape(question_name), answer1 = html.unescape(final_answers[next_que][0]), answer2 = html.unescape(final_answers[next_que][1]), answer3 = html.unescape(final_answers[next_que][2]), 
                                   answer4 = html.unescape(final_answers[next_que][3]))
              
                            
    if question_type == 'boolean':   
        print(final_answers)
        return render_template("quiz.html", question = str(next_que + 1) + ") "+ html.unescape(question_name), answer1 = 'True', answer2 = 'False')

@app.route("/display_score/<score><amount>")
def display_score(score, amount):
    global nickname
    try:
        return render_template("score.html",  nickname = nickname, score = score, amount = amount)  
    except :
        return render_template("score.html",  nickname = "User", score = score, amount = amount)  
    
     
   

      
if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")
    
    