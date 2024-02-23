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

    if int(given) > int(product_cost):
        return f"Your change is NGN{int(given) - int(product_cost)}"
    elif int(given) == int(product_cost):
        return "Product cost is equal amount given, therefore you deserve no change!"
    else:
        return "Amount given is less than product cost!, therefore complete payment."


if __name__ == "__main__":
    print(change(amount_given, cost))
