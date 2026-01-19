header = """\tBOOKSTORE RECEIPT
\t------------------"""

item_line = "\n\tBook Title: {}\t₹{}"

item1 = item_line.format("Python Basics", 450)
item2 = item_line.format("Data Science Intro", 600)

total_price = 450 + 600
total_line = "\n\tTotal Amount:\t₹{}".format(total_price)

thank_you = "\n\n\tThank you for shopping with us!"

receipt = header + item1 + item2 + total_line + thank_you

print(receipt.upper())
