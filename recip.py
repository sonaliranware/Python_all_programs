#This Project contains code to ask user to select a recipe from a dictionary
#Then it prints all the ingredients required for the reciepe
#If ingredients are not available it diplays the message and adds the ingredient to shopping list
#Prints the shopping list at the end

from Ingredient_Dictionary import fridge,recipes

#Creating empty dictionary to display food item and for shoping list
display_dict = {}
shopping_dict={}

#defining function to add food items not in fridge for shopping
def shopping(data : dict, item : str,amount : int) -> None:
    if item in data:
        data[item] += amount
    else:
        data[item] = amount

#Adding recipes to new dictionary with index number
for key,values in enumerate(recipes):
    display_dict[key+1]= values

print("*"*80)
text = "Welcome to Smart Fridge\n"
print("{}".format(text.center(80)))


while True:
    print("\nPlease select recipe :")
    print("*"*40)
    for key,value in display_dict.items():
        print(f"{key:3} - {value}")
    print("Enter 0 to Exit")

    choice = int(input(": "))
    if choice == '0' or choice == 0:
        break
    elif choice in display_dict:
        selected_item = display_dict[choice]
        print("-"*40)
        print(f"You have selected {selected_item}")
        print(".......Please wait\nLoading Ingredients :\n")
        ingredients = recipes[selected_item]

    print()
    for food_item,req_quantity in ingredients.items():
       print(food_item,req_quantity)
       #print(".......Please wait\nChecking Fridge for Availability of Ingredients :\n")
       quantity_in_fridge = fridge.get(food_item,0)
       
       if req_quantity <= quantity_in_fridge:
           print(food_item," is availabe")
       else:
           quantity_to_buy = req_quantity-quantity_in_fridge
           print(quantity_to_buy ,food_item," needs to be bought")
           shopping(shopping_dict,food_item,quantity_to_buy)

print("-*"*25)
text_new = "Shopping List"
print("{}".format(text_new.center(40)))
for item,quant in shopping_dict.items():
    print("{0:20} : {1}".format(item,quant))
            











            
            
    
