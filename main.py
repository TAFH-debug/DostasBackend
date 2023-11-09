from flask import Flask
import json


app = Flask(__name__)

@app.route("/")
def hello_world():
    return json.dumps({"username": "Talim", "email": "aushahman2007@gmail.com"})

if __name__ == "__main__":
    app.run(debug=True)