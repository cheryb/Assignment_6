import sqlite3
database = sqlite3.connect("assignment5.db")
cursor = database.cursor()

# ########  Add/remove course from semester schedule ###############
# course = 23243
# cursor.execute("""SELECT TITLE FROM COURSE WHERE CRN=?""", [course])
# for row in iter(cursor.fetchone, None):
#     print(row)

# ########### Log-in/Log-out ##############
# choice = "lovelacea"
# cursor.execute("""SELECT NAME, SURNAME FROM STUDENT WHERE EMAIL=?""", [choice])
# for row in iter(cursor.fetchone, None):
#     print(row)
#     print("Welcome", choice)

# choice2 = "bernoullid"
# cursor.execute("""SELECT NAME, SURNAME FROM INSTRUCTOR WHERE EMAIL=?""", [choice])
# for row in iter(cursor.fetchone, None):
#     print(row)
#     print("Welcome", choice2)

# choice3 = "rubinv"
# cursor.execute("""SELECT NAME, SURNAME FROM ADMIN WHERE EMAIL=?""", [choice])
# for row in iter(cursor.fetchone, None):
#     print(row)
#     print("Welcome", choice3)

############ Assemble and print course roster (instructor) ###########

# name = "Joseph Fourier"
# cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTOR=?;""", [name])
# for row in iter(cursor.fetchone, None):
#     print(row)

# name = "Jones Fourier"
# cursor.execute("""SELECT * FROM COURSE WHERE INSTRUCTOR=?;""", [name])

# if list(iter(cursor.fetchone, None)) == []:
#     print("Profesor not found")
# else:
#     for row in iter(cursor.fetchone, None):
#         print(row)


############ Add/remove courses from the system (admin) ############

# adding courses
# crn, title, department, time, day, semester, year, credits, instructor = 23301, 'FEEDBACK AND CONTROL', 'BSEE', 4200, 'TR', 'SUMMER', 2022, 4, 'Jenny Song'
# cursor.execute("""INSERT INTO COURSE VALUES('%d', '%s', '%s', '%d', '%s', '%s', '%d', '%d', '%s');""" % (crn, title, department, time, day, semester, year, credits, instructor))

# removing courses
# title = 'FEEDBACK AND CONTROL'
# cursor.execute("""DELETE FROM COURSE WHERE title = '%s';""" % title)

# title = 'CALCULUS 2'
# cursor.execute("""DELETE FROM COURSE WHERE title = '%s';""" % title)

############ Search all courses (all users) ############

# return titles for all courses
# cursor.execute("""SELECT title FROM COURSE""")
# course_list = cursor.fetchall()
# for c in course_list:
#     print(c)

# # return info on all courses
# cursor.execute("""SELECT * FROM COURSE""")
# course_list = cursor.fetchall()
# for c in course_list:
#     print(c)


############ Search courses based on parameters (all users) ############

# return all HUSS courses
# crn, title, department, time, day, semester, year, credits, instructor = 0, None, 'HUSS', 0, None, None, 0, 0, None
# cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%d' OR TITLE = '%s' OR DEPARTMENT = '%s' OR TIME = '%d' OR DAY = '%s' OR SEMESTER = '%s' OR YEAR = '%d' OR CREDITS = '%d' OR INSTRUCTOR = '%s';""" % (crn, title, department, time, day, semester, year, credits, instructor)) 

# course_list = cursor.fetchall()
# for c in course_list:
#     print(c)

# return all BSME courses and all courses taught by Jones Yu
crn, title, department, time, day, semester, year, credits, instructor = 0, None, 'BSME', 0, None, None, 0, 0, 'Jones Yu'
cursor.execute("""SELECT * FROM COURSE WHERE CRN = '%d' OR TITLE = '%s' OR DEPARTMENT = '%s' OR TIME = '%d' OR DAY = '%s' OR SEMESTER = '%s' OR YEAR = '%d' OR CREDITS = '%d' OR INSTRUCTOR = '%s';""" % (crn, title, department, time, day, semester, year, credits, instructor)) 

course_list = cursor.fetchall()
for c in course_list:
    print(c)


database.commit()
database.close()
