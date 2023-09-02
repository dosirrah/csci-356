"""
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

    # a multi-line string starts with three double quotes and only ends with three double quotes.

    def __init__(self, num_sides: int):
        """
        Create a multi-sided die.

        :param num_sides: number of sides on a die.
        :type num_sides: int
        """
        if num_sides < 1:
            raise ValueError("Invalid number of sides: %d" % num_sides)
        self.num_sides = num_sides
        self.current_value = self.roll()

    def __repr__(self):
        return "%s" % self.current_value

    def roll(self) -> int:
        """Perform a roll

           :return: an integer denoting a roll of the die.
           :rtype: int
        """
        self.current_value = random.randrange(1,self.num_sides+1)
        return self.current_value


my_die = MSDie(-7)
for i in range(5):
    print(my_die)
    my_die.roll()

d_list = [MSDie(6), MSDie(20)]
print(d_list)
