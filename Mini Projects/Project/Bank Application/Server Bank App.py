# server application

def view_acc_info():
    acc_num = input("Enter Account Number to view Account Information : ")
    fobj = open("all_accounts.txt", "r")
    flag = 1
    for oneline in fobj:
        ls = oneline.split("~")
        if ls[0] == acc_num:
            flag = 2
            print("Account Holder Name : " + ls[3])
            print("Account Balance : " + ls[2])
            print("Mobile Number : " + ls[4])
            print("Email Id : " + ls[5])
            print("Address : " + ls[6], end = " ")

    if flag == 1:
        print("Invalid Account Number. No such record found.")
    fobj.close()

def withdrawal():
    acc_num = input("Enter Account Number : ")
    wamt = int(input("Enter Amount to Withdraw : "))

    fobj = open("all_accounts.txt", "r")
    all_lines = fobj.readlines()

    i = 0
    flag = 1
    for oneline in all_lines:
        ls = oneline.split("~")
        if ls[0] == acc_num:
            if wamt > int(ls[2]):
                print("Insufficient Balance in Account")
                flag = 2
                break
            elif wamt < int(ls[2]):
                ls[2] = str(int(ls[2]) - wamt)
                new_str = "~".join(ls)
                all_lines[i] = new_str
                print(str(wamt) + " withdrawn successfully")
                flag = 2
                break

    fobj.close()

    if flag == 1:
        print("Invalid Account Number.No such record found.")
    if flag == 2:
        fobj = open("all_accounts.txt", "w")
        fobj.writelines(all_lines)
        fobj.close()

def deposit():
    acc_num = input("Enter Account Number : ")
    
    fobj = open("all_accounts.txt", "r")
    all_lines = fobj.readlines()

    i = 0
    flag = 1
    for oneline in all_lines:
        ls = oneline.split("~")
        if ls[0] == acc_num:
            if wamt > int(ls[2]):
                print("Insufficient Balance in Account")
                flag = 2
                break
            elif wamt < int(ls[2]):
                ls[2] = str(int(ls[2]) - wamt)
                new_str = "~".join(ls)
                all_lines[i] = new_str
                print(str(wamt) + " withdrawn successfully")
                flag = 2
                break

    fobj.close()

def fine_to_min_account():
    pass

def credit_interest():
    pass

def create_new_account():
    import random
    ipin = random.randint(1111,9999)
    nm = input("Enter Account Holder Name : ")
    ibal = input("Enter Initial Balance : ")
    mob = input("Enter Mobile Number : ")
    email = input("Enter Email Address : ")
    addr = input("Enter Address : ")

    fobj = open("all_accounts.txt", "r")
    fdata = fobj.readlines()
    accnum = len(fdata) + 1
    fobj.close()

    fobj = open("all_accounts.txt", "a")
    fobj.write(str(accnum) + "~" + str(ipin) + "~" + ibal + "~" + nm + "~" + mob + "~" + email + "~" + addr + "\n" )
    fobj.close()

    fobj = open("ac" + str(accnum) + ".txt", "w")
    fobj.close()

    print("New Account Opening Successful..")
    print("Kindly Note your PIN : ", ipin)
    print("You are requested to change PIN immediately")

def configuration():
    fobj1 = open("all_accounts.txt", "a")
    fobj1.close()

configuration()
while True:
    input()
    print("1 - Create New Account")
    print("2 - Credit Interest")
    print("3 - Fine to Minimum Balance")
    print("4 - Deposit")
    print("5 - Withdrawal")
    print("6 - View Account Information")
    print("7 - EXIT")
    ch = int(input("Provide your choice : "))
    if ch==1: create_new_account()
    elif ch==2: credit_interest()
    elif ch==3: fine_to_min_account()
    elif ch==4: deposit()
    elif ch==5: withdrawal()
    elif ch==6: view_acc_info()
    elif ch==7: exit(0)
