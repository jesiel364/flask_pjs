from flask import Flask, render_template, url_for, flash, redirect, request
import requests

app = Flask('__main__')

@app.route('/')
def index():
    advice = requests.get('https://api.adviceslip.com/advice').json()
    for key in advice:
        conselho = advice.get(key)['advice']
        print(conselho)
    return render_template('/home.html', data = conselho)
    
if __name__ == '__main__':
    app.run(debug=True, port=8089)