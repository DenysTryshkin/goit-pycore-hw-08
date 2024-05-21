""" Цей файл містить реалізацію асистента для роботи з адресною книгою. """

from address_book import AddressBook
from record import Record
from data_handling import save_data, load_data


def input_error(func):
    """ Обробляє помилки що можуть виникнути """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact does not exist!"
        except ValueError:
            return "Something went wrong"
        except IndexError:
            return "Please provide the required argument for the command."
    return inner


@input_error
def add_contact(args, book: AddressBook):
    """ Функція додавання контакту """
    if len(args) != 2:
        raise ValueError("Invalid number of arguments for add_contact")
    name, phone = args
    record = Record(name=name)
    record.add_phone(phone)
    book.add_record(record)
    return "Contact added."


@input_error
def change_contact(args, book: AddressBook):
    """ Функція для змінення контакту """
    if len(args) != 3:
        return "Invalid number of arguments. "
    name, old_number, new_number = args
    record = book.find(name)
    if record is None:
        return ValueError
    else:
        record.edit_phone(old_number, new_number)
        return "Contact updated"


@input_error
def show_phone(args, book: AddressBook):
    """ Функція для виведення телефону """
    if len(args) != 1:
        raise ValueError("Invalid number of arguments.")
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError(f"Contact '{name}' does not exist.")
    return f"Contact name: {name}, phone: {record.phones[0]}"



@input_error
def show_all(book: AddressBook):
    """ Функція виведення data """
    if not book:
        return "No contacts saved!"
    return "\n".join([f"{name}: {phone}" for name, phone in book.items()])


@input_error
def add_birthday(args, book: AddressBook):
    """ Функція добавлення дня народження """
    if len(args) != 2:
        return "Invalid number of arguments."
    name, date = args
    record = book.find(name)
    if record:
        record.add_birthday(date)
        return "Birthday added."
    else:
        return f"Contact '{name}' is not in the addressbook"


def show_birthday(args, book):
    """ Функція для виведення дати народження контакту """
    if len(args) != 1:
        raise ValueError
    name = args[0]
    record = book.find(name)
    if name not in book:
        raise KeyError
    return f"Contact name: {name}, birthday: {record.birthday}"


def parse_input(user_input):
    """ Розділяє введений рядок на команду та аргументи """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    """ Головна функція боту, де прописані команди """
    book = load_data()
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            save_data(book)
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, book))
        elif command == "change":
            print(change_contact(args, book))
        elif command == "phone":
            print(show_phone(args, book))
        elif command == "all":
            print(show_all(book))
        elif command == "add-birthday":
            print(add_birthday(args, book))
        elif command == "show-birthday":
            print(show_birthday(args, book))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
