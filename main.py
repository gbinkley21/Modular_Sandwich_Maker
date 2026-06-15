# Gavin Binkley
# 6/14/2026
import data
from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()




def main():
    machine_is_on = True
    while machine_is_on:
        choice = input("What would you like? (small/medium/large/report/off):").lower()
        if choice == "off":
            machine_is_on = False
        elif choice == "report":
            print(f"Bread: {resources['bread']}slice(s)")
            print(f"Ham: {resources['ham']}slice(s)")
            print(f"Cheese: {resources['cheese']}ounce(s)")
        elif choice in recipes:
            sandwich = recipes[choice]

            if sandwich_maker_instance.check_resources(sandwich['ingredients']):
                payment = cashier_instance.process_coins()

                if cashier_instance.transaction_result(payment, sandwich['cost']):

                    sandwich_maker_instance.make_sandwich(choice, sandwich['ingredients'])

if __name__=="__main__":
    main()