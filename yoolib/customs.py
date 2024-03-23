from enum import StrEnum
from string import digits, punctuation
from typing import TypeAlias, get_args


class classproperty:
    """
    Decorator that converts a method with a single cls argument into a property
    that can be accessed directly from the class.
    """

    def __init__(self, method=None):
        self.fget = method

    def __get__(self, instance, cls=None):
        return self.fget(cls) if self.fget else None

    def getter(self, method):
        self.fget = method
        return self


def to_enum_attr(value: str):
    table = str.maketrans(" ", "_", punctuation)
    return_value = value.translate(table).upper()
    if return_value[0] in digits:
        return_value = f"_{return_value}"
    return return_value


class TypeTool:
    """
    Tool for type hinting with `Literal[str, ...]`

    Usage:
    ```
    from typing import Literal
    from yoolib.customs import TypeTool

    class Foo(TypeTool):
        type_alias = Literal["a", "b", "c"]

    >>> Foo.type_alias
    typing.Literal["a", "b", "c"]

    >>> Foo.type_tuple
    ("a", "b", "c")

    >>> Foo.type_enum
    <enum 'Foo_Enum'>

    >>> Foo.type_enum.A
    <enum 'Foo_Enum.A': 'a'>

    >>> print(Foo.type_enum.B, Foo.type_enum.C)
    b c
    ```
    """

    type_alias: TypeAlias

    @classproperty
    def type_tuple(cls) -> tuple:
        assert cls.type_alias
        return get_args(cls.type_alias)

    @classproperty
    def type_enum(cls) -> StrEnum:
        assert cls.type_tuple
        return StrEnum(
            f"{cls.__name__}_Enum", {to_enum_attr(i): i for i in cls.type_tuple}
        )
