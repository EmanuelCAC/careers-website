from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        "id": 1,
        "title": "Data Analyst",
        "location": "Bengaluru, India",
        "salary": "R$ 10,000.00"
    },
    {
        "id": 2,
        "title": "Data Scientist",
        "location": "Delhi, India",
        "salary": "R$ 15,000.00"
    },
    {
        "id": 3,
        "title": "Frontend Engineer",
        "location": "Remote",
        "salary": "R$ 12,000.00"
    },
    {
        "id": 4,
        "title": "Backend Engineer",
        "location": "San Francisco, USA",
    },
]

@app.route("/")
def hello_world():
    return render_template('home.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)