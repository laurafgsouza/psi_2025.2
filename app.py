from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return 'Essa é minha primeira aplicação em Flask!'

@app.route('/contato')
def contato():
  return render_template('contato.html')

@app.route('/exemplo')
def exemplo():
  return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
  return render_template('exemplo2.html')

if __name__ == '__main__':
    app.run()