from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import sqlite3
import os

app = Flask(__name__)
app.secret_key = "najnaj_pozarevac"

DATABASE = 'dataBase/app.db'

def init_db():
    db = sqlite3.connect(DATABASE)
    stmt = db.cursor()
    stmt.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            message TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()
    db.close()

def save_message(name, email, message):
    db = sqlite3.connect(DATABASE)
    stmt = db.cursor()
    stmt.execute('''
        INSERT INTO messages (name, email, message)
        VALUES (?, ?, ?)
    ''', (name, email, message))
    db.commit()
    db.close()

def get_all_messages():
    db = sqlite3.connect(DATABASE)
    stmt = db.cursor()
    stmt.execute('SELECT * FROM messages ORDER BY created_at DESC')
    messages = stmt.fetchall()
    db.close()
    return messages

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'zulbrad23@gmail.com'
app.config['MAIL_PASSWORD'] = 'mzrxllrrihbtrwyj'
app.config['MAIL_DEFAULT_SENDER'] = 'zulbrad23@gmail.com'

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
        save_message(name, email, message)
        msg = Message(subject=f"Poruka od {name}",
                      sender=email,
                      recipients=['zulbrad23@gmail.com'])
        msg.body = f"Od: {name} <{email}> \n\n Poruka:\n{message}"
        mail.send(msg)
        flash("Poruka je poslata i sačuvana!", "success")
    except Exception as e: 
        print("Greška pri slanju maila", e)
        flash("Greška pri slanju poruka", "error")

    return redirect(url_for('kontakt'))

@app.route('/admin/messages')
def admin_messages():
    messages = get_all_messages()
    return render_template('admin_messages.html', messages=messages)

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)