#defining function to find cost of shipping
def shipping_cost(number_of_items):
    total_shipping_cost = 10.95 + (2.95 * (number_of_items - 1))
    return total_shipping_cost

#reading input to find number of items
n = input("Please enter the number of items purchased: ")
if n.isalpha() == True:
    print("Please input an integer.")
    exit()
elif float(n) % 1 != 0:
    print("Please input an integer.")
    exit()
elif float(n) <= 0:
    print("Please input an integer.")
    exit()
else:
    n = int(n)
shipping_cost = float(shipping_cost(n))
shipping_cost = round(shipping_cost, 2)

print("The shipping charge is $" + str(shipping_cost))