from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def todo_form():
    return render_template('todo_form.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)

