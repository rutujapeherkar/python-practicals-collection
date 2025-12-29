import datetime

def issue_book():
    bnum = input("Enter Book Number : ")
    enr = input("Enter Enrollment Number : ")
    a = datetime.date.today()
    idate = str(a.day) + "-" + str(a.month) + "-" + str(a.year)

    fobj = open("all_issued.txt", "a")
    fobj.write(bnum + "," + enr + "," + idate + ",NR\n")
    fobj.close()
    print("Book Issued...")
    
def return_book():
    ret_book = input("Enter Book Number to Return : ")
    a = datetime.date.today()
    rdate = str(a.day) + "-" + str(a.month) + "-" + str(a.year)

    flag = 1
    fobj = open("all_issued.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    i = 0
    while i <len(all_lines):
        oneline = all_lines[i]
        ls = oneline.split(",")
        if ls[0] == ret_book and ls[3] == "NR\n":
                ls[3] = rdate + "\n"
                new_str = ",".join(ls)
                all_lines[i] = new_str
                flag = 2
                break
        i = i + 1

    if flag == 1:
        print("Invalid Book Number. No such Book is Issues...")
    if flag == 2:
        fobj2 = open("all_issued.txt", "w")
        fobj2.writelines(all_lines)
        fobj2.close()
        print("Book Returned...")


def view_not_ret_books():
    fobj = open("all_issued.txt", "r")
    for oneline in fobj:
        ls = oneline.split(",")
        if ls[3] == "NR\n":
            print(ls[0], ls[1], ls[2], sep="\t")
    fobj.close()


def add_new_book():
    bnum = input("Enter Book Number : ")
    btitle = input("Enter Book Title : ")
    bauth = input("Enter Author  Name : ")
    bpublication = input("Enter Publication Name : ")

    fobj = open("all_books.txt", "a")
    fobj.write(bnum + "," + btitle + "," + bauth + "," + bpublication + "\n")
    fobj.close()
    print("New Book Added...")


def add_new_stud():
    senr = input("Enter Student Enrollment No : ")
    sname = input("Enter Student Name : ")
    semail = input("Enter Student Email : ")
    smob = input("Enter Student Mobile No : ")

    fobj = open("all_stud.txt", "a")
    fobj.write(senr + "," + sname + "," + semail + "," + smob + "\n")
    fobj.close()
    print("New Student Added...")

def book_history():
    bnum = input("Enter Book Number : ")
    i = 1
    fobj = open("all_issued.txt", "r")
    print("Book Number", bnum, "was issued to the following Students : ")
    for oneline in fobj:
        a = oneline.split(",")
        if a[0] == bnum:
            print(str(i) + ". " + a[1])
            i = i + 1
    fobj.close()

def stud_history():
    senr = input("Enter Student Enrollment No : ")
    i = 1
    fobj = open("all_issued.txt", "r")
    print("Student issued following books : ")
    for oneline in fobj:
        a = oneline.split(",")
        if a[1] == senr:
            print(str(i) + ". " + a[0])
            i = i + 1
    fobj.close()
def search_book():
   sbook = input("Enter Book Number : ")
   fobj = open("all_books.txt", "r")
   for oneline in fobj:
       ans = oneline.split(",")
       if ans[0] == sbook:
           print("Book Name : ", ans[1])
           print("Book Author : ", ans[2])
           print("Book Publication : ", ans[3])
   fobj.close()
def search_stud():
    ssenroll = input("Enter Student Enrollment No : ")
    fobj = open("all_stud.txt", "r")
    for oneline in fobj:
        ans = oneline.split(",")
        if ans[0] == ssenroll:
            print("Student Name : ", ans[1])
            print("Student Email : ", ans[2])
            print("Student Mobile No : ", ans[3])
    fobj.close()

while True:
    input()
    print("Select operation")
    print("1 - Issue Book")
    print("2 - Return Book")
    print("3 - View Not Returned Books")
    print("4 - Add New Book")
    print("5 - Add New Student")
    print("6 - Search Book")
    print("7 - Search Student")
    print("8 - Book History")
    print("9 - Student History")
    print("0 - EXIT")
    ch = int(input("Provide your choice : ") )
    if ch==1: issue_book()
    elif ch==2: return_book()
    elif ch==3: view_not_ret_books()
    elif ch==4: add_new_book()
    elif ch==5: add_new_stud()
    elif ch==6: search_book()
    elif ch==7: search_stud()
    elif ch==8: book_history()
    elif ch==9: stud_history()
    elif ch==0: exit(0)
