from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# import os HOME_DIR = os.getenv('HOME_DIR')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///C:\\Users\\Orwell\\Documents\\GitProjects\\dockerizing-flask\\sqlite.db'

app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)


class Firmas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(30))
    comentario = db.Column(db.String(5000))


@app.route('/')
def landing():
    result = Firmas.query.order_by(Firmas.id.desc()).all()
    return render_template('index.html', result=result)


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

        return redirect(url_for('landing    '))


if __name__ == '__main__':
    app.run(debug=True)
