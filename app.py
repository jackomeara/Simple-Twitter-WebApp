from flask import Flask, render_template, url_for, redirect
from twitter import TwitterBot
from woeid import resolve_id
from forms import search
from configparser import ConfigParser
from flask_mysqldb import MySQL
from datetime import datetime


app = Flask(__name__)

config = ConfigParser()
config.read("creds.ini")
app.config['SECRET_KEY'] = config.get("db_creds", "secret_key")
app.config['MYSQL_USER'] = config.get("db_creds", "mysql_user")
app.config['MYSQL_PASSWORD'] = config.get("db_creds", "mysql_password")
app.config['MYSQL_HOST'] = config.get("db_creds", "mysql_host")
app.config['MYSQL_DB'] = config.get("db_creds", "mysql_db")
mysql = MySQL(app)


@app.route('/', methods=['POST', 'GET'])
def get_homepage():
    form = search()
    if form.validate_on_submit():
        location = form.location.data
        return redirect(url_for('get_trending_func', location=location))
    return render_template("home.html", form=form)

@app.route("/trending/<location>")
def get_trending_func(location):
    id = resolve_id(location)
    if id != None:
        results =  TwitterBot().get_trending(id)
        # cursor = mysql.connection.cursor()
        # cursor.execute(''' INSERT INTO info_table VALUES(%s,%s)''',(datetime.now(), location, results[0], results[1], results[2]))
        # mysql.connection.commit()
        # cursor.close()
        return results
    else:
        return "invalid location"



if __name__ == "__main__":
  app.run(debug=True)