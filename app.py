from flask import Flask,render_template,request,redirect,url_for
import sqlite3 as sql

app=Flask("__name__")

@app.route("/",methods=["post","get"])
def insert1():
    if request.form.get("id")!=None:
        id=request.form.get("id")
        name=request.form.get("name")

        conn=sql.connect("db.db")
        cur=conn.cursor()
        cur.execute("insert into t (id,name) values (?,?)",(id,name))
        conn.commit()

    return render_template("index.html")

@app.route("/update/<id>",methods=["post","get"])
def update1(id):
    conn=sql.connect("db.db")
    conn.row_factory=sql.Row
    cur=conn.cursor()
    cur.execute("select * from t where id=?",(id,))
    x=cur.fetchone()

    if request.form.get("name")!=None:
        id=request.form.get("id")
        name=request.form.get("name")

        conn=sql.connect("db.db")
        cur=conn.cursor()
        cur.execute("update t set name=? where id=?",(name,id))
        conn.commit()
        return render_template("index.html")

    return render_template("update.html",data=x)
    




if __name__=="__main__":
    app.run(debug=True)