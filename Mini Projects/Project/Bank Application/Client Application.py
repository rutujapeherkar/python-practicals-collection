
def check_balance():
    '''
	accept account number and pin number
	if both matches then display current balance
    '''
    acc_num = input("Enter Account Number : ")
    pin_num = input("Enter Pin Number :")

    fobj = open("all_accounts.txt", "r")
    for oneline in fobj:
        ls = oneline.split(",")

def transfer_amt():
    '''
	accept account number and pin number
	if both matches then accept account number of
	receiver. Send amount.
	Before transferring, check sufficient balance
    '''

def change_pin():
    '''
	accept account number and pin number
	if both matches then:
		accept new pin
		re-enter new pin
	if both matches, then update original pin
    '''

def view_transaction_history():
   '''
	accept account number and pin number
	if both matches then display last 10 transactions
    '''

def view_account_info():
    '''
	accept account number and pin number
	if both matches then display account information
	like account holder's name, accout balance,
	address, mobile number, email, etc...
    '''

while True:
    print("1 - Check Balance")
    print("2 - Transfer Amount")
    print("3 - Change PIN")
    print("4 - View Transaction History")
    print("5- View Account Information")
    print("6 - EXIT")
    ch = int(input("Provide your choice : "))
    if ch==1: check_balance()
    elif ch==2: transfer_amt()
    elif ch==3: change_pin()
    elif ch==4: view_transaction_history()
    elif ch==5: view_account_info()
    elif ch==6: exit(0)

