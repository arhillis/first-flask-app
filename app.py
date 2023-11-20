from flask import Flask, render_template
from flask_cors import CORS


app = Flask(__name__)
CORS(app)



STUDENTS = [{
    'first_name': 'Emma',
    'last_name': 'Woodhouse',
    'grades': {
        'MATH 101': 80,
        'ENGL 101': 75,
        'SCI 101': None,
        'SOC_ST 101': 85
    }
}, {
    'first_name': 'Elizabeth',
    'last_name': 'Bennett',
    'grades': {
        'MATH 201': 88,
        'ENGL 201': 95,
        'SCI 201': None,
        'SOC_ST 201': 90
    }
}, {
    'first_name': 'Elinor',
    'last_name': 'Dashwood',
    'grades': {
        'MATH 301': 96,
        'ENGL 301': 88,
        'SCI 301': None,
        'SOC_ST 301': 87
    }
}]


@app.route("/")
def hello_world():
  return render_template("index.html", students=STUDENTS)

@app.route("/students")
def get_students():
    return STUDENTS

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
