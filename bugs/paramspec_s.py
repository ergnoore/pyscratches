import typing as t


P = t.ParamSpec('P')


class WithInitProtocol(t.Protocol[P]):

    def __init__(self, *args: P.args, **kwargs: P.kwargs) -> None:
        raise NotImplementedError()


class WithInitExample:

    def __init__(self, foo: int) -> None:
        print(foo)


def wrap(obj: t.Type[WithInitProtocol[P]]) -> t.Callable[P, None]: raise NotImplementedError(obj)


wrap(WithInitExample)()  # Incorrect?
