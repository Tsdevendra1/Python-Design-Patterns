"""
Why: You want to initiate a concrete implementation of some interface based on some given parameters

Example: You want to serialize some data, but you may want "JSON" or "XML" serialization. A factory would give you a concrete implementation to serialize
this data

"""
from abc import ABC, abstractmethod
from enum import Enum
from typing import Dict


class SerializerInterface(ABC):

    @abstractmethod
    def serialize(self, data: Dict) -> str:
        pass


class SerializerFormat(Enum):
    json = 0
    xml = 1


class JSONSerialization(SerializerInterface):

    def serialize(self, data: Dict) -> str:
        # Implementation omitted
        pass


class XMLSerialization(SerializerInterface):

    def serialize(self, data: Dict) -> str:
        # Implementation omitted
        pass


def serializer_factory(serialization_format: SerializerFormat) -> SerializerInterface:
    if serialization_format == SerializerFormat.json:
        return JSONSerialization()
    elif serialization_format == SerializerFormat.xml:
        return XMLSerialization()


def main():
    data = {"test_data": 0}
    serialize = serializer_factory(serialization_format=SerializerFormat.json)
    serialize.serialize(data=data)


if __name__ == "__main__":
    main()
