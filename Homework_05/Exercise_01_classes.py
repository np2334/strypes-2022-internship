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

    def __eq__(self, other_object):
        return other_object.__bill == self.__bill

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

    def __add_bill(self, bill):
        billValue = int(bill)
        if self.__total.get(billValue) == None:
            self.__total[billValue] = 0
        self.__total[billValue] += 1
        
    def __remove_bills(self, bills):
        for bill in bills:
            self.__total[int(bill)] -= 1

    def take_money(self, money):
        if isinstance(money, BillBatch):
            for bill in money:
                self.__add_bill(bill)
        else:
            self.__add_bill(money)

    def total(self):
        sum = 0
        for key, value in self.__total.items():
            sum += key * value
        return sum

    def inspect(self):
        for key, value in self.__total.items():
            print("{}$ bills - {}".format(key, value))

    def draw_amount(self, sum):
        if self.total() < sum:
            raise ValueError("Not enough cash")

        bills = []
        for key, value in self.__total.items():
            if sum == 0:
                break

            if key <= sum:
                for i in range(0, value):
                    bills.append(Bill(key))
                    sum -= key

                    if key > sum:
                        break 

        self.__remove_bills(bills)
        return BillBatch(bills)

    def draw_bills(self, bills_dictionary):
        bills = []
        for key, value in bills_dictionary.items():
            if self.__total.get(key) != None and self.__total[key] >= value:
                for i in range(0, value):
                    bills.append(Bill(key))
            else:
                raise ValueError("Not enough bills of {}".format(key))

        self.__remove_bills(bills)
        return bills
                

    

        

        
        
    
    