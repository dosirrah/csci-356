"""
Problem 2

In many ways it would be better if all fractions were maintained in
lowest terms right from the start. Modify the constructor for the
Fraction class so that GCD is used to reduce fractions immediately.
Notice that this means the __add__ function no longer needs to reduce.
Make the necessary modifications.
"""

from __future__ import annotations  # allows __eq__, __add__, etc. to take Fraction as a type hint.


def gcd(m: int, n: int) -> int:
    """
    The Greatest Common Divisor (GCD) of two numbers is the largest integer
    that divides both numbers with zero remainder.

    :param m: a positive integer
    :type m: int
    :param n: another integer
    :type n: int
    :return: the greatest common divisor.
    """

    # The param names and type specifications in the docstring are restucturedText (reST)
    # intended for use by the documentation generation tool Sphinx.  However,
    # PyCharm will also recognize the reST and use it to auto-generate
    # text to appear in text when the pointer is hovered over an identifier
    # (e.g., a variable name, class name, module name, method name, function name, or
    # package name).

    # The type hints are "hints" (i.e., suggestions) used by IDEs like PyCharm to
    # provide information

    if m == 0 and n == 0:
        raise ValueError("The greatest common divisor of zero and zero is undefined.")

    # The implementation of GCD in the book didn't handle the case when n is zero
    # even though mathematically GCD is well defined when one of the two numbers
    # for which we are finding a greatest common divisor is zero.
    if n == 0:
        return m

    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


class Fraction:          # from Listing 1
    """A Fraction object represents a mathematical fraction."""
    # Because the string above appears before any statements within the class, it
    # becomes the documentation for the Fraction class.

    def __init__(self, top: int, bottom: int):
        """Top and bottom are the numerator and denominator of the fraction respectively.

        :param top: numerator of the fraction.
        :type top: int
        :param bottom: denominator of the fraction.
        :type bottom: int

        """
        # Raising an exception when passed a zero denominator is not requested in the
        # problem, but it seems rational.
        if bottom == 0:
            raise ZeroDivisionError("The denoinator of a fraction cannot be zero.")

        # I used restructured text above to document the constructor's parameters.
        # restructured text is used by Sphinx to genereate pretty HTML documentation
        # from the source code.
        self.num = top
        self.den = bottom

        divisor = gcd(top, bottom)
        self.num = self.num // divisor
        self.den = self.den // divisor

    def show(self) -> None:
        """Pretty prints the fraction"""
        print(self.num, "/", self.den)

    def __str__(self) -> str:
        """:returns: A string representation of the Fraction.
           :rtype: str
           """
        return str(self.num) + "/" + str(self.den)

    def __add__(self, otherfraction: Fraction) -> Fraction:
        """
            :param otherfraction: The second parameter passed to the "+" operator.
            :type otherFraction: Fraction
            :returns: A Fraction containing the sum of self and the passed Fraction.
            :rtype: Fraction
           """

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)  # reduction now happens inside Fraction's constructor.

    def __eq__(self, other: Fraction) -> bool:
        """Compares this fraction to the passed "other" fraction.

           :returns true if and only if the Fraction 'self' equals the passed other.
           :rtype: bool
           """

        # if we know that the fractions are already reduced then we can also simplify
        # __eq__ so that it directly compares numerator to numerator and
        # denominator to denominator.
        return self.num == other.num and self.den == other.den

    def getNum(self) -> int:
        """
        :return: the numerator.
        """
        # My aside: the function is called getNum in the problem from the text, but camelCase for
        # method names is not accepted convention in Python.  CamelCase is when
        # each word in a name except possibly the first starts with an upper-case character.
        #
        # For the names of methods, functions, and variables the convention is to use either all
        # lowercase or snake_case, e.g., "get_num."
        return self.num

    def getDen(self) -> int:
        """
        :return: the denominator.
        """
        return self.den
