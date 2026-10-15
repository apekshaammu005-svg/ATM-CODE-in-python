import time

password = 1234
balance = 20000

print("WELCOME TO ABC BANK")
print("insert the card")
print("press 1. yes 2. no")
card = int(input())

if card == 1:
    print("select your language")
    print("press 1. english 2. kannada 3. hindi")
    lang = int(input())

    if lang == 1:
        print("enter your pin")
        pin = int(input())

        if pin == password:
            print("select the option")
            print("press 1. balenq 2. withdraw 3. deposit")
            choice = int(input())

            if choice == 1:
                print("your available balance is", balance)

            elif choice == 2:
                print("enter the amount (multiples of 100 only)")
                amt = int(input())


                if amt <= 0 or amt % 100 != 0:
                    print("invalid amount! Must be a positive multiple of 100.")
                elif amt > balance:
                    print("\ntransaction failed !! Insufficient balance.")
                else:

                    balance -= amt

                    print("your transaction is processing....")
                    time.sleep(5)
                    print("pls collect your cash !!")
                    time.sleep(4)

                    print("do you want to check your balance")
                    print("press 1. yes 2. no")
                    choice1 = int(input())

                    if choice1 == 1:
                        print("your available balance is", balance)

                    print("thank you visit again!!")
            elif choice==3:
                print("enter the amount to deposit(multiple by 100 only)")
                dep_amt=int(input())
                if dep_amt<=0 or dep_amt%100!=0:
                    print("invaild amount ! deposit amount must be multiple by 100 ")
                else:
                    print("pls place your cash inside...")
                    time.sleep(4)
                    print("cash is received and processing...")
                    time.sleep(3)
                    balance+=dep_amt
                    print("deposited successfully!!")
                    print("do ypu want check your balance?")
                    print("1. yes 2. no")
                    choice2=int(input())
                    if choice2==1:
                        print("your balance is",balance)
                    else:
                        print("thank you visit again")

            else:
                print("invalid choice")

        else:
            print("pls enter correct password")

    else:
        print("please select only english")
else:
    print("please insert your card properly")