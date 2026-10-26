#FLASK - мінімалістичний фреймворк
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index')

@app.route('/')
def home():
    menu = ['Home', 'About', 'Contacts']
    return render_template('index.html', title='Home', menu=menu)

if __name__ == '__main__':
    app.run(debug=True)