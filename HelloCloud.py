from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello RUK-COM is Great! </h1>'

@app.route('/home', methods=['GET', 'POST'])
def home():
    links = ['https://ruk-com.in.th',
            'https://www.google.com',
            'https://www.python.org',
            'https://www.kmutnb.ac.th']
    return render_template('example.html', links=links)

if __name__ == '__main__':
    app.debug = True

    app.run(host='0.0.0.0', port=80)