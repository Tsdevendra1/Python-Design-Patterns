"""
Why: You want to receive updates/notification when some change/event occurs in another object

Example: You have an auctioneer, the bidders need to know when a bid has been received. The bidder would be an observer.

Words:
    Subject -> The class that updates the observers
    Observer -> The class that wants to be notified
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, updated_subject_or_value: Subject):
        pass


class Subject(ABC):

    @abstractmethod
    def add(self, observer: Observer):
        pass

    @abstractmethod
    def remove(self, observer: Observer):
        pass

    @abstractmethod
    def notify_all_observers(self):
        pass


class ConcreteSubject(Subject):
    __observers: [Observer] = []

    def remove(self, observer: Observer):
        self.__observers.remove(observer)

    def add(self, observer: Observer):
        self.__observers.append(observer)

    def notify_all_observers(self):
        for observer in self.__observers:
            observer.update(updated_value_or_subject=self)


class ConcreteObserver(Observer):

    def update(self, updated_subject_or_value: Subject):
        # do something with updated value - implementation omitted
        pass
