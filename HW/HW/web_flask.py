from flask import Flask, render_template

app = Flask(__name__) 
@app.route('/')

#display file
def index():
    return render_template('web_flask.html')

#set ip
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)