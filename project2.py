list_items=[]
def add_items():
 name=input("enter your item name")
 price=float(input("enter price"))
 new_item={'name':name,'price':price}
 list_items.append(new_item)
 print("item '{}' with price '{}' is inserted".format(name,price))
def show_items():
   if not list_items:
    print(" your list is empty")
   else:
    print("your items is ")
    for i ,item in enumerate(list_items,1) :
        print("{} .{}-Rs{}".format(i,item['name'],item['price'])) 
      
def delete_items():
   n=int(input("enter index no for item which is deleted"))
   if 1<=n<=len(list_items):
    delete_items=list_items.pop()
    print(n)
    print(delete_items['name'])
    print(delete_items['price'])
   else:
    print("your index item not found......") 


def update_items():
    n=int(input("enter index no for item which is deleted"))
    if 1<=n<=len(list_items):
     name1=input("enter updated name")
     price1=float(input("enter updated price"))
     item=list_items[n-1]
     item['name']=name1
     item['price']=price1
     print("{} .{}-Rs{}".format(n,item['name'],item['price'])) 
    else:
        print("item not found")  

while True:
    print("\nMenu")
    print("1.insert data")
    print("2:show data")
    print("3.update data")
    print("4:delete data")
    print("5:exit")
    choice=input("Enter your choice ")
    if choice=='1':
        add_items()
    elif choice=='2':
        show_items() 
    elif choice=='3':
        update_items()  
    elif choice=='4':
        delete_items() 
    elif choice=='5':
        print("yoy are exit from operations")
        break
    else:
        print("invalid choice")
    ans=input("Do you want to continue.....")
    if(ans.lower()!='y'):
        break    





