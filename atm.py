import time
amount=10000
def withdraw():
    global amount
    am=int(input("Enter amount to withdraw:"))
    if am<=amount and am>0:
        if am%100==0:
            print("withdraw success")
            amount=amount-am
            time.sleep(5)
            print("Thanks for using Fraud bank")
        else:
            print("enter only 100multiples")
    else:
        print("invalid amount")
def deposit():
     global amount
     am=int(input("Enter amount to deposit:"))
     amount+=am
     print("total amt:",amount)
     print("deposit success")
def transfer():
    global amount
    am=int(input("Enter amount to transfer:"))
    if am<=10000 :
        print("transfer success")
    else:
        print("insufficient balance")
def balance():
    print(amount)


print("\t\t**Welcome to fraud bank**")
ch=3
while ch>0:
    name=input("enter username:")
    psw=input("enter password:")

    if name=="admin" and psw=="345":
        op=input("Select\n1.withdraw\n2.deposit\n3.transfer\n4.balance")
        if op=='1':
            withdraw()
            break
        elif op=='2':
            deposit()
            break
        elif op=='3':
            transfer()
            break
        elif op=='4':
            balance()
            break
        else:
            print("no option")
            














        
    
        
