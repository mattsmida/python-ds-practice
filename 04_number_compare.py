def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """

    # This is a hated solution.
    # Do better.

    # (Don't nest your ternaries, instead, use a conditional block.)
    # (But nice try.)
    return ("First is greater" if a > b else (
        "Second is greater" if b > a else "Numbers are equal"))