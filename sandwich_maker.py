### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}



class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print("Please insert coins.")

        large_dollars = int(input("How many large dollars?: "))
        half_dollars = int(input("How many half dollars?: "))
        quarters = int(input ("How many quarters?: "))
        nickels = int(input("How many nickels?: "))

        total = large_dollars * 1.00
        total += half_dollars * 0.50
        total += quarters * 0.25
        total += nickels * 0.05

        return total

    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins < cost:
            print("Sorry there is not enough money. Money Refunded")
            return False
        else:
            change = round(coins-cost, 2)
            print(f"Here is ${change} in change.")
            return True


    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]

        print(f"{sandwich_size} Sandwich is ready. Enjoy!")



sandwich_machine = SandwichMachine(resources)
machine_is_on = True
while machine_is_on:
    choice = input("What would you like?: (small/medium/large/off/report): ").lower()

    if choice == "off":
        machine_is_on = False
    elif choice == "report":
        print(f"Bread: {sandwich_machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {sandwich_machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {sandwich_machine.machine_resources['cheese']} pound(s)")
    elif choice == "small" or choice == "medium" or choice == "large":
        sandwich = recipes[choice]

        if sandwich_machine.check_resources(sandwich["ingredients"]):
            payment = sandwich_machine.process_coins()

            if sandwich_machine.transaction_result(payment, sandwich["cost"]):
                sandwich_machine.make_sandwich(choice, sandwich["ingredients"])

    else:
        print("Invalid choice. Please choose small, medium, large, report, or off.")