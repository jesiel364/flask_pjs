from flask import Flask, render_template, url_for, flash, redirect, request

app = Flask('__main__')

@app.route('/')
def index():
    return render_template('/home.html')
    
if __name__ == '__main__':
    app.run(debug=True, port=8089)