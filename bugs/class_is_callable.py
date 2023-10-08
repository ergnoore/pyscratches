import typing as t


class MyClass:

    def __init__(self, a: int, b: str) -> None:
        print(a, b)


def is_callable(obj: t.Callable) -> None:
    print(obj)


is_callable(MyClass)
