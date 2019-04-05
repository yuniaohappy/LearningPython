from flask import Flask,render_template
from flask_bootstrap import Bootstrap

li = ['Tom','Rose','Lipeng']

app = Flask(__name__)
bootstrap = Bootstrap(app)
@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/user01/<name>")
def user01(name):
    # user = User("Tom",13)
    return render_template("user01.html",name = name)

@app.route("/user/<name>")
def user(name):
    return render_template("user.html",name=name)

@app.route("/lis")
def lis01():
    return render_template("user.html",li = li)

class User:
    def __init__(self,name,age):
        self.name = name
        self.age = age



if __name__ == "__main__":
    app.run(debug=True)