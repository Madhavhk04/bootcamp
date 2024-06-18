import sqlite3 as sql

conn = sql.connect("database/futurense.db")
cur = conn.cursor()

def userinfo(username):
    cur.execute("SELECT * FROM User WHERE username = (?)",(username,))
    value = cur.fetchall()
    return value

# s = input()
# print(userinfo(s)[0])
