"""
This module contains classes and functions related to dice rolling.

MSDie is taken from chapter 2 of *Problem Solving with Algorithms and Data Structures using Python*.

"""

import random


class MSDie:
    """
    Multi-sided die

    Instance Variables:
        current_value
        num_sides

    """

    def __init__(self, num_sides: int):
        """
        Constructor of a MSDie.

        :param num_sides: number of sides of this die.
        :type num_sides: int
        """
        if type(num_sides) is not int:
            raise TypeError
        if num_sides <= 0:
            raise ValueError("The number of sides of a die must be "
                             "a positive integer.")

        self.num_sides = num_sides
        self.current_value = self.roll()

    def roll(self) -> int:
        """
        Performs one cast of the multi-sided die and returns the result.

        :return: the value of the roll.
        :rtype: int
        """
        self.current_value = random.randrange(1, self.num_sides+1)
        return self.current_value

    def __str__(self):
        return str(self.current_value)

    def __repr__(self):
        return "MSDie({}) : {}".format(self.num_sides, self.current_value)


# If you uncomment this, it will reveal the __name__ assigned by the interpreter
# to the current module. If the module is being run directly from the shell prompt
# then __name__ is assigned to "__main__"
#
#   $ python msdie.py
#   inside msdie.py __name__: __main__
#   [...]
#
# If insteade msdie.py is imported into another module like myprog.py, __name__ is assigned
# to the module name.
#
#   $ python myprog.py
#   inside msdie.py __name__: msdie
#
print("inside msdie.py __name__:", __name__)

if __name__ == "__main__":

    def main():
        """Program that is run to show examples of how use the MSDie class."""
        # I create a function named main() so that it variables defined in main()
        # are kept out of the module-scope.  In this case my_die and d_list are
        # local to main().
        print("running main part of msdie.py")
        my_die = MSDie(6)

        for i in range(5):
            print(my_die)
            my_die.roll()

        d_list = [MSDie(6), MSDie(20)]
        print(d_list)

    main()
