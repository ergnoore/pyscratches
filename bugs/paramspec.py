import typing as t


P = t.ParamSpec('P')


class MyCallable:

    def __call__(self, arg: int) -> int:
        return arg + 1


def func(arg: str) -> int:
    return int(arg) + 1


def test(a: t.Callable[P, int], b: t.Callable[P, int]):
    print(a, b)


test(MyCallable(), func)  # OK?
