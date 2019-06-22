from flask import Flask,render_template,session

app = Flask(__name__,template_folder='templates')
app.config.from_object('settings.DevClass')
@app.route('/index')
def index():
    return render_template('index01.html')

if __name__ == '__main__':
    app.run(debug=True)
#
# import importlib
# path = 'setting.Foo'
# p,c = path.split('.',maxsplit=1)
# m = importlib.import_module(p)
# cls = getattr(m,c)
# print(type(cls()))
# print(dir(cls))