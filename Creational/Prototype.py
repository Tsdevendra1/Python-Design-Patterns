"""
Why: You have a class you want to copy/clone. Traditionally, you would initiate a new instance of this class and copy over all the property values. However,
this doesn't always work because the class may have private properties which can't be copied over from outside the class.
To get around this we delegate the copying to the class we want to copy. We provide a common interface, e.g. .clone() so that we're not dependent on the
concrete type of the class either.

Another reason to use this pattern is when cloning is time consuming/requires more resources than you have available.


Its called prototype because the class that implements .clone() is consider the prototype, and its values are copied to
the clone.
"""
from abc import ABC, abstractmethod


class CloneInterface(ABC):

    # It is up to the implementer to choose whether it is a deep or shallow copy
    @abstractmethod
    def clone(self):
        pass


class SomeClassWeWanToClone(CloneInterface):

    def __init__(self, int_value: int, string_value: str):
        self.__int_value = int_value
        self.__string_value = string_value

    def clone(self):
        # Notice that if we wanted to clone this class from the outside, it would be impossible since int_value and _string_value are private
        return SomeClassWeWanToClone(int_value=self.__int_value, string_value=self.__string_value)
