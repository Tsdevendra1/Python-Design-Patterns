"""
Why: You have a tree structure and you want to be able to use leaf and non leaf nodes with the same interface.

Words:
    Composite -> Part of the tree that can hold child leafs
    Component -> Any node of the tree
"""
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Optional, List


class ComponentInterface(ABC):
    _parent: Optional[ComponentInterface] = None

    def set_parent(self, parent: Optional[ComponentInterface]):
        self._parent = parent

    def add(self, component: ComponentInterface):
        pass

    def remove(self, component: ComponentInterface):
        pass

    def do_some_operation(self) -> str:
        pass

    # Use this to check whether you can use the add/remove operations
    @abstractmethod
    def is_composite(self) -> bool:
        pass


class Leaf(ComponentInterface):
    # Leaf doesn't implement add or remove

    def is_composite(self) -> bool:
        return False

    def do_some_operation(self) -> str:
        # Leaves normally do the bulk of the operations, implementation omitted
        pass


class Composite(ComponentInterface):
    _children: [ComponentInterface] = []

    def add(self, component: ComponentInterface):
        component.set_parent(parent=self)
        self._children.append(component)

    def remove(self, component: ComponentInterface):
        component.set_parent(parent=None)
        self._children.remove(component)

    def do_some_operation(self) -> str:
        result: List[str] = []
        for child in self._children:
            result.append(child.do_some_operation)

        return "".join(result)

    def is_composite(self) -> bool:
        return True
