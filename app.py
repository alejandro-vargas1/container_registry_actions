from flask import Flask

app = Flask(__name__)
# New comment
@app.route("/")
def hello_world():
    return "Hello world"

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8080)
