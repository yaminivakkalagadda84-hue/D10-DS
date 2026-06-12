d={i:i for i in range(1,11)}
print(d)
d={i:i**2 for i in range(1,11)}
print(d)
d={i:i**3for i in range(1,11)}
print(d)
names=["a","bb","ccc"]
d={i:len(i)for i in names}
print(d)
d={i for i in range(1,11) if i%2==0 }
print(d)
words='mississippi'
d={i:words.count(i)for i in words}
print(d)
things={"pen":10,"book":120,"bag":700,"eraser":5}
d={k:v for k,v in things.items() if v>100}
print(d)
lst=[1,2,3,4,5,6,7,8]
d={i:i**2 for i in lst if i%2!=0}
print(d)
names=['apple','hi','banana','cat','elephant']
d={i:len(i)for i in names}
print(d)
dict={'x':1,'y':2,'z':3}
d= {v:k for k,v in dict.items()}
print(d)
marks={'ram':28,'sam':45,'tom':90}
d={k:'pass' if v>35 else 'fail' for k,v in marks.items()}
print(d)
lst=[1,1,2,2,2,3,3]
d={i:lst.count(i)for i in lst}
print(d)
s="python makes coding fun"
d={i:len(i)for i in s.split()}
print(d)