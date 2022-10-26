import sqlite3 
from flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    c = sqlite3.connect('HW1.sqlite3')
    cur = c.cursor()
    # cur.execute("SELECT Students.student_id , Students.f_name ,Students.l_name , Subjects.sub_id FROM Students, Subjects")
    cur.execute("SELECT Students.student_id , Students.f_name ,Students.l_name\
        , Subjects.sub_id , Subjects.subject_name\
        ,Registration.grade , Teachers.f_name , Teachers.l_name from Students\
        JOIN Registration\
            on Students.student_id = Registration.student_id\
        JOIN Subjects\
            on Registration.sub_id = Subjects.sub_id\
        JOIN Teachers\
            on Subjects.teacher_id = Teachers.teacher_id\
        ;")
    test = cur.fetchall()
    return render_template("index.html", test=test)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)