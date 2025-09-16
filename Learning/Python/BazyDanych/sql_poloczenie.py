import pymysql as mysql

con = mysql.Connect(host='localhost', unix_socket='', user='root', passwd='', db='mysql')

cur = con.cursor()


cur.execute("use dziennikluty23")
zapytanieWyswietl = cur.execute("show tables")
cur.close()


wbd = con.cursor()

wbd.execute("show databases")



con.commit()
cur.close()