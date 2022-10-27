from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Date, CHAR, VARCHAR
from Data import Registration, Students, Teacher, Subjects , session



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://webadmin:SALhsy91225@10.104.9.147:5432/testdb'
app.config['SQLALCHEMY_TRACK_MPDIFICATION'] = False


@app.route('/')
def index():
    result = session.query(Students.student_id,Students.f_name,Students.l_name,Registration.sub_id,Subjects.subject_name,Registration.grade,Teacher.tf_name,Teacher.tl_name)\
        .outerjoin(Registration,Students.student_id == Registration.student_id)\
            .outerjoin(Subjects,Registration.sub_id == Subjects.sub_id)\
                .join(Teacher,Subjects.teacher_id == Teacher.teacher_id).all()
    return render_template('index8.html', result=result)



if __name__ == '__main__':
    app.run(host= '0.0.0.0',port= 80,debug=True)
    
