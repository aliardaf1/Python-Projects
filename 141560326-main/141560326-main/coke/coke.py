amount =50
while amount>0:
    print("Amount Due: " ,amount , sep="")
    inserted = (int)(input("Insert Coin: "))
    if (inserted == 5 or inserted == 10 or inserted == 25):
        amount = amount - inserted

if amount < 0 :
    amount = amount*(-1)
print("Change Owed: " ,amount , sep ="")
