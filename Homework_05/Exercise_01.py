from Exercise_01_classes import Bill, BillBatch, CashDesk
print("Testing class Bill")
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

print("\n\n\n\nTesting class BillBatch")

values = [10, 20, 50, 100]
bills = [Bill(value) for value in values]
batch = BillBatch(bills)
for bill in batch:
    print(bill)

print("\n\n\n\nTesting class CashDesk")

values = [10, 20, 50, 100, 100, 100]
bills = [Bill(value) for value in values]
batch = BillBatch(bills)
desk = CashDesk()
desk.take_money(batch)
desk.take_money(Bill(10))
print(desk.total()) # 390
desk.inspect()


print("\n\n\n\nTesting functions draw_amount and draw_bills")
print("\n\nCashDesk starting bills:")
values = [50, 20, 100, 100, 50, 10, 10, 10, 10, 10, 5, 5]
bills = [Bill(value) for value in values]
batch = BillBatch(bills)
desk = CashDesk()
desk.take_money(batch)
desk.inspect()

print("\n\nAfter draw_amount(30)\n\nReturned amount:")
returned_amount = desk.draw_amount(30)
for bill in returned_amount:
    print(bill)

print("\n\nAfter draw_amount(125)\n\nReturned amount:")
returned_amount = desk.draw_amount(125)
for bill in returned_amount:
    print(bill)

print("\n\nCashDesk left bills:")
desk.inspect()

print("\n\nAfter draw_bills({10: 2, 5: 1})\n\nReturned amount:")
returned_amount = desk.draw_bills({10: 2, 5: 1})
for bill in returned_amount:
    print(bill)

print("\n\nCashDesk left bills:")
desk.inspect()

#desk.draw_bills({10: 2, 5: 1})  ValueError: Not enough bills of 10