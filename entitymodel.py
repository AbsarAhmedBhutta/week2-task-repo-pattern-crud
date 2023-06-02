class User:
    def __init__(self, user_id, name):
        self.id = user_id
        self.name = name

    def __repr__(self):
        return f"User ID: {self.id}, Name: {self.name}"


class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __repr__(self):
        return f"User ID: {self.id}, Name: {self.name}, Price:{self.price}"


class Order:
    def __init__(self, id, user, product_name):
        self.id = id
        self.user = user
        self.product_name = product_name

    def __repr__(self):
        return f"User ID: {self.id}, Name: {self.user}, Price:{self.product_name}"

class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"User ID: {self.id}, Name: {self.name}"

class Review:
    def __init__(self, id, product_name, user, rating, comment):
        self.id = id
        self.product_name = product_name
        self.user = user
        self.rating = rating
        self.comment = comment

    def __repr__(self):
        return f"User ID: {self.id}, Name: {self.product_name}, Price:{self.user}, rating:{self.rating}, comment:{self.comment}"
