import datetime

def generate_bill():
    obj = open("all_bills.txt", "a")
    a = datetime.date.today()
    obj1 = open("all_bills.txt", "r")
    temp = obj1.readlines()
    bnum = len(temp) + 1
    obj1.close()
    bdate = str(a.day) + "-" + str(a.month) + "-" + str(a.year) + "\n"
    sum = 0
    code = input("Enter dish code to calculate its bill : ")
    mobj = open("menu.txt", "r")
    ls = mobj.readlines()
    i = 0
    while i < len(ls):
        a = ls[i].split(",")
        if code == a[0]:
            sum = sum + int(a[2])
        i = i + 1
    tot = sum
    date = bdate
    s = str(bnum) + "," + str(tot) + "," + bdate

    obj.write(s)

    print("Bill generated....")
def view_menu():
    fobj = open("menu.txt", "r")
    for oneline in fobj:
        ls = oneline.split(",")
        print(ls[0] + " - " + ls[1] + " --> " + "Rs." + ls[2] , end = "")

    fobj.close()
    obj = open("all_bills.txt", "r")
    temp = obj.readlines()

def add_new_dish():
    dish_code = input("Enter Dish Code : ")
    dish_name = input("Enter Dish Name : ")
    dish_price = input("Enter Dish Price : ")

    fobj = open("menu.txt", "a")
    fobj.write(str(dish_code) + "," + dish_name + "," + dish_price + "\n")
    fobj.close()
def update_dish_price():
    dcode = input("Enter Dish Code : ")
    new_dprice = input("Enter New Dish Price : ")
    fobj = open("menu.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    i = 0
    flag = 1
    while i < len(all_lines):
        oneline = all_lines[i]
        ls = oneline.split(",")
        ls[2] = new_dprice
        new_str = ",".join(ls)
        all_lines[i] = new_str
        flag = 2
        break
    i = i + 1

    if flag == 1:
        print("Invalid Dish Number. No Such Dish present in Menu")
    if flag == 2:
        fobj2 = open("menu.txt", "w")
        fobj2.writelines(all_lines)
        fobj2.close()
        print("Dish Price Updated...")
def view_today_collection():
    a = datetime.date.today()
    bdate = str(a.day) + "-" + str(a.month) + "-" + str(a.year) + "\n"

    fobj = open("all_bills.txt", "r")
    ls = fobj.readlines()
    i = 0
    sum = 0
    while i < len(ls):
        a = ls[i].split(",")
        if a[2] == bdate:
            sum = sum + int(a[1])
        i = i + 1
    print("Today's collection is : ", sum)

def view_collection_of_specific_date():
    date = input("Enter date : ")
    obj = open("all_bills.txt", "r")
    ls = obj.readlines()
    i = 0
    flag = 0
    sum = 0
    while i < len(ls):
        a = ls[i].split(",")
        if a[2] == date:
            sum = sum + int(a[1])
            flag = 1
        i = i + 1

    if flag == 0:
        print("Invalid date. No such bill found onn this date.")
    if flag == 1:
        print("Total Collection on ", date ," is :", sum)


def view_collection_between_specific_dates():
    first = input("Enter first date : ")
    second = input("Enter second date : ")
    obj = open("all_bills.txt", "r")
    ls = obj.readlines()
    i = 0
    j = 0
    while i < len(ls):
        a = ls[i].split(",")
        if first == a[2]:
            break
        i = i + 1
    while i < len(ls):
        a = ls[j].split(",")
        if second == a[2]:
            break
    sum = 0
    while i < j:
        a = ls[i + 1].split(",")
        sum = sum + int(a[2])
        i = i + 1
    print("Total collection between", first, "to" , "second date is  :", sum)


def add_new_employee():
    fobj = open("all_employees.txt", "a")
    fobj.close()
    fobj2 = open("all_employees.txt", "r")
    all_lines = fobj2.readlines()
    emp_id = len(all_lines) + 1
    fobj2.close()

    emp_name = input("Enter Employee Name : ")
    emp_add = input("Enter Employee Address : ")
    emp_mob = input("Enter Employee Mobile No : ")
    emp_aadhar = input("Enter Employee Aadhar No : ")

    a = datetime.date.today()
    emp_jdate = str(a.day) + "-" + str(a.month) + "-" + str(a.year)

    fobj = open("all_employees.txt", "a")
    fobj.write(str(emp_id) + "," + emp_name + "," + emp_add + "," + emp_mob + "," + emp_aadhar + "," + emp_jdate + ",WORKING\n")
    fobj.close()

    print("Employee Added...")

def update_employee_info():
    emp_id = input("Enter Employee ID : ")
    fobj = open("all_employees.txt", "r")
    all_lines = fobj.readlines()
    fobj.close()

    i = 0
    flag = 1
    while i < len(all_lines):
        oneline = all_lines[i]
        ls = oneline.split(",")
        if ls[0] == emp_id:
            print("Select an Option : ")
            print("1 - To Update Name ")
            print("2 - To Update Address")
            print("3 - To Update Mobile No")
            print("4 - To Update Aadhaar No")
            print("5 - To Update Resignation Profile")
            ch = input("Provide your choice : ")

            if ch == "1":
                ename = input("Enter New Name : ")
                ls[1] = ename
                new_str = ",".join(ls)
                all_lines[i] = new_str
                flag = 2
                break

            if ch == "2" :
                eadd = input("Enter New Address : ")
                ls[2] = eadd
                new_str = ",".join(ls)
                all_lines[i] = new_str
                flag = 2
                break

            if ch == "3":
                emob = input("Enter New Mobile No : ")
                ls[3] = emob
                new_str = ",".join(ls)
                all_lines[i] = new_str
                flag = 2
                break

            if ch == "4" :
                eadd = input("Enter New Aadhar No : ")
                ls[4] = eadd
                new_str = ",".join(ls)
                all_lines[i] = new_str
                flag = 2
                break

            if ch == "5":
                rprofile = input("Do you really want to resign (Y/N) : ")
                if rprofile == "Y" or ch == "y":
                    a = datetime.date.today()
                    emp_rdate = str(a.day) + "-" + str(a.month) + "-" + str(a.year)
                    ls[6] = emp_rdate + "\n"
                    new_str = ",".join(ls)
                    all_lines[i] = new_str
                    flag = 2
                    break

        i = i + 1

    if flag == 1:
        print("Invalid Employee Id. No such Employee present")
    if flag == 2:
        fobj3 = open("all_employees.txt", "w")
        fobj3.writelines(all_lines)
        fobj3.close()
        print("Employee Data Updated ")

while True:
    print("\nSelect an option")
    print("1 - Generate Bill")
    print("2 - View Menu")
    print("3 - Add New Dish")
    print("4 - Update Dish Price")
    print("5 - View Today's Collection")
    print("6 - View Collection of Specific Date")
    print("7 - View Collection between Specific Dates")
    print("8 - Add New Employee")
    print("9 - Update Employee Info")
    print("0 - Exit")
    ch = int(input("Provide your choice : "))

    if ch==1: generate_bill()
    elif ch==2: view_menu()
    elif ch==3: add_new_dish()
    elif ch==4: update_dish_price()
    elif ch==5: view_today_collection()
    elif ch==6: view_collection_of_specific_date()
    elif ch==7: view_collection_between_specific_dates()
    elif ch==8: add_new_employee()
    elif ch==9: update_employee_info()
    elif ch==0: exit(0)

