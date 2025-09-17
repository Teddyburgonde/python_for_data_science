def count_in_list(lst, item):
    """
    Count how many times a specific item appears in a list.

    This function iterates over the given list
    and returns the total number
    of occurrences of the specified item.

    :param lst:
        A list of elements in which to search.
    :param item:
        The element whose occurrences will be counted.
    :returns:
        An integer representing the number
        of times ``item`` appears in ``lst``.
    """
    return lst.count(item)
