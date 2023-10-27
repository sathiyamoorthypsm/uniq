from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'sathiP@123'
app.config['MYSQL_DB'] = 'flaskproject'
 
mysql = MySQL(app)
@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    mysql.connection.commit()
    cursor.close()
    return render_template('index.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        age = request.form['age']
        cursor = mysql.connection.cursor()
        cursor.execute(''' INSERT INTO details VALUES(%s,%s,%s)''',(id,name,age))
        mysql.connection.commit()
        cursor.close()
        return redirect('/result')
@app.route('/result')
def result():
    cursor = mysql.connection.cursor()
    cursor.execute("select * from details")
    users=cursor.fetchall()
    cursor.close()
    return render_template("result.html",users=users)

if __name__ == '__main__':
    app.run(debug=True)
