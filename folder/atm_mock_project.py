import datetime
import random

accnt = []
pawd = []
data_base = []

def init():
    
    print("*****Welcome to the ABC Bank Limited!*****\nDo you have an account with us?")
    
    ans = input("Yes/No: ")
    
    if ans.lower() == "no":
        
        register()
        
    elif ans.lower() == 'yes':
        
        print("\n******Log in to your ABC bank account******")
        
        login()
        
    else:

        while ans.lower() != 'yes' and ans.lower() != 'no':

            print("Invalid option")

            ans = input("Yes/No: ")

            if ans.lower() == "no":
        
                register()

            elif ans.lower() == 'yes':

                login()

def gen_acc_num():
    
    return random.randrange(1111111111, 9999999999)

def register():
    
    print("\n***Please enter the following details to create your account now!***")
    
    f_name = input("What is your first name?\n")
    
    l_name = input("What is your last name?\n")
    
    email = input("What is your email?\n")
    
    pwd = input("Create a password\n")
    
    conf_pwd = input("Confirm password\n")
    
    while conf_pwd != pwd:
        
        print("Passwords do not match. Make sure passwords match\n")
        
        pwd = input("Create a password\n")
        
        conf_pwd = input("Confirm password\n")
        
    acc_number = gen_acc_num()
    
    accnt.append(acc_number)
    
    pawd.append(pwd)
    
    _dict = {}
    
    _dict[acc_number] = {}
    
    _dict[acc_number]['f_name'] = f_name
    
    _dict[acc_number]['l_name'] = l_name
    
    _dict[acc_number]['email'] = email

    data_base.append(_dict)
    
    print(f"Account has been successfully created!\nYour account number is {acc_number}. \n\nPlease log in to your account.")
    
    login()

def login():
    
    acc_num = input("\nEnter account number\n")
    
    password = input("Enter your password\n")

    count = 0
 
    while acc_num not in accnt and password not in pawd:

        print("Invalid account number and password! Please try again.")
        
        acc_num = input("\nEnter account number\n")
        
        password = input("Enter your password\n")

                   
    print("You are logged in!\n\n")
    
    bank()

def bank():
    
    print("************************************************")
    
    print(datetime.datetime.now().strftime("%A %d %B %Y"))
    
    now = datetime.datetime.now()
    
    print(now.strftime('%I:%M:%S %p\n'))
    
    print(f"******** You are welcome ********")
    
    while True:
        
        print("\nPlease choose your option( To exit choose 4):")
        
        print("1. Withdrawal")
        
        print("2. Cash Deposit")
        
        print("3. Complaint")
        
        print("4. Exit")

        choice = int(input("\nOption: "))

        balance = 0

        if choice == 4:
            
            break
        
        else:
            
            if choice == 1:
                
                print("\nYou selected option 1.\nHow much would you like to withdraw?")
                
                withdrawn = int(input("Amount: "))
                
                print(f"Take your cash!\nYour Current balance is {balance}")
                
            elif choice == 2:
                
                print("\nYou selected option 2.\nHow much would you like to deposit?")
                
                deposit = int(input("Amount: "))
                
                balance += deposit
                
                print(f"Cash deposited!\nYour Current balance is {deposit}")
                
            elif choice == 3:
                
                print("\nWhat issue will you like to report?")
                
                issue = input("Issue: ")
                
                if issue:
                    
                    print("Thank you for contacting us. We will get back to you!")
                    
                else:
                    
                    pass

    
init()
