from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "najnaj_pozarevac"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'dusan.ristic.car@gmail.com'
app.config['MAIL_PASSWORD'] = 'najnaj_pozarevac'
app.config['MAIL_DEFAULT_SENDER'] = 'dusan.ristic.car@gmail.com'

mail =Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def kontakt():
    return render_template('kontakt.html')

@app.route('/meni')
def meni():
    return render_template('meni.html')

@app.route('/send-message', methods = ['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    if not name or not email or not message:
        flash("Molimo popunite sva polja!", "error")
        return redirect(url_for('kontakt'))
    
    try:
        msg = Message(subject=f"Poruka od {name}",
                      sender=email,
                      recipients=["dusan.ristic.car@gmail.com"])
        msg.body = f"Od: {name} <{email}> \n\n Poruka:\n{message}"
        mail.send(msg)
        flash("Poruka je poslata!", "success")
    except Exception as e: 
        print("Greška pri slanju maila", e)
        flash("Greška pri slanju poruka", "error")

    return redirect(url_for('kontakt'))


if __name__ == '__main__':
    app.run(debug=True)