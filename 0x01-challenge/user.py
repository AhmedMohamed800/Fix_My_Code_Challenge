#!/usr/bin/python3
"""
User class
"""


class User():
    """create a user"""

    def __init__(self):
        """initiate a user"""
        self.__email = None

    @property
    def email(self):
        """getter of the user's email"""
        return self.__email

    @email.setter
    def email(self, value):
        """setter of user's email"""
        if type(value) is not str:
            raise TypeError("email must be a string")
        self.__email = value


if __name__ == "__main__":
    u = User()
    u.email = "john@snow.com"
    print(u.email)
