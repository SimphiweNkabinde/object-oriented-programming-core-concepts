class User:
    def __init__(self, username, password):
        # private attributes
        self.__username = username
        self.__password = password

    # private methods
    def __compare_password(self, password):
        return self.__password == password
    
    def __valid_password(self, password):
        if len(password) < 3:
            return False
        if password.find(" ") != -1:
            return False
        return True

    # public methods
    def reset_password(self, current_password, new_password):
        match = self.__compare_password(current_password)
        if match == False:
            return False
        valid = self.__valid_password(new_password)
        if valid == False:
            return False

        self.__password = new_password
        return True
    
    def set_username(self, username):
        if len(username) < 1:
            return False
        self.__username = username
        return True
    def get_username(self):
        return self.__username
    
    def verify_password(self, password):
        return self.__compare_password(password)


user1 = User("bob", "bob@123")

user1.set_username("james")
new_username = user1.get_username()
print(new_username)

user1.reset_password("bob@123", "james@123")
is_valid_password = user1.verify_password("james@123")
print(is_valid_password)
