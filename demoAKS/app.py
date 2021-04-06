import random
from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')


@app.route("/hello", methods=['POST'])
def hello():
	nome = str(request.form['nome'])
		
	return render_template("hello.html", nome=((str(nome))))
	

@app.route("/")
def main():
	return render_template('index.html')


if __name__ == "__main__":
	app.run()


