import mysql.connector as mc

db= mc.connect(host='localhost', user='root', password='Hacker1928@', db = 'menagerie')
cursor=db.cursor()

cursor.execute("SELECT * FROM pet WHERE sex = 'f' AND species = 'dog'; ")
print(cursor.fetchall())
