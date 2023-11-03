import psycopg2
import matplotlib.pyplot as plt

username = 'Krakovych_Boryslav'
password = '111'
database = 'labs3-6'
host = 'localhost'
port = '5432'

query_1 = '''
select level_id, count(distinct(results.student_id)) from student,results
where results.student_id in(select student_id from student where gender='female') group by level_id  
'''

query_2 = '''
select ethnicity, count(student_id) from student group by ethnicity
'''

query_3 = '''
select student_id, score from results
where test_id = '1' and student_id in(select student_id from student where gender='male')
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:

    cur = conn.cursor()

    cur.execute(query_1)
    print("Query 1")
    for row in cur:
        print(row)
    print("\n")

    cur.execute(query_2)
    print("Query 2")
    for row in cur:
        print(row)
    print("\n")

       
    cur.execute(query_3)
    print("Query 3")
    for row in cur:
        print(row)
    print("\n")


