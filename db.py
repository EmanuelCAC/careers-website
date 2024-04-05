import sqlite3
import os

db_connection = os.environ['DATABASE']

def load_jobs_from_db():
    con = sqlite3.connect(db_connection)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM jobs")
    jobs = [dict(row) for row in res.fetchall()]
    con.close()
    return jobs

def load_job_from_db(id):
    con = sqlite3.connect(db_connection)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    res = cur.execute("SELECT * FROM jobs Where id = ?", id)
    job = [dict(row) for row in res.fetchall()]
    if job == []:
        return None
    con.close()
    return job[0]

def add_application_to_db(job_id, data):
    con = sqlite3.connect(db_connection)
    cur = con.cursor()
    cur.execute(
        """
            INSERT INTO applications(job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (job_id, data['full_name'],
              data['email'],
              data['linkedin_url'],
              data['education'],
              data['work_experience'],
              data['resume_url'])
    )
    con.commit()