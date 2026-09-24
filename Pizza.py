print('1.small(150) 2.medium(250) 3.Large(500)')
choice=int(input("Enter your size: "))
qty=int(input("Enter your quantity: "))
match choice:
    case 1:
        bill=qty*150
        print(bill)
    case 2:
        bill=qty*250
        print(bill)

    case 3:
        bill=qty*500
        print(bill)

    case _:
        print("invalid choice")


#small = 4 -> offer 500 ml coke free
#medium = 2 -> offer 1 ltr coke free
#large = 2 -> offer 1 ltr coke + ice cream
