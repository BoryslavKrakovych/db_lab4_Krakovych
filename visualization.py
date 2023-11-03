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
    #стовпчикова діаграма
    cur.execute(query_1)
    level_id= []
    count_of_female_students = []


    for row in cur:
        level_id.append(row[0])
        count_of_female_students.append(row[1])

    x_range = range(len(level_id))
 
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    bar = bar_ax.bar(x_range, count_of_female_students, label='count')
    bar_ax.bar_label(bar, label_type='center') 
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(level_id)
    bar_ax.set_xlabel('Рівень освіти')
    bar_ax.set_ylabel('Кількість студенток')
    bar_ax.set_title('Кількість студенток, що писали певний рівень освіти')

    #кругова діаграма 
    cur.execute(query_2)
    ethnicity = []
    count_of_students = []
    for row in cur:
        ethnicity.append(row[0])
        count_of_students.append(row[1])

    pie_ax.pie(count_of_students, labels=ethnicity, autopct='%1.1f%%')
    pie_ax.set_title('Частка етнічних груп у студентів та студенток')

    #точковий графік залежності
    cur.execute(query_3)
    male_student_id = []
    result = []
    for row in cur:
        male_student_id.append(row[0])
        result.append(row[1])


    graph_ax.plot(male_student_id, result, marker='o')
    graph_ax.set_xlabel('ID рівня освіти')
    graph_ax.set_ylabel('Кількість студентів-чоловіків')
    graph_ax.set_title('Графік залежності студента та оцінки за написаний ним тест з математики')

    for qnt, price in zip(male_student_id, result):
        graph_ax.annotate(price, xy=(qnt, price), xytext=(7, 2), textcoords='offset points')


mng = plt.get_current_fig_manager()
mng.resize(2000, 800)

plt.show()
plt.savefig('lab4.png')