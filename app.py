from UnitOfWork import *
from EntityRepository import *

from entitymodel import *

user_repo = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()
catagory_repo = CategoryRepository()
review_repo = ReviewRepository()

# Unit of work

user_uow = User_UnitOfWork()
product_uow = Product_UnitOfWork()
order_uow = Order_UnitOfWork()
category_uow = Category_UnitOfWork()
review_uow = Review_UnitOfWork()

entity_work = input('''
ENTER THE ENTITY TO WORK ON:
> enter 'U' for User,
> enter 'P' for Product,
> enter 'O' for Order,
> enter 'C' for Category,
> enter 'R' for Review,
:-''')

if entity_work == 'U':
    while True:
        user_crud_op = input('enter update/get/delete/search/add/commit/rollback operations for user (or enter "exit" '
                             'to end):')
        if user_crud_op == 'add':
            id = input("enter user id")
            name = input("enter user name")

            user = User(id, name)

            user_repo.add(id, user)
        elif user_crud_op == 'get':
            users = user_repo.get()
            for key, user_list in users.items():
                for user in user_list:
                    print(user)
        elif user_crud_op == 'update':
            id = input("enter user id for updating:")
            name = input("enter user updated name:")

            user = User(id, name)

            user_repo.update(id, user)
        elif user_crud_op == 'delete':
            id = input("enter user id for deletion:")
            user_repo.delete(id)

        elif user_crud_op == 'search':
            id = input("enter user id for search:")
            print(user_repo.search(id))

        elif user_crud_op == 'commit':
            commit_name = input('enter Commit name:')
            user_uow.commit(commit_name)

        elif user_crud_op == 'rollback':
            rollback_name = input('enter the name of commit to rollback:')
            user_uow.rollback(rollback_name)

        elif user_crud_op == 'exit':
            break

        else:
            print('wrong key')

elif entity_work == 'P':
    while True:
        product_crud_op = input(
            'enter update/get/delete/search/add/commit/rollback operations for user (or enter "exit" '
            'to end):')
        if product_crud_op == 'add':
            id = input("enter product id")
            product_name = input("enter product name")
            product_price = float(input("enter product price"))

            product_vals = Product(id, product_name, product_price)
            product_repo.add(id, product_vals)

        elif product_crud_op == 'get':
            users = product_repo.get()
            for key, product_list in users.items():
                for product in product_list:
                    print(product)

        elif product_crud_op == 'update':
            id = input("enter product id")
            product_name = input("enter product name")
            product_price = float(input("enter product price"))

            product_vals = Product(id, product_name, product_price)
            product_repo.update(id, product_vals)

        elif product_crud_op == 'delete':
            id = input("enter user id for deletion:")
            product_repo.delete(id)

        elif product_crud_op == 'search':
            id = input("enter user id for search:")
            print(product_repo.search(id))

        elif product_crud_op == 'commit':
            commit_name = input('enter Commit name:')
            product_uow.commit(commit_name)

        elif product_crud_op == 'rollback':
            rollback_name = input('enter the name of commit to rollback:')
            product_uow.rollback(rollback_name)

        elif product_crud_op == 'exit':
            break

        else:
            print('wrong key')

elif entity_work == 'O':
    while True:
        orders_crud_op = input('enter update/get/delete/search/add/commit/rollback operations for user (or enter '
                               '"exit" '
                               'to end):')
        if orders_crud_op == 'add':
            id = input("enter order id")
            user_order_name = input("enter order name")
            order_order_user = input("enter order user nme")

            order_vals = Order(id, user_order_name, order_order_user)
            order_repo.add(id, order_vals)

        elif orders_crud_op == 'get':
            orders = order_repo.get()
            for key, order_list in orders.items():
                for order in order_list:
                    print(order)

        elif orders_crud_op == 'update':
            id = input("enter order id")
            user_order_name = input("enter order name")
            order_order_user = input("enter order user nme")

            order_vals = Order(id, user_order_name, order_order_user)
            order_repo.update(id, order_vals)

        elif orders_crud_op == 'delete':
            id = input("enter order id for deletion:")
            order_repo.delete(id)

        elif orders_crud_op == 'search':
            id = input("enter user id for search:")
            print(order_repo.search(id))

        elif orders_crud_op == 'commit':
            commit_name = input('enter Commit name:')
            order_uow.commit(commit_name)

        elif orders_crud_op == 'rollback':
            rollback_name = input('enter the name of commit to rollback:')
            order_uow.rollback(rollback_name)

        elif orders_crud_op == 'exit':
            break

        else:
            print('wrong key')


elif entity_work == 'C':
    while True:
        catagory_crud_op = input('enter update/get/delete/search/add/commit/rollback operations for user (or enter '
                                 '"exit" '
                                 'to end):')

        if catagory_crud_op == 'add':
            id = input("enter product id")
            catagory_name = input("enter catagory name")

            catagory_vals = Category(id, catagory_name)

            catagory_repo.add(id, catagory_vals)

        elif catagory_crud_op == 'get':
            catagorys = catagory_repo.get()
            for key, catagory_list in catagorys.items():
                for product in catagory_list:
                    print(product)

        elif catagory_crud_op == 'update':
            id = int(input("enter catagory id"))
            catagory_name = input("enter catagory name")

            catagory_vals = Category(id, catagory_name)

            catagory_repo.update(id, catagory_vals)
        elif catagory_crud_op == 'delete':
            id = int(input("enter catagory id for deletion:"))
            catagory_repo.delete(id)

        elif catagory_crud_op == 'search':
            id = input("enter user id for search:")
            print(catagory_repo.search(id))

        elif catagory_crud_op == 'commit':
            commit_name = input('enter Commit name:')
            category_uow.commit(commit_name)

        elif catagory_crud_op == 'rollback':
            rollback_name = input('enter the name of commit to rollback:')
            category_uow.rollback(rollback_name)

        elif catagory_crud_op == 'exit':
            break

        else:
            print('wrong key')


elif entity_work == 'R':
    while True:
        rev_crud_op = input('enter update/get/delete/search/add/commit/rollback operations for user (or enter "exit" '
                            'to end):')
        if rev_crud_op == 'add':
            id = input("enter review id")
            product_name_r = input("enter review name")
            user_r = input("enter review user_r name")
            rating_r = input("enter review rating_r")
            comment_r = input("enter review comment_r")

            review_vals = Review(id, product_name_r, user_r, rating_r, comment_r)
            review_repo.add(id, review_vals)

        elif rev_crud_op == 'get':
            reviews = review_repo.get()
            for key, review_list in reviews.items():
                for product in review_list:
                    print(product)

        elif rev_crud_op == 'update':
            id = input("enter review id")
            product_name_r = input("enter review name")
            user_r = input("enter review user_r name")
            rating_r = input("enter review rating_r")
            comment_r = input("enter review comment_r")

            review_vals = Review(id, product_name_r, user_r, rating_r, comment_r)
            review_repo.update(id, review_vals)

        elif rev_crud_op == 'delete':
            id = int(input("enter review id for deletion:"))
            review_repo.delete(id)

        elif rev_crud_op == 'search':
            id = input("enter user id for search:")
            print(review_repo.search(id))

        elif rev_crud_op == 'commit':
            commit_name = input('enter Commit name:')
            review_uow.commit(commit_name)

        elif rev_crud_op == 'rollback':
            rollback_name = input('enter the name of commit to rollback:')
            review_uow.rollback(rollback_name)

        elif rev_crud_op == 'exit':
            break

        else:
            print('wrong key')
else:
    print("Wrong Key! Try again")
