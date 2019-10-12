from flask import Flask, request, redirect, render_template
import cgi

#opens app (website)
app = Flask(__name__)
#displays runtime errors in the terminal and browser
app.config['DEBUG'] = True

@app.route("/")
def signup_form():
    return render_template('signup_form.html')

@app.route("/", methods=['POST'])
def validate_signup():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    #username check
    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid username. Must be 3 or more characters."
        username = ""
    elif " " in username:
        username_error = "Invalid username. Username cannot contain any spaces."
        username = ""

    #password check
    if len(password) < 3 or len(password) > 20:
        password_error = "Invalid password. Must be 3 or more characters."
        password = ""
    elif " " in password:
        password_error = "Invalid password. Password cannot contain any spaces."
        password = ""
    
    #verifying password
    if verify != password:
        verify_error = "Passwords do not match."
        password = ""
        verify = ""

    #email check
    if not email == "":
        if len(password) < 3 or len(password) > 20 or " " in email or not email.count("@") == 1 or not email.count(".") == 1:
            email_error = "The email is not in the correct format."

    if not username_error and not password_error and not verify_error and not email_error:
        return redirect ('/confirmation?username={0}'.format(username))
    else:
        return render_template('signup_form.html', username = username, password = password, verify = verify, email = email, username_error = username_error, password_error = password_error, verify_error = verify_error, email_error = email_error)

@app.route("/confirmation")
def confirmation_pg():
    username = request.args.get('username')
    return render_template('confirmation.html', username = username)


app.run()
