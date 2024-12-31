from flask import Flask, render_template
import json

app = Flask(__name__)

with open("aws_questions.json", "r") as file_aws_questions:
    aws_questions = json.load(file_aws_questions)

with open("networking_questions.json", "r") as file_networking_questions:
    networking_questions = json.load(file_networking_questions)

with open("interview_questions.json", "r") as file_interview_questions:
    interview_questions = json.load(file_interview_questions)

with open("misc.json", "r") as file_misc_questions:
    misc_questions = json.load(file_misc_questions)    

notecards = {
    "aws_questions": aws_questions,
    "networking_questions": networking_questions,
    "interview_questions": interview_questions,
    "misc_questions": misc_questions
}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notecards/<category>')
def show_notecards(category):
    cards = notecards.get(category, [])
    return render_template('notecards.html', notecards=cards, category=category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
