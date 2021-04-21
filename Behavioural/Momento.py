"""
Why: You have a class with state. You want to be able to rollback changes on this class without exposing the actual state.

"""
from __future__ import annotations

import copy
import datetime
from abc import ABC, abstractmethod


class ClassWithState:
    __state: [str] = []

    def print_current_state(self):
        print(self.__state)

    def modify_state(self):
        self.__state.append("Something new")

    def save(self) -> Momento:
        return ConcreteMomento(name="ewq", date=datetime.date.today(), state=self.__state)

    def restore(self, momento: Momento):
        # Here we don't reference the concrete type of the momento here, the idea is that the conrete type is never referenced, and hence the internal state
        # of this class is never exposed
        state = momento.get_internal_state()
        self.__state = state


# A memento saves the internal state of the class. However the interface doesn't show how the state is saved, only a concrete implementation does.
class Momento(ABC):

    @abstractmethod
    def get_name(self) -> str:
        pass

    @abstractmethod
    def get_date_momento_was_saved(self) -> datetime.date:
        pass


class ConcreteMomento(Momento):

    def __init__(self, name: str, date: datetime.date, state: [str]):
        self.__name = name
        self.__date = date
        self.__state = copy.deepcopy(state)

    def get_date_momento_was_saved(self) -> datetime.date:
        return self.__date

    def get_name(self) -> str:
        return self.__name

    def get_internal_state(self) -> [str]:
        return self.__state


class CareTaker:
    __momentos: [Momento] = []

    def __init__(self, originator: ClassWithState):
        self.__originator = originator

    def save(self):
        momento = self.__originator.save()
        self.__momentos.append(momento)

    def undo(self):
        if len(self.__momentos) == 0:
            return

        last_momento = self.__momentos.pop()
        self.__originator.restore(momento=last_momento)


def main():
    originator = ClassWithState()
    caretaker = CareTaker(originator=originator)

    originator.print_current_state()
    caretaker.save()

    originator.modify_state()
    originator.print_current_state()
    caretaker.save()

    originator.modify_state()
    originator.print_current_state()
    caretaker.save()

    caretaker.undo()
    originator.print_current_state()
    caretaker.undo()
    originator.print_current_state()
    caretaker.undo()
    originator.print_current_state()


if __name__ == "__main__":
    main()
