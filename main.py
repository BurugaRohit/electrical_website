from flask import Flask, render_template, request, redirect, url_for, flash
import pymysql
import pymysql.cursors
app = Flask(__name__)


# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='rohipra@70',
                             db='electrical_site',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        mobilenumber = request.form.get('mobilenumber')
        message = request.form.get('message')
        cursor = connection.cursor()
        sql = "INSERT INTO customers_details (name, email, mobilenumber, message) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, email, mobilenumber, message))
        connection.commit()
        flash('Your Message has been sent to Proprietor', 'success')
        connection.close()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.secret_key = 'some_secret'
    app.run(debug=True)
