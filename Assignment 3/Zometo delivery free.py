order_price=input("Enter the zometo order price:")

#convert variable in flot
order_price=float(order_price)

#10% delivery free
delivery_fee= order_price*0.10

final_bill = order_price+delivery_fee

print("Your final bill is",final_bill)

