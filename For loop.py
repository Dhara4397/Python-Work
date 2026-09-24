
#for in
for i in range(1,11):
    print(i)


#start from 0 if not start from 1,2
for a in range (10):
    print(a)

#while
# (< always add +) and (> always add -)
j=1
while j <=5:
    print(j)
    j=j+1


k=5
while k >=1:
    print(k)
    k=k-1


for i in range(1,5):  #row
    for j in range(1,5): #column
        print("*",end='')
    print()


for i in range(1,5):  #row
    for j in range(1,i+1): #column
        print("*",end='')
    print()

