"""
Why: You sent a request, there may be an arbitrary number of processing required on this request. You pass the request from the first client that handles the request
to the second, to the third, etc... until it reaches someone who wants to properly handle the request and return something based on the request. Everything
between the request and this end client merely gets the request as an input and returns the same request as an output.

Example: Middleware handler in django (the request is passed from one middleware to another, until it reaches the django code)

"""
from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):
    _next_handler: Handler = None

    def set_next_handler(self, handler) -> Handler:
        self._next_handler = handler
        # return the handler when setting the next handler, so it is easier to chain
        return handler

    @abstractmethod
    def handle_request(self, request: str) -> int:
        pass


class ConcreteHandler1(Handler):

    def handle_request(self, request: str) -> int:
        if request == "some value":
            return 4
        else:
            return self._next_handler.handle_request(request=request)


class ConcreteHandler2(Handler):

    def handle_request(self, request: str) -> int:
        if request == "another value":
            return 20
        else:
            return self._next_handler.handle_request(request=request)


class Client:

    def process_request(self, handler: Handler) -> int:
        return handler.handle_request(request="some data")


def main():
    client = Client()
    handler_1 = ConcreteHandler1()
    handler_2 = ConcreteHandler2()
    handler_1.set_next_handler(handler=handler_2)
    client.process_request(handler=handler_1)


if __name__ == "__main__":
    main()