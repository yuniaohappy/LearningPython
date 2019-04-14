from flask import Flask,render_template,session,redirect,url_for,flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

li = ['Tom','Rose','Lipeng']

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)
app.config['SECRET_KEY'] = 'lipeng'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1/flask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy()

@app.route("/",methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        flash('提交成功啦！！！')
        return redirect(url_for('index'))
    return render_template('index.html',form=form,name=session.get('name'),current_time=datetime.utcnow())

# def hello():
#     return render_template("index.html",current_time=datetime.utcnow())
# def index():
#     name = None
#     form = NameForm()
#     if form.validate_on_submit():
#         name = form.name.data
#         print(name)
#         form.name.data = ''
#     return render_template('index.html',form=form,name=name,current_time=datetime.utcnow())

@app.route("/user01/<name>")
def user01(name):
    # user = User("Tom",13)
    return render_template("user01.html",name = name)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500


@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

@app.route("/lis")
def lis01():
    return render_template("user.html",li = li)

# class User:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

class NameForm(FlaskForm):
    name = StringField('您的姓名是?',validators=[DataRequired()])
    submit = SubmitField('提交')

class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(64),unique=True)
    users = db.relationship('User',backref='role')
    def __repr__(self):
        return '<Role %r>' % self.name
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),unique=True,index=True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    def __repr__(self):
        return '<User %r>' % self.username


# if __name__ == "__main__":
#     app.run(debug=True)