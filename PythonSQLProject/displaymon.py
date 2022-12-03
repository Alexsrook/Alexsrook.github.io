import mysql.connector as mc
from tabulate import tabulate

db= mc.connect(host='localhost', user='root', password='Hacker1928@', db = 'menagerie')
cursor=db.cursor()

cursor.execute("SELECT name, birth, MONTH(birth) FROM pet;")
pd = cursor.fetchall()

print(tabulate(pd, headers = ['name', 'birth', 'MONTH(birth)'], tablefmt='psql'))