"""
Why: You already have some interface requirement by a client you wrote. You want to use a third party library, but it doesn't fit the interface requirement.
You wrap the third party library in an adapter class to fit the interface requirement.

Example: You have a class which holds global app settings. There is no point in having multiple instances of this, so a single instance will encapsulate the
entire app settings.

"""
from abc import ABC, abstractmethod


class ClientSpecifiedInterface(ABC):

    @abstractmethod
    def client_required_method(self) -> int:
        pass


class ThirdPartyLibrary:

    def has_some_useful_functionality(self) -> int:
        pass


class AdapterClass(ClientSpecifiedInterface):

    def __init__(self, third_party_library: ThirdPartyLibrary):
        self.__third_party_library = third_party_library

    def client_required_method(self) -> int:
        return self.__third_party_library.has_some_useful_functionality()
