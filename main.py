#create table users(id int primary key auto_increment, name varchar(20) UNIQUE, password varchar(20));
#Для name я використав обмеження UNIQUE щоб не можна було зареєструватися з того самого імені.

import mysql.connector

connection = mysql.connector.connect(host="127.0.0.1",
                                    database="project",
                                    user="root",
                                    password="")

cursor=connection.cursor()

def register():
    name = input("Hello, enter your name: ")
    password = input("Enter your password: ")

    a = cursor.execute("select name, password from users where name = %s and password = %s", (name, password))

    if cursor.fetchone() is None:
        cursor.execute("insert into users(name, password) values(%s, %s)", (name, password))
        connection.commit()
        print('Regestration completed!')
    else:
        print('User is exist or wrong password.')

def login():
    name = input("Enter name: ")
    password = input("Enter password: ")

    a = cursor.execute("select name, password from users where name = %s and password = %s", (name, password))

    if not cursor.fetchone():
        print("User missing or password is wrong.")
    else:
        print("Welcome")

enter = input("Enter you action (reg or log): ")
if enter == 'reg':
    register()
elif enter == 'log':
    login()

cursor.execute("select * from users")
data=cursor.fetchall()
print(data)
cursor.close()