fruits=["apple","banana","cherry"]
vegetables=["carrot","broccoli","spinach"]
beverages=["water","juice","soda"]
fruits.append("orange")
vegetables.insert(1,"cabbage")
beverages.remove("soda")
inventory=[fruits,vegetables,beverages]
first_two_fruits=fruits[0:2]
print(first_two_fruits)
last_vegetable=vegetables[-1]
print(last_vegetable)
fruit_lengths = [len(fruit) for fruit in fruits]
print("Lengths of fruit names:", fruit_lengths)
yes = "Water" in beverages
print("Is 'Water' in beverages?", yes)
first_items_tuple = (fruits[0], vegetables[0], beverages[0])
print("Tuple of first items:", first_items_tuple)

