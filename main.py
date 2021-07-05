from flask import Flask, render_template, request, redirect
from helpers import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

app.config.from_object("config")

@app.route("/", methods=["POST"])
def upload_file():
    files = request.files.getlist("user_file")
    print(files)
    print(S3_BUCKET)
    output = ""
    for file in files:
        output += str(upload_file_to_s3(file, app.config["S3_BUCKET"]))
    return output


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)

