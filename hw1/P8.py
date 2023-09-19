"""
My solution to problem 8.

  7. Research the __radd__ method. How does it differ from __add__? When is it used? Implement __radd__.
  8. Repeat the last question but this time consider the __iadd__ method.

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

    if m < 0:
        m = -m

    if n < 0:
        n = -n

    while m % n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm % oldn
    return n


def tassert(b: bool, s: str) -> None:
    """
    Raises a TypeError when the passed boolean is False.

    :param b: a boolean to be evaluated.
    :param s: an error message.
    :return: None
    """
    if not b:
        raise TypeError(s)


class Fraction:  # from Listing 1
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
        tassert(type(top) == int, "the numerator must be an integer")
        tassert(type(bottom) == int, "the denominator must be an integer")

        # normalize the representation of negative fractions so that the
        # negative either does not appear at all or appears in the numerator.
        if bottom < 0:
            bottom = -bottom
            top = -top

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

    def __add__(self, otherfraction: Fraction | int) -> Fraction:
        """
            :param otherfraction: The second parameter passed to the "+" operator.
            :type otherfraction: Fraction
            :returns: A Fraction containing the sum of self and the passed Fraction.
            :rtype: Fraction
           """
        # There is no requirement in problem 7 that we support integers
        # as the rhs of the plus operation, but it is strange if we support integers
        # as the left-hand side, but we do not support integers as the right-hand side.
        if type(otherfraction) == int:
            otherfraction = Fraction(otherfraction, 1)
        elif not isinstance(otherfraction, Fraction):
            return NotImplemented

        newnum = self.num * otherfraction.den + self.den * otherfraction.num
        newden = self.den * otherfraction.den
        return Fraction(newnum, newden)  # reduction now happens inside Fraction's constructor.


    def __radd__(self, lhs: int) -> Fraction:
        """
        Called when __add__ for some type other than Fraction cannot handle a Fraction as
        the right-hand side of an add (+) operation.  In this case self is the right-hand
        side of the add (+) operation.

        :param lhs: an integer that will be added to the fraction.
        :return: returns the result of the addition of the int with the Fraction.
        :rtype: Fraction
        """
        if type(lhs) != int:
            return NotImplemented

        return Fraction(lhs, 1) + self

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

    def __sub__(self, other_fraction: Fraction) -> Fraction:
        """
        :param other_fraction: fraction subtracted from self.
        :type other_fraction: Fraction
        :return: the difference between self and other_fraction.
        :rtype: Fraction
        """
        n1 = self.num * other_fraction.den
        n2 = other_fraction.num * self.den
        d = self.den * other_fraction.den
        return Fraction(n1 - n2, d)

    def __mul__(self, other_fraction: Fraction) -> Fraction:
        """
        :param other_fraction:
        :type other_fraction: Fraction
        :return: self multiplied with other_fraction.
        :rtype: Fraction
        """
        return Fraction(self.num * other_fraction.num, self.den * other_fraction.den)

    def __truediv__(self, bottom: Fraction) -> Fraction:
        """
        :param bottom: the denominator of a division as in self/bottom.
        :return: the true division of self and bottom.
        :rtype: Fraction
        """
        # implemented as inverting *bottom* and multiplying the inversion with *self*.
        return Fraction(self.num * bottom.den, self.den * bottom.num)

    def __gt__(self, rhs: Fraction) -> bool:
        """
        :param rhs: used in self > rhs.
        :return: true iff self > rhs.
        """
        n1 = self.num * rhs.den
        n2 = self.den * rhs.num
        return n1 > n2

    def __ge__(self, rhs: Fraction) -> bool:
        """
        :param rhs: used in self >= rhs
        :return: true iff self >= rhs
        """
        n1 = self.num * rhs.den
        n2 = self.den * rhs.num
        return n1 >= n2

    def __lt__(self, rhs: Fraction) -> bool:
        """
        :param rhs: used in self < rhs
        :return: true iff self < rhs
        """
        n1 = self.num * rhs.den
        n2 = self.den * rhs.num
        return n1 < n2

    def __le__(self, rhs: Fraction) -> bool:
        """
        :param rhs: used in self <= rhs
        :return: true iff self <= rhs
        """
        n1 = self.num * rhs.den
        n2 = self.den * rhs.num
        return n1 <= n2

    def __ne__(self, rhs: Fraction) -> bool:
        """
        :param rhs: used in self != rhs
        :return: true iff self != rhs
        """
        n1 = self.num * rhs.den
        n2 = self.den * rhs.num
        return n1 != n2

    def __iadd__(self, rhs: Fraction|int) -> Fraction:
        """
        Implements the += operator, which adds the right-hand side (rhs) to
        self and then saves the result in self.  Unlike the add(+) operation, += modifies
        the value of self.

        :param rhs: the right-hand side of the += operation.
        :return: self.
        """
        if type(rhs) == int:
            rhs = Fraction(rhs, 1)
        elif not isinstance(rhs, Fraction):
            return NotImplemented

        return self + rhs
