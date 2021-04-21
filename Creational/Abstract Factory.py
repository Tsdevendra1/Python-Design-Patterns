"""
Why: You want to create a group of classes which are related in some way. You don't care about the implementation of these classes, just that they follow
some interface. An abstract factory provides an interface to create each class separately, a concrete factory would give concrete implementations of the
classes to be created. Each concrete factory must ensure that the classes created are compatible with each other.

Example: You have an abstract factory called "Document Creator". You want to be able to .create_resume() and .create_cover_letter(). One concrete factory might
create return a FancyResume and a FancyCoverLetter, whereas another might create a ModernResume, and ModernCoverLetter. You can see that each factory groups
the classes as they are compabtilbe with each other
"""
from abc import ABC, abstractmethod


class CoverLetter(ABC):

    @abstractmethod
    def do_something(self):
        pass


class Resume(ABC):

    @abstractmethod
    def do_something(self):
        pass


class DocumentCreatorAbstractFactory(ABC):

    @abstractmethod
    def create_resume(self) -> Resume:
        pass

    @abstractmethod
    def create_cover_letter(self) -> CoverLetter:
        pass


class FancyResume(Resume):
    def do_something(self):
        pass


class FancyCoverLetter(CoverLetter):
    def do_something(self):
        pass


class ModernResume(Resume):
    def do_something(self):
        pass


class ModernCoverLetter(CoverLetter):
    def do_something(self):
        pass


class FancyDocumentCreator(DocumentCreatorAbstractFactory):
    def create_resume(self) -> Resume:
        return FancyResume()

    def create_cover_letter(self) -> CoverLetter:
        return FancyCoverLetter()


class ModernDocumentCreator(DocumentCreatorAbstractFactory):
    def create_resume(self) -> Resume:
        return ModernResume()

    def create_cover_letter(self) -> CoverLetter:
        return ModernCoverLetter()


def client(factory: DocumentCreatorAbstractFactory):
    resume = factory.create_resume()
    cover_letter = factory.create_cover_letter()

    resume.do_something()
    cover_letter.do_something()


def main():
    modern_factory = ModernDocumentCreator()
    fancy_factory = FancyDocumentCreator()

    # Works with both factorys
    client(factory=modern_factory)
    client(factory=fancy_factory)


if __name__ == "__main__":
    main()
