class User:
    def __init__(self, user_id, username):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User(451, 'tony')
user2 = User(674, 'frodo')
user3 = User(646, 'leonardo')


print(user1.user_id)
print(user1.username)

user1.follow(user2)
user1.follow(user3)

print(user1.following)
print(user1.followers)
