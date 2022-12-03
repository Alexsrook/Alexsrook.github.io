import mysql.connector as mq

db= mq.connect(host='localhost', user='root', password='Hacker1928@')

print("----- Databases ------")

cursor=db.cursor()

cursor.execute("SHOW DATABASES")

for i in cursor:
    print(i)

print("----------------")