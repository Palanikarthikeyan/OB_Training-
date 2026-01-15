from flask import *
import sqlite3

app = Flask(__name__)

@app.route("/")
def f1():
    return render_template('display.html',sname=["OL6.5","OL6.7","RHL5","OL8"])
@app.route("/mypage",methods=["POST","GET"])
def f2():
    try:
        if request.method == "POST":
            emp_name = request.form["n1"]
            emp_dob = request.form["n2"]
            with sqlite3.connect("emp.db") as conn:
                sth = conn.cursor()
                sth.execute("insert into emp(name,dob) values(?,?)",(emp_name,emp_dob))
                conn.commit()
        message="Data Subimitted Successfully"
    except Exception as eobj:
        conn.rollback()
        message = "Insert operation is failed"
    finally:
        return f"<h2><font color=blue>{message}</font></h2>"

@app.route("/display")
def f3():
    conn = sqlite3.connect("emp.db")
    conn.row_factory = sqlite3.Row
    sth = conn.cursor()
    sth.execute("select *from emp")
    records = sth.fetchall()
    return render_template("records.html",T_records = records)

@app.route("/data")
def f4():
    conn = sqlite3.connect("emp.db")
    sth = conn.cursor()
    sth.execute("select *from emp")
    records = sth.fetchall()
    return jsonify({"emp_records":records})
if __name__ == '__main__':
    app.run(debug = True)
