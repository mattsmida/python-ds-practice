def list_manipulation(lst, command, location, value=None):
    """Mutate lst to add/remove from beginning or end.

    - lst: list of values
    - command: command, either "remove" or "add"
    - location: location to remove/add, either "beginning" or "end"
    - value: when adding, value to add

    remove: remove item at beginning or end, and return item removed

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'remove', 'end')
        3

        >>> list_manipulation(lst, 'remove', 'beginning')
        1

        >>> lst
        [2]

    add: add item at beginning/end, and return list

        >>> lst = [1, 2, 3]

        >>> list_manipulation(lst, 'add', 'beginning', 20)
        [20, 1, 2, 3]

        >>> list_manipulation(lst, 'add', 'end', 30)
        [20, 1, 2, 3, 30]

        >>> lst
        [20, 1, 2, 3, 30]

    Invalid commands or locations should return None:

        >>> list_manipulation(lst, 'foo', 'end') is None
        True

        >>> list_manipulation(lst, 'add', 'dunno') is None
        True
    """

    if (command != 'remove' and command != 'add'):
        return None
    if (location != 'beginning' and location != 'end'):
        return None
    
    if (location == 'beginning'):
        # add or subtract
        if (command == 'add'):
            lst.insert(0, value)
            return lst
        elif (command == 'remove'):
            return lst.pop(0)
    elif (location == 'end'):
        # add or subtract
        if (command == 'add'):
            lst.append(value)
            return lst
        elif (command == 'remove'):
            return lst.pop()
        
# elif unecessary, but makes it readable
# if, elif elif elif .etc
# can leave out 44-46 return none, will still return none