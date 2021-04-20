"""
Why: You want to be able to choose an implementation of some interface at runtime

Example: You have a logger, which allows the implementation to be selected at runtime. Sometimes you want to output the log to a textfile, sometimes you may
want to do something completely different.

Words:
    Strategy Interface -> The interface that defines what a "Strategy" can implement
    Strategy -> A concrete implementation of a "Strategy Interface"
    Context -> Some class/function/etc... that requires a "Strategy"
"""
from abc import ABC, abstractmethod
from typing import List


class StrategyInterface(ABC):
    """
    The Strategy interface declares operations common to all supported versions
    of some algorithm.

    The Context uses this interface to call the algorithm defined by Concrete
    Strategies.
    """

    @abstractmethod
    def do_algorithm(self, data: str) -> int:
        pass


class Context:

    def __init__(self, strategy: StrategyInterface):
        self.__strategy = strategy

    def run(self, data: str) -> int:
        return self.__strategy.do_algorithm(data=data)


class ExampleStrategy1(StrategyInterface):

    def do_algorithm(self, data: str) -> int:
        return int(data)


class ExampleStrategy2(StrategyInterface):

    def do_algorithm(self, data: str) -> int:
        # Does nothing with data and always returns 4
        return 4


def main():
    selected_strategy_at_runtime = ExampleStrategy1()
    context = Context(strategy=selected_strategy_at_runtime)

    output = context.run(data="0")
    assert output == 0

if __name__ == "__main__":
    main()
