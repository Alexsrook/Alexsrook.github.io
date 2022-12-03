import mysql.connector as mc

db= mc.connect(host='localhost', user='root', password='Hacker1928@', db = 'menagerie')
cursor=db.cursor()

cursor.execute("SELECT owner, COUNT(*) FROM pet GROUP BY owner;")
print(cursor.fetchall())