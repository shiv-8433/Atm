import time

print("Plese insert your Card")

time.sleep(4)

password=1234

pin=int(input("enter your Atm pin"))

balance=10000

if pin== password:
   
    print(""" 
          1 == Balance inq
          2 == Cash withdraw 
          3 == Deposit amount
          4 == Exit
         """
          )
    
    try:
        option=int(input("please enter your choise"))
    except:
        print("please enter valid option")

    
    if option==1:
        print(f"your current balance is{balance}")

    if option==2:
        withdraw_amount=int(input("plese enter withdraw_amount "))

        balance=balance-withdraw_amount

        print(f"{withdraw_amount} is debited from your account")
        print(f"your current balance is{balance}")


    if option==3:
        deposit_amount=int(input("please enter deposit_amount"))

        balance=balance+deposit_amount

        print(f"{deposit_amount}iscredit your account")

        print(f"your current balance is{balance}")

    if option==4:
       
        "break"

    

else:
    print("Your pin number is wrong please try again")