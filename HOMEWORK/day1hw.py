import random
price_rice = 45.0
price_sugar = 40.0
price_oil = 130.0

qty_rice = 3.0
qty_sugar = 2.5
qty_oil = 1.8

total_rice = price_rice * qty_rice
total_sugar = price_sugar * qty_sugar
total_oil = price_oil * qty_oil
total_bill = total_rice + total_sugar + total_oil

total_bill_int = int(total_bill)
total_bill_str = str(total_bill_int)

delivery_charge = random.randint(5, 10)
final_bill = total_bill_int + delivery_charge

print("Total for Rice: ₹", int(total_rice))
print("Total for Sugar: ₹", int(total_sugar))
print("Total for Oil: ₹", int(total_oil))
print("Total Bill (before delivery): ₹", total_bill_int)
print("Total Bill as String: '" + total_bill_str + "'")
print("Delivery Charge: ₹", delivery_charge)
print("Final Bill (including delivery): ₹", final_bill)