import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root",passwd="", database="railway")

mycursor = mydb.cursor();

mycursor.execute("select * from signup")
result = mycursor.fetchall()


for i in result:
    print(i)
