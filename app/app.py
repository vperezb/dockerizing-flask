from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from scripts import sender_presenter as sp
# import os HOME_DIR = os.getenv('HOME_DIR')

import json

def read_json(path):
    with open('strings.json') as f:
        return json.load(f)


app = Flask(__name__)

@app.route('/push_sender')
def sender():
    return render_template('push_sender.html')


@app.route('/send_push_by_token', methods=['POST'])
def send_push_by_token():
    push_engine = sp.__initialize_app(r'app\data\firebase_secrets\PRO.json')
    if not request.form['push_data']:
        push_data = read_json(r'app\data\default_push_data.json')
    else:
        push_data = request.form['push_data']
    response = sp.send_to_token(request.form['fcm_token'], push_data, push_engine, False)
    return (response)

@app.route('/suscribe_token_to_topic', methods=['POST'])
def suscribe_token_to_topic():
    push_engine = sp.__initialize_app(r'app\data\firebase_secrets\PRO.json')
    response = sp.subscribe_to_topic(request.form['topic'], [request.form['fcm_token']], push_engine)
    return (response)


@app.route('/send_push_by_topic', methods=['POST'])
def send_push_by_topic():
    push_engine = sp.__initialize_app(r'app\data\firebase_secrets\PRO.json')
    if not request.form['push_data']:
        push_data = read_json(r'app\data\default_push_data.json')
    else:
        push_data = request.form['push_data']
    response = sp.send_to_topic(request.form['fcm_topic'], push_data, push_engine, False)
    return (response)

app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///C:\\Users\\Orwell\\Documents\\GitProjects\\dockerizing-flask\\sqlite.db'

app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)


class Firmas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    comentario = db.Column(db.String(5000))

@app.route('/firma/', methods=['GET', 'POST'])
def firma():
    if request.method == 'GET':
        return render_template('firma.html')
    else:
        nombre = request.form['nombre']
        comentario = request.form['comentario']

        firma = Firmas(nombre=nombre, comentario=comentario)
        db.session.add(firma)
        db.session.commit()

        return redirect(url_for('landing'))

@app.route('/result_firmas')
def landing():
    result = Firmas.query.order_by(Firmas.id.desc()).all()
    return render_template('index.html', result=result)

@app.route('/base')
def base_html():
    return render_template('base.html')


if __name__ == '__main__':
    app.run(debug=True)
