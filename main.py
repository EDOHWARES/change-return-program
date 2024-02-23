cost = ""

while not cost.isdigit() or int(cost) < 10:
    cost = input("What is the cost of the product? ")

    try:
        if int(cost) < 10:
            print("If cost is less than NGN10, you don't need this program!")
        elif not cost.isdigit():
            print("Cost must be a digit!")
    except ValueError:
        print("Cost must be a digit")


amount_given = ""

while not amount_given.isdigit() or int(amount_given) < 10:
    amount_given = input("How much did you give the seller? ")

    if not amount_given.isdigit():
        print("Amount must be a digit!")
    elif int(amount_given) < 10:
        print("If cost is less than NGN10, then you don't need this program!")


def change(given, product_cost):

    in_dollars = f"$-{int(given) - int(product_cost)}"
    in_quarters = f"(¼)-{(int(given) - int(product_cost)) / 4}"
    in_dimes = f"#-{(int(given) - int(product_cost)) / 10}"
    in_nickels = f"Ni-{(int(given) - int(product_cost)) / 20}"
    in_pennies = f"¢-{(int(given) - int(product_cost)) / 100}"

    if int(given) > int(product_cost):
        return f"""
Your change is:
{in_dollars} in dollars
{in_quarters} in quarters
{in_dimes} in dimes
{in_nickels} in nickels
{in_pennies} in pennies
"""
    elif int(given) == int(product_cost):
        return "Product cost is equal amount given, therefore you deserve no change!"
    else:
        return "Amount given is less than product cost!, therefore complete payment."


if __name__ == "__main__":
    print(change(amount_given, cost))
