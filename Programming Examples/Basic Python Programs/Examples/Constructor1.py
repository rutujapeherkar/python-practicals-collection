class Student:
    def __init__(self):
        self.roll_num = 101
        self.name = "Joseph"

    def __init__(self,rno,nm):
        self.roll_num = rno
        self.name = nm

    def display(self):
        print(self.roll_num, self.name)


st = Student()
st.display()

st2 = Student(22,"rutu")
st2.display()