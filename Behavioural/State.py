"""
Why: You want to change the behaviour of some class, based on some internal state.

Example: You have a location tracker class, you  start the tracker, then pause the tracker. When the tracker is paused, pausing it again won't
have any behaviour, compare to when the tracker was enabled. This shows an example where a .pause_tracker() function would have different functionality
depending on the internal state

Words:
    Context -> The "Parent" class whos behaviour changes based on internal state
    State -> The internal state of the parent, which has behaviour linked to it
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional


class Context(ABC):

    @abstractmethod
    def transition_to_state(self, state: TrackerStateInterface):
        pass


class TrackerStateInterface(ABC):

    @abstractmethod
    def start_tracker(self):
        pass

    @abstractmethod
    def pause_tracker(self):
        pass


class EnabledLocationTrackerState(TrackerStateInterface):

    def __init__(self, context: Context):
        self._context = context

    def pause_tracker(self):
        # Do some stuff related to pausing...
        print("pause in enabled tracker")
        self._context.transition_to_state(state=DisabledLocationTrackerState(context=self._context))

    def start_tracker(self):
        # Do some stuff related to starting...
        print("start in enabled tracker")
        pass


class DisabledLocationTrackerState(TrackerStateInterface):

    def __init__(self, context: Context):
        self._context = context

    def pause_tracker(self):
        # Do some stuff related to pausing...
        print("pause in disabled tracker")
        pass

    def start_tracker(self):
        # Do some stuff related to starting...
        print("start in disabled tracker")
        self._context.transition_to_state(state=EnabledLocationTrackerState(context=self._context))


class LocationTracker(Context):

    def __init__(self):
        self.__state: TrackerStateInterface = EnabledLocationTrackerState(context=self)
        self.__state.context = self

    def start_tracking(self):
        self.__state.start_tracker()

    def pause_tracker(self):
        self.__state.pause_tracker()

    def transition_to_state(self, state: TrackerStateInterface):
        self.__state = state


def main():
    tracker = LocationTracker()
    tracker.start_tracking()
    tracker.pause_tracker()
    tracker.start_tracking()


if __name__ == "__main__":
    main()
