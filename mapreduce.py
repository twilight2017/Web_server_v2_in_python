from functools import reduce
from operator import add

"""
    map(func, *iterables) --> map object

    Make an iterator that computes the function using arguments from
    each of the iterables.  Stops when the shortest iterable is exhausted.
    map函数用变量集中的每个变量去执行这个函数
    """
ls = map(lambda x: len(x), ["ana", "bob", "catty", "dogge"])
print('ls', ls)
reduce(add, ls)