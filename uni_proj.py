import os
import sys
import fileinput

class student():

    def file_name(self,item):
        self.fname = item

    def first_name(self,item):
        self.firstName = item
        f = open(self.fname,'x')
        f.write(self.firstName + '\n')

    def last_name(self,item):
        self.lastName = item
        f = open(self.fname,'a')
        f.write(self.lastName + '\n')

    def father_name(self,item):
        self.fatherName = item    
        f = open(self.fname,'a')
        f.write(self.fatherName + '\n')

    def national_code(self,item):
        self.nationalCode = item      
        f = open(self.fname,'a')
        f.write(self.nationalCode + "\n")
        
    def address(self,item):
        self.Address = item    
        f = open(self.fname,'a')
        f.write(self.Address + '\n')

    def phone_number(self,item):
        self.phoneNumber = item    
        f = open(self.fname,'a')
        f.write(self.phoneNumber + '\n')

    def user_name(self,item):
        self.userName = item
        f = open(self.fname,'a')
        f.write(self.userName + '\n')
        
    def password(self,item):
        self.Password = item
        f = open(self.fname,'a')
        f.write(self.Password + '\n')

    def student_code(self,item):
        self.studentCode = item 
        f = open(self.fname,'a')
        f.write(self.studentCode)      
    

class master():

    def file_name(self,item):
        self.fname = item

    def first_name(self,item):
        self.firstName = item
        f = open(self.fname,'x')
        f.write(self.firstName + '\n')

    def last_name(self,item):
        self.lastName = item
        f = open(self.fname,'a')
        f.write(self.lastName + '\n')

    def father_name(self,item):
        self.fatherName = item
        f = open(self.fname,'a')
        f.write(self.fatherName + '\n')
    
    def national_code(self,item):
        self.nationalCode = item
        f = open(self.fname,'a')
        f.write(self.nationalCode + "\n")
    
    def address(self,item):
        self.Address = item
        f = open(self.fname,'a')
        f.write(self.Address + '\n')

    def phone_number(self,item):
        self.phoneNumber = item
        f = open(self.fname,'a')
        f.write(self.phoneNumber + '\n')

    def user_name(self,item):
        self.userName = item
        f = open(self.fname,'a')
        f.write(self.userName + '\n')
    
    def password(self,item):
        self.Password = item
        f = open(self.fname,'a')
        f.write(self.Password + '\n')
    
    def instructor_number(self,item):
        self.instructorNumber = item
        f = open(self.fname,'a')
        f.write(self.instructorNumber)   


class education_expert():


    def students_file(self, item):
        f = open('studentsName.txt', 'a')
        f.write(item + '\n')

    def masters_file(self, item):
        f = open('mastersName.txt', 'a')
        f.write(item + '\n')

    def first_name(self,item):
        self.firstName = item

    def last_name(self,item):
        self.lastName = item

    def father_name(self,item):
        self.fatherName = item
    
    def national_code(self,item):
        self.nationalCode = item
    
    def address(self,item):
        self.Address = item

    def phone_number(self,item):
        self.phoneNumber = item

    def user_name(self,item):
        self.userName = item
    
    def password(self,item):
        self.Password = item

    def employee_code(self,item):
        self.employeeCode = item
    
    def addStudent(self,item):
        
        for i in range(item):

            print('please enter the new file name for keeping new information:')
            x = str(input('use the name of new student:') + '_student.txt')

            self.students_file(x)

            s = student()
            s.file_name(x)
            print('please enter the information of new student:')

            s.first_name(input('Name:'))
            s.last_name(input('LastName:'))
            s.father_name(input('FatherName:'))
            s.national_code(input('Nationalcode:'))
            s.address(input('Address:'))
            s.phone_number(input('PhoneNumber:'))
            s.user_name(input('UserName:'))
            s.password(input('Password:'))
            s.student_code(input('StudentCode:'))

    def addMaster(self,item):
        
        for i in range(item):

            print('please enter the new file name for keeping new information:')
            x = str(input('use the name of new master:') + '_master.txt')

            self.masters_file(x)

            s = master()
            s.file_name(x)
            print('please enter the information of new student:')

            s.first_name(input('Name:'))
            s.last_name(input('LastName:'))
            s.father_name(input('FatherName:'))
            s.national_code(input('Nationalcode:'))
            s.address(input('Address:'))
            s.phone_number(input('PhoneNumber:'))
            s.user_name(input('UserName:'))
            s.password(input('Password:'))
            s.instructor_number(input('InstructorNumber:'))

    def showStudents(self):
        
        f = open('studentsName.txt','r')
        print(f.read())
    
    def showMasters(self):
        f = open('mastersName.txt','r')
        print(f.read())

    def removeStudnet(self, item):
        
        if os.path.exists(item):
            os.remove(item)
        else:
            print("The student does not exist")
    
    def removeMaster(self, item):
        if os.path.exists(item):
            os.remove(item)
        else:
            print("The msater does not exist")

    def addLesson(self,item):
        
        for i in range(item):

            print('please enter the new file name for keeping new information:')
            x = str(input('use the name of new lesson:') + '_lesson.txt')

            l = lesson(x)

            l.lesson_name(input('Lesson name:'))
            l.lesson_number(input('Lesson number:'))

    def change(self, item):
        
        print ("enter Text to search for:")
        textToSearch = input( "> " )

        print ("Text to replace it with:")
        textToReplace = input( "> " )

        print ("File to perform Search-Replace on:")
        fileToSearch  = item
        #fileToSearch = 'D:\dummy1.txt'

        tempFile = open( fileToSearch, 'r+' )

        for line in fileinput.input( fileToSearch ):
            tempFile.write( line.replace( textToSearch, textToReplace ) )
        tempFile.close()

class lesson:

    def __init__(self, item):
        self.fname = item

    def lesson_name(self,item):
        self.lessonName = item
        f = open(self.fname,'x')
        f.write(self.lessonName + '\n')
    
    def lesson_number(self,item):
        self.lessonNumber = item
        f = open(self.fname,'a')
        f.write(self.lessonNumber)

karshenas = education_expert()

#karshenas.addStudent(2)

#karshenas.showStudents()

#karshenas.removeStudnet('ali_student.txt')

#karshenas.addLesson(3)

#karshenas.addMaster(2)

#karshenas.showMasters()

#karshenas.removeMaster('iman_master.txt')

#karshenas.change('demo.txt')

#s1 = student('ali')