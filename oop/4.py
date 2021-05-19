class Student:
    def setval(self,name,grade,rollno):
        self.name=name
        self.grade=grade
        self.rollno=rollno
    def printval(self):
        print(self.name)
        print(self.grade)
        print(self.rollno)
st=Student()
st.setval("ANU","class:4"  ,12)
st.printval()
