SELECT Students.student_id, Students.f_name, Students.l_name, Subject.subject_id, Subject.subject_name, Registration.grade, Teachers.f_name, Teachers.l_name FROM Students
join Registration
on Registration.student_id = Students.student_id
JOIN Subject
on Registration.subject_id = Subject.subject_id
JOIN Teachers
on Subject.teacher_id = Teachers.teacher_id