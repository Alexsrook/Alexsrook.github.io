import mysql.connector as mq
db= mq.connect(host='localhost', user='root', password='Hacker1928@', db = 'menagerie')
cursor=db.cursor()

cursor.execute("DESCRIBE pet;")
print(cursor.fetchall())
