import mysql.connector as mq

db= mq.connect(host='localhost', user='root', password='Hacker1928@', db='menagerie')

cursor=db.cursor()

cursor.execute("DROP DATABASE IF EXISTS menagerie")
print("Database has been dropped")