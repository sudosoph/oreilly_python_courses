# Goal:
# Print the value, question, and answer for 10 Jeopardy clues.

# SQL:
# SELECT text, answer, value FROM clue LIMIT 10

import sqlite3

connection = sqlite3.connect("jeopardy.db")
cursor = connection.cursor()

cursor.execute("SELECT text, answer, value FROM clue LIMIT 10")
results = cursor.fetchall()

# TODO: process results.
for clue in results:
    text, answer, value = clue
    # text = clue[0]
    # answer = clue[1]
    # value = clue[2]

    # [$200]
    # Question: ____
    # Answer: What is ___?

    print("[$%s]" % (value,))
    print("Question: %s" % (text,))
    print("Answer: What is '%s'?" % (answer,))
    print("")

connection.close()