from flask import Flask
from company import submit_assignment
app = Flask(__name__)

@app.route("/")
def hello_world():
    return submit_assignment('Apythonbot1', 'rajat@1999')