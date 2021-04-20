"""
Why: you want to only initiate one instance of a class ever, and only every make changes to this one class

Example: You have a class which holds global app settings. There is no point in having multiple instances of this, so a single instance will encapsulate the
entire app settings.

"""


class Singleton(object):
    def __new__(cls, *args, **kwds):
        it = cls.__dict__.get("__it__")
        if it is not None:
            return it
        cls.__it__ = it = object.__new__(cls)
        it.init(*args, **kwds)
        return it

    def init(self, *args, **kwds):
        pass
