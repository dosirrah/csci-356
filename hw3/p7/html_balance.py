from stack import Stack


def html_balance(fname: str) -> bool:
    """
    Test whether there are as many '<' characters as '>' characters in the
    passed HTML file.  This does not take into account HTML comments.

    :param fname:
    :return: whether the HTML file has a balanced number of less than and greater than
       characters.
    """

    stack = Stack()
    with open(fname) as fp:
        while True:
            ch = fp.read(1)
            if not ch:
                break

            # this is a bit silly.  We could just use a counter.
            if ch == "<":
                stack.push("<")
            elif ch == ">":
                if stack.is_empty():
                    return False
                stack.pop()

    return stack.is_empty()