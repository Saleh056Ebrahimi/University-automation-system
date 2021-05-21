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

    def selectUnit(self , item):
        f = open('studentsName.txt','r')
        found = False
        for line in f:
            if item in line:
                found = True

        if found == False:
            print('the student does not exist!!!')
        else:
            print('These lessons are limited :')
            print()

            f1 = open('mastersName.txt','r')
            for i in f1:
                n = i.split('.')
                f2 = open(n[0]+ '_lessons.txt','r')
                nn = n[0].split('_')
                print(nn[0],': ')
                for line in f2:
                    print('\t'+line,end = '')



            print()
            print('----------')
            print('for select units you have to first choice lesson name and then choice masnter name')
            print('select lessons:')

            check = 'yes'
            lst = {}
            while check == 'yes':
                print('enter the lesson name :')
                les = input('>')
                f5 = open('lessons.txt','r')
                for line1 in f5:
                    l1 = line1.split('_')
                    if les == l1[0]:
                        print('enter the master name :')
                        mas = input('>')
                        f6 = open('mastersName.txt','r')
                        for line2 in f6:
                            l2 = line2.split('_')
                            if mas == l2[0]:
                                lst[les] = mas
                                print('do you still want to continue?') 
                                print('for continue enter yes else enter no :')
                                check = input('>')

            print('------------')
            fname = item.split('_')
            f3 = open(fname[0] + '_lessons.txt','x')
            
            keys = []
            vals = []
            
            for i in lst.keys():
                keys.append(i)
            for i in lst.values():
                vals.append(i)

            for i in range(len(lst)):
                f3.write(keys[i]+' : '+vals[i]+'\n')  
        
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

    def showStudentsAndGrade(self, masterName):
        n = masterName.split('_')
        name = n[0]
        lst_for_students = []
        f = open('mastersName.txt','r')
        for line1 in f:
            if masterName in line1:
                newMasterName = masterName.split('.')
                f1 = open(newMasterName[0]+'_lessons.txt','r')
                print('these are the lessons of master :')
                print()
                for line2 in f1:     
                    print(line2,end='')
                print('------------------')
                print('if you want to see students of one lesson shoice one lesson.')
                print()
                lessonEntered = input('>:')
                f2 = open('studentsName.txt','r')
                for line3 in f2:
                    splitedLine = line3.split('_')
                    studentName = splitedLine[0]
                    f3 = open(studentName+'_lessons.txt','r')
                    for studnetLessons in f3:
                        lst = studnetLessons.split(':')
                        if lessonEntered in lst[0] and name in lst[1]:
                            lst_for_students.append(studentName)
                            print(studentName)
        print('--------------')
        print('Do you want to give a student a grade?')
        print('if you want enter "yes".')
        check = input('>:')
        while check == 'yes':
            studentNameForGrade = input('enter the student name :')
            for stud in lst_for_students:
                if studentNameForGrade == stud:
                    mark = input('print the mark of ' + studentNameForGrade + ':')
                    f4 = open('marks_of_' + studentNameForGrade + '.txt','a')
                    f4.write(lessonEntered+':' + mark + '\n')
            print('If you want to continue enter "yes".')
            check = input('>:')
                

                        

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


#karshenas = education_expert()

#karshenas.addStudent(1)

#karshenas.showStudents()

#karshenas.removeStudnet('ali_student.txt')

#karshenas.addLesson(6)

#karshenas.addMaster(4)

#karshenas.showMasters()

#karshenas.removeMaster('iman_master.txt')

#karshenas.change('demo.txt')

#karshenas.addLessonForMaster('hasan_master.txt')

#s = student()

#s.selectUnit('saleh_student.txt')

m = master()

m.showStudentsAndGrade('iman_master.txt')
