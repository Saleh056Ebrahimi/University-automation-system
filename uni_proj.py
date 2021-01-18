import os
import sys
import fileinput

class student():

    def file_name(self,item):
        self.fname = item

    def first_name(self,item):
        self.firstName = item
        f = open(self.fname,'x')
        f.write('FirstName:' + self.firstName + '\n')

    def last_name(self,item):
        self.lastName = item
        f = open(self.fname,'a')
        f.write('LastName:' + self.lastName + '\n')

    def father_name(self,item):
        self.fatherName = item    
        f = open(self.fname,'a')
        f.write('FatherName:' + self.fatherName + '\n')

    def national_code(self,item):
        self.nationalCode = item      
        f = open(self.fname,'a')
        f.write('NationalCode:' +self.nationalCode + "\n")
        
    def address(self,item):
        self.Address = item    
        f = open(self.fname,'a')
        f.write('Address:' +self.Address + '\n')

    def phone_number(self,item):
        self.phoneNumber = item    
        f = open(self.fname,'a')
        f.write('PhoneNumber:' +self.phoneNumber + '\n')

    def user_name(self,item):
        self.userName = item
        f = open(self.fname,'a')
        f.write('UserName:' +self.userName + '\n')
        
    def password(self,item):
        self.Password = item
        f = open(self.fname,'a')
        f.write('Password:' +self.Password + '\n')

    def student_code(self,item):
        self.studentCode = item 
        f = open(self.fname,'a')
        f.write('StudentCode:' +self.studentCode)      
    

class master():

    def file_name(self,item):
        self.fname = item

    def first_name(self,item):
        self.firstName = item
        f = open(self.fname,'x')
        f.write('FirstName:' +self.firstName + '\n')

    def last_name(self,item):
        self.lastName = item
        f = open(self.fname,'a')
        f.write('LastName:' +self.lastName + '\n')

    def father_name(self,item):
        self.fatherName = item
        f = open(self.fname,'a')
        f.write('FatherName:' +self.fatherName + '\n')
    
    def national_code(self,item):
        self.nationalCode = item
        f = open(self.fname,'a')
        f.write('NationalCode:' +self.nationalCode + "\n")
    
    def address(self,item):
        self.Address = item
        f = open(self.fname,'a')
        f.write('Address:' +self.Address + '\n')

    def phone_number(self,item):
        self.phoneNumber = item
        f = open(self.fname,'a')
        f.write('PhoneNumber:' +self.phoneNumber + '\n')

    def user_name(self,item):
        self.userName = item
        f = open(self.fname,'a')
        f.write('UserName:' +self.userName + '\n')
    
    def password(self,item):
        self.Password = item
        f = open(self.fname,'a')
        f.write('Password:' +self.Password + '\n')
    
    def instructor_code(self,item):
        self.instructorCode = item
        f = open(self.fname,'a')
        f.write('InstructorCode:' +self.instructorCode)   


class education_expert():


    def students_file(self, item):
        f = open('studentsName.txt', 'a')
        f.write(item + '\n')

    def masters_file(self, item):
        f = open('mastersName.txt', 'a')
        f.write(item + '\n')

    def lesssons_file(self, item):
        f = open('lessons.txt', 'a')
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
            s.instructor_code(input('InstructorCode:'))

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

            self.lesssons_file(x)

            l = lesson(x)

            l.lesson_name(input('Lesson name:'))
            l.lesson_number(input('Lesson number:'))

    def change(self, item):
        
        print ("enter Text to search for:")
        textToSearch = input( "> " )

        print ("Text to replace it with:")
        textToReplace = input( "> " )

        #print ("File to perform Search-Replace on:")
        fileToSearch  = item

        tempFile = open( fileToSearch, 'r+' )

        for line in fileinput.input( fileToSearch ):

                tempFile.write( line.replace( textToSearch, textToReplace ) )

        tempFile.close()


    def addLessonForMaster(self, item):
        self.masterfile = item
        f1 = open(self.masterfile,'r')

        for line in f1:
            if 'InstructorCode' in line:
                l = line.split(':')
                lst = LessonsOfMaster(l[1])

        f1.close()

        name = self.masterfile.split('.')

        f3 = open(name[0] + '_lessons.txt','w')
        for i in lst:
            f3.write(i)

        
        
                

class lesson:

    def __init__(self, item):
        self.fname = item

    def lesson_name(self,item):
        self.lessonName = item
        f = open(self.fname,'x')
        f.write('LessonName:'+ self.lessonName + '\n')
    
    def lesson_number(self,item):
        self.lessonNumber = item
        f = open(self.fname,'a')
        f.write('LessonNumber:' +self.lessonNumber)

def LessonsOfMaster(item):
    mastercode = list(item)
    lessonlist = []
    mydict = {}
    f = open('lessons.txt','r')
    for line1 in f:
        m = line1.split('\n')    
        l = open(m[0],'r')
        for line2 in l:
            n = line2.split(':')
            mydict.update({n[0] : n[1]})
        if mydict['LessonNumber'] in mastercode:
            lessonlist.append(mydict['LessonName'])        
     
    return lessonlist


karshenas = education_expert()

#karshenas.addStudent(1)

#karshenas.showStudents()

#karshenas.removeStudnet('ali_student.txt')

#karshenas.addLesson(6)

#karshenas.addMaster(3)

#karshenas.showMasters()

#karshenas.removeMaster('iman_master.txt')

#karshenas.change('demo.txt')

karshenas.addLessonForMaster('hojat_master.txt')

#s1 = student('ali')