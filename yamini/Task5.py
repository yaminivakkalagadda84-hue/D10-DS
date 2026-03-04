num=int(input('enter the value:'))
num1=num
rev=0
while num>0:
    id=num%10
    rev+=id**3
    num=num//10
    print(rev)
    if rev==num:
        print("it is armstrong number")
    else:
        print("it is not a armstrong number")