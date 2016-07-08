from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key='erhguiehrglsidriuwehfwe7887433g47g8'

@app.route('/')
def index():
	try:
		session['counter']+=1
	except KeyError:
		session['counter']=1
	return render_template('index.html', count=session['counter'])

@app.route('/dumb')
def submit():
	session['counter']+=1
	return redirect('/')

@app.route('/clear')
def clear():
	session.clear()
	return redirect('/')

app.run(debug=True)
