def to_lower(character):
    return chr(ord(character) + 32) if ord(character) in range (65, 91) else character
        
def find_books(list_of_books, book_partial_title):
    found_books = []
    for book in list_of_books:
        for i in range(0, len(book)):
            book_character = book[i]
            if to_lower(book_character) == to_lower(book_partial_title[0]):
                isFullMatch = True
                for j in range(1, len(book_partial_title)):
                    if i + j >= len(book):
                        isFullMatch = False
                        break

                    currentCharacter = to_lower(book_partial_title[j])

                    if currentCharacter != to_lower(book[i + j]):
                        isFullMatch = False
                
                if isFullMatch:
                    found_books.append(book)
                    # ако търсената дума се повтаря ще я добавя няколко пъти, затова break-вам
                    break
    return found_books


library = [
    "Harry Potter and the Philosopher's Stone", 
    "Harry Potter and the Chamber of Secrets", 
    "The Adventures of Sherlock Holmes”, “The Chamber"]
book_name = "Harry Potter"

print(find_books(library, book_name))

library = [
    "Harry Potter and the Philosopher's Stone", 
    "Harry Potter and the Chamber of Secrets", 
    "The Adventures of Sherlock Holmes", 
    "The Chamber"]
book_name = "The chamber"
print(find_books(library, book_name))

print(find_books([], "Non Existing Book"))

library = [
    "Harry Potter and the Philosopher's StoneHarry Potter", 
    "Harry Potter and the Chamber of Secrets", 
    "The Adventures of Sherlock Holmes", 
    "The Chamber"]
book_name = "Harry Potter"
print(find_books(library, book_name))

#print(to_lower("A"))
#print(to_lower("Z"))
#print(to_lower("a"))
#print(to_lower("z"))
#print(to_lower("!") + "A")