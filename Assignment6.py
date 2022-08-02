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

# 1 • Add/remove course from semester schedule (based on course ID number).

#def add_remove_course_from_schedule():
#    print("You have selected option 1. Add/remove course from semester schedule (based on course ID number).")
#    choice2 = input("Do you want to add (1) or remove(2) this course from your schedule: ")
#    while choice2 == 1 or 2:
       
#        choice2 = int(choice2)
#        if choice2 == 1:

#            course = input("Enter course ID number: ")
#            course = int(course)
#            cursor.execute("""SELECT crn FROM COURSE WHERE crn=?""", [course])
#            for row in iter(cursor.fetchone, None):
#                print(row)
                
#        elif choice2 == 2:
#            course = input("Enter course ID number: ")
#            course = int(course)
#            cursor.execute("""SELECT crn FROM COURSE WHERE crn=?""", [course])
#            for row in iter(cursor.fetchone, None):
#                print(row)

## 4 • Log-in, log-out (all users).
#def log_in_log_out():
#    print("You have selected option 4. Log-in, log-out (all users).")
#    choice = input("Are you a student (1), instructor(2) or admin(3)? ")
#    choice = int(choice) 
#    name = input("Enter email: ")
#    if choice == 1:
#        cursor.execute("""SELECT email FROM STUDENT WHERE email=?""", [name])
#        for row in iter(cursor.fetchone, None):
#            print(row)
#            print("You are now logged in")
#    elif choice == 2:
#        cursor.execute("""SELECT email FROM INSTRUCTOR WHERE email=?""", [name])
#        for row in iter(cursor.fetchone, None):
#            print(row)
#            print("You are now logged in")
#    elif choice == 3:
#        cursor.execute("""SELECT email FROM ADMIN WHERE email=?""", [name])
#        for row in iter(cursor.fetchone, None):
#            print(row)
#            print("You are now logged in")

## 7 • A menu to implement the use-cases. ######## DONE #######

#user_input = input("Please select an option \n 1. Add/remove course from semester schedule (based on course ID number). \n 2. Assemble and print course roster (instructor). \n 3. Add/remove courses from the system (admin). \n 4. Log-in, log-out (all users). \n 5. Search all courses (all users). \n 6. Search courses based on parameters (all users): \n")
#user_input = int(user_input)

#if user_input == 1:
#    add_remove_course_from_schedule()
#elif user_input == 2:
#    print_course()
#elif user_input == 3:
#    add_remove_course_from_system()
#elif user_input == 4:
#    log_in_log_out()
#elif user_input == 5:
#    search_all_courses()
#elif user_input == 6:
#    search_specific_courses()
#database.commit()
#database.close()
