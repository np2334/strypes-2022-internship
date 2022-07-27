class InvalidPaymentError(BaseException):
    def __init__(self, message):
        super().__init__(message)

class Item():
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def __repr__(self):
        return "{} - {}".format(self.__name, self.__price)

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

class Person():
    def __init__(self, first_name, last_name, balance):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__balance = balance
        self.__list_of_items = []

    def __repr__(self):
        return "{} {} balance: {}".format(self.__first_name, self.__last_name, self.__balance)

    def get_balance(self):
        return self.__balance

    def buy(self, item):
        item_price = item.get_price()
        if item_price > self.__balance:
            raise InvalidPaymentError("Current balance: {}, Item price: {}".format(self.__balance, item_price))
        else:
            self.__balance -= item_price
            self.__list_of_items.append(item)

    def get_list_of_items(self):
        return self.__list_of_items