import json

# reading the file to start the sales
fd = open("record.json", "r")
txt = fd.read()
fd.close()

record = json.loads(txt)

# print(record)

prod_id = str(input("Enter product id: "))
name = str(input("Enter name of the product: "))
price = str(input("Enter price in Rs.: "))
ram = str(input("Enter ram: "))
quantity = int(input("Enter quantity : "))
resolution = str(input("Enter resolution of the product: "))
battery_type = str(input("Enter battery type: "))
storage = str(input("Enter storage in GB: "))

if prod_id in record.keys():
    record[prod_id]['quantity'] = int(record[prod_id]['quantity']) + quantity


record[prod_id] = {'name': name, 'price': price, 'ram': ram, 'quantity': quantity, 'resolution': resolution, 'battery_type': battery_type, 'storage': storage}
print(record)

# saving into json file
js = json.dumps(record)

fd = open("record.json", "w")
fd.write(js)
fd.close()
