"""
Why: You have many composable classes. But you want a simple interface to work with. You wrap all those composable classes in a class which provides this
simple interface.

"""


class ComposableClass1:

    def does_some_useful_stuff(self) -> int:
        pass


class ComposableClass2:

    def some_other_useful_stuff(self) -> int:
        pass


class Facade:

    def __init__(self, class1: ComposableClass1, class2: ComposableClass2):
        self.__class1 = class1
        self.__class2 = class2

    def simple_interface(self) -> int:
        return self.__class1.does_some_useful_stuff() + self.__class2.some_other_useful_stuff()
