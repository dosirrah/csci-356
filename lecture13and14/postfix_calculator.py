"""This is a variant of 4.9.3.1 for postfix evaluation, but this supports
floating point values."""

from stack import Stack


def is_float(value):
    """
    Returns whether the passed string contains a floating point value.
    :param value: string possibly containing a floating point value.
    :return: whether the passed string contains a floating point value.
    """
    try:
        float(value)
        return True
    except ValueError:
        return False


def evalate_postfix(expression: str) -> float:
    # Split the text into tokens using space as the delimiter
    tokens = expression.split()

    # Print the tokens
    # Convert tokens that are strings containing integers to actual integers
    # and tokens that contain numbers (including decimals) to floats
    for i, token in enumerate(tokens):
        if is_float(token):
            tokens[i] = float(token)

    s = Stack()

    for t in tokens:
        if type(t) == float:
            s.push(t)
        elif t == "+":
            arg2 = s.pop()
            arg1 = s.pop()
            s.push(arg1 + arg2)
        elif t == "-":
            arg2 = s.pop()
            arg1 = s.pop()
            s.push(arg1 - arg2)
        elif t == "*":
            arg2 = s.pop()
            arg1 = s.pop()
            s.push(arg1 * arg2)
        elif t == "/":
            arg2 = s.pop()
            arg1 = s.pop()
            s.push(arg1 / arg2)

    try:
        answer = s.pop()
    except IndexError:
        raise ValueError(f"Invalid expression: \"{expression}\"")

    if not s.is_empty():
        raise ValueError(f"Invalid expression: \"{expression}\"")

    return answer


if __name__ == "__main__":

    def main():
        while True:
            try:
                # Read a line of text from the user
                expression = input("Enter a line of text: ")
                answer = evalate_postfix(expression)
                print(f"answer: %s" % answer)
            except ValueError:
                print(f"Invalid expression: \"{expression}\"")


    main()
