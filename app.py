from EntityRepository import *

from entitymodel import *

user_repo = UserRepository()
product_repo = ProductRepository()
order_repo = OrderRepository()
catagory_repo = CategoryRepository()
review_repo = ReviewRepository()

entity_work = input('''
ENTER THE ENTITY TO WORK ON:
> enter 'U' for User,
> enter 'P' for Product,
> enter 'O' for Order,
> enter 'C' for Category,
> enter 'R' for Review,
:-''')


if entity_work == 'U':
    total_user_entries = int(input("How many entries you want to do"))
    for i in range(total_user_entries):
        id = input("enter user id")
        name = input("enter user name")

        user = User(id, name)

        user_repo.add(id, [user])

    for ops in range(4):
        user_crud_op = input('enter update/get/delete operations for user')
        if user_crud_op == 'get':
            users = user_repo.get()
            for key, user_list in users.items():
                for user in user_list:
                    print(user)
        elif user_crud_op == 'update':
            for i in range(total_user_entries):
                id = input("enter user id for updating:")
                name = input("enter user updated name:")

                user = User(id, name)

                user_repo.update(id, [name])
        elif user_crud_op == 'delete':
            id = int(input("enter user id for deletion:"))
            user_repo.delete(id)

        else:
            print('wrong key')

elif entity_work == 'P':
    total_user_entries = int(input("How many entries you want to do"))
    for i in range(total_user_entries):
        id = input("enter product id")
        product_name = input("enter product name")
        product_price = float(input("enter product price"))

        product_vals = Product(id, product_name, product_price)

        product_repo.add(id, [product_vals])

    for ops in range(4):
        product_crud_op = input('enter update/get/delete operations for user')
        if product_crud_op == 'get':
            users = product_repo.get()
            for key, product_list in users.items():
                for product in product_list:
                    print(product)
        elif product_crud_op == 'update':
            id = int(input("enter product id"))
            product_name = input("enter product name")
            product_price = float(input("enter product price"))

            product_vals = Product(id, product_name, product_price)

            product_repo.add(id, [product_vals])
        elif product_crud_op == 'delete':
            id = int(input("enter user id for deletion:"))
            product_repo.delete(id)

        else:
            print('wrong key')

elif entity_work == 'O':
    total_user_entries = int(input("How many entries you want to do"))
    for i in range(total_user_entries):
        id = int(input("enter order id"))
        user_order_name = input("enter order name")
        order_order_user = input("enter order user nme")

        order_vals = Product(id, user_order_name, order_order_user)

        order_repo.add(id, [order_vals])

    for ops in range(4):
        product_crud_op = input('enter update/get/delete operations for user')
        if product_crud_op == 'get':
            orders = order_repo.get()
            for key, order_list in orders.items():
                for product in order_list:
                    print(product)
        elif product_crud_op == 'update':
            id = int(input("enter order id"))
            user_order_name = input("enter order name")
            order_order_user = input("enter order user nme")

            order_vals = Product(id, user_order_name, order_order_user)

            order_repo.add(id, [order_vals])
        elif product_crud_op == 'delete':
            id = int(input("enter order id for deletion:"))
            order_repo.delete(id)

        else:
            print('wrong key')
elif entity_work == 'C':
    total_user_entries = int(input("How many entries you want to do"))
    for i in range(total_user_entries):
        id = int(input("enter product id"))
        catagory_name = input("enter catagory name")

        catagory_vals = Category(id, catagory_name)

        catagory_repo.add(id, [catagory_vals])

    for ops in range(4):
        catagory_crud_op = input('enter update/get/delete operations for user')
        if catagory_crud_op == 'get':
            catagorys = catagory_repo.get()
            for key, catagory_list in catagorys.items():
                for product in catagory_list:
                    print(product)
        elif catagory_crud_op == 'update':
            id = int(input("enter catagory id"))
            catagory_name = input("enter catagory name")

            catagory_vals = Category(id, catagory_name)

            catagory_repo.add(id, [catagory_vals])
        elif catagory_crud_op == 'delete':
            id = int(input("enter catagory id for deletion:"))
            catagory_repo.delete(id)

        else:
            print('wrong key')
elif entity_work == 'R':
    total_user_entries = int(input("How many entries you want to do"))
    for i in range(total_user_entries):
        id = int(input("enter review id"))
        product_name_r = input("enter review name")
        user_r = input("enter review name")
        rating_r = input("enter review name")
        comment_r = input("enter review name")

        review_vals = Review(id, product_name_r, user_r, rating_r, comment_r)

        review_repo.add(id, [review_vals])

    for ops in range(4):
        catagory_crud_op = input('enter update/get/delete operations for user')
        if catagory_crud_op == 'get':
            reviews = review_repo.get()
            for key, review_list in reviews.items():
                for product in review_list:
                    print(product)
        elif catagory_crud_op == 'update':
            id = int(input("enter review id"))
            product_name_r = input("enter review name")
            user_r = input("enter review name")
            rating_r = input("enter review name")
            comment_r = input("enter review name")

            review_vals = Review(id, product_name_r,user_r, rating_r, comment_r)

            review_repo.add(id, [review_vals])
        elif catagory_crud_op == 'delete':
            id = int(input("enter review id for deletion:"))
            catagory_repo.delete(id)

        else:
            print('wrong key')
else:
    print("Wrong Key! Try again")



