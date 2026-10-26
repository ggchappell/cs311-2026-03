#!/usr/bin/env python3
# rpn_calc.py
# Glenn G. Chappell
# Started: 2026-10-25
# Updated: 2026-10-26
"""Text-Input RPN Calculator.
For CS 311 Fall 2026
"""


def rpn_eval(s, lexeme):
    """Do RPN action based on given int stack & lexeme (command).
    * <int>    - push int value
    * + - * /  - pop 2 operands, push int result
    * c C      - clear stack

    Errors are signaled via exceptions: IndexError, ValueError,
    ZeroDivisionError.
    """

    attr = getattr(s, "append", None)
    assert callable(attr)
    attr = getattr(s, "pop", None)
    assert callable(attr)
    assert isinstance(lexeme, str)

    try:
        val = int(lexeme)
    except:
        pass  # Exception raised means this lexeme is not an int
    else:
        s.append(val)
        return

    if lexeme in { "+", "-", "*", "/" }:
        if len(s) < 2:
            s.clear()
            raise IndexError("rpn_eval: pop from empty Stack")
        b = s.pop()
        a = s.pop()
        assert isinstance(a, int)
        assert isinstance(b, int)

        match lexeme:
            case "+":
                s.append(a + b)
            case "-":
                s.append(a - b)
            case "*":
                s.append(a * b)
            case "/":
                if b == 0:
                    raise ZeroDivisionError("rpn_eval: div by zero")
                s.append(a // b)

    elif lexeme in { "c", "C" }:
        s.clear()

    else:
        raise ValueError("rpn_eval: bad command")


def print_stack(s):
    """Print top of given Stack, or message that Stack is empty."""

    assert isinstance(s, list)

    if s:
        print(f"Top of Stack: {s[-1]}")
    else:
        print("<Empty Stack>")


def rpn_calc():
    """Do RPN computation. Input tokens & pass to rpn_eval until q/Q."""

    # String constants
    PROMPT = "Commands (q to quit): "
    QUIT_MSG = "*** Quitting"
    ERROR_MSG = "*** ERROR: "

    # Set up stack
    s = list()  # Stack used for RPN evaluation

    # Initial print
    print_stack(s)
    print()

    # Input & handle commands until quit command
    while True:
        try:
            line = input(PROMPT)
        except (OSError, EOFError):
            print()
            print()
            print(QUIT_MSG)
            return

        lexemes = line.split()
        if not lexemes:
            continue

        print()

        for lexeme in lexemes:
            if lexeme == "q" or lexeme == "Q":
                print(QUIT_MSG)
                return

            try:
                rpn_eval(s, lexeme)
            except (IndexError, ValueError, ZeroDivisionError) as e:
                print(f"{ERROR_MSG}{e}")

            print_stack(s)

        print()


# Main program

if __name__ == "__main__":
    print("Reverse Polish Notation Expression Evaluation")
    print()

    rpn_calc()

