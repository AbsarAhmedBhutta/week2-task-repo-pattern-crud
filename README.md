# week2-Assignment

**Implement Unit of work, repository pattern (CRUD and search operations) for at
least 5 entities using generics and abstract classes and interfaces** 


This Assignment works on command line , So According to this I have tryed to Implement Unit of work, repository pattern
CRUD and search operations.

I have created 6 modules in total they are:
- entitymodel

    I have created 5 entites User,Product,Order,Category and Review.In python entities refer as
    Db Tables or Classes. I am not using db here thats why i am using classes instead,

- IRepository
    This module is the interface for other repositories, python doesnnt have builtin interface So i have 
    implemented interface using ABC in which I have defined the Generic Structure for the repositories it contain 
    CRUD methods and Search.

- EntityRepository
    In this module the methods are implemented and each method ovverrides the methods in interface
    I have used dict to perform data proccessing.

- IUnitOfWork
    This module is the interface for UnitOfWork.cantains Commit and Rollback Functions

- UnitOfWork
    In this module commit and rollback functions are implemented for all entities.
- 
- and finally app.py
    finally this module has the business logic for this assignment.


