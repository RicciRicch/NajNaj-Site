# NajNaj Site

NajNaj je web aplikacija za restoran sa modernim dizajnom koristeći Flask i Tailwind CSS.

## 🚀 Tehnologije

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **CSS Framework**: Tailwind CSS v3
- **Email**: Flask-Mail

## 📁 Struktura projekta

```
NajNaj-Site/
├── app.py                 # Flask aplikacija
├── templates/             # HTML template-ovi
│   ├── base.html
│   ├── home.html
│   ├── kontakt.html
│   └── meni.html
├── static/                # Static fajlovi
│   ├── css/
│   │   ├── input.css      # Tailwind input
│   │   └── output.css     # Build-ovan CSS
│   ├── js/
│   ├── image/
│   └── video/
├── package.json           # Node.js zavisnosti
├── tailwind.config.js     # Tailwind konfiguracija
└── README.md
```

## 🛠️ Instalacija

### 1. Kloniranje repozitorijuma
```bash
git clone https://github.com/your-username/najnajPromene.git
cd najnajPromene
```

### 2. Instaliranje Node.js zavisnosti
```bash
npm install
```

### 3. Instaliranje Python zavisnosti
```bash
pip install flask flask-mail
```

## 🚀 Pokretanje

### Development
```bash
# Build Tailwind CSS u watch modu
npm run dev

# U drugom terminalu, pokreni Flask aplikaciju
python app.py
```

### Produkcija
```bash
# Build Tailwind CSS
npm run build

# Pokreni Flask aplikaciju
python app.py
```

## 🌐 Pristup aplikaciji

Aplikacija je dostupna na: `http://localhost:5000`

## 📧 Kontakt forma

Aplikacija uključuje funkcionalnu kontakt formu koja šalje email-ove kroz Flask-Mail.

## 🎨 Tailwind CSS

Projekat koristi Tailwind CSS v3 sa custom konfiguracijom:
- Custom boje: `rose` (#F7B3C9), `blue` (#7FCECD)
- Custom fontovi: Kreon, Pacifico
- Server-side build proces

## 📝 Licenca

Ovaj projekat je privatni i pripada NajNaj restoranu. 