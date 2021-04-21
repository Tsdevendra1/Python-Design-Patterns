"""
Why: You want to iterate over some collection, but want to decouple this iteration from the implementation of the collection. E.g. you might have a set,
dictionary or list which hold int values. You maybe not care which data structure it uses, just that you want to iterate over it
"""
from abc import ABC, abstractmethod
from typing import Optional, Any


class CollectionOfWords:
    words: [str] = []

    def append(self, word: str):
        self.words.append(word)


class IteratorInterface(ABC):

    @abstractmethod
    def next(self) -> Any:
        pass


class CollectionOfWordsIterator(IteratorInterface):

    def __init__(self, word_collection: CollectionOfWords):
        self._current_index = 0
        self._word_collection = word_collection

    def next(self) -> Optional[str]:
        index = self._current_index
        self._current_index += 1
        if index < len(self._word_collection.words):
            return self._word_collection.words[index]
        else:
            return None


def client(some_iterator: IteratorInterface) -> [str]:
    current_value = some_iterator.next()
    values: [str] = []
    while current_value is not None:
        values.append(current_value)
        current_value = some_iterator.next()

    return values


def main():
    collection = CollectionOfWords()
    collection.append("word 1")
    collection.append("word 2")
    iterator = CollectionOfWordsIterator(word_collection=collection)
    values = client(some_iterator=iterator)
    assert (values == ["word 1", ["word 2"]])


if __name__ == "__main__":
    pass
