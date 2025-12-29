
class Student:
    enroll = 226022
    name = 'Rutuja'
    branch = 'CO'

    def accept_val(self):
        enroll = int(input("Enter enrollment no : "))
        name = input("Enter name : ")
        branch = input("Enter branch : ")
    def show_val(self):
        print("Enrollment no is : ", self.enroll)
        print("Name is          : ", self.name)
        print("Branch is        : ",self.branch)



s1 = Student()

print("\nAccepting student's information : ")
s1.accept_val()

print("\nDisplaying student's information : ")
s1.show_val()