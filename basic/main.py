from flask import Flask, render_template, request, url_for, redirect, flash

app = Flask(__name__)

@app.route('/')
def index():
    flash('Aceitar Cookies?', 'info')
    return render_template('/home.html')


if __name__ == "__main__":
    app.secret_key = '12345'
    app.run(debug=True, port=8089)

