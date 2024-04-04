import sqlite3

con = sqlite3.connect("database.sqlite")

cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
if res.fetchall() != []:
    cur.execute("DROP TABLE jobs")
    print("Data dropped successfully")

cur.execute("CREATE TABLE jobs (title TEXT, location TEXT, salary FLOAT)")
print("Table created successfully!")

cur.execute(
"""
  INSERT INTO jobs(title, location, salary) VALUES
            ("Data Analyst", "Bengaluru, India", 10000),
            ("Data Scientist", "Delhi, India", 15000),
            ("Frontend Engineer", "Remote", 12000),      
            ("Backend Engineer", "San Francisco, USA", null)
"""
)
con.commit()
print("Data inserted successfully!")

con.close()