class Cashier:
    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")

        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = large_dollars * 1.00
        total += half_dollars * 0.50
        total += quarters * 0.25
        total += nickels * 0.05

        return total

    def transaction_result(self, coins, cost):
        if coins < cost:
            print("Sorry there is not enough money. Money refunded.")
            return False
        else:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True