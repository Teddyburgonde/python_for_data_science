def ft_tqdm(lst: range) -> None:
    """
    Custom implementation of tqdm.

    This function mimics the behavior of the tqdm
    library by displaying a
    progress bar in the terminal while iterating
    over a given range. It uses
    the `yield` keyword to return each element
    one by one, allowing it to be
    used in a standard `for` loop.

    :param lst:
        The range (or any iterable with a known length) to iterate over.
    :yields:
        Each element from the input iterable, in order.
    :example:
        >>> from time import sleep
        >>> for elem in ft_tqdm(range(100)):
        ...     sleep(0.01)
    """
    total = len(lst)
    for i, elem in enumerate(lst):
        percent = (i + 1) / total * 100
        bar_len = 60
        filled = int(bar_len * (i + 1) / total)
        bar = "=" * filled + ">" + " " * (bar_len - filled - 1)
        print(f"\r{percent:3.0f}%|[{bar}]| {i+1}/{total}", end="")
        yield elem
