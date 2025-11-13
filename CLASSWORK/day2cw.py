
header = "RECEIPT\n\tBOOKSTORE - THANK YOU FOR YOUR PURCHASE\n"

item1 = "\tBOOK TITLE: {}\t– ₹{}\n".format("Python Basics", 450)
item2 = "\tBOOK TITLE: {}\t– ₹{}\n".format("Data Science Intro", 600)

total = "\tTOTAL:\t\t₹{}\n".format(450 + 600)

thank_you = "\n\tWE APPRECIATE YOUR BUSINESS. PLEASE VISIT AGAIN!"

receipt = header + item1 + item2 + total + thank_you

print(receipt.upper())