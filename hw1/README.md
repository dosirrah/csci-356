# HW1 Comments

All problems in this homework are taken from the text

This assignment had some ambiguities.  E

## HW1 description

This section was posted on blackboard.

For those who have had Python before and need a review, or who have 
experience with other languages but have never used Python... this
serves as an introduction.   Before trying these problems, work through
the examples in sections 1.7 through and including 1.13.  You can play
with Python from within the book itself if you are viewing it on the web
at  1.7. Review of Basic Python — Problem Solving with Algorithms and Data
Structures 

There is nothing to turn in from working through sections 1.7-1.13.  It
is just to provide practice and context for the homework problems.

Do the following programming excercises 1 through 9 and 11 from section 1.17:
https://runestone.academy/ns/books/published/pythonds/Introduction/Exercises.html

Place each answer in a separate Python file named P1.py for problem 1, P2.py
for problem 2 and so on.  Place all of them in a tar ball and upload them to
blackboard.  Each problem is worth 1 points.  So there are a maximum of 10 
points on the homework.  All homeworks are weighted equally in the final
grade for the course.   

## Problem 7 is now extra credit

Problem 7 does not specify what types should be supported
by `__radd__`.  In my implementation of Problem 6, I supported 
adding a Fraction to an integer.  For example,

    >>> from P7 import Fraction
    >>> x = 5 + Fraction(1,2)
    >>> x
    <P7.Fraction object at 0x1032246d0>
    >>> str(x)
    '11/2'

I would expect returning x to output the same or similar
to `str(x)`; however, typing x on a Python command-line invokes
Fraction's `__repr__` method which wasn't added until Problem 9.

## Problem 7 & 8

In both problems 7 and 8, the types that must be supported for
the argument are unspecified.  Any reasonable implementation
was accepted for credit.

## Problem 9

The problem does not specify the expected representation in the
returned string.  Any reasonable representation of the Fraction
was accepted for
credit.

## Problem 11 is double extra credit

Problem 11 took me more than any of the other problems, especially
when I composed a HalfAdder from the LogicCircuit classes provided
in the text.  The Problem description itself did not sufficiently 
define a programming interface for the HalfAdder class, nor did 
it describe whether the HalfAdder should be implemented using
existing LogicCircuit classes.  Due to the ambiguity and 
difficulty of the problem (esp if one were to implement it 
using existing LogicCircuit classes), I changed this to 
being worth 2 points instead of 1 and made it extra credit.