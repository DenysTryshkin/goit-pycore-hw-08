""" Цей файл надає клас Phone для представлення номерів телефонів. """
from field import Field

class Phone(Field):
    """ Представляє номер телефону. """

    def __init__(self, number):
        """ Ініціалізує Phone з номером телефону. """
        self.value = self.correct_number(number)

    def correct_number(self, number):
        """ Перевіряє, чи є наданий номер коректним номером телефону. """
        if len(number) == 10 and number.isdigit():
            return number
        else:
            raise ValueError("Phone number must include exactly 10 digits")       