def authorize(funcion):
    def wrapper(user, *args, **kwargs):
        if getattr(user, 'is_admin', False):  
            return funcion(user, *args, **kwargs)
        else:
            print("Acceso denegado")
            return None
    return wrapper

class User:
    def __init__(self, name, is_admin):
        self.name = name
        self.is_admin = is_admin


@authorize
def example_function(user):
    print(f"Hola {user.name}")


admin_user = User("Franco", True)  
regular_user = User("Juan", False)  


example_function(admin_user)
example_function(regular_user)
