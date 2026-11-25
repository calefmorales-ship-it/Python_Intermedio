
from abc import ABC, abstractmethod


class User(ABC):
    """Base class for all users in the system."""

    @abstractmethod
    def get_role(self):
        pass

    @abstractmethod
    def has_permission(self, permission):
        pass


class AdminUser(User):
    """Administrator user with full permissions."""

    def __init__(self, name):
        self.name = name

    def get_role(self):
        return "Admin"

    def has_permission(self, permission):
        return True


class RegularUser(User):
    """Standard user with limited permissions."""

    def __init__(self, name):
        self.name = name
        self.permissions = ["read"]

    def get_role(self):
        return "Regular"

    def has_permission(self, permission):
        return permission in self.permissions


user1 = AdminUser("Carlos")
user2 = RegularUser("Andrea")

print(user1.get_role())
print(user2.get_role())

print(user1.has_permission("delete"))
print(user2.has_permission("delete"))
print(user2.has_permission("read"))
