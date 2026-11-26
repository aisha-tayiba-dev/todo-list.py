import json
product = {}
item_id = 1

while True:
    choice = input('Choose an option:\n1. Add item\n2. View items\n3. Update item\n4. Delete item\n5. Exit\nEnter your choice: ')    # CREATE
# create
    if choice == '1':
        name = input('Enter item name: ')
        price = input('Enter item price: ')
        quantity = input('Enter item quantity: ')
        status = input('Enter item status (done/pending): ')
        product[item_id] = {
            'name': name,
            'price': price,
            'quantity': quantity,
            'status': status,
            'id': item_id
        }
        item_id += 1
        print('Item added successfully.')

    # READ
    elif choice == '2':
        if not product:
            print('No items in the list.')
        else:
            print('\nItems in the list:')
            for key, item in product.items():
             print(product) 

    # UPDATE
    elif choice == '3':
        search_product_name = input('Enter the Name of the item to update: ')
        found = False
        for key, item in product.items():
            if item['name'] == search_product_name:
                found = True
                print(
                    f"Found item: ID: {item['id']}, "
                    f"Name: {item['name']}, "
                    f"Price: {item['price']}, "
                    f"Quantity: {item['quantity']}, "
                    f"Status: {item['status']}"
                )
                new_name = input('Enter new name (leave blank to keep current): ')
                if new_name:
                    item['name'] = new_name
                new_price = input('Enter new price (leave blank to keep current): ')
                if new_price:
                    item['price'] = new_price
                new_quantity = input('Enter new quantity (leave blank to keep current): ')
                if new_quantity:
                    item['quantity'] = new_quantity
                new_status = input('Enter new status (done/pending, leave blank to keep current): ')
                if new_status:
                    item['status'] = new_status
                print('Item updated successfully.')
                break
        if not found:
            print('Item not found.')

    # DELETE
    elif choice == '4':
        delete_by_name = input('Enter the name of the item to delete: ')
        found = False
        for key, item in product.items():
            if item['name'] == delete_by_name:
                found = True
                del product[key]
                print('Item deleted successfully.')
                break
        if not found:
            print('Item not found.')

    # EXIT
    elif choice == '5':

        # the imported json module is used to write the product dictionary to a file named 'product.json' in JSON format. The 'indent=4' argument is used to format the JSON output with an indentation of 4 spaces for better readability. After saving the data, a message indicating that the program is exiting is printed, and the loop is broken to terminate the program.
        with open('product.json', 'w') as f:
            json.dump(product, f, indent=4)
        print('Exiting...')
        break

    else:
        print('Invalid choice. Please try again.')
