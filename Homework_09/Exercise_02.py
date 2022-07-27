def test_decorator(func):
    def wrapper():
        result = func()
        return result.upper()
    return wrapper   

@test_decorator
def get_name():
    return "example name"

print(get_name())