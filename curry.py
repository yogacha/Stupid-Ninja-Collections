from typing import Callable
import functools


def keyword_first(wrapped: Callable):    
    """
    Partial applied keyword arguments of `wrapped` function.

    Before:
        f(1, 2, 3, x=4, y=5, z=6)
    After:
        kwargs_acceptor(x=4, y=5, z=6)(1, 2, 3)
    """
    def kwargs_acceptor(**kwargs):
        wrapper = functools.partial(wrapped, **kwargs)
        wrapper.__name__ = wrapped.__name__
        return wrapper
    
    functools.update_wrapper(kwargs_acceptor, wrapped)
    kwargs_acceptor.__doc__ = """NOTE: Pass kwargs only.\n\n"""
    if wrapped.__doc__:
        kwargs_acceptor.__doc__ += wrapped.__doc__

    return kwargs_acceptor


def update_wrapper(wrapper, wrapped, *args, **kwargs):
    """
    Extended version of `functools.update_wrapper` that pass `__kwdefaults__`
    """
    res = functools.update_wrapper(wrapper, wrapped, *args, **kwargs)
    wrapper.__kwdefaults__ = wrapped.__kwdefaults__
    return res

functools.update_wrapper(update_wrapper,  functools.update_wrapper)  # inherit doc string
