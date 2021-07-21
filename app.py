from flask import Flask, render_template, session, redirect, url_for, jsonify, request
import requests, random
app = Flask(__name__)



@app.route("/quiz")
def quiz():
    return render_template("quiz.html")

@app.route("/user/input", methods = ["POST"])
def user_input():
    amount = request.form.get("amount")
    category = request.form.get("category")
    difficulty = request.form.get("difficulty")
    typeQ = request.form.get("type")
    
    url = getUrl(amount, category , difficulty, typeQ)
    Json = getJson(url)
    correct_answers, final_answers, question_list = toDict(Json)
    quiz(correct_answers,final_answers,question_list) 

    return quiz(correct_answers,final_answers,question_list)
   

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
    
    return correct_list, final_answers, question_list


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/quiz")
def quiz_2():
    return render_template("quiz.html")

@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/next/question", methods = ["POST"]) 
def next_question():
    answer = request.form.get("answers")
    print(answer)
    return answer


def quiz(correct_answers,final_answers,question_list):
    #redirect("/quiz")
    didNotPressButton = True  
    if didNotPressButton:
        question_type = next(iter(question_list.values()))
        print(question_type)                     
        print(next(iter(question_list)))                   
        question_name = next(iter(question_list))

        if question_type == 'multiple':
            print('hi')
            #return redirect('/quiz',  question = question_name, answer1 = final_answers[0][0], answer2 = final_answers[0][1], answer3 = final_answers[0][2], answer4 = final_answers[0][3])
            
            return render_template('quiz.html',  question = question_name, answer1 = final_answers[0][0], answer2 = final_answers[0][1], answer3 = final_answers[0][2], answer4 = final_answers[0][3])
              
                            
        elif question_type == 'boolean':
            return render_template("quiz.html", question = question_name, answer1 = 'True', answer2 = 'False')
                            
                          
      #if next button is pressed              

   
#if next button is pressed
    #iterate through dict 
    #grab key nad value for each
    #
   #if value is boolean  
      #question = key (display in question)
      #if T/F two options
         #return two options disable 3 and 4
         
   #elif value is multiple
      #question = key (display in question)
      #2D answers - loop through and set for each answer (nested for loop)
      #
      #loop and display all 4 options
    


    #return render_template("quiz.html", question = question_list[0], answer1 = correct_answers[0], answer2 = 'answer 2', answer3 = 'answer 3', answer4 = 'answer 4')
    #return render_template("quiz.html", question = 'does this work?', answer1 = 'answer 1', answer2 = 'answer 2', answer3 = 'answer 3', answer4 = 'answer 4')


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
#     amount, category, difficulty, typeQ = user_input()
# url = getUrl(str(amount), str(category), str(difficulty), str(typeQ))

      
#    questions, correct_answers, incorrect_answers = toDict(url)
    