



# class MyClass:

#     def __new__(cls):
#         pass 

#     def __init__(self, name):
#         self.name = name

#     @property
#     def name(self):
#         return self.name
    
#     @name.getter
#     def name(self, name):
#         if not isinstance(name, str):
#             raise

#     @classmethod
#     def greet(cls):
#         print(f"Hello, my name is {cls.name}")

#     @staticmethod
#     def greet_2():
#         print('SOme')



        

# object_1 = MyClass(name='A')

# # def some_decorator(*args, **kwargs):
# #     def two(func):
# #         def wrapper(*args, **kwargs):
# #             print('Before calling')
# #             func()
# #             print('After calling')

# #         return wrapper
# #     return two


# @some_decorator('some/path')
# def one():
#     print('I am one funcution')

# one()

