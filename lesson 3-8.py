class Students:
    __counter = 0
    def __init__(self, **kwargs):
        self.__name = kwargs.get('name') 
        self.__age = kwargs.get('age')
        self.__group = kwargs.get('group')
        Students.__counter += 1
        

    def __str__(self) -> str:
        return f'Hi! I am new student, my name is {self.__name}. I am {self.__age}.\
    I want to join {self.__group} group'

    def get_students_count():
        return f'Now we have {Students.__counter} students'
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if type(value) != int:
            print('The age must be integer!')
        else:
            self.__age = value

    
    @property
    def check(self):
        if self.__age < 18:
            return 'Sorry, You must be 18'
        if self.__group == 3:
            return 'Sorry, not enough people for this course'
        else:
            return 'You registered'


    
student_1 = Students(name = 'John Smitt', age = 23, group = 3)
student_2 = Students(name = 'Andru Bing', age = 17, group = 1)
student_3 = Students(name = 'Kate Black', age = 20, group = 1)
print(student_1.name)
student_1.name = 'John Brown'
student_1.age = 2.5
student_1.age = 25
print(student_1)

print(Students.get_students_count())

print(student_1.check)
print(student_2.check)
print(student_3.check)


