def last_element(lst):
    """Return last item in list (None if list is empty.)

        >>> nums = [1, 2, 3]
        >>> last_element(nums)
        3
        >>> last_element([]) is None
        True

    Make sure original list has not been mutated:

        >>> nums == [1, 2, 3]
        True
    """

    # if (lst is not []):
    if (not lst):
        return None
    return lst[-1]


    # Instead, if anything in the list, let's get the last thing
    # (That's more clear).

    # This is more straightforward
    # if lst:
        # return lst[-1]