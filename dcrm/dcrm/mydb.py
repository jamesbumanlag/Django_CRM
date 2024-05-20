# Install Mysql on your computer
# https://dev.mysql.com/download/installer
# pip install mysql
# pip install mysql-connector or
# pip install mysql-connection-python



import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = '0911'


    )


# prepare a cursor object
cursorObject = dataBase.cursor()


# Create a database
cursorObject.execute("CREATE DATABASE elderco")


print('All Done')