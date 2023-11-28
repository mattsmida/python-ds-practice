def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of items.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # [1.count, 2.count, 1.count] >> [1:2, 2:1, 1: 2]
    # find the max count - [2]
    # return the key of the max count

    # returns 
    freq_count_to_num = [(nums.count(num), num) for num in nums]
    num = max(freq_count_to_num)[1]
    return num