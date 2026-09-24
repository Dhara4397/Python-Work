product_price=499
discount=50
is_flash_sale='True'

product_price = int(product_price)
is_flash_sale = bool(is_flash_sale)


final_price=product_price - discount

print("Product Price:", product_price)
print("Discount:", discount)
print("Flash Sale:", is_flash_sale)
print("final price" ,  final_price)
