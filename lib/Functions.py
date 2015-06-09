def fixed_point(f, start, stop):

    while start != stop:
        yield start
        start = f(start)