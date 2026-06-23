import datetime
products = {
    1:{"name":"Laptop", "price": 50000},
    2:{"name":"Keyboard", "price": 3000},
    3:{"name":"Mouse","price":2000},
    4:{"name":"Cables","price":200},
    5:{"name":"Mobile","price":10000},
    6:{"name":"HeadSet", "price":2000}
}
cart =[]
total_amount = 0
print("--------------WELCOME TO E-COMMERS STORE---------------")

#Display Prodcuts
for key,value in products.items():
    print(f"{key}.{value['name']}- Rs.{value['price']}")
while True:
    choice = int(input("\nEnter your choice(0 to exit)"))
    if choice == 0:
        break
    if choice in products:
        qty = int(input("\nEnter your quantity:"))
        product_name = products[choice]['name']
        price = products[choice]['price']
        total = price * qty
        
        cart.append((product_name,qty,price,total))
        total_amount +=total
        print(f"Added {product_name} * {qty}")
    else:
        print("Invalid Choice")

#Generate Invoice
print("--------------------Invoice----------------------")

print(f"{'Item':<12}{'Qty':<8}{'Price':<10}{'Total':<10}")
for item in cart:

    print(f"{item[0]:<12}{item[1]:<8}{item[2]:<10}{item[3]:<10}")
print("---------------------------------------------------")
print(f"Total Amount:{total_amount}")

#Save to a file
with open("invoice.txt","a") as file:
    file.write("\n--------Invoice-----------\n")
    file.write(str(datetime.datetime.now())+"\n")
    file.write(f"{'Item':<12}{'Qty':<8}{'Price':<10}{'Total':<10}\n")
    for item in cart:
        file.write(f"{item[0]:<12}{item[1]:<8}{item[2]:<10}{item[3]:<10}\n")
    file.write(f"Total Amount:{total_amount}\n")
    file.write("------------------------------")
print("\n Invoice saved to file")