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
    return render_template('/salvos.html')
    
@app.route('/salvar/<string:key>')
def salvar(key):
    print(key)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True, port=8089)