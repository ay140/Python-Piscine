from typing import Any


# --- My notes ---
# "Allowed functions: None" for this exercise means we can't import
# the real `statistics` module or numpy to cheat - every formula
# below is written by hand. (Naming this file "statistics.py" also
# means it shadows the real standard-library module if you ever try
# to `import statistics` from inside this folder - that's on purpose,
# it's literally what we're replacing.)


def _mean(values):
    """Arithmetic mean: sum of the values divided by how many there are."""
    return sum(values) / len(values)


def _median(values):
    """Middle value of the sorted data (average of the two middle
    ones if there's an even amount of data)."""
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        raise IndexError("median of empty data")
    mid = n // 2
    if n % 2 == 1:
        return ordered[mid]
    return (ordered[mid - 1] + ordered[mid]) / 2


def _percentile(values, p):
    """p-th percentile using linear interpolation between the two
    closest ranked values (this is the same method numpy's
    np.percentile uses by default)."""
    ordered = sorted(values)
    n = len(ordered)
    if n == 0:
        raise IndexError("percentile of empty data")
    if n == 1:
        return float(ordered[0])
    # "rank" is where the p-th percentile would sit if we could pick
    # a fractional index into the sorted list, e.g. index 1.5 means
    # "halfway between the value at index 1 and the value at index 2".
    rank = (n - 1) * (p / 100)
    lower = int(rank)
    upper = lower if lower == rank else lower + 1
    if lower == upper:
        return float(ordered[lower])
    fraction = rank - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def _quartile(values):
    """25th and 75th percentile of the data, as a [Q1, Q3] list."""
    return [_percentile(values, 25), _percentile(values, 75)]


def _variance(values):
    """Population variance: average of the squared distance of every
    value to the mean."""
    if not values:
        raise ZeroDivisionError("variance of empty data")
    mean = _mean(values)
    return sum((x - mean) ** 2 for x in values) / len(values)


def _std(values):
    """Population standard deviation: square root of the variance."""
    return _variance(values) ** 0.5


# One dictionary to map a requested stat's NAME to the function that
# computes it. This avoids a long if/elif/elif/... chain below.
_COMPUTE = {
    "mean": _mean,
    "median": _median,
    "quartile": _quartile,
    "std": _std,
    "var": _variance,
}


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """Print every statistic requested through kwargs, computed on args.

    Each kwarg's VALUE (not its key) picks the statistic: it must be
    one of "mean", "median", "quartile", "std" or "var". The key
    itself can be anything (see the subject's tester.py, which uses
    silly key names like "toto"/"tutu") - it only exists so several
    stats can be requested in the same call.
    Unknown values are silently ignored. If a requested stat cannot
    be computed (typically: no data at all), "ERROR" is printed
    instead of letting an exception crash the program.
    """
    for _, requested in kwargs.items():
        compute = _COMPUTE.get(requested)
        if compute is None:
            continue
        try:
            result = compute(args)
        except (ZeroDivisionError, IndexError, TypeError):
            print("ERROR")
        else:
            print(f"{requested} : {result}")
