#Define the menu of Cafe
menu = {
    '1':150,
    '2':80,
    '3':90,
    '4':60,
    '5':50
}
#Greet
print("\n---WELCOME TO OUR CAFE---\n")
print("1. Biriyani: ₹150\n2. Chawmin: ₹80\n3. Pizza: ₹90\n4. Momo: ₹60\n5. Coffee: ₹50")

order_total = 0

item_1 = input("Choose a number what You want to Order = ")

#Set Conditions
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Dish {item_1} added in your Order List")
else:
    print(f"Ordered item {item_1} is not available yet!")

another_order = input("Do you want to Order another Dish? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Choose another Dish number = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Dish {item_2} added in your Order List")
    else:
        print(f"Ordered item {item_2} is not available!")

print(f"Total Amount {order_total}")