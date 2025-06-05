class Student:
    name = ""
    rollno = 0 #default attributes
     #dont want to create during class

    def __init__(self , x , y):
        self.name = x
        self.rollno = y

    def display_info(self):
        print(f"{self.name} has a rollno {self.rollno}")

    def __str__(self):
        return f"class is broing not the class"

# student1 = Student()
# student1.name = "ram"
# student1.rollno = 98

# student2 = Student()
# student2.name = "sam"

# print(student2.name)
# student2.display_info()


student1 = Student("Ram" , 98)
student2 = Student("Sam" , 99)


print(student2) # trying access this obj as String


