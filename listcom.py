''' list comprehesion---it is use make program length shorter(make code shorter)
in that create new list  with the help of another list'''
lang=["java","python","WD","SQL","oracle"]
newlist=[]
for x in lang:
    if "a" in x:
        newlist.append(x)
print(newlist)      

#by using list comprehesion 
#synatx:[expression for item in iterable if coondition=True]
lang1=["java","python","WD","SQL","oracle"]
newlist1=[x for x in lang1 if "a" in x]
print(newlist1)

num=[1,2,3,4,5]
numlist=[ x*2 for x in num]
print(numlist)