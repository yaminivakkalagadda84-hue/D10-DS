num=1
while num<=5:
    print(num)
    num+=1
count=10
while count>0:
    print(count)
    count-=1
while False:
    print('yamini')
num=2
while num<=10:
    print(num)
    num+=2
num=10
while num>=1:
    print(num)
    num-=1
i=1
while i<=10:
    print(f"5 x {i}={5*i}")
    i+=1
x=int(input('enter the value:'))
while x>=0:
    if x%2==0:
        print("even number")
    else:
        print("odd number")
print(x)
num=int(input('enter the value:'))
num1=num
rev=0
while num>0:
    ld=num%10
    print(ld)
    num=num//10
    print(rev)
    if rev==num1:
        print("it is a palindrome")
    else:
        print("it is not palindrome")
