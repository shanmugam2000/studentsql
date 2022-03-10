import sqlite3 as sql
from prettytable import PrettyTable
connection=sql.connect("studentmanagement.db")

listOfStudTable=connection.execute("select name from sqlite_master where type='table' AND name='student'").fetchall()

if listOfStudTable!=[]:
    print("Table is already Created")
else:
    connection.execute('''create table student(
                              ID integer primary key autoincrement,
                              Name text,
                              RollNo integer,
                              AdmnNo integer,
                              ExamName text,
                              EnglishMark integer,
                              MathsMark integer,
                              PhysicsMark integer,
                              ChemistryMark integer,
                              BiologyMark integer
                              );''')
    print("Table Created Successfully.")

while True:
    print("1. Add Student :")
    print("2. View Student :")
    print("3. Search Student using Partial name :")
    print("4. Search student using  Roll number :")
    print("5. Update Student with Admission Number :")
    print("6. Delete using Admission Number :")
    print("7. Student Detail Who is Topper in Physics :")
    print("8. Total Count of Students in class :")
    print("9. Average Mark of Student in English :")
    print("10. Student Who Scored Below Average in Maths :")
    print("11. Student Who Scored Above Average in Chemistry :")
    print("12. EXIT")

    choice=int(input("Enter choice :"))

    if choice==1:
        getName=input("Enter name :")
        getRollNum=input("Enter the Roll Number :")
        getAdmNum=input("Enter the Admission Number :")
        getExamName=input("Enter the Examination Name :")
        getEng=input("Enter English Mark :")
        getMat=input("Enter the Maths Mark :")
        getPhy=input("Enter the Physics Mark :")
        getChem=input("Enter  the Chemistry Mark :")
        getBiology=input("Enter the Biology Mark :")

        connection.execute("insert into student(Name,RollNo,AdmnNo,ExamName,EnglishMark,MathsMark,PhysicsMark,ChemistryMark,BiologyMark)\
                           values('"+getName+"',"+getRollNum+","+getAdmNum+",'"+getExamName+"',"+getEng+","+getMat+","+getPhy+","+getChem+","+getBiology+")")
        connection.commit()
        print("Student Data Added Successfully.")

    elif choice==2:
        result=connection.execute("select * from student")
        table = PrettyTable(["ID", "NAME", "ROLL NO", "ADMISSION NUM", "EXAM NAME", "ENGLISH", "PHYSICS","CHEMISTRY","BIOLOGY"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7],i[8]])
        print(table)

    elif choice == 3:
        getName = input("Search the Partial Name Which you want:")

        result=connection.execute("select * from student where Name like '"+getName+"%'")
        table=PrettyTable(["ID","NAME", "ROLL NO", "ADMISSION NUM", "EXAM NAME", "ENGLISH", "PHYSICS","CHEMISTRY","BIOLOGY"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6],i[7],i[8]])
        print(table)

    elif choice==4:
        getRollNum = input("Enter the Roll Number to Search ")


        result=connection.execute("select * from student where RollNo="+getRollNum+" or AdmnNo="+getAdmNum+"")
        table = PrettyTable(["ID", "NAME", "ROLL NO", "ADMISSION NUM", "EXAM NAME", "ENGLISH", "PHYSICS", "CHEMISTRY", "BIOLOGY"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)

    elif choice==5:
        getAdmNum = input("Enter the Admission Number to get Update :")

        getName = input("Enter the name :")
        getRollNum = input("Enter the Roll Number ;")
        getExamName = input("Enter the Examination Name :")
        getEng = input("Enter English Mark :")
        getMat = input("Enter the Maths Mark :")
        getPhy = input("Enter the Physics Mark :")
        getChem = input("Enter  the Chemistry Mark :")
        getBiology = input("Enter the Biology Mark :")
        connection.execute("update student set Name='"+getName+"',RollNo="+getRollNum+",ExamName='"+getExamName+"',EnglishMark="+getEng+",MathsMark="+getMat+",PhysicsMark="+getPhy+",ChemistryMark="+getChem+",BiologyMark="+getBiology+" where AdmnNo="+getAdmNum+"")
        connection.commit()
        print("Updated Successfully.")

    elif choice==6:
        getAdmNum = input("Enter the Admission Number to get Delete :")
        connection.execute("delete from student where AdmnNo="+getAdmNum+"")
        connection.commit()
        print("Data Deleted Successfully.")

    elif choice==7:
        result=connection.execute("select * from student where Physics_Mark=(select  max(Physics_Mark) from student)")
        table = PrettyTable(["ID", "NAME", "ROLL NO", "ADMISSION NUM", "EXAM NAME", "ENGLISH", "PHYSICS", "CHEMISTRY", "BIOLOGY"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)

    elif choice==8:
        result=connection.execute("select count(*) from student")
        for i in result:
            print("Total student Count :" ,i[0])

    elif choice==9:
        result = connection.execute("select avg(English_Mark) from student")
        for i in result:
            print("Average English Mark :", i[0])

    elif choice==10:

        result=connection.execute("select * from student where Maths_Mark < (select avg(Maths_Mark) from student)")
        table = PrettyTable(["ID", "NAME", "ROLL NO", "ADMISSION NUM", "EXAM NAME", "ENGLISH", "PHYSICS", "CHEMISTRY", "BIOLOGY"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)

    elif choice==11:
        result=connection.execute("select * from student where Maths_Mark > (select avg(Maths_Mark) from student)")
        table = PrettyTable(["ID", "NAME", "ROLL NO", "ADMISSION NUM", "EXAM NAME", "ENGLISH", "PHYSICS", "CHEMISTRY", "BIOLOGY"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
        print(table)

    elif choice==12:
        break

    else:
        print("invalid option")