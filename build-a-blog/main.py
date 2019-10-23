#build-a-blog
from flask import Flask, request, redirect, render_template, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
#'mysql+pymysql://user:password@server:portNumber/databaseName'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:build-a-blog@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True
db = SQLAlchemy(app)
app.secret_key = 'y448kGcys&zP4B'

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


#create BlogPost table table
class BlogPost(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(1000))

    def __init__(self, title, body):
        self.title = title
        self.body = body

#main
@app.route('/blog')
def index():
    blog_id = str(request.args.get('id'))
    blogs = BlogPost.query.all()
    myblog = BlogPost.query.get(blog_id)

    return render_template('blog.html', blogs=blogs, myblog=myblog)

@app.route('/newpost', methods=['POST', 'GET'])
def newpostadd():
    
    if request.method == 'POST' :
        blogpost_title = request.form['title']   
        blogbody = request.form['body']
        title_error_msg = ''
        body_error_msg = ''
        

        if title_error(blogpost_title):
            title_error_msg = "Please input a title."
            return render_template('newpost.html', title_error=title_error_msg, body_error=body_error_msg, blogbody=blogbody)
        if body_error(blogbody):
            body_error_msg = "Please input blog content."
            return render_template('newpost.html', title_error=title_error_msg, body_error=body_error_msg, blogpost_title=blogpost_title)
                   
        else:
            mynewpost = BlogPost(blogpost_title, blogbody)
            db.session.add(mynewpost)
            db.session.commit()  
            return redirect('blog/?id=' + str(blog.id)) 
    else:
            return render_template('newpost.html') 

if __name__ == '__main__':
    app.run()