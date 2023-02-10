from main import AddressBook, Contact
import unittest

class AddressBookTest(unittest.TestCase):
    def test_add_contact(self):
        test_book = AddressBook()
        test_book.add_contact('Dylan', '123-456-7890','123 Main St', 'dylans@codingtemple.com')

        # Make sure there is now one and only one contact
        self.assertEqual(len(test_book.contacts), 1)

        # Make sure the item in the list is actually a contact
        self.assertIsInstance(test_book.contacts[0], Contact)

    def test_contact_instantiation(self):
        test_contact = Contact('Dylan', '123-456-7890','123 Main St', 'dylans@codingtemple.com')

        self.assertEqual(test_contact.name, 'Dylan')
        self.assertEqual(test_contact.phone_number, '123-456-7890')
        self.assertEqual(test_contact.address, '123 Main St')
        self.assertEqual(test_contact.email, 'dylans@codingtemple.com')

    def test_delete(self):
        test_book = AddressBook()
        test_book.add_contact('Dylan', '123-456-7890','123 Main St', 'dylans@codingtemple.com')

        test_book.delete_contact('Dylan')

        self.assertEqual(len(test_book.contacts), 0)

        
        test_book.add_contact('Dylan', '123-456-7890','123 Main St', 'dylans@codingtemple.com')
        test_book.add_contact('Liam', '123-456-7890','123 Main St', 'liamp@codingtemple.com')

        test_book.delete_contact('Dylan')

        self.assertEqual(len(test_book.contacts), 1)

        self.assertEqual(test_book.contacts[0].name, 'Liam')

unittest.main()