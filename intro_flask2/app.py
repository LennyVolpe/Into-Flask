from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/even', methods=['GET'])
def even():
    num = request.form.get('num')
    if num is None:
        return "No query parameter was included"
    try:
        num = int(num)
    except ValueError:
        even = str(num) + " is an not number."
        return render_template('even.html', even=even)
    if num % 2 == 0:
        even = str(num) + " is an even number."
    else:
        even = str(num) + " is an odd number."
    return render_template('even.html', even=even)


if __name__ == '__main__':
    app.run(debug=True)
