def ft_filter(function, iterable):
	"""
	Custom implementation of Python's built-in filter function.
	Returns a list with items for which function(item) is True.
	"""
	return [item for item in iterable if function(item)]	