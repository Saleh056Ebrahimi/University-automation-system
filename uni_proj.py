class main:
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

class student(main):
    
    def student_code(self,item):
        self.studentCode = item
    

class master(main):
    
    def instructor_number(self,item):
        self.instructorNumber = item


class education_expert(main):

    def employee_code(self,item):
        self.employeeCode = item

class lesson:

    def lesson_name(self,item):
        self.lessonName = item
    
    def lesson_number(self,item):
        self.lessonNumber = item