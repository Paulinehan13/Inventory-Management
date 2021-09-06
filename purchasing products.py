import json

# reading the file to start the sales
fd = open("record.json", "r")
txt = fd.read()
fd.close()

record = json.loads(txt)
# print(record)

prod_id = str(input("Enter product id: "))
quantity = int(input("Enter quantity : "))
name = str(input("Enter customer name: "))

if prod_id in record.keys():
    if int(record[prod_id]['quantity']) <= 0:
        print("product not in stock")
    elif int(record[prod_id]['quantity']) < quantity:
        print("only", int(record[prod_id]['quantity']), "is available")
    else:
        record[prod_id]['quantity'] = int(record[prod_id]['quantity']) - quantity
        # BILL
        product = record[prod_id]['name']
        price = record[prod_id]['price']
        billing_amount = int(record[prod_id]['price']) * quantity
        print("_____________________________________________\n")
        print("Product Name: ", product)
        print("Price of a product: ", price)
        print("Quantity purchased: ", quantity)
        print("_____________________________________________\n")
        print("Billing Amount: Rs. ", billing_amount)
        print("______________________________________________\n")
        print("Thank you for your purchase.")
        print("Have a Nice Day!!")

        # updating into sales json file
        fs = open("sales.json", "r")
        sale = fs.read()
        fs.close()
        sales = json.loads(sale)
        sales[len(sales) + 1] = {'prod': prod_id, 'quantity': quantity, 'billing_amount': billing_amount, 'customer_name': name}
        # print(sales)

        jss = json.dumps(sales)
        fs = open("sales.json", "w")
        fs.write(jss)
        fs.close()
else:
    print("Invalid product id")

# print(record)

# updating into  record json file
js = json.dumps(record)

fd = open("record.json", "w")
fd.write(js)
fd.close()
