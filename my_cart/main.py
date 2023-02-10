# Create a class called cart that retains items and has methods to add, remove, and show

class Cart():
    def __init__(self):
        self.carts = []

    def add_items(self, item, quantity):
        while True:
            if quantity.isdigit():
                quantity = int(quantity)
                new_items = Items(item, quantity)
                self.carts.append(new_items)
                return
            else:
                print('Please enter amount in digits')

    def remove_items(self, delete_item, delete_quantity):
        for i in range(len(self.carts)):
            if self.carts[i].item.lower() == delete_item.lower():
                while True:
                    if delete_quantity.isdigit():
                        delete_quantity = int(delete_quantity)
                        self.carts[i].quantity -= delete_quantity
                        print(
                            f'{delete_quantity} {delete_item} has been removed.')
                        if self.carts[i].quantity == 0:
                            self.carts.pop(i)
                            print(f'{delete_item} have been removed.')
                        return
                    else:
                        print('Please enter quantity in digits')
                        return
        print(f'{delete_item} was not found')

    def show_list(self):
        if not self.carts:
            print('There are no items in your cart.')
            return

        for items in self.carts:
            print(
                f'Currently you have {items.quantity} {items.item} in your cart.')

    def run(self):
        while True:
            user_selection = input(
                'What would you like to do? (add/remove/show/checkout): ').lower()
            if user_selection == 'add':
                item = input('What item would you like to add?: ')
                quantity = input('How many items would you like to add?: ')
                my_cart.add_items(item, quantity)
                my_cart.show_list()
            elif user_selection == 'remove':
                my_cart.show_list()
                delete_item = input('What item would you like to remove?: ')
                delete_quantity = input('How many would you like to remove?: ')
                my_cart.remove_items(delete_item, delete_quantity)
                my_cart.show_list()
            elif user_selection == 'show':
                my_cart.show_list()
            elif user_selection == 'checkout':
                print('Purchasing the following items in cart: ')
                for items in self.carts:
                    print(f'{items.quantity} {items.item}')
                print('Thank you for shopping with us')
                return
            else:
                print('Please enter a valid selection. (add/remove/show/checkout): ')


class Items():
    def __init__(self, item, quantity):
        self.item = item
        self.quantity = quantity


# my_cart = Cart()
# # my_cart.run()
