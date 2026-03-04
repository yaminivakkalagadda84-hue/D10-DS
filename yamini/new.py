x=int(input('enter the value:'))
x1=x
rev=0
while x>0:
    id=x%10
    rev=rev*10+id
    x=x//10
    print(rev)
    if rev==x1:
        print("it is palindrome")
    else:
        print("it is not palindrome")

