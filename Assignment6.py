import sqlite3
database = sqlite3.connect("assignment5.db")
cursor = database.cursor()



########  Add/remove course from semester schedule ###############
course = 23243
cursor.execute("""SELECT TITLE FROM COURSE WHERE CRN=?""", [course])
for row in iter(cursor.fetchone, None):
    print(row)

########### Log-in/Log-out ##############
choice = "lovelacea"
cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE EMAIL=?""", [choice])
for row in iter(cursor.fetchone, None):
    print(row)
    print("Welcome", choice)

choice2 = "bernoullid"
cursor.execute("""SELECT NAME, SURNAME FROM INSTRUCTOR WHERE EMAIL=?""", [choice])
for row in iter(cursor.fetchone, None):
    print(row)
    print("Welcome", choice2)

choice3 = "rubinv"
cursor.execute("""SELECT NAME, SURNAME FROM ADMIN WHERE EMAIL=?""", [choice])
for row in iter(cursor.fetchone, None):
    print(row)
    print("Welcome", choice3)

