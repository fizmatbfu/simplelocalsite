from flask import Flask
from createhtml import create
app = Flask(__name__)

@app.route("/")
def createMainPage():
    return create("")

@app.route('/<path:subpath>')
def createSubPage(subpath):
    return create(subpath)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)