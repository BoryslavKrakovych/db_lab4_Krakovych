--1. Вивести рівень освіти та кількість студенток, що писали тести на диплом цього рівня 
select level_id, count(distinct(results.student_id)) from student,results
where results.student_id in(select student_id from student where gender='female') group by level_id  

--2. Вивести кількість студентів-чоловіків, які написали тест з математики на певний бал
select count(student_id), score from results
where test_id = '1' and student_id in(select student_id from student where gender='male') group by score

--3. Вивести етнічні групи і кількість студентів та сутденток, які належать до кожної з етнічних груп
select ethnicity, count(student_id) from student group by ethnicity



