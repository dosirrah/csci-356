"""My solution to problem 11 of 1.17.

11. The most simple arithmetic circuit is known as the half-adder. Research the simple
half-adder circuit. Implement this circuit.

A half adder has two inputs and outputs the sum and a carry bit.  The sum is
implemented as an XOR between the two inputs and the carry is implemented as
an AND of the two inputs.
"""

# Problem 11 is a bit unclear.  How do I implement the half adder?
# Do I compose it from existing gates written in chapter 1, or do I implement
# with two ouputs such that all of its internal logic
# is implemented with code rather than as a composition of gates?
#
# As a composition of gates we run into a problem, to implement Xor I need
# a way to fan-out an input so that the same input can be connected to multiple
# logic gates.
#
# I decided to do this the easy way.  Don't compose it from gates.
#
# Aside: The way the classes are written in the book are not amenable to unit testing
# because they take input from the user.  I thus added a circuit element called
# a "Source" which can be turned on or off.  For purposes of this example, a
# switch is considered a LogicGate and thus can be connected to the inputs of
# other LogicGate objects.

# based on code from 1.13.2.1


class LogicGate:
    """
    A base class for all logic gates.
    """

    def __init__(self, n: str):
        """
        Initialize the baseclass state for all logic gates.

        :param n: a human-readable label for the logic gate.
        """
        self.name = n
        self.output = None

    def getLabel(self) -> str:
        """
        :return: the label of the LogicGate
        """

        # By Python convention this function name should use snake case rather than camcel case.
        return self.name

    def getOutput(self) -> int:
        """
        Calculates the output from the logic gate.

        :return: output from the logic gate.
        """
        self.output = self.performGateLogic()
        return self.output


class BinaryGate(LogicGate):
    """
    A base class for all binary logic gates.
    """

    def __init__(self, n: str):
        """
        Initialize the baseclass state for all binary logic gates.

        :param n: a human-readable label for the logic gate.
        :type n: str
        """
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self) -> int:
        """
        :return: return the value input on pin A.
        """
        if self.pinA is None:
            return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self) -> int:
        """
        :return: return the value input on pin B.
        """
        if self.pinB is None:
            return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self, source: LogicGate) -> None:
        """
        :param source: attach the source to the next unused input pin.
        """
        if self.pinA is None:
            self.pinA = source
        else:
            if self.pinB is None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):
    """Logic gate implementing a binary "and" operator on two inputs."""

    def __init__(self, n: str):
        """
        :param n: a human-readable label for the logic gate.
        :type n: str
        """
        BinaryGate.__init__(self, n)

    def performGateLogic(self) -> int:
        """
        :return: the result of the logic operation.
        """

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    """Logic gate implementing a binary "or" operator on two inputs."""

    def __init__(self, n: str):
        """
        :param n: a human-readable label for the logic gate.
        :type n: str
        """
        BinaryGate.__init__(self, n)

    def performGateLogic(self) -> int:
        """
        :return: the result of the logic operation.
        """

        a = self.getPinA()
        b = self.getPinB()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class Source(LogicGate):
    """A source generates a constant output until set to some other
       output value."""

    def __init__(self, n: str):
        """
        :param n: a human-readable label for the logic gate.
        :type n: str
        """
        super(Source, self).__init__(n)
        self.output_value = 0

    def set(self, x : int) -> None:
        """Set the output value for the source.
           :param x: output value for this source.
           :type x: int
        """
        self.output_value = x

    def performGateLogic(self) -> int:  # method name should be snake_case (see PEP 8). --Dave
        """
        :return: the result of the logic operation.
        """
        return self.output_value


class UnaryGate(LogicGate):
    """
    A base class for all unary logic gates.
    """

    def __init__(self, n: str):
        """
        :param n: a human-readable label for the logic gate.
        :type n: str
        """
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self) -> int:   # method name should be snake_case (see PEP 8). --Dave
        """
        :return: input from the upstream logic gate or from user input.
        """
        if self.pin is None:   # In Python, by convention we compare a variable to None using "is" rather than ==.

            # HERE: I think it is bad form to bake user input into a base class.  It would be better
            # to abstract user input into a subclass of a Source class.
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self, source) -> None:    # method name should be snake_case (see PEP 8). --Dave
        """
        :param source: attach the source to the next unused input pin.
        """
        if self.pin is None:   # In Python, by convention we compare a variable to None using "is" rather than ==.
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self, n: str):
        """
        :param n: a human-readable label for the "not" logic gate.
        :type n: str
        """

        UnaryGate.__init__(self,n)

    def performGateLogic(self) -> int:  # method name should be snake_case (see PEP 8). --
        """
        :return: the result of the logic operation.
        """

        if self.getPin():
            return 0
        else:
            return 1


class Connector:

    def __init__(self, fgate: LogicGate, tgate: LogicGate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):    # method name should be snake_case (see PEP 8). --Dave
        return self.fromgate

    def getTo(self):      # method name should be snake_case (see PEP 8). --Dave
        return self.togate


class HalfAdder(BinaryGate):
    """This implementation of a HalfAdder is built from the already defined
       logic gates.
    """

    def __init__(self, n: str):
        """
        :param n: a human-readable label for the "half adder" logic gate.
        :type n: str
        """
        super(HalfAdder, self).__init__(n)

        # (in1 and not in2) or (not in1 and in2) = xor bit
        #      ^^^ ^^^      ^^  ^^^     ^^^
        #      A1  N2       O1  N1      A2
        #
        # in1 and in2 = carry bit

        # This is a bit of a hack.  The way that the gates are implemented is that
        # if there is no input then every time getOutput is called, the user will queries
        # for the value on the pin.  When getOutput is called on the HalfAdder, I
        # will query each input pin exactly once and then save the value in a switch holding
        # the value on true or false until the next call to the HalfAdder's getOutput.
        # I would prefer to reimplement the gates so that they don't take input from the user
        # at all, but this would change all of the code from the book.  Hmmm.... --Dave

        self._source_a = Source("SA")   # using snake_case or lowercase for variables (see PEP8).
        self._source_b = Source("SB")

        # create an Xor from And and Not gates.
        and1 = AndGate("A1")
        not2 = NotGate("N2")
        not1 = NotGate("N1")
        and2 = AndGate("A2")

        Connector(self._source_a, and1)
        Connector(self._source_b, not2)
        Connector(not2, and1)
        Connector(self._source_a, not1)
        Connector(self._source_b, and2)
        Connector(not1, and2)

        self._xor = OrGate("O1")  # the output of this OR gate is the XOR of input1 and input2.
        Connector(and1, self._xor)
        Connector(and2, self._xor)

        self._carry = AndGate("AndCarry")
        Connector(self._source_a, self._carry)
        Connector(self._source_b, self._carry)


    def performGateLogic(self) -> (int, int):    # method name should be snake_case (see PEP 8). --Dave
        """
        :return: a pair of integers wherein the first is the output of an XOR opreration
        dnd second is a carry bit.  Together the pair forms the outputs of a half adder.
        """

        # store the values of the pins in a "sources" which generate constant
        # output.  This avoids having the user queried twice for pin a's or
        # pin b's input value.
        a = self.getPinA()
        b = self.getPinB()
        self._source_a.set(a)
        self._source_b.set(b)

        out = self._xor.getOutput()     # xor will query source_a and source_b.
        carry = self._carry.getOutput() # carry will query source_a and source_b again.
        return out, carry


if __name__ == "__main__":
    # When a module is run directly as with "python P11.py", the __name__ variable
    # is set to "__main__".  However, when a module is imported into another module
    # such as the unit tests, __name__ is set to the name via which the module was
    # imported, e.g.,  if you import mymodule then inside mymodule.py __name__ is
    # "mymodule".  Likewise, when P11_v2.py is impored into test_p11_v2, P11_v2.py
    # has the name "p11_v2".

    def main():

        # Implement a half-adder using an Xor Gate

        hadd = HalfAdder("H")
        print(hadd.getOutput())

        # g1 = AndGate("G1")
        # g2 = AndGate("G2")
        # g3 = OrGate("G3")
        # g4 = NotGate("G4")
        # c1 = Connector(g1,g3)
        # c2 = Connector(g2,g3)
        # c3 = Connector(g3,g4)

        # print(g4.getOutput())

    main()

