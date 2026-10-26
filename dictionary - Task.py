d1={
    1:"C",
    2:"C++",
    3:"Python",
    4:"Java"
}
print(d1)

match =str(input("Enter the value:"))
if match in d1.values():
    print("Value matched",match)
else:
    print("Value not matched")
    choice=(input("Do you want to add this value?(yes/no):"))

    if choice=="yes":
        print("Value added")
        new_key=max(d1.keys())+1
        d1[new_key]=match
        print("new value added successfully")
        print(d1)
    else:
       print("Thank you")




