from flask import request, render_template
from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


def main():
    app.run()

if __name__ == '__main__':
    main()