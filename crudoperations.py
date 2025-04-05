items_list = []

def create_item():
    """Create a new item and add it to the list."""
    name = input("Enter the item name: ")
    price = float(input("Enter the item price: "))
    new_item = {'name': name, 'price': price}
    items_list.append(new_item)
    print("Item '{}' with price {} created.".format(name, price))

def read_items():
    """Read and display all items in the list."""
    if not items_list:
        print("No items found.")
    else:
        print("Items:")
        for i, item in enumerate(items_list, 1):
            print("{}. {} - ${}".format(i, item['name'], item['price']))

def update_item():
    """Update the specified item in the list."""
    read_items()
    index = int(input("Enter the index of the item to update: "))
    if 1 <= index <= len(items_list):
        new_name = input("Enter the new item name: ")
        new_price = float(input("Enter the new item price: "))
        item = items_list[index - 1]
        item['name'] = new_name
        item['price'] = new_price
        print("Item {} updated: {} - ${}".format(index, item['name'], item['price']))
    else:
        print("Invalid index. No item found at index {}.".format(index))

def delete_item():
    """Delete the specified item from the list."""
    read_items()
    index = int(input("Enter the index of the item to delete: "))
    if 1 <= index <= len(items_list):
        deleted_item = items_list.pop(index - 1)
        print("Item {} deleted: {} - ${}".format(index, deleted_item['name'], deleted_item['price']))
    else:
        print("Invalid index. No item found at index {}.".format(index))

# Main loop for user interaction
while True:
    print("\nMenu:")
    print("1. Create item")
    print("2. Read items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        create_item()
    elif choice == '2':
        read_items()
    elif choice == '3':
        update_item()
    elif choice == '4':
        delete_item()
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 5.")
    ans=input("do you want to continue")
    if(ans.lower()!='y'):
        break

        
