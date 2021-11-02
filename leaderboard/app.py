from flask import Flask
from flask import render_template
import mysql.connector

app = Flask(__name__)

@app.route("/")
def get_leaderboard_data():
    connection = mysql.connector.connect(host='localhost',
                                        database='mydb',
                                        user='root',
                                        password='pingpong1!')
    
    mycursor = connection.cursor()
    mycursor.execute("SELECT * FROM pongLeaderboard")
    users = mycursor.fetchall()
    res = sort_users(users)
    return render_template('leaderboard.html', user_list=res)

def sort_users(users):
    list = []
    for user in users:
        list.append((user[1], user[2]))
    list.sort(key = lambda x: x[1], reverse=True) 
    finalList = []
    rank = 1
    for sortedUser in list:
        finalList.append((rank, sortedUser[0], sortedUser[1]))
        rank = rank + 1
    print(finalList)
    return finalList

if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)

