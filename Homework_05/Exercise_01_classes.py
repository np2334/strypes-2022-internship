class Bill:
    def __init__(self, bill):
        if bill < 0:
            raise ValueError("Value is negative")
        elif not isinstance(bill, int):
            raise TypeError("Value is not int")

        self.__bill = bill

    def __str__(self):
        return "A {}$ bill".format(self.__bill)

    def __repr__(self):
        return self.__str__() 

    def __int__(self):
        return self.__bill

    def __eq__(self, otherObject):
        return True if otherObject.__bill == self.__bill else False

    def __hash__(self):
        return hash(self.__bill)

class BillBatch:
    def __init__(self, bills):
        self.__bills = bills

    def __len__(self):
        return len(self.__bills)

    def total(self):
        sum = 0
        for bill in self.__bills:
            sum += bill.__bill

        return sum

    def __getitem__(self, index):
        if index < len(self.__bills):
            return self.__bills[index]
        else:
            raise IndexError("Index not present")

class CashDesk:
    def __init__(self):
        self.__total = {}

    def __magic_function_bill(self, bill):
        billValue = int(bill)
        if self.__total.get(billValue) == None:
            self.__total[billValue] = 0
        self.__total[billValue] += 1
        
    def take_money(self, money):
        if isinstance(money, BillBatch):
            for bill in money:
                self.__magic_function_bill(bill)
        else:
            self.__magic_function_bill(money)

    def total(self):
        sum = 0
        for key, value in self.__total.items():
            sum += key * value
        return sum

    def inspect(self):
        for key, value in self.__total.items():
            print("{}$ bills - {}".format(key, value))

    def withdraw(self, sum):
        if self.total() < sum:
            raise ValueError("Not enough cash")

        
        
    
    