__author__ = 'salmon-the-wise'
import sqlite3 as sq
# postgresql
import psycopg2 # implements DB API v2.0


with sq.connect("tmp.sqlite") as con:  # открыли соединение с базой данных
    cur = con.cursor()  # получили курсор
    for row in cur.execute(
            "select courses.name, year, sum(score) * 1.0 / count(*) "
            "from participation "
            "inner join students "
            "on student_id = students.id "
            "inner join courses "
            "on course_id = courses.id "
            "group by course_id, year"):  # группировать можно и по паре значений
        print(row)