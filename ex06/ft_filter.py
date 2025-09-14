def ft_filter(function, iterable):
	"""
    Custom implementation of Python's built-in filter function.

    This function applies `function` to each element of `iterable` and
    returns a list of all elements for which the function evaluates to True.

    :param function:
        A function that takes one argument and returns True or False.
    :param iterable:
        An iterable (e.g., list, tuple, string) to filter.
    :returns:
        A list containing only the elements of `iterable`
        for which `function(element)` is True.

    :example:
        >>> ft_filter(lambda x: x > 2, [1, 2, 3, 4])
        [3, 4]
    """
	return [item for item in iterable if function(item)]	