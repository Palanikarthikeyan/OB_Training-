from flask import Flask,redirect,url_for
app_obj = Flask(__name__)

@app_obj.route("/")
def f1():
    return "<h1>Welcome to Flask Application</h1>"

@app_obj.route("/home")
def f2():
    return "<h2>This is home page</h2>"

@app_obj.route("/mypage/<content>")
def f3(content):
    return f"<h2>Response Content:{content}</h2>"

@app_obj.route("/myurl")
def f4():
    return redirect(url_for('f2'))

if __name__ == '__main__':
    app_obj.run(debug=True)

