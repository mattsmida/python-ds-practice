def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    output = ''
    to_swap_lower = to_swap.lower()
    for char in phrase:
        if char.lower() == to_swap_lower and char.isupper():
            output += char.lower()
        elif char.lower() == to_swap_lower and char.islower():
            output += char.upper()
        else:
            output += char

    return output