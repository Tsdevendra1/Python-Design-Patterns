"""
Why: You want to wrap an existing concrete interface (like a decorator), the difference is you control access to the object being decorated, therefore also
restricting functionality depending on some required condition. It is also more likely that the proxy knows the concrete type of the class it is proxying
compared to the decorator pattern where this is less likely.
"""
from abc import ABC, abstractmethod


class SomeInterface(ABC):

    @abstractmethod
    def do_something(self):
        pass


class ConcreteImplementation(SomeInterface):
    def do_something(self):
        print("hello")


class Proxy(SomeInterface):

    def __init__(self, concrete: ConcreteImplementation):
        self.__concrete = concrete

    def do_something(self):
        if self.__check_has_access():
            self.__concrete.do_something()
            self.__log_has_access()

    def __check_has_access(self) -> bool:
        # Do some checks...
        return False

    def __log_has_access(self):
        # Do some stuff here...
        pass
