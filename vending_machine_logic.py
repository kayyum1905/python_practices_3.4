items = {
    '1': ('Soda', 1.75),
    '2': ('Water', 0.95),
    '3': ('Juice', 2.25)
}


def admin_operation():
    print('*'*5, 'Admin Panel', '*'*5)
    admin_input = input('press q to go to main menu or press anything to add product:\n')
    if admin_input == 'q':
        execute()
    else:
        add_new_item()


def add_new_item():
    print('Adding new item')
    new_key = input('Please enter product id:')
    new_product = input('Please enter product name:')
    new_price = input('Please enter product price:')
    new_value = (new_product, new_price)
    print('- - updating - -\n'*5)
    items.update({str(new_key): new_value})
    print('Successful!')
    execute()


def customer_operation(user_choice):
    for product_id, item in sorted(zip(items.keys(), items.values())):
        if product_id == user_choice:
            print('You choose:', item[0], 'it\'s cost is only:', item[1])
            payment_operation()


def payment_operation():
    payment_method = int(input('Enter 1 to pay via or 2 to pay\n'))
    if payment_method == 1:
        print('Thank you')
        execute()
    elif payment_method == 2:
        print('Please enter the money')
    else:
        print('Invalid input')
        payment_operation()


def process_input():
    user_input = input('\nPlease enter product no:\n')
    if user_input == 'admin':
        admin_operation()
    elif str(user_input) in items:
        customer_operation(user_input)
    else:
        print('Invalid input please try again\n')
        execute()


def list_products():
    print('Product No | Product | Price:')
    for product_id, item in sorted(zip(items.keys(), items.values())):
        print(product_id, ' - '*3, item[0], ' - '*2, item[1])


def execute():
    list_products()
    process_input()

execute()
