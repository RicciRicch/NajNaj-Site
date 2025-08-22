from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import sqlite3
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY", "najnaj_pozarevac")

# Putanja do baze iz okruženja (env), podrazumevano na messages.db u root-u
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.getenv("DB_PATH", os.path.join(BASE_DIR, "app.db"))

def init_db():
    try:
        # Ako je putanja u poddirektorijumu, obezbedi da postoji direktorijum
        db_dir = os.path.dirname(DATABASE)
        if db_dir:
            os.makedirs(db_dir, exist_ok=True)
        print(f"Kreiram/proveravam bazu: {DATABASE}")
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        
        # Kreiraj tabelu ako ne postoji
        cursor.execute('''
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
        print(f"Baza spremna: {DATABASE}")
        
    except Exception as e:
        print(f"GREŠKA pri inicijalizaciji baze: {e}")

def save_message(name, email, message):
    try:
        print(f"Pokušavam da sačuvam poruku od: {name} ({email}) u {DATABASE}")
        
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        
        # Ubaci poruku
        cursor.execute('''
            INSERT INTO messages (name, email, message)
            VALUES (?, ?, ?)
        ''', (name, email, message))
        
        db.commit()
        db.close()
        
        print("Poruka uspešno sačuvana u bazu!")
        return True
        
    except Exception as e:
        print(f"GREŠKA pri čuvanju poruke: {e}")
        return False

def get_all_messages():
    try:
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute('SELECT * FROM messages ORDER BY created_at DESC')
        messages = cursor.fetchall()
        db.close()
        print(f"Učitano {len(messages)} poruka iz baze")
        return messages
    
    except Exception as e:
        print(f"GREŠKA pri čitanju poruka: {e}")
        return []

# Mail konfiguracija iz okruženja
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT', '587'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS', 'true').lower() in ('1','true','yes')
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME', 'zulbrad23@gmail.com')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD', 'mzrxllrrihbtrwyj')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER', 'zulbrad23@gmail.com')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

mail = Mail(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contact')
def kontakt():
    return render_template('kontakt.html')

@app.route('/meni')
def meni():
    return render_template('meni.html')

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    print(f"Primljena poruka od: {name} ({email})")
    print(f"Sadržaj: {message[:50]}...")

    if not name or not email or not message:
        flash("Molimo popunite sva polja!", "error")
        return redirect(url_for('kontakt'))
    
    # Prvo sačuvaj u bazu
    if save_message(name, email, message):
        try:
            # Zatim pošalji mail
            msg = Message(subject=f"Poruka od {name}",
                          sender=email,
                          recipients=[os.getenv('MAIL_TO', 'zulbrad23@gmail.com')])
            msg.body = f"Od: {name} <{email}> \n\n Poruka:\n{message}"
            mail.send(msg)
            flash("Poruka je poslata i sačuvana!", "success")
            print("Mail uspešno poslat")
        except Exception as e: 
            print(f"Greška pri slanju maila: {e}")
            flash("Poruka je sačuvana, ali došlo je do greške pri slanju email-a", "warning")
    else:
        flash("Greška pri čuvanju poruke u bazu", "error")
        print("Poruka NIJE sačuvana u bazu!")

    return redirect(url_for('kontakt'))

@app.route('/admin/messages')
def admin_messages():
    print(f"Admin panel - tražim poruke u bazi: {DATABASE}")
    messages = get_all_messages()
    print(f"Admin panel - pronađeno {len(messages)} poruka")
    return render_template('admin_messages.html', messages=messages)

if __name__ == '__main__':
    print("=== POKRETANJE APLIKACIJE ===")
    init_db()
    print("=== APLIKACIJA POKRENUTA ===")
    app.run(debug=True, host='0.0.0.0', port=5000)