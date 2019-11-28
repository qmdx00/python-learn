from flask import Flask, render_template

"""
flask tutorial example
"""
app = Flask(__name__)


@app.route('/')
def hello():
    fruits = ['orange', 'apple', 'banana']
    return render_template('index.html', title='Home', fruits=fruits)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
