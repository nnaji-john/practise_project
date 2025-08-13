class User:
    #all_users = []


    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email
        #User.all_users.append(self)
        print('user created!')

    def introduce(self, guest_name):
        print("Hello, {}, I'm {}, contact me at {}.".format(guest_name, self.name, self.email))

    def __repr__(self): # type: ignore
        return "User(username='{}', name='{}', email='{}')".format(self.username, self.name, self.email)

    def __str__(self):
        return self.__repr__()

user1 = User('janedoe', 'Jane Doe', 'jane@deo.com')

user2 = User('johnnyman', 'johnpaul', 'johnpaul@deo.com')

user3 = User('johndoe', 'John Doe', 'john@deo.com')

print(user1.name)
print(user2.email)
user2.introduce('James')
print(user3)

class UserDatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        if not isinstance(user, User):
            raise TypeError("insert expects a User instance")
        i = 0
        while i < len(self.users) and self.users[i].username < user.username:
            i += 1
        # duplicate guard
        if i < len(self.users) and self.users[i].username == user.username:
            raise ValueError(f"User already exists: {user.username}")
        self.users.insert(i, user)

    def find(self, username):
        for user in self.users:
            if user.username == username:
                return user
        return None

    def update(self, user):
        for u in self.users:
            if u.username == user.username:
                u.name = user.name
                u.email = user.email
                return True
        return False


    def listAll(self):
        return list(self.users)



# Create sample profiles for testing
jude = User('jude', 'Jude', 'jude@deo.com')
chris =  User('chris', 'Chris', 'chris@deo.com')
joy = User('joy', 'Joy', 'joy@deo.com')
philip = User('philip', 'Philip', 'philip@deo.com')
janice = User('janice', 'Janice', 'janice@deo.com')
peter = User('peter', 'Peter', 'peter@deo.com')
jaana = User('jaana', 'Jaana', 'jaana@deo.com')

#print(User.all_users)    
users_list = [jude, chris, joy, philip, janice, peter, jaana]

print(User)
print(jude.email)

# Create a UserDatabase instance
# Create a user database instance
database = UserDatabase()

# Insert users into the database
database.insert(jude)
database.insert(chris)
database.insert(joy)
database.insert(philip)
database.insert(janice)
database.insert(peter)
database.insert(jaana)


print("DB (index | username | name | email)")
for i, u in enumerate(database.users):
    print(f"{i:2d} | {u.username:10} | {u.name:12} | {u.email}")

print("Usernames (sorted):", [u.username for u in database.users])

try:
    database.insert(User('chris', 'X', 'x@x.com'))
except ValueError as e:
    print("Duplicate check OK:", e)








# list some scenerios to test the class methods insert, find, update, listAll.
# Simple problem defination: insert user in a list sorted by username, find user by username, update user by username, list all users.
# insert user to list and keep it sorted by username
# fnd user object by username with details from the querry
# update user object by username with details of the querry
# Return list of all users sorted by username

# 'chris' < 'jude' # True
# True, so chris comes before jude in the sorted list
# 'jaana' > 'philip' # False
# False, so jaana comes after philip in the sorted list


