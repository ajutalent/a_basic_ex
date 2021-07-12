from flask import Flask, render_template


app = Flask(__name__)


@app.route("/aju")
def aju():
    return render_template('aju.html')


if __name__ == '__main__':
    app.run()
