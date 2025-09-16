import pymysql as mysql

class sql:
    words = []
    fakewords = []

def connect():
    con = mysql.Connect(host='sql11.freesqldatabase.com', unix_socket='', user='sql11667150', passwd='bLZfXF6JCd', db='sql11667150')
    cur = con.cursor()

    cur.execute("select * from words")
    for c in cur:
        sql.words.append(c)

    fakewords = cur.execute("select * from fakewords")
    for c in cur:
        sql.fakewords.append(c)

    cur.close()

connect()