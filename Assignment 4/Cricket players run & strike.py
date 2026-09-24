print('1.Excellent,2.Good')
run=int(input("Enter your run: "))
strike_rate=int(input("Enter your strike rate: "))
if run>50 and strike_rate>120:
    print("Excellent")

elif run>30 and strike_rate>100:
    print("Good")

else:
    print("Need to improvement")