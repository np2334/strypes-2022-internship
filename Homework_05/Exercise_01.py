from Exercise_01_classes import Bill, BillBatch, CashDesk

a = Bill(10)
b = Bill(5)
c = Bill(10)

print(int(a))
print(str(a))
print(b)

if a == c:
    print("a equals c")

money_holder = {}
money_holder[a] = 1

if c in money_holder:
    money_holder[c] += 1

print(money_holder) 

print("\n\n\n\n")

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]
batch = BillBatch(bills)
for bill in batch:
    print(bill)

print("\n\n\n\n")

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BillBatch(bills)
desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total()) # 390
desk.inspect()