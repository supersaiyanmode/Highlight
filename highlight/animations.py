
def linear_transition(start, end, steps):
    if steps < 1:
        raise ValueError("No of steps need to be at least 1.")

    delta = [float(y - x) / steps for x, y in zip(start, end)]
    cur = list(start)

    for _ in range(steps):
        cur = [x + y for x, y in zip(cur, delta)]
        yield cur

    yield end


def quadratic_transition(start, end, steps, a=1):
    # Shift origin
    shift = start
    start = [x - y for x, y in zip(start, shift)]
    end = [x - y for x, y in zip(end, shift)]

    cur = start
    for _ in range(steps):
        pass