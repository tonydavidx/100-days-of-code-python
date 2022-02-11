from textwrap import wrap


class User:
    def __init__(self, name):
        self.name = name
        self.authenticated = False


def is_authenicated_decorator(function):
    def wrapper(*args, **kwargs):
        if args[0].authenticated == True:
            return function(args[0])
        else:
            print("You are not authenticated")
    return wrapper


@is_authenicated_decorator
def create_blog_post(user):
    print(f'New blog post created by {user.name}')


user1 = User('Leonardo')
user1.authenticated = True
create_blog_post(user1)
