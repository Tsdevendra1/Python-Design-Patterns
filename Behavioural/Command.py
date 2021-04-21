"""
Why: Its callbacks, but you encapsulate the call back in a class so that you already have all the information required to execute it at any given time. The
thing calling the call back also doesn't need to know what information the call back requires.

Example: You have a stock order executor class. It can call .execute() on any stock order. But the executor doesn't need to know if its a build or sell stock order.
It can call the stock orders at any given time
"""
from abc import ABC, abstractmethod
from typing import Optional


class CommandInterface(ABC):

    @abstractmethod
    def execute_command(self):
        pass


class ConcreteCommand(CommandInterface):

    def __init__(self, required_data_for_command: str):
        self.__data = required_data_for_command

    def execute_command(self):
        print(self.__data)


class CommandExecutor:
    __before_start_operation: Optional[CommandInterface]
    __after_operation_end: Optional[CommandInterface]

    def set_before_operation_starts_command(self, command: CommandInterface):
        self.__before_start_operation = command

    def important_operation(self):

        before = self.__before_start_operation
        after = self.__after_operation_end
        if before is not None:
            before.execute_command()

        # IMPORTANT STUFF HAPPENS HERE...

        if after is not None:
            after.execute_command()

    def set_after_operation_end_command(self, command: CommandInterface):
        self.__after_operation_end = command


def main():
    executor = CommandExecutor()
    command_1 = ConcreteCommand(required_data_for_command="Hello")
    command_2 = ConcreteCommand(required_data_for_command="Context unaware")

    executor.set_before_operation_starts_command(command=command_1)
    executor.set_after_operation_end_command(command=command_2)

    executor.important_operation()


if __name__ == "__main__":
    main()
