# Defining the class (template for instagram users)
class User:
    def __init__(self, username, bio, profile_picture):
        # Attributes: properties every user will have
        self.username = username
        self.bio = bio
        self.profile_picture = profile_picture

    # Methods: actions every user can perform
    def follow(self, another_user):
        return f"{self.username} followed {another_user.username}"


# Instantiation: Creating objects (individual users)
user1 = User("Jacob", "Love python and Java", "jacob.png")
user2 = User("Taylor", "games and food", "taylor.png")

print("---- USER CLASS------")
# Accessing attributes (using dot notation)
print(f"Username: {user1.username}\nBio: {user1.bio}\nProfile Picture: {user1.profile_picture}")
print(f"\nUsername: {user2.username}\nBio: {user2.bio}\nProfile Picture: {user2.profile_picture}")

# Calling methods
result = user1.follow(user2)
print(f"\n{result}")

# Defining the class
class Book:
    def __init__(self, title, author, price):
        # Attributes
        self.title = title
        self.author = author
        self.price = price

    # Methods
    def apply_discount(self, discount_percentage):
        return self.price - ((self.price * discount_percentage) / 100 )
    
book1 = Book("Stormbreaker", "Anthony Horowitz", 100)
book2 = Book("Clean Code", "Robert Cecil Martin", 1580)

print("\n---- BOOK CLASS------")
print(f"Title: {book1.title}\nAuthor: {book1.author}\nPrice: R{book1.price}")
print(f"Discount Price (10%): R{book1.apply_discount(10)}")

print(f"\nTitle: {book2.title}\nAuthor: {book2.author}\nPrice: R{book2.price}")
print(f"Discount Price (15%): R{book2.apply_discount(15)}")

