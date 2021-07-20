from flask import Flask, render_template, session, redirect, url_for, jsonify, request
import requests, random
app = Flask(__name__)


@app.route("/user/input", methods = ["POST"])
def user_input():
    amount = request.form.get("amount")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    typeQ = request.form.get("type")

    return amount, category, difficulty, typeQ
   

def getUrl(amount, category, difficulty, typeQ):
    Base_url = 'https://opentdb.com/api.php?amount=' + str(amount)
    final_url = Base_url
   #category
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
    print('f answers ', final_answers)
    print('c list' , correct_list)
    
    return correct_list,final_answers,question_list


@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")


@app.route("/info")
def info():
    return render_template("info.html")

   
@app.route("/quiz")
def quiz(correct_answers, final_answers, question_list):
   
   
    return render_template("quiz.html", question = question_list[0], answer1 = correct_answers[0], answer2 = 'answer 2', answer3 = 'answer 3', answer4 = 'answer 4')
    #return render_template("quiz.html", question = 'does this work?', answer1 = 'answer 1', answer2 = 'answer 2', answer3 = 'answer 3', answer4 = 'answer 4')


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
#     amount, category, difficulty, typeQ = user_input()
# url = getUrl(str(amount), str(category), str(difficulty), str(typeQ))

    url = getUrl(str(2), 'default_c', 'easy', 'multiple')
    Json = getJson(url)
    print(toDict(Json))
#     questions, correct_answers, incorrect_answers = toDict(url)
    