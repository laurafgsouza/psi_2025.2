from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'hellooo world!'

@app.route('/contato')
def contato():
    return 'gomes.laura@escolar.ifrn.edu.br'

if __name__ == '__main__':
    app.run()