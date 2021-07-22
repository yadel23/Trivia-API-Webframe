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
    correct_answer_list = []
    incorrect_answers_list = []
    all_answers = []   
    for value in json_data['results']:
        question_list[value['type']] = value['question']
        correct_answer_list.append(value['correct_answer'])
        incorrect_answers_list.append(value['incorrect_answers'])
        for i in range(len(incorrect_answers_list)):
            all_answers = correct_answer_list[i] + incorrect_answers_list[i]
            random.shuffle(all_answers)
      
    
    print(all_answers)
    return question_list, correct_answer_list, incorrect_answers_list
   



@app.route("/")
@app.route('/home')
def home():
    return render_template("home.html")


@app.route("/info")
def info():
    return render_template("info.html")

   
@app.route("/quiz")
def quiz(question_list, correct_answers, incorrect_answers):
    return render_template("quiz.html", question = question_list[0], answer1 = correct_answers[0], answer2 = 'answer 2', answer3 = 'answer 3', answer4 = 'answer 4')
    #return render_template("quiz.html", question = 'does this work?', answer1 = 'answer 1', answer2 = 'answer 2', answer3 = 'answer 3', answer4 = 'answer 4')

#https://opentdb.com/api.php?amount=2&category=18&difficulty=easy&type=multiple

if __name__ == '__main__':
    #app.run(debug = True, host = '0.0.0.0')
#     amount, category, difficulty, typeQ = user_input()
# url = getUrl(str(amount), str(category), str(difficulty), str(typeQ))

     url = getUrl(str(2), 'default_c', 'easy', 'multiple')
#     print(url)
     print(toDict(url))
#     questions, correct_answers, incorrect_answers = toDict(url)
    
      