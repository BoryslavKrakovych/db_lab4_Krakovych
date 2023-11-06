--1. Вивести рівень освіти та кількість студенток, що писали тести на диплом цього рівня 
select level_id, count(distinct(results.student_id)) from student,results
where results.student_id in(select student_id from student where gender='female') group by level_id  

--2. Вивести етнічні групи і кількість студентів та сутденток, які належать до кожної з етнічних груп
select ethnicity, count(student_id) from student group by ethnicity

--3. Вивести id студентів-чоловіків, та їх бали за тест з математики
select student_id, score from results
where test_id = 1 and student_id in(select student_id from student where gender='male')

