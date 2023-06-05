from IRepository import Interface
from entitymodel import *
from typing import TypeVar, Dict, List, Union

T = TypeVar('T')
Key = Union[str, int]


class UserRepository(Interface[User]):
    def __init__(self):
        self.users: Dict[Key, List[User]] = {}
        self.committed_data = {}

    def add(self, key: Key, user: User) -> None:
        if key in self.users:
            self.users[key].append(user)
        else:
            self.users[key] = [user]

    def delete(self, key: Key) -> None:
        if key in self.users:
            del self.users[key]
        else:
            print('Not Found')

    def get(self) -> Dict[Key, List[User]]:
        return self.users

    def search(self, key: Key) -> List[User]:
        if key in self.users:
            return self.users[key]
        else:
            print('obj not found')

    def update(self, key: Key, updated_user: User) -> None:
        if key in self.users:
            self.users[key] = [updated_user]
        else:
            print('obj not found')


# -----------------------------------------------------------------------

class ProductRepository(Interface[Product]):
    def __init__(self):
        self.products: Dict[Key, List[Product]] = {}

    def add(self, key: Key, product: Product) -> None:
        if key in self.products:
            self.products[key].append(product)
        else:
            self.products[key] = [product]

    def get(self) -> Dict[Key, List[Product]]:
        return self.products

    def update(self, key: Key, updated_product: Product) -> None:
        if key in self.products:
            self.products[key] = [updated_product]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.products:
            del self.products[key]
        else:
            print('Not Found')

    def search(self, key: Key) -> List[Product]:
        if key in self.products:
            return self.products[key]
        else:
            print('obj not found')


# -----------------------------------------------------------------------


class OrderRepository(Interface[Order]):
    def __init__(self):
        self.orders: Dict[Key, List[Order]] = {}

    def add(self, key: Key, order: Order) -> None:
        if key in self.orders:
            self.orders[key].append(order)
        else:
            self.orders[key] = [order]

    def get(self) -> Dict[Key, List[Order]]:
        return self.orders

    def update(self, key: Key, updated_order: Order) -> None:
        if key in self.orders:
            self.orders[key] = [updated_order]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.orders:
            del self.orders[key]
        else:
            print('Not Found')

    def search(self, key: Key) -> List[Order]:
        if key in self.orders:
            return self.orders[key]
        else:
            print('obj not found')


# -----------------------------------------------------------------------


class CategoryRepository(Interface[Category]):
    def __init__(self):
        self.categories: Dict[Key, List[Category]] = {}

    def add(self, key: Key, category: Category) -> None:
        if key in self.categories:
            self.categories[key].append(category)
        else:
            self.categories[key] = [category]

    def get(self) -> Dict[Key, List[Category]]:
        return self.categories

    def update(self, key: Key, updated_category: Category) -> None:
        if key in self.categories:
            self.categories[key] = [updated_category]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.categories:
            del self.categories[key]
        else:
            print('Not Found')

    def search(self, key: Key) -> List[Category]:
        if key in self.categories:
            return self.categories[key]
        else:
            print('obj not found')


# -----------------------------------------------------------------------


class ReviewRepository(Interface[Review]):
    def __init__(self):
        self.reviews: Dict[Key, List[T]] = {}

    def add(self, key: Key, review: T) -> None:
        if key in self.reviews:
            self.reviews[key].append(review)
        else:
            self.reviews[key] = [review]

    def get(self) -> Dict[Key, List[T]]:
        return self.reviews

    def update(self, key: Key, updated_review: T) -> None:
        if key in self.reviews:
            self.reviews[key] = [updated_review]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.reviews:
            del self.reviews[key]
        else:
            print('Not Found')

    def search(self, key: Key) -> List[Review]:
        if key in self.reviews:
            return self.reviews[key]
        else:
            print('obj not found')
