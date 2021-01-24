# -*- coding: utf-8 -*-

import psycopg2
import psycopg2.extensions
from remote_jobs import jobs

psycopg2.extensions.register_type(psycopg2.extensions.UNICODE)
psycopg2.extensions.register_type(psycopg2.extensions.UNICODEARRAY)


connection = psycopg2.connect(
    database="remote_jobs",
    user="postgres",
    password="z9djxxz0",
    host="127.0.0.1",
    port="5432"
)

cur = connection.cursor()

job_title_ = jobs.position
city_ = jobs.city
salary_ = jobs.salary
skills_ = jobs.skills
offers_ = jobs.offers
responsibilities_ = jobs.responsibilities
project_info_ = 'None'
link_ = jobs.url

cur.execute(
    '''
    INSERT INTO data(job_title, city, salary, skills, offers, responsibilities, project_info, link) 
    VALUES('%s', '%s','%s', '%s','%s', '%s','%s', '%s');
    ''' % (job_title_, city_, salary_, skills_, offers_, responsibilities_, project_info_, link_)
)

select_print = 'SELECT * FROM data'
cur.execute(select_print)

records = cur.fetchall()
for row in records:
    print(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7])
    print()


connection.commit()

connection.close()
