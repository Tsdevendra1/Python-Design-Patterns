"""
Why: You want to have reusable components which can send events, another class may want to be aware of these events, but to provide loose coupling and
re-usability you use a mediator to dictate how these classes interact with each other.

"""
from abc import ABC, abstractmethod
from typing import Optional


class MediatorInterface(ABC):

    @abstractmethod
    def notify_mediator_of_event(self, sender: object, event: str):
        pass


class BaseComponent:
    _mediator: Optional[MediatorInterface]

    def set_mediator(self, mediator: MediatorInterface):
        self._mediator = mediator


class Component1(BaseComponent):

    def do_a(self):
        # DO stuff related to a..
        print("a")
        self._mediator.notify_mediator_of_event(sender=self, event="A")

    def do_b(self):
        # DO stuff related to a..
        print("b")
        self._mediator.notify_mediator_of_event(sender=self, event="B")


class Component2(BaseComponent):

    def do_c(self):
        # DO stuff related to a..
        print("c")
        self._mediator.notify_mediator_of_event(sender=self, event="C")

    def do_d(self):
        # DO stuff related to a..
        print("d")
        self._mediator.notify_mediator_of_event(sender=self, event="D")


class ConcreteMediator(MediatorInterface):

    def __init__(self, component_1: Component1, component_2: Component2):
        self.__component_1 = component_1
        self.__component_1.set_mediator(mediator=self)
        self.__component_2 = component_2
        self.__component_2.set_mediator(mediator=self)

    def notify_mediator_of_event(self, sender: object, event: str):
        if event == "A":
            self.__component_2.do_d()
        if event == "D":
            self.__component_1.do_b()


def main():
    component_1 = Component1()
    component_2 = Component2()
    mediator = ConcreteMediator(component_1=component_1, component_2=component_2)

    component_1.do_a()

    component_2.do_d()


if __name__ == "__main__":
    main()
