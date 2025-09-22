from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return 'Essa é minha primeira aplicação em Flask!'

@app.route('/contato')
def contato():
  x = 'maria'
  y = 'maria@gmail.com'
  return render_template('contato.html', nome=x, email=y)

@app.route('/exemplo')
def exemplo():
  return render_template('exemplo.html')

@app.route('/exemplo2')
def exemplo2():
  return render_template('exemplo2.html')

@app.route('/perfil', defaults={'nome': 'fulano'})
@app.route ('/perfil/<nome>')
def perfil(nome):
  return render_template ('perfil.html', nome = nome)

@app.route('/semestre/<x>')
def semestre (x):
  return render_template('semestre.html', x=x)

if __name__ == '__main__':
    app.run()