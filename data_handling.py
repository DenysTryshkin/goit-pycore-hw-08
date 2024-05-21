import pickle

from address_book import AddressBook

PICKLE_FILE = "contacts.pkl"



def save_data(book, filename=PICKLE_FILE):
    with open(filename, "wb") as file:
        pickle.dump(book, file)


def load_data(filename=PICKLE_FILE):
    try:
        with open(filename, "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return AddressBook()