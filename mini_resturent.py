print("----welcome to restaurant----")
Name = str(input("Pleas enter your name : "))
number = int(input("Enter your phone number:" ))

food_items = {
    "A1": ("Biryani", 250),
    "A2": ("Burger", 300),
    "A3": ("Karahi", 800),
    "A4": ("Kebab", 150),
    "A5": ("Pizza", 540),
    "A6": ("Steak", 900),

    "B1": ("Samosa", 50),
    "B2": ("French Fries", 150),
    "B3": ("Chaat", 100),
    "B4": ("Chicken Roll", 180),
    "B5": ("Nuggets", 200),

    "C1": ("Naan", 30),
    "C2": ("Roti", 20),
    "C3": ("Paratha", 60),
    "C4": ("Fried Rice", 250),

    "D1": ("Ice Cream", 100),
    "D2": ("Gulab Jamun", 50),
    "D3": ("Cake", 150),
    "D4": ("Waffles", 200)
}

print("------------------------------------ A.Main Dishes--------------------------------------")  

print(  "A1.Biryani\n ",
        "A1.Burger\n ",
        "A3.Karahi\n ",
        "A4.Kebab\n ",
        "A5.Pizza\n ",
        "A6.Steak\n ")

print("------------------------------------B.street food snackes-------------------------------")

print(  "B1.Samosa\n",
        "B2.French Fries\n",
        "B3.Chaat\n",
        "B4.Chicken Roll\n",
        "B5.Nuggets\n"
        )

print("------------------------------------C.Drain Gains-----------------------------------------")

print(  "C1Naan\n",
        "C2.Roti\n",
        "C3.Paratha\n",
        "C4.Fried Rice\n")

print("----------------------------------D.desserts sweets----------------------------------------")

print(  "D1.Ice Cream\n",
        "D2.Gulab Jamun\n",
        "D3.Cake\n",
        "D4.Waffles\n")
print("--------------------------------end of menu ----------------------------------------------")


total_bill = 0

while True:

    order = input("Enter food code (e.g. A1): ").upper()

    if order in food_items:

        food, price = food_items[order]

        quantity = int(input("Enter quantity: "))

        item_total = price * quantity
        total_bill = total_bill + item_total

        print("You ordered:", food)
        print("Item total:", item_total)

    else:
        print("Sorry, this item is not available")
        continue

    choice = input("Do you want to order more? (yes/no): ").lower()

    if choice == "no":
        break

ammount = int(input("Enter your payment amount: "))

final = ammount - total_bill

print("\n---------- FINAL BILL ----------")
print("------------------------")
print("Customer:", Name) 
print("------------------------")
print("Total bill:", total_bill)
print("------------------------")
print("Amount paid:", ammount)
print("------------------------")

if final >= 0:
    print("------------------------")
    print("Remaining charges:", final)
else:
    print("Amount still due:", abs(final))


print("Thank you", Name, "for choosing our restaurant!")

print("------------------------")
import datetime

while True:
    now = datetime.datetime.now()

    print("Date:", now.strftime("%d-%m-%Y"))
    print("Time:", now.strftime("%I:%M:%S %p"))

    break  