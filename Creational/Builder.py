"""
Why: You want to initiate/setup a complex class with a simple interface.

Example: You want to build a query, querying certain aspects
"""

from __future__ import annotations


class QueryOperation:
    def __init__(self, something_useful_for_the_query: str):
        self._property = something_useful_for_the_query


class Query:
    _operations: [QueryOperation]

    def __init__(self, operations: [QueryOperation]):
        self._operations = operations

    def run(self):
        print(self._operations)


class QueryBuilder:
    _operations: [QueryOperation] = []

    def add_some_operation1(self, data: str) -> QueryBuilder:
        self._operations.append(QueryOperation(data))
        return self

    def add_some_operation2(self, data: str) -> QueryBuilder:
        self._operations.append(QueryOperation(data))
        return self

    def build(self) -> Query:
        return Query(operations=self._operations)


def main():
    query = QueryBuilder().add_some_operation1("data").add_some_operation2("data 2").build()
    query.run()


if __name__ == "__main__":
    main()
