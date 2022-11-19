from flask import Flask, render_template, url_for, flash, redirect, request
import requests
import sqlite3



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

        #Register
        name = request.form['nick']
        newEmail = request.form['newEmail']
        newPwd = request.form['newPwd']
        newPwd2 = request.form['newPwd2']
        dados = name, newEmail, newPwd

        try:
            if newPwd == newPwd2:
                conn = sqlite3.connect('users.db')
                cursor = conn.cursor()
                cursor.execute('''
                INSERT INTO users (nome, email, senha)
                VALUES (?,?,?)
                ''',dados)
                conn.commit()
                flash(f'Sua conta foi criada com sucesso!', 'success')
            else:
                flash('As senhas não são iguais!', 'danger')
        except:
            flash('Não foi possivel completar o cadastro', 'danger')
                

            
        return redirect(url_for('login'))




        
    

@app.route('/entrar', methods=['POST', 'GET'])
def entrar():
    if request.method == 'POST':
        
        #Login
        email = request.form['email']
        pwd = request.form['pwd']
        dados = email, pwd
        print(dados)

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT senha FROM users where email=?', (email,))
        # flash('Usuário logado', 'success')
        # senha = str(cursor.fetchone(3))
        
        if cursor.fetchone()[0] == pwd:
        # else:
            flash('logado', 'light')
        else:
            flash('Não encontrado', 'light')



        # except:
        #     flash('Usuário não encontrado', 'danger')
        #     return redirect(url_for('login'))


    return redirect(url_for('index'))


if __name__ == '__main__':
    app.secret_key='12345'
    app.run(debug=True, port=8089)