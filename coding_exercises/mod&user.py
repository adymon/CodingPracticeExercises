"""

User & Moderator uses Inheritance

"""


class User:
    active_users = 0

    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"

    @classmethod
    def from_string(cls, data_str):
        first, last, age = data_str.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    def logout(self):
        User.active_users -= 1
        return f"{self.full_name()} has logged out"

    def full_name(self):
        return f"{self.first} {self.last}"

    def initials(self):
        return f"{self.first[0]}.{self.last[0]}"

    def likes(self, thing):
        return f"{self.first} likes {thing}"

    def is_senior(self):
        return self.age >= 65

    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th Birthday {self.first}"


class Moderator(User):
    active_moderators = 0

    def __init__(self, first, last, age, community):
        super().__init__(first, last, age)
        self.community = community
        Moderator.active_moderators += 1

    def mod_logout(self):
        Moderator.active_moderators -= 1
        return f"{self.full_name()} successfully logged out"

    @classmethod
    def display_active_moderators(cls):
        return f"There are currently {cls.active_moderators} active moderators"

    def remove_post(self):
        return f"{self.full_name()} removed the post from {self.community} community"


print(User.display_active_users())
user1 = User("Jane", "Doe", 21)
user2 = User("John", "Smith", 25)
print(User.display_active_users())
print(user1.likes("Chocolate"))
print(user2.logout())
print(User.display_active_users())
user3 = user1.from_string("Jane1, Doe, 27")
print(user3.full_name())
print(User.display_active_users())
mod1 = Moderator('John1', 'Smith', 18, 'Genius')
print(mod1.full_name())
print(mod1.display_active_moderators())
print(mod1.remove_post())
print(mod1.mod_logout())
print(mod1.display_active_moderators())

