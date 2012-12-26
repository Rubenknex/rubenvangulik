import os
from flask import Flask, render_template

DEBUG = True

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def info():
	return render_template('info.html');

@app.route('/cycling/')
def cycling():
	return render_template('cycling.html');

@app.route('/coding/')
def coding():
	return render_template('coding.html');

@app.route('/blog/')
def blog():
	return render_template('blog.html');

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)