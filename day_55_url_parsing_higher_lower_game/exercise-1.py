
def logging_decorator(function):
    def wrapper(*args):
        output = function(args[0], args[1])
        print(f"the function {function.__name__} was called")
        print(f"It returned {output}")
    return wrapper


@logging_decorator
def calculate_age(birth_year, current_year):
    return current_year - birth_year


calculate_age(1993, 2022)
