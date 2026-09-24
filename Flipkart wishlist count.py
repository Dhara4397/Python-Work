wishlist_count=input("Enter your wishlist count: ")

wishlist_count=int(wishlist_count)

if wishlist_count >= 1000:
    wishlist_count = f"{wishlist_count / 1000:.1f}K"
else:
    wishlist_count = f"{wishlist_count}"

print("Your wishlist count is", wishlist_count)




