#BLOGZ
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://blogz:blogz@localhost:8889/blogz'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y448kGcys&zP4C'


#errors for blog
def title_error(blog_title):
    if len(blog_title) > 0:
        return False
    else:
        return True

def body_error(blog_body):
    if len(blog_body) > 0:
        return False
    else:
        return True

# def password_validate(password):
#     #true means there's an error, false means there isn't an error
#     space = False
#     for char in password:
#         if char.isspace() == True:
#             space = True
#     if 2 < len(password) < 20 and space == False:
#         return False
#     else:
#         return True

class Blog(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('user_id'))

    def __init__(self, title, body, user_id):
        self.title = title
        self.body = body
        self.user = user_id


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db. Column(db.String(120), unique=True)
    password = db.Column(db.String(120))

    def __init__(self, username, password):
        self.username = username
        self.password = password


#require login or register before being able to see posts
@app.before_request
def require_login():
    allowed_routes = ['login', 'register', 'index']
    if request.endpoint not in allowed_routes and 'username' not in session:
        return redirect('/login')

#page with list of all usernames
@app.route('/index', methods=['POST', 'GET'])
def index():
    users = User.query.all()
    return render_template('index.html', users=users)


@app.route('/login', methods=['POST', 'GET'])
#login requirements
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and password:
            #"remember" that the user has logged in
            session['username'] = username
            flash("Logged in")
            return redirect('/newpost')
        else:
            #explain why login failed
            flash('User password incorrect, or user does not exist', 'error')

    return render_template('login.html')


@app.route('/register', methods=['POST', 'GET'])
#register requirements
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']

        username_error = ""
        password_error = ""
        verify_error = ""
        existing_user = User.query.filter_by(username=username).first()

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

        #if no errors, check that its not an existing user
        if not username_error and not password_error and not verify_error and not existing_user:
            #if it's not an existing user, save them to the database
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
            #"remember" the user
            session['username'] = username
            return redirect('/newpost')
            
        else:
            #curly braces in html form = new variable above
            return render_template('register.html', username = username, username_error = username_error, password_error = password_error, verify_error = verify_error)

    else:
        return render_template('register.html')


#logout
@app.route('/logout')
def logout():
    del session['username']
    return redirect('/')


#main page, see all posts
@app.route('/blog')
def blog():
    user_id = str(request.args.get('user'))
    owner = Blog.query.filter_by(id=user_id).first()
    blogs = Blog.query.filter_by(user=owner).all()

    blog_id = str(request.args.get('id'))    
    myblog = Blog.query.get(blog_id)

    return render_template('blog.html', blogs=blogs, myblog=myblog)


    #main page, see all posts
# @app.route('/myblogposts')
# def myblogposts():
#     owner = User.query.filter_by(username=session['username']).first()
#     blogs = Blog.query.filter_by(user=owner).all()

#     blog_id = str(request.args.get('id'))    
#     myblog = Blog.query.get(blog_id)

#     return render_template('myblogposts.html', blogs=blogs, myblog=myblog)


@app.route('/newpost', methods=['POST', 'GET'])
#making a new post
def newpost():
    if request.method == 'POST' :
        blog_title = request.form['title']   
        blogbody = request.form['body']
        owner = User.query.filter_by(username=session['username']).first()
        title_error_msg = ''
        body_error_msg = ''
        
        if title_error(blog_title):
            title_error_msg = "Please input a title."
            #curly braces in html form = new variable above
            return render_template('newpost.html', title_error=title_error_msg, body_error=body_error_msg, blogbody=blogbody)
            
        elif body_error(blogbody):
            body_error_msg = "Please input blog content."
            return render_template('newpost.html', title_error=title_error_msg, body_error=body_error_msg, blog_title=blog_title)
                    
        else:
            new_blog = Blog(blog_title, blogbody, owner)
            db.session.add(new_blog)
            db.session.commit()  
            return redirect('/index') 
    else:
            return render_template('newpost.html') 

#delete blog
@app.route('/delete-blog', methods=['POST'])
def delete_blog():

    blog_id = int(request.form['blog-id'])
    blog = Blog.query.get(blog_id)
    blog.completed = True
    db.session.add(blog)
    db.session.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run()