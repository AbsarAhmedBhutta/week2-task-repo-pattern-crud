from IUnitOfWork import IUnitOfWork
from EntityRepository import *
import datetime
from typing import TypeVar, Dict, List, Union, Generic

T = TypeVar('T')
Key = Union[str, int]

user_repo = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()
catagory_repo = CategoryRepository()
review_repo = ReviewRepository()


class User_UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.users_data = user_repo.get()
        self.users_commited_data: Dict[Key] = {}
        self.is_committed = False

    def commit(self, commit_name):
        if self.users_data.items() is None:
            print("No data found")
        else:
            self.users_commited_data[commit_name] = self.users_data
            print(datetime.datetime.now())
            print(f'Commits made till now are:{self.users_commited_data.keys()}')

    def rollback(self, key: Key) -> None:
        keys_to_remove = []
        for i in self.users_commited_data:
            if i == key:
                keys_to_remove.append(i)

        for j in keys_to_remove:
            del self.users_commited_data[key]

        print('roll backed')


class Product_UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.users_data = user_repo.get()
        self.product_commited_data: Dict[Key] = {}
        self.is_committed = False

    def commit(self, commit_name):
        if self.users_data.items() is None:
            print("No data found")
        else:
            self.product_commited_data[commit_name] = self.users_data
            print(datetime.datetime.now())
            print(f'Commits made till now are:{self.product_commited_data.keys()}')

    def rollback(self, key: Key) -> None:
        keys_to_remove = []
        for i in self.product_commited_data:
            if i == key:
                keys_to_remove.append(i)

        for j in keys_to_remove:
            del self.product_commited_data[key]

        print('roll backed')


class Order_UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.users_data = user_repo.get()
        self.orders_commited_data: Dict[Key] = {}
        self.is_committed = False

    def commit(self, commit_name):
        if self.users_data.items() is None:
            print("No data found")
        else:
            self.orders_commited_data[commit_name] = self.users_data
            print(datetime.datetime.now())
            print(f'Commits made till now are:{self.orders_commited_data.keys()}')

    def rollback(self, key: Key) -> None:
        keys_to_remove = []
        for i in self.orders_commited_data:
            if i == key:
                keys_to_remove.append(i)

        for j in keys_to_remove:
            del self.orders_commited_data[key]

        print('roll backed')


class Category_UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.users_data = user_repo.get()
        self.category_commited_data: Dict[Key] = {}
        self.is_committed = False

    def commit(self, commit_name):
        if self.users_data.items() is None:
            print("No data found")
        else:
            self.category_commited_data[commit_name] = self.users_data
            print(datetime.datetime.now())
            print(f'Commits made till now are:{self.category_commited_data.keys()}')

    def rollback(self, key: Key) -> None:
        keys_to_remove = []
        for i in self.category_commited_data:
            if i == key:
                keys_to_remove.append(i)

        for j in keys_to_remove:
            del self.category_commited_data[key]

        print('roll backed')


class Review_UnitOfWork(IUnitOfWork):
    def __init__(self):
        self.users_data = review_repo.get()
        self.reviews_commited_data: Dict[Key] = {}

    def commit(self, commit_name):
        if self.users_data.items() is None:
            print("No data found")
        else:
            self.reviews_commited_data[commit_name] = self.users_data
            print(datetime.datetime.now())
            print(f'Commits made till now are:{self.reviews_commited_data.keys()}')

    def rollback(self, key: Key) -> None:
        keys_to_remove = []
        for i in self.reviews_commited_data:
            if i == key:
                keys_to_remove.append(i)

        for j in keys_to_remove:
            del self.reviews_commited_data[key]

        print('roll backed')
