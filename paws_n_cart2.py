print("Welcome To the Valentina's Shopping Cart")
print()

petFoodItems = ["Cat nip", "Dog Leash","Fish Food","Bird Seeds", "Hamster Wheel"]
price = [25.5, 28.75, 20.22, 15.5, 35.5]

print("ITEM", "PRICE(GBP), excl Tax", sep= "\t\t\t")
for i in range(len(petFoodItems)):
    print(str(i+1)+ "." + petFoodItems[i], price[i], sep="\t\t")

print()

shopping_complete = 0

shopping_cart = []
shopping_quant = []

while shopping_complete == 0:
    order = int(input("Enter 1 to 5 to select a pet food item, 6 to proceed to checkout\n"))    

    if order <= 5:
        print("User is shopping")
        print("You selected", petFoodItems[order-1])
        quant = int(input("How many units do you wish to purchase\n"))

        if petFoodItems[order-1] in shopping_cart:
            print("Repeated selection")
            idx = shopping_cart.index(petFoodItems[order-1])
            print(idx)
            shopping_quant[idx] += quant
        else:
            print("New selection")
            shopping_cart.append(petFoodItems[order-1])
            shopping_quant.append(quant)
    elif order == 6:
        print("Proceeding to checkout")
        shopping_complete = 1
    else:
        print("Invalid input")

print()
print("Shopping is complete, displaying shopping cart")

print()
print("ITEM ", "QUANT", "\b\b\b\b\b\b\b\bUNIT PRICE", "\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\bTOTAL", sep =" \t\t\t" )
for i in range(len(shopping_cart)):
    idx = petFoodItems.index(shopping_cart[i])
    unit_price = price[i]
    total_price = round(shopping_quant[i] * unit_price, 2)
    print(shopping_cart[i], shopping_quant[i], unit_price, total_price, sep =" \t\t")








