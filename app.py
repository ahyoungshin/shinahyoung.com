from flask import Flask
from flask import render_template

app=Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

if __name__=='__main__':
    import os
    app.run('0.0.0.0', port=os.environ.get('PORT', 5000))