
# The next line promotes the name Bag from within bag.py to be at the package scope.
# As such, if I want to import Bag into a Python module, I would do the following:
#  from lecture5.bag import Bag
#
# Without the next line I would have to do the following:
#
#  from lecture5.bag.bag import Bag

from .bag import Bag
