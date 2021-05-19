class Student:
    school="School:TOC H Public School"
    def setval(self,name,age,rollno,grade):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.grade=grade
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.rollno)
        print(self.grade)
        print(Student.school)
st=Student()
st.setval("Name:Anu","Age:13","Roll no:7","Class:VI")
st.printval()

