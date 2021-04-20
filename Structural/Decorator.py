"""
Why: You want to add some functionality on top of some concrete implementation of an interface

Example: You want to log everytime a function gets called, you can wrap the class in a decorator which logs this function any time its called.

Caveats: Both the implementation and decorator must conform to the same interface that is to be decorated

Words:
    Strategy Interface -> The interface that defines what a "Strategy" can implement
    Strategy -> A concrete implementation of a "Strategy Interface"
    Context -> Some class/function/etc... that requires a "Strategy"
"""
from abc import ABC, abstractmethod


class SomeInterface(ABC):

    @abstractmethod
    def some_function(self) -> int:
        pass


class ConcreteImplementationOfSomeInterface(SomeInterface):

    def some_function(self) -> int:
        return 45


class LogTheFunctionDecorator(SomeInterface):

    def __init__(self, concrete_implementation: SomeInterface):
        self.__concrete_implementation = concrete_implementation

    def __do_some_logging(self):
        # Implementation omitted
        pass

    def some_function(self) -> int:
        concrete_implementation_value = self.__concrete_implementation.some_function()
        self.__do_some_logging()
        return concrete_implementation_value
