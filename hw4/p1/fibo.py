

def fibo_recurse(n : int) -> list:
    """
    Create a list containing the Fibonacci numbers from 0 to and
    including n.  $F_0=0, F_1=1, F_n=F_{n-1}+F_{n-2}$.

    :param n: sequence contains up to and includeing $F_n$.
    :return: the sequence as a list.
    """
    def _recurse(n : int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        return _recurse(n-1) + _recurse(n-2)

    if n < 0:
        raise  ValueError
    x = []
    for i in range(0, n+1):
        x.append(_recurse(i))
    return x

def fibo_iterative(n: int) -> list:
    if n < 0:
        raise ValueError
    elif n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    x = [0, 1]
    for i in range(2, n+1):
        x.append(x[i-2] + x[i-1])
    return x

# x = fibo_recurse(8)
# print(x)
# x = fibo_iterative(8)
# print(x)
