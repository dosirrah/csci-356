

import msdie

print("inside myprog.py __name__", __name__)
print("hi")
die = msdie.MSDie(6)
x = die.roll()
print("I rolled", x)
