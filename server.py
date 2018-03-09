from flask import Flask, render_template, request, redirect,session,flash
import re 
# import datetime
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'

@app.route('/')
def landing_page():
	return render_template('index.html')

@app.route('/user', methods=["POST"])
def create_user():
	# print str(request.form['date'])
	# print "Datetime date: " + str(date.today())
	isSubmitted = True
	if(len(request.form['first_name']) == 0 or len(request.form['last_name']) == 0):
		flash(u"Must input a name!",'error')
		isSubmitted = False
	elif(not str(request.form['first_name']).isalpha() or (not str(request.form['last_name']).isalpha())):
		flash("Names can not contain Numbers!",'error')	
		isSubmitted = False
	if(len(request.form['password']) == 0 or (len(request.form['confirm_password']) == 0)):
		flash('Need to create a password!','error')	
		isSubmitted = False
	elif(str(request.form['password']) != (str(request.form['confirm_password']))):
		flash("Error: Passwords must match!",'error')
		isSubmitted = False
	# elif (re.search('/[A-Z]/',request.form['password'])):
	capital_matches = re.search(r'[A-Z]',str(request.form['password']))
	number_matches = re.search(r'[0-9]',str(request.form['password']))
	if(capital_matches == None):
		flash("Error: Password needs to have at least 1 Uppercase letter",'error') 
	if(number_matches == None):
		flash("Error: Password needs to have at least 1 number",'error')
	print "Password = " + str(request.form['password'])
	# print str(capital_matches[0])
	# if(isSubmitted):
	# 	flash("Thanks for submitting your information!",'valid')
				
	return redirect('/')	
	
app.run(debug=True)