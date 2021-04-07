# Goal:
# Print the names of 10 Jeopardy categories.

# SQL:
# SELECT name FROM category LIMIT 10
import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()

print("Example categories:\n")

for category in results:
    print(category[0])

connection.close()