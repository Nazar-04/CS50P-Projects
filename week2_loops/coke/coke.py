def main():
    amount_due = 50
    valid_coins = [25, 10, 5]

    while amount_due > 0:
        print(f"Amount Due: {amount_due}")
        coin = int(input("Insert Coin: "))

        if coin in valid_coins:
            amount_due -= coin
        else:
            print("Invalid coin")

    print(f"Change Owed: {abs(amount_due)}")

main()
