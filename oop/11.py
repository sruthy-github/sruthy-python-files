class Person:      #parent class/base class/super class
    def details(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printdetails(self):
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):       #child class/derived class/sub class
    def det(self,rollno,school):
        self.rollno=rollno
        self.school=school
    def prints(self):
        print(self.rollno)
        print(self.school)
per=Person()
per.details("Anu",13,"F")
per.printdetails()
st=Student()
st.details("Anu",13,"F")
st.printdetails()
st.det(4,"Toc H")
st.prints()
