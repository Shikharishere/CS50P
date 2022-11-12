accepted_coins = [25, 10, 5]
amount_due = 50

print("Amount Due: 50")

while True:

    coin = int(input("Insert Coins: "))
    if coin in accepted_coins:
        amount_due -= coin
        if amount_due == 0:
            print(f"Change owed: {amount_due}")
            break
        else:
            print(f"Amount owed: {amount_due}")
    else:
        print(f"Amount due: {amount_due}")
        continue