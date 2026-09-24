print('1.small(150) 2.medium(250) 3.Large(500)')
size=int(input("Enter your size: "))
qty=int(input("Enter your quantity: "))
match size:
    case 1 if qty>3:
        bill=qty*150
        print(bill)
        print('offer:500 ml coke free')

    case 2 if qty >1:
        bill = qty * 250
        print(bill)
        print('offer:1ltr coke free')

    case 2 if qty>1:
        bill = qty * 500
        print(bill)
        print('offer:1 ltr coke free and Ice cream')

    case _:
        print("offer not available ")


#small = 4 -> offer 500 ml coke free
#medium = 2 -> offer 1 ltr coke free
#large = 2 -> offer 1 ltr coke + ice cream
