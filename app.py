import os
import sys
from flask import Flask, render_template
from flask_frozen import Freezer

DEBUG = True

app = Flask(__name__)
freezer = Freezer(app)

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
	if len(sys.argv) > 1 and sys.argv[1] == 'build':
		freezer.freeze()
	else:
		port = int(os.environ.get('PORT', 5000))
		app.run(host='0.0.0.0', port=port)