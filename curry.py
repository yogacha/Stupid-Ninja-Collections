from typing import List, Callable, Hashable
from functools import update_wrapper


def args_post_application(wrapped: Callable):    
    """
    Partial applied keyword arguments of `wrapped` function.

    Before:
        f(1, 2, 3, x=4, y=5, z=6)
    After:
        kwargs_acceptor(x=4, y=5, z=6)(1, 2, 3)
    """
    def kwargs_acceptor(**kwargs):

        def wrapper(*args, **kw):
            kw = {**kwargs, **kw}
            return wrapped(*args, **kw)

        # copy & update, not changing meta function
        kwargs = {**wrapped.__kwdefaults__, **kwargs}
        update_wrapper(wrapper, wrapped)

        return wrapper
    
    update_wrapper(kwargs_acceptor, wrapped)
    kwargs_acceptor.__doc__ = """NOTE: Post applied args, use kwargs only.\n\n"""
    if wrapped.__doc__:
        kwargs_acceptor.__doc__ += wrapped.__doc__

    return kwargs_acceptor
