from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h2>Hello world!</h2>'

@app.route('/home')
def home():
    render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
