"""
Why: You want to interact/add some behaviour to an existing class, but you don't want to change the class itself.

"""
from __future__ import annotations

from abc import ABC, abstractmethod


# The visitor should know the concrete type
class AnyVisitor(ABC):

    @abstractmethod
    def visit_a(self, a: A):
        pass

    @abstractmethod
    def visit_b(self, b: B):
        pass


class ConcreteVisitor1(AnyVisitor):

    def visit_a(self, a: A):
        # Process a...
        pass

    def visit_b(self, b: B):
        # Process b...
        pass


class ConcreteVisitor2(AnyVisitor):

    def visit_a(self, a: A):
        # Process a...
        pass

    def visit_b(self, b: B):
        # Process b...
        pass


class Visitable(ABC):

    @abstractmethod
    def accept(self, visitor: AnyVisitor):
        pass


class A(Visitable):

    def accept(self, visitor: AnyVisitor):
        visitor.visit_a(a=self)


class B:

    def accept(self, visitor: AnyVisitor):
        visitor.visit_b(b=self)


def main():
    a = A()
    b = B()
    visitor_1 = ConcreteVisitor1()
    visitor_2 = ConcreteVisitor2()

    a.accept(visitor=visitor_1)
    a.accept(visitor=visitor_2)

    b.accept(visitor=visitor_1)
    b.accept(visitor=visitor_2)


if __name__ == "__main__":
    main()
