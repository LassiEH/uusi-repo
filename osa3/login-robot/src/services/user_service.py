from entities.user import User
import sys,pdb
import re

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)
        self.invalid_username(username)
        self.short_password(password)
        self.short_username(username)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise Exception("Username and password are required")

        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa

    def invalid_username(self, username):
        if not re.match("^[a-z]+$", username):
            print("Invalid characters in username")
            raise Exception("Invalid characters in username")
    
    def short_password(self, password):
        if len(password) < 8:
            raise Exception("Password is too short")

    def short_username(self, username):
        if len(username) < 3:
            print("Username is too short")
            raise Exception("Username is too short")
        
    def valid_password(self, password):
        if len(password) <= 7 or re.match("^[a-z]+$", password):
            raise Exception("Password not strong enough")
        
