"""
Why: You have some algorithm that needs to run. Most of it requires some common implementation, but part of the algorithm is allowed to be changed by subclasses
The template method refers to the common implementation part.

"""
from abc import ABC, abstractmethod


class SomeAbstractClass(ABC):

    def template_method(self) -> None:
        self.some_common_operation()
        self.some_common_operation_2()
        self.an_overridable_part_of_the_algorithm()

    def some_common_operation(self) -> None:
        print("something")

    def some_common_operation_2(self) -> None:
        print("something")

    @abstractmethod
    def an_overridable_part_of_the_algorithm(self):
        pass


class ConcreteClass(SomeAbstractClass):

    def an_overridable_part_of_the_algorithm(self):
        # Some custom behaviour here...
        pass


def client(implementation: SomeAbstractClass):
    # Notice we use the abstract class here since we don't care how its implemented
    pass