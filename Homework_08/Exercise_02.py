from Exercise_02_exception import InvalidPaymentError, Person, Item

items = [
    Item("Car", 250.0),
    Item("Cat", 50.0),
    Item("Snack", 2.0),
    Item("Beer", 5.0),
    ]

person_one = Person("Pesho", "Peshev", 300.0)
person_two = Person("Ivan", "Ivanchev", 55.0)

person_one.buy(items[1])
person_one.buy(items[2])


print(person_one)
print(person_one.get_list_of_items())
print("\n")

person_two.buy(items[0])