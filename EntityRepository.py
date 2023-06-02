from IRepository import Interface

from typing import TypeVar, Dict, Generic

from typing import TypeVar, Dict, List, Union


T = TypeVar('T')
Key = Union[str, int]


class UserRepository(Interface):
    def __init__(self):
        self.users: Dict[Key, List[T]] = {}

    def add(self, key: Key, user: T) -> None:
        if key in self.users:
            self.users[key].append(user)
        else:
            self.users[key] = [user]

    def delete(self, key: Key) -> None:
        if key in self.users:
            del self.users[key]

    def get(self) -> Dict[Key, List[T]]:
        return self.users

    def search(self, key: Key) -> Dict[Key, List[T]]:
        if key in self.users:
            return self.users
        else:
            print('obj not found')

    def update(self, key: Key, updated_user: T) -> None:
        if key in self.users:
            self.users[key] = [updated_user]
        else:
            print('obj not found')


# -----------------------------------------------------------------------

class ProductRepository(Interface):
    def __init__(self):
        self.products: Dict[Key, List[T]] = {}

    def add(self, key: Key, product: T) -> None:
        if key in self.products:
            self.products[key].append(product)
        else:
            self.products[key] = [product]

    def get(self) -> Dict[Key, List[T]]:
        return self.products

    def update(self, key: Key, updated_product: T) -> None:
        if key in self.products:
            self.products[key] = [updated_product]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.products:
            del self.products[key]

    def search(self, key: Key) -> Dict[Key, List[T]]:
        if key in self.products:
            return self.products
        else:
            print('obj not found')


# -----------------------------------------------------------------------


class OrderRepository(Interface):
    def __init__(self):
        self.orders: Dict[Key, List[T]] = {}

    def add(self, key: Key, order: T) -> None:
        if key in self.orders:
            self.orders[key].append(order)
        else:
            self.orders[key] = [order]

    def get(self) -> Dict[Key, List[T]]:
        return self.orders

    def update(self, key: Key, updated_order: T) -> None:
        if key in self.orders:
            self.orders[key] = [updated_order]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.orders:
            del self.orders[key]

    def search(self, key: Key) -> Dict[Key, List[T]]:
        if key in self.orders:
            return self.orders
        else:
            print('obj not found')


# -----------------------------------------------------------------------


class CategoryRepository(Interface):
    def __init__(self):
        self.categories: Dict[Key, List[T]] = {}

    def add(self, key: Key, category: T) -> None:
        if key in self.categories:
            self.categories[key].append(category)
        else:
            self.categories[key] = [category]

    def get(self) -> Dict[Key, List[T]]:
        return self.categories

    def update(self, key: Key, updated_category: T) -> None:
        if key in self.categories:
            self.categories[key] = [updated_category]
        else:
            print('obj not found')

    def delete(self, key: Key) -> None:
        if key in self.categories:
            del self.categories[key]

    def search(self, key: Key) -> Dict[Key, List[T]]:
        if key in self.categories:
            return self.categories
        else:
            print('obj not found')


# -----------------------------------------------------------------------


class ReviewRepository(Interface):
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

    def search(self, key: Key) -> Dict[Key, List[T]]:
        if key in self.reviews:
            return self.reviews
        else:
            print('obj not found')
