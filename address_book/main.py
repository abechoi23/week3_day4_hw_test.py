class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, address, email):
        # name = input('Enter Name: ')
        # phone_number = input('Enter Phone Number: ')
        # address = input('Enter Address: ')
        # email = input('Enter Email: ')

        new_contact = Contact(name, phone_number, address, email)
        self.contacts.append(new_contact)

    def delete_contact(self, delete_name):
        # delete_name = input('Enter name to delete: ')

        for i in range(len(self.contacts)):
            if self.contacts[i].name.lower() == delete_name.lower():
                self.contacts.pop(i)
                print('Contact Deleted')
                return

        print(f'{delete_name} was not found.')

    def print_contacts(self):
        for contact in self.contacts:
            print(f'{contact.name}')
            print(f'Phone Number: {contact.phone_number}')
            print(f'Address: {contact.address}')
            print(f'Email: {contact.email}')

    def run(self):
        while True:
            user_choice = input(
                'What would you like to do? (add/delete/show/quit)').lower()

            if user_choice == 'add':
                name = input('Enter Name: ')
                phone_number = input('Enter Phone Number: ')
                address = input('Enter Address: ')
                email = input('Enter Email: ')
                self.add_contact(name, phone_number, address, email)
            elif user_choice == 'delete':
                delete_name = input('Enter name to delete: ')
                self.delete_contact(delete_name)
            elif user_choice == 'show':
                self.print_contacts()
            elif user_choice == 'quit':
                self.print_contacts()
                return
            else:
                print('That was not valid input, please try again.')


class Contact:
    def __init__(self, name, phone_number, address, email):
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email

# my_address_book = AddressBook()
# my_address_book.run()