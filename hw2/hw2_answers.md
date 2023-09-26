---
header-includes:
  - "\\usepackage{amsmath}"
  - "\\usepackage{graphicx}"
---

# Homework 2 solutions

<!--
These solutions are written in markdown using latex for math.  markdown is 
meant to be readable as text, but it doesn't handle math well.  latex provides the
best math editing environment I know, and pandoc can convert the markdown
into beautiful pdf using latex to render the math.

If I were writing a paper for publication, I would use latex directly
for everything, but I would not use it in a programming class, because markdown 
is recognized by many development tools including gitlab, github, and pycharm.

So that you don't have to figure out how to use pandoc, I committed the pdf file
directly into our class git repository.  git can store non-code, but git 
will not try to merge changes to such files.  Although I put the pdf in 
git, I only place non-code into git repositories sparingly.
-->

**Problem 1** Give the Big-O performance of the following code fragment:

```
    for i in range(n):      # (1)  n * (steps (2) and (3))
        for j in range(n):  # (2)  n * (step (3))
            k = 2 + 2       # (3)  O(1)
```

Let $T(n)$ denote the execution time measured in steps of the
code fragment above.

Let $T_3$ denote the time to execute step (3).
Let $T_2$ denote the time to execute steps (2) and (3).
Let $T_1$ denote the time to execute steps (1), (2), and (3).
Since $T_1$ contains the time to execute all of the steps, $T = T_1$.

$T_3$ takes at least two steps.  The addition and the assignment.  In
machine langauge, this may take additional steps to read and write the
result from memory.  We cannot know exactly how many machine language
instructions this code may compile down to, because that will depend
on the specifics of the CPU architecture.  We can however know that
the number of instructions will be bounded by some constant.  It will
never take 1000 instructions to implement step (3) on any existing
processor.  As such, we can say there exists a constant $C_3$ number
of steps for which

\begin{equation}
  T_3(n) \leq C_3
\end{equation}

The definition of big O states

\begin{equation}
  f(n) = O(g(n)) 
\end{equation}

if and only if there exists some $C$ and $n_0$ such that
$f(n) \leq C\cdot g(n)$ for all $n > n_0$.

\begin{equation}
 T_3(n) = O(1)
\end{equation}

because $T_3(n) \leq C_3 \cdot 1$ regardless of $n$, because
we choose to set $C=C_3$.


Because step (2) repeats step (3) $n$ times,

\begin{equation}
 T_2(n) = n \cdot T_3(n)
\end{equation}

Because step (1) repeats step (2) and (3) $n$ times,

\begin{equation}
T(n) = T_1(n) = n \cdot T_2(n) = n^2 T_3(n) = C \cdot n^2 \label{eq:p1_eq1}
\end{equation}

From the definition of big-O,

\begin{equation}
  \boxed{T(n) = O(n^2)}
\end{equation}

NOTE: We can also say $T(n) = O(n^3)$ and $T(n) = O(2^n)$, because
big-O notation establishes an upper bound.  However, when we ask for
the big-O of a particular code fragment, we want the tightest
upper bound.  You will not get full credit if you said that the
time complexity of the code fragment is $O(n^3)$.

**Problem 2** Give the Big-O performance of the following code fragment:

```
    for i in range(n):    # (1)  n * (step (2))
        k = 2 + 2         # (2)  O(1)
```

The time complexity of the code above becomes

\begin{equation}
  T(n) = n \cdot O(1)
\end{equation}

so

\begin{equation}
  \boxed{T(n) = O(n)}
\end{equation}

**Problem 3** Give the Big-O performance of the following code fragment:

```
    i = n            # (1)  O(1)
    while i > 0:     # (2)  log_2(n) * (steps (3) and (4))
        k = 2 + 2    # (3)  O(1)
        i = i // 2   # (4)  O(1)
```

Let $T(n)$ denote th enumber of steps to execute the code fragement
above.

Because step (4) divides i by 2 on each iteration, this causes
the i reach 0 in $log_2(n)+1$ divisions.  Thus the time complexity
of the code above in big-O notation becomes

\begin{equation}
   T(n) = O(1) + (log_2(n)+1) \cdot (O(1) + O(1))    \label{eq:p2_eq1}
\end{equation}

Because $log_2(n)$ grows with $n$ while the $O(1)$ terms do not, 
the $log_2(n)$ becomes the dominant term as $n$ grows.  Thus
Forumula \ref{eq:p2_eq1} becomes

\begin{equation}
  T(n) = O(log_2(n))
\end{equation}

It so happens that we can convert between bases by multiplying
by a constant.  Remember back to your math, the log base change rule states

\begin{equation}
  log_b(a) = \frac{log_c(a)}{log_c(b)}  \label{eq:p2_eq2}
\end{equation}

As such,

\begin{equation}
 log_k(n) = \frac{log_2(n)}{log_2(k)}
\end{equation}

Note that $\log_2(k)$ is a constant.  We can thus define a constant
$C=\frac{1}{log_2(k)}$ such that Equation \ref{eq:p2_eq2} becomes

\begin{equation}
 log_k(n) = C log_2(n)
\end{equation}

This means

\begin{equation}
  O(log_2(n)) = O(log_3(n)) = O(log_4(n)) = ...
\end{equation}

Since I can do this for any $k$, we often drop the base and state

\begin{equation}
  O(log_2(n)) = O(log(n))
\end{equation}

so

\begin{equation}
  \boxed{T(n) = O(log(n))}
\end{equation}

**Problem 4** Give the Big-O performance of the follwoing code fragment:

```
    for i in range(n):         # (1)  n * (steps (2) through (4))
       for j in range(n):      # (2)  n * (steps (3) through (4))
           for k in range(n):  # (3)  n * (step (4))
               k = 2 + 2       # (4)  O(1)  
```

Due to the triple nesting of for loops the code block above has time
complexity give by 

\begin{equation}
  n \cdot n \cdot n \cdot O(1) = O(n^3)
\end{equation}


**Problem 5**: (2 points) The Bag class from lectures 6 and 7 can be
found in the class repository at

    https://git.cs.olemiss.edu/harrison/csci-356

in

    lectures6and7/bag/bag.py
    
Add an iterator class to Bag.  The iterator class must pass the unit
tests committed in the repository in the directory
`hw2/bag/test_bag.py`.  You will receive *partial credit if you do not
write unit tests for your iterator class, or if the code lacks comments
or type hints.*  Write to test more conditions than the tests given
in `test_bag.py`.  The tests should cover edge conditions like the 
iterator should work as expected on an empty list.

**Answer 5**

See hw2/bag/bag.py

These should pass the tests in hw2/test_bag.py as well as the
additional tests in hw2/test_bag_extended.py.

The additional tests just test a couple edge cases.


**Problem 6**: (2 points) Write a program that verifies that the list
index operator is O(1).  The program must plot the run time of the
list index operator as a function of n using matplotlib.

**Answer 6**

See p6.py

Possible plot:

\begin{center}
\includegraphics[width=0.7\textwidth]{hw2_p6_list_index.png}
\end{center}

In this plot, there doesn't appear to be any correlation between $n$ and 
the time to execute an index operation.   This would be the case
if the operation takes $O(1)$ time.


**Problem 7**: (2 points) Write a program that compares the performance of the
`del` operator on lists and dictionaries.  The main program should plot
the run time of each on the same plot as a function of n.  Also plot
functions that bound the time complexity and print out what you think
is the time complexity of `del` operators for lists and dictionaries
using big-O notation.  When measuring performance on the list `del`
operator, be sure to delete items at random locations from the list.

**Answer 7**

See p7.py

\begin{center}
\includegraphics[width=0.7\textwidth]{hw2_p7_del.png}
\end{center}

Red denotes average execution time per delete from a dict containing
$n$ items.  Blue denotes the same thing but for lists.

From this it looks like the time complexity of deletion from a dict is
O(1), but deletion from a list is O(n).
