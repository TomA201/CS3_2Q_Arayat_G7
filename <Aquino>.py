class Contact:
    def __init__(self, name, phonenumber, address, zipcode, dateadded):
        self.__name = name
        self.__phonenumber = phonenumber
        self.__address = address
        self.__zipcode = zipcode
        self.__dateadded = datedadded

    def __str__(self, name, phonenumber, address, zipcode, dateadded):
        return "Contact Name: " + name
        return "Contact Phone Number: " + phonenumber
        return "Contact Address: " + address
        return "ZIP Code: " + zipcode
        return "Date Added: " + dateadded


class Phonebook:
    def __init__(self, contactlist):
        self.__contactlist = []

    def addcontact(self, contactlist):
