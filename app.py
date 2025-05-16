from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def kontakt():
    return render_template('kontakt.html')

@app.route('/meni')
def meni():
    return render_template('meni.html')

if __name__ == '__main__':
    app.run(debug=True)