from functools import wraps

def my_decorator(func):
    @wraps(func)  # Preserve __name__, __doc__, etc.
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet(name):
    """Greet someone"""
    return f"Hello {name}"

print(greet.__name__)  # "greet" (not "wrapper")
print(greet.__doc__)   # "Greet someone" 