import sqlite3
import os

db_connection = os.environ['DATABASE']

con = sqlite3.connect(db_connection)

cur = con.cursor()

res = cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
if res.fetchall() != []:
    cur.execute("DROP TABLE jobs")
    print("Data dropped successfully")

cur.execute("""CREATE TABLE jobs (
            id                INTEGER PRIMARY KEY AUTOINCREMENT,
            title             VARCHAR(250)  NOT NULL,
            location          VARCHAR(250)  NOT NULL,
            salary            DECIMAL(10, 2),
            currency          VARCHAR(10),
            responsabilities  VARCHAR(2000),
            requirements      VARCHAR(2000)
            )""")
print("Table created successfully!")

cur.execute(
"""
  INSERT INTO jobs(title, location, salary, currency, responsabilities, requirements) VALUES
            (
              "Data Analyst",
              "Bengaluru, India",
              1000000,
              "Rs.",
              "Process data using Python, SQL and other tools through the analytics data pipeline.
              Identify and translate business rules into specifications and documentation.
              Ensure quality control and follow peer review guidelines.
              Adhere to best practices and standards, maintaining process efficiencies.",
              "Bachelor's degree (required) or above in Computer Science, Mathematics, Economics, or experience in related analytical field.
              Excellent analytic and creative problem-solving skills
              1-3 years Python and SQL programming experience.
              Basic skills in MS Excel.
              Knowledge of cloud computing platforms (AWS, GCP) and knowledge of Spark is desired."
              ),
            (
              "Data Scientist",
              "New Delhi, India",
              1500000,
              "Rs.",
              "Draft detailed scope for assigned projects, addressing suggested methodology and execution framework.
              Execute on the plan with appropriate data mining, analytical and data science techniques.
              Perform quality assurance of data and deliverables for work performed by other Data Scientists, Data Engineers and self.
              Accountable for the quality of the end solution or model by planning the required reviews on code and process.",
              "Expert knowledge in Deep Learning techniques and exploring newer approaches like federated learning and transfer learning.
              Proficient in some or all of the following techniques: Linear & Logistic Regression, Decision Trees, Random Forests, K-Nearest Neighbors, Markov Chain, Monte Carlo, Gibbs Sampling, Evolutionary Algorithms, Support Vector Machines.
              Proficient in advanced data mining and statistical modeling techniques, including Predictive modeling"
              ),
            (
              "Frontend Engineer",
              "Remote",
              150000,
              "R$",
              "Translate designs and wireframes into high quality JS, CSS, HTML templates.
              Design, build, and maintain high performance, reusable, and reliable UI components and products.
              Ensure the best possible performance, quality, and optimize for maximum speed and scalability.
              Identify and correct bottlenecks and fix bugs.
              Help maintain code quality, organization, and automatization.",
              "Strong knowledge of programming skills in JS, CSS and HTML.
              Familiarity with responsive and adaptive web design, and good knowledge of JS libraries such as JQuery.
              Strong knowledge of about atleast one of the JS frameworks (e.g. VueJS, Angular JS, NodeJS, ReactJS).
              Experience with building websites, ability to handle cross browser compatibility issues."
              ),      
            (
              "Backend Engineer",
              "San Francisco, USA",
              120000,
              "$",
              "Design and develop a cloud based backend.
              Participate and produce a scalable cloud based backend system.
              Design and develop REST based APIs.
              Interact with customer directly and with other stakeholders in the organization.",
              "Hands on experience with building a web backend in Java or Golang.
              Knowledge of designing and building REST APIs.
              Proven experience in building a scalable and resilient backend.
              Good understanding of database schemas and using both relational (SQL) and noSQL based data stores.
              Strong analytical and debugging skills."
              )
"""
)
con.commit()
print("Data inserted successfully!")

con.close()