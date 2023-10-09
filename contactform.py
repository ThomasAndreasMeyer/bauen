from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    address = request.form.get('address')
    phone = request.form.get('phone')
    email = request.form.get('email')
    message = request.form.get('message')  # Neue Zeile, um die Nachricht zu erhalten
    
    # Hier können Sie die Formulardaten, einschließlich der Nachricht, verarbeiten, speichern oder senden

    return "Vielen Dank für Ihre Nachricht!"

if __name__ == '__main__':
    app.run(debug=True)
