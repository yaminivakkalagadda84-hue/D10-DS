for i in range(1,21):
    if i%3==0:
        print(f"{i}---- fizz")
for j in range(1,21):
    if j%5==0:
        print(f"{j}---buzz")
for k in range(1,21):
    if k%3==0 & k%5==0:
        print(f"{k}----fizzbuzz")