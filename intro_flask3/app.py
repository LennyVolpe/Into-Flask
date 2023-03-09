from flask import Flask, render_template, request

app = Flask(__name__)


events = ['Charlotte Hackathon', 'Football Tryouts',
          'Biology Research', 'Code9', 'Job Fair']
students = {}


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        event = request.form['event']
        if not name:
            error = 'Input Your Name'
        elif not events:
            error = 'Select An Events'
        else:
            students[name] = event
            return render_template('users.html', students=students)

        return render_template('home.html', events=events, error=error)

    return render_template('home.html', events=events)


@app.route('/users')
def users():
    return render_template('users.html', students=students)


if __name__ == '__main__':
    app.run(debug=True)
