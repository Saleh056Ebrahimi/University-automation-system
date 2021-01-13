class student():

    def __init__(self,item):
        self.i = item

    def first_name(self,item):
        self.firstName = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'w')
        f.write(self.firstName + '\n')

    def last_name(self,item):
        self.lastName = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.lastName + '\n')

    def father_name(self,item):
        self.fatherName = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.fatherName + '\n')

    def national_code(self,item):
        self.nationalCode = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.nationalCode + "\n")
        
    def address(self,item):
        self.Address = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.Address + '\n')

    def phone_number(self,item):
        self.phoneNumber = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.phoneNumber + '\n')

    def user_name(self,item):
        self.userName = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.userName + '\n')
        
    def password(self,item):
        self.Password = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.Password + '\n')

    def student_code(self,item):
        self.studentCode = item
        fileName = 'studen{}.txt'
        f = open(fileName.format(self.i),'a')
        f.write(self.studentCode)      
    

class master():

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
    
    def instructor_number(self,item):
        self.instructorNumber = item


class education_expert():

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
    
    def addDanshjo(self,item):
        
        for i in range(item):

            s = student(i)

            print('please enter the information of new student:')

            s.first_name(input('Name:'))
            s.last_name(input('LastName:'))
            s.father_name(input('FatherName:'))
            s.national_code(input('Nationalcode:'))
            s.address(input('Address:'))
            s.phone_number(input('PhoneNumber:'))
            s.user_name(input('UserName:'))
            s.password(input('Password:'))

class lesson:

    def lesson_name(self,item):
        self.lessonName = item
    
    def lesson_number(self,item):
        self.lessonNumber = item

karshenas = education_expert()

karshenas.firstName = 'ali'
karshenas.lastName = 'alizade'

karshenas.addDanshjo(3)