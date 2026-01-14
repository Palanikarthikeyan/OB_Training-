from flask import *

app = Flask(__name__)

@app.route("/")
def f1():
    return render_template('display.html',sname=["OL6.5","OL6.7","RHL5","OL8"])
@app.route("/mypage",methods=["POST","GET"])
def f2():
    if request.method == "POST":
        emp_name = request.form["n1"]
        emp_dob = request.form["n2"]
        return f"<h2>Emp name is:<b>{emp_name.title()} DOB:{emp_dob}</b></h2>"
    else:
        return render_template('index.html')

@app.route("/contact/<mobileNo>")
def f3(mobileNo):
    return render_template('view.html',T_mobileNo=mobileNo)

@app.route("/myrequest")
def f4():
    return redirect(url_for('f3',mobileNo=9494002))

@app.route("/data")
def f5():
    d={"IP":["10.20.30.40","10.23.45.45","10.20.44.34"],
       "interface":["eth0","eth1","eth2","lo"],
       "config_file":{'F1':"net.cfg",'F2':"info.cfg"}}
    return jsonify(d)


if __name__ == '__main__':
    app.run(debug = True)