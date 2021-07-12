from flask import Flask
app = Flask(__name__)


@app.route('/name/<name>')  # 1.name is url 2. name is variable
def show_name(name):
    return 'Hello {}'.format(name)


@app.route('/id/<int:id>')
def show_int(id):
    return 'Your Id is : {}'.format(id)


@app.route('/balance/<float:balance>')
def show_float(balance):
    return 'Your Balance is : {}'.format(balance)


if __name__ == '__main__':
    app.run(debug=True)
