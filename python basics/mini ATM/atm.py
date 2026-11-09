# def withdraw(balance, amount):
#     if amount<=0:
#         raise ValueError("Enter correct amount")
#     elif amount>balance:
#         raise ValueError("Insufficient balance")
#     else:
#         return balance-amount
# def atm():
#      try:
#         balance=10000
#         opin="1234"
#         pin=input("ENter pin: ")
#         if pin==opin:
#             print("Welcome!")
#         else:
#             raise ValueError("Incorrect PIN!")
#         amount=input("Enter withdraw amount")
#         balance=withdraw(balance,amount)
        
#      except ValueError as e:
#         print("Error",e)
#      else:
#             print("Successfully withdraw")
#             print("Remaining balance: ",balance)
#      finally:
#             print("Thank you for using ATM")
            
# atm()
        
          



def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Enter correct amount")

    elif amount > balance:
        raise ValueError("Insufficient balance")

    else:
        return balance - amount


def atm():
    
        while True:
            try:
             balance = 10000
             opin = "1234"

             pin = input("Enter PIN: ")

             if pin == opin:
              print("Welcome!")
             else:
              raise ValueError("Incorrect PIN!")

             amount = float(input("Enter withdrawal amount: "))

             balance = withdraw(balance, amount)

            except ValueError as e:
             print("Error:", e)

            else:
             print("Successfully withdrawn!")
             print("Remaining balance:", balance)

            finally:
                print("ATM transaction attempt finished!")
        print("Thank you for using ATM!")
exit


atm()
