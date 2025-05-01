def decorator(func):
    def wrapper (args, **kwargs):
        print("decorating...")
        resultado=func(args,**kwargs)
        return resultado
    return wrapper

@decorator
def greet():
    print("HI!")

greet()