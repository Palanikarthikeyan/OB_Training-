from flask import Flask

app_obj = Flask(__name__)

@app_obj.route("/")
def f1():
	return "<h2><font color=green>Welcome to Flask App</font></h2>"
@app_obj.route("/aboutus")
def f2():
	return "<h1>This is About Us Webpage</h1>"

@app_obj.route("/contactus/<number>")
def f3(number):
	return f"<h1>Contact Number:{number}</h1>"

if __name__ == '__main__':
	app_obj.run(debug = True)
