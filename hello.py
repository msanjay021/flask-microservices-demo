from flask import Flask, request

app = Flask(__name__)


@app.route("/user/<username>")
def hello_world(username):
    return ("*".join(f"{username*50}"))


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files[r'C:\Users\User\Downloads\important.txt']
        f.save('D:/Ashu/programming/BE/Python/Flask/flaskHW/uploads/uploaded_file.txt')
    return "success"