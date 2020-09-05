from flask import Flask, redirect

import random, json, csv

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

"""

TASK 

Implement an endpoint `/api/fetch` that returns the contents of `data.csv` as JSON

1) Load/transcribe `data.csv`
2) Save each entry's full name, time zone, and department
3) Return the JSON data at the endpoint

"""

# your work here

# opens the csv file from files, can be modified to take in outside csv's
with open ("data.csv", "r") as f:

    reader = csv.reader(f)

    #clearing the first label line
    next(reader)

    #dictionary to store the csv values
    data = {"employees" : []}

    #interates through the CSV and places them in a dictionary
    for row in reader:

        #doesn't need Id, and combines first and last name
        data["employees"].append({
            "name": (row[1] + " " + row[2]),
            "timezone": row[3],
            "dept": row[4]})

@app.route('/api/fetch')
def index():
    # automatically converts the data dictonary to JSON in python 3
    return data



"""

DOCUMENTATION WEBPAGE BELOW

"""


@app.route("/")
def redirect_to_api():
    return redirect("/api", code=301)

@app.route("/api")
def api_home():
    return """
        <style>
            body {
                font-family: sans-serif;
                max-width: 900px;
                width: 90%;
                margin: 0 auto 0 auto;
                padding: 5vh 30px 0 30px;
                background: rgb(240,240,240);
            }
            pre, code {
                background: #121212;
                color: white;
            }
            code {
                padding: 4px;
            }
            pre code {
                padding: 0;
            }
            pre {
                padding: 10px;
            }
            hr {
                margin: 2em 0;
            }
        </style>
        <h1>Founders Fall 2020 Backend Take-Home API</h1>
        <p>Add the endpoint <code>`/api/fetch`</code> accessible via a GET request which returns the list of employees from <code>`data.csv`</code> as JSON.</p><hr />
        <h2>API (to be implemented)</h2>
        <h4>Request</h4>
<pre><code><b>GET</b>
Scheme: http
Filename: /api/fetch</code></pre>
        <h4>Response</h4>
<pre><code>employees: [
            <br />  {
            <br />      name: <i>FULL NAME OF EMPLOYEE</i>,
            <br />      timezone: <i>TIMEZONE</i>,
            <br />      dept: <i>EMPLOYEE'S DEPARTMENT</i>,
            <br />  }
            <br />  ...
        <br />]</code></pre>"""

