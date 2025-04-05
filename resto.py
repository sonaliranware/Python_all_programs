options={1:"breakfast",2:"lunch",3:"dinner",4:"desert",5:"drink",6:"main menu",7:"quit"}
breakfast={1:"sandwich",2:"poha",3:"pasta",4:"Cereal",5:"Avocado Toast"}
lunch={6:"pizza",7:"burger",8:"salsa jam",9:"paneer chilli",10:"chicken wings"}
dinner={11:"dal rice",12:"indian thali",13:"kashmiri thali",14:"dosa",15:"sambhar"}
desert={16:"choclate",17:"vanilla",18:"butterscotch",19:"strawberry"}
drink={20:"frooti",21:"haywards",22:"jaam ae mehfil"}

while True :
    print("************************  WELCOME TO HOTEL  ************************************", end  = '\n\n' )
    print("""                  \n            Below are the Food items avialable in this hotel""", end  = '\n\n' )
    print('1:"breakfast",2:"lunch",3:"dinner",4:"desert",5:"drink",6:"main menu",7:"quit"', end  = '\n\n')
    

    
    choice = int(input("Enter you choice  - 1/2/3/4/5/6/7 :  "))

    

    
 
    if choice not in options:
      print("Please enter valid option ")
      continue


    
    if choice  ==  1 :
      print("""breakfast for today is""",breakfast, end  = '\n\n' )
      select=int(input("enter your dish  :    1/2/3/4/5   :"))
      if select not in breakfast:
       print("Please enter valid option ")
      if select == 1:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif select == 2:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif select == 3:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif select == 4:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif select == 5:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      print("************************  THANKS FOR VISITING  ************************************", end  = '\n\n' )
      continue

    
    elif choice == 2:
      print("""\nlunch for today is""",lunch, end  = '\n\n' )
      choose=int(input("enter your dish  :    6/7/8/9/10   :"))
      if choose not in lunch:
         print("Please enter valid option ")
      if choose == 6:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif choose == 7:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif choose == 8:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif choose == 9:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif choose == 10:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      print("************************  THANKS FOR VISITING  ************************************", end  = '\n\n' )
      continue

    
    elif choice == 3:
      print("""\ndinner for today is""",dinner, end  = '\n\n' )


      
      pick=int(input("enter your dish  :    11/12/13/14/15  :"))


      
      if pick not in dinner:
         print("Please enter valid option ")
      if pick == 11:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif pick == 12:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif pick == 13:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif pick == 14:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif pick == 15:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      print("************************  THANKS FOR VISITING  ************************************", end  = '\n\n' )
      continue


    
    elif choice == 4:
      print("""\ndesert for today is""",desert, end  = '\n\n' )
      
      chuniye=int(input("enter your dish  :   16/17/18/19  :"  ))
      
      if chuniye not in desert:
         print("Please enter valid option ")
      if chuniye == 16:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif chuniye == 17:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif chuniye == 18:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif chuniye == 19:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      print("************************  THANKS FOR VISITING  ************************************", end  = '\n\n' )
      continue  
        

    elif choice == 5:
      print("""\ndrink for today is""",drink, end  = '\n\n' )
      
      uthao=int(input("enter your dish  :   20/21/22  :"))
      
      if uthao not in drink:
         print("Please enter valid option ")
      if uthao == 20:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif uthao == 21:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      elif uthao == 22:
          import random
          print("the amount is ",random.randint(120,590),"enjoy your meal ")
      print("************************  THANKS FOR VISITING  ************************************", end  = '\n\n' )
      continue


    elif choice == 6:
        continue

    else:
       choice == 7
    break
