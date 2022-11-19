from flask import Flask, render_template, url_for, flash, redirect, request
import requests

app = Flask('__main__')

@app.route('/')
def index():
    advice = requests.get('https://api.adviceslip.com/advice').json()
    for key in advice:
        conselho = advice.get(key)['advice']
        key_id = advice.get(key)['id']
        print(conselho, key_id)
    return render_template('/home.html', conselho = conselho, key_id = key_id)
    
@app.route('/salvos')
def salvos():
    requisicao = requests.get('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/Motify').json()
    return render_template('/salvos.html', data = requisicao)
    
@app.route('/salvar/<string:advice>', methods=['POST', 'GET'])
def salvar(advice):
    
    requisicao = requests.post('https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/Motify', data=({'advice': advice}))
    print(advice)
    return redirect(url_for('index'))

@app.route('/salvos/remover/<string:key>', methods=['POST', 'GET'])

def deletar(key):

    requisicao = requests.delete(f'https://625e20a26c48e8761ba572c5.mockapi.io/api/v1/Motify/{key}')
    print(key)
    return redirect(url_for('salvos'))

@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template('/login.html')

@app.route('/registrar', methods=['POST', 'GET'])
def registrar():
    if request.method == 'POST':
        
        email = request.form['email']
        pwd = request.form['pwd']
        print(email, pwd)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=8089)