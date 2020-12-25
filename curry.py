from typing import Callable
from functools import partial, update_wrapper


def args_post_application(wrapped: Callable):    
    """
    Partial applied keyword arguments of `wrapped` function.

    Before:
        f(1, 2, 3, x=4, y=5, z=6)
    After:
        kwargs_acceptor(x=4, y=5, z=6)(1, 2, 3)
    """
    def kwargs_acceptor(**kwargs):
        wrapper = partial(wrapped, **kwargs)
        wrapper.__name__ = wrapped.__name__
        return wrapper
    
    update_wrapper(kwargs_acceptor, wrapped)
    kwargs_acceptor.__doc__ = """NOTE: Post applied args, use kwargs only.\n\n"""
    if wrapped.__doc__:
        kwargs_acceptor.__doc__ += wrapped.__doc__

    return kwargs_acceptor
