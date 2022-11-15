from flask import Flask, render_template, request, flash, redirect, url_for

app =  Flask('__main__')

@app.route('/')
def index():
    return render_template('/index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8089)