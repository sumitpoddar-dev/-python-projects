 # ACCOUNT BALANCE WITHDRAW AND CHECK

balance = int(input(" enter your balance"))
withdraw = int(input("enter withdraw amount"))

if withdraw<=0:

    print("invalid withdraw amount")
elif withdraw <= balance:

    print("withdraw successful")
    print("available balance ", balance - withdraw)

else:
    print("withdraw uncsuccessful")

 