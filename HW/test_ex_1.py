import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import CHAR, VARCHAR, Column, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('sqlite:///test_02.sqlite3')
Base = declarative_base()

class Registration_table(Base):
    __tablename__ = "Registration"
    student_id = Column(CHAR(13),ForeignKey('Students.student_id'), nullable=False)
    subject_id = Column(VARCHAR(15), ForeignKey('Subject.subject_id'), nullable=False)
    year = Column(CHAR(4), nullable=False)
    semester = Column(CHAR(1), nullable=False)
    grade = Column(CHAR(2), primary_key=True)
    

class Subject_table(Base):
    __tablename__ = "Subject"
    subject_id = Column(VARCHAR(15), primary_key=True, nullable=False)
    subject_name = Column(VARCHAR(50), nullable=False)
    cradit = Column(Integer, nullable=False)
    teacher_id = Column(CHAR(3))

class Students_table(Base):
    __tablename__ = 'Students'
    student_id = Column(CHAR(13),primary_key=True, nullable=False)
    f_name = Column(VARCHAR(30), nullable=False)
    l_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50),nullable=False)


class Teachers_table(Base):
    __tablename__ = "Teachers"
    teacher_id = Column(CHAR(3), primary_key=True, nullable=False)
    f_name = Column(VARCHAR(30), nullable=False)
    l_name = Column(VARCHAR(30), nullable=False)
    e_mail = Column(VARCHAR(50),nullable=False)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

Students_all_1 = Students_table(student_id="6406022620031", f_name="Chalongrath", l_name="Kodlord", e_mail="s6406022620031@email.kmutnb.ac.th")
Students_all_2 = Students_table(student_id="6406022620037", f_name="Bunnapon", l_name="Takumwan", e_mail="s6406022620037@email.kmutnb.ac.th")
Students_all_3 = Students_table(student_id="6406022620011", f_name="Jakapat", l_name="Jodduangchan", e_mail="s6406022620011@email.kmutnb.ac.th")

Teachers_table_1 = Teachers_table(teacher_id="AMK",f_name="Anirach", l_name="Mingkhwan", e_mail="Anirach@email.kmutnb.ac.th")
Teachers_table_2 = Teachers_table(teacher_id="WKN",f_name="Watcherachai", l_name="Kongsiriwattana", e_mail="Watcherachai@email.kmutnb.ac.th")
Teachers_table_3 = Teachers_table(teacher_id="STS",f_name="Sarayoot", l_name="Tanessakulwattana", e_mail="Sarayoot@email.kmutnb.ac.th")

Subject_table_1 = Subject_table(subject_id="060233112", subject_name="DATA ENGINEERING", cradit="3", teacher_id="STS")
Subject_table_2 = Subject_table(subject_id="060233113", subject_name="ADVANCED COMPUTER PROGRAMMIN", cradit="3", teacher_id="AMK")
Subject_table_3 = Subject_table(subject_id="060233133", subject_name="ADVANCED NETWORK AND PROTOCO", cradit="3", teacher_id="ANM")

Registration_table_1 = Registration_table(student_id="6406022620031", subject_id="060233112", year="2565", semester="2", grade="A+")
Registration_table_2 = Registration_table(student_id="6406022620038", subject_id="060233113", year="2565", semester="2", grade="A")
Registration_table_3 = Registration_table(student_id="6406022620037", subject_id="060233133", year="2565", semester="2", grade="B+",)

Registration_table_4 = Registration_table(student_id="6406022620037", subject_id="060233112", year="2565", semester="2", grade="B")
Registration_table_5 = Registration_table(student_id="6406022620037", subject_id="060233113", year="2565", semester="2", grade="C+")
Registration_table_6 = Registration_table(student_id="6406022620037", subject_id="060233133", year="2565", semester="2", grade="C")

Registration_table_7 = Registration_table(student_id="6406022620011", subject_id="060233112", year="2565", semester="2", grade="D+")
Registration_table_8 = Registration_table(student_id="6406022620011", subject_id="060233113", year="2565", semester="2", grade="D")
Registration_table_9 = Registration_table(student_id="6406022620011", subject_id="060233133", year="2565", semester="2", grade="F")

session.add(Students_all_1)
session.add(Students_all_2)
session.add(Students_all_3)

session.add(Teachers_table_1)
session.add(Teachers_table_2)
session.add(Teachers_table_3)

session.add(Subject_table_1)
session.add(Subject_table_2)
session.add(Subject_table_3)

session.add(Registration_table_1)
session.add(Registration_table_2)
session.add(Registration_table_3)
session.add(Registration_table_4)
session.add(Registration_table_5)
session.add(Registration_table_6)
session.add(Registration_table_7)
session.add(Registration_table_8)
session.add(Registration_table_9)

session.commit()