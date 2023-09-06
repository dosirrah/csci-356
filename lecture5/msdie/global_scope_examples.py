# In class I discussed the global keyword and local vs. global scope.
# I advocated moving globals inside a function named main() so that
# the variables would become local rather than polluting the namespace
# of the module.
#
# In Python "global" is a keyword that can be placed inside a function
# to tell Python to use a specified global variable rather than
# creating a local (see fixed_bar() ) below.  "global" is a bit of a misnomer
# because "global" variables really exist within the namespace of the module
# in which the variable is first assigned.  A global variable is really
# a "module variable."

from msdie import MSDie


def foo():

    # foo uses the "global" global_die.  global_die was first set right
    # before the call to foo().  Thus it is defined at global (really module)
    # scope. Since it is at global scope it can be used inside foo() without passing
    # it into foo().
    #
    # HOWEVER, beware...this function works because we never assign to global_die.
    # See bar().
    global_die.roll()
    print("Called globa_die within bar and it resulted in a", global_die)


def bar():   # broken
    # Calling the bar() function results in the following exception:
    #   UnboundLocalError: local variable 'global_die' referenced before assignment
    # The exceptoin occurs because the act of assigning MSDie(4) to global_die
    # creates a variable "global_die" that is of local scope.  The choice to make
    # global_die a local affects the entire function and thus the first appearance
    # of glogal_die within bar occurs before the global_die has been assigned.
    global_die.roll()
    print("Called globa_die within bar and it resulted in a", global_die)

    global_die = MSDie(4)
    global_die.roll()
    print("Called globa_die within bar and it resulted in a", global_die)


def fixed_bar():  # fixed version of bar().

    # By declaring global_die "global," fixed_bar will use the global_die
    # defined right before the call to bar().
    global global_die
    global_die.roll()
    print("Called globa_die within bar and it resulted in a", global_die)

    global_die = MSDie(4)
    global_die.roll()
    print("Called globa_die within bar and it resulted in a", global_die)


if __name__ == "__main__":

    def main():
        """Program that is run to show examples of how use the MSDie class."""
        # I create a function named main() so that it variables defined in main()
        # are kept out of the module-scope.  In this case my_die and d_list are
        # local to main().
        print("\nrunning main part of msdie.py")
        my_die = MSDie(6)

        for i in range(5):
            print(my_die)
            my_die.roll()

        d_list = [MSDie(6), MSDie(20)]
        print(d_list)

    # This die is in module-scope.  Confusing Python refers to names that are
    # in module scope as being global scope.  (see foo()).
    global_die = MSDie(8)
    # bar()   # <--- intentionally broken.
    fixed_bar()

    # I would suggest not creating globals like global_die at all and instead
    # do all the example usage of MSDie inside main() or functions called from
    # main().
    main()

    # # try to access my_die.  This fails because my_die is local to main.
    # # my_die ceases to exist upon return from main().  The access below
    # # generates the exception:
    # #
    # #    NameError: name 'my_die' is not defined
    # print("ms_die has value", my_die)

