/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/js/**/*.js",
    "./app.py"
  ],
  theme: {
    extend: {
      fontFamily: {
        'primary': ['Kreon', 'serif'],
        'secondary': ['Pacifico', 'cursive'],
      },
      colors: {
        'rose': '#F7B3C9',
        'blue': '#7FCECD',
      }
    },
  },
  plugins: [],
} 