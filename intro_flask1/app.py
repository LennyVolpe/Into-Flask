from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():

    date = datetime.now()

    time = words = "The current date time is " + \
        date.strftime('%A, %B %d %Y %H:%M:%S')
    return render_template('home.html', time=time)


if __name__ == "__main__":
    app.run(debug=True)
