# import asyncio
# from functools import wraps
#
# def async_step(func):
#     """
#     Custom decorator to run async pytest-bdd steps properly.
#     """
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         # Ensures the coroutine function runs in an asyncio event loop
#         return asyncio.run(func(*args, **kwargs))
#     return wrapper
from types import SimpleNamespace

from pytest_bdd.steps import given, when, then

def async_step(step_decorator):
    def wrapper(step):
        @step_decorator
        def sync_step(*args, **kwargs):
            # Ensure the coroutine is awaited
            return step(*args, **kwargs)
        return sync_step
    return wrapper


"""Convert a nested SimpleNamespace to a nested dictionary."""
def ns_to_dict(namespace):
    if not isinstance(namespace, SimpleNamespace):
        return namespace  # Return the value if it's not a SimpleNamespace
    return {key: ns_to_dict(value) for key, value in vars(namespace).items()}


def dict_to_namespace(d):
    """Convert a dictionary to a SimpleNamespace."""
    if isinstance(d, dict):
        return SimpleNamespace(**{k: dict_to_namespace(v) if isinstance(v, dict) else v for k, v in d.items()})
    return d