""" tinybench - my benchmark boilerplate to quick test stuff

`I also have this as a snippet, but having it as a package seems more
useful.`

Tinybench runs a given list of functions using `timeit` and spits out some
basic statistics on them.

Synopsis
========

```console
from tinybench import bench

def f1(): ...  # implementation version 1
def f2(): ...  # implementation version 2

bench(f1, f2)
```

Usage
=====

There's not much more to add to the example above, except that `timeit.timeit`
expects a function without arguments.  So if you want to benchmark an already
existing function that requires parameters, you have to create a partial of it
or wrap it in a lambda or function that provides these.

The following call shows the defaults.  `number` goes directly into `timeit`,
runs is just a loop over multiple `timeit` calls to have another layer to
average out random load spikes on the computer.

`bench(fn1, fn2, ..., number=1_000_000, runs=5)`

will run 5 iterations of `timeit(f1, number=1_000_000)`, followed by all other
given `fnNN`.  It collects the average, median, and stdev for each function
and run, and will also print out the timing results while the benchmark is
running, so you have a "still alive" sign.

Finally, it will print all run-statistics as well as stats over the runs as
summary.
"""

from statistics import mean, median, stdev
from timeit import timeit
from collections.abc import Callable


def bench(*fns: Callable, runs: int = 5, number: int = 1_000_000) -> None:
    summary = []
    outer_timings = []
    for fn in fns:
        print(fn.__name__)
        print('-' * 72)
        timings = []
        for i in range(runs):
            timings.append(timeit(fn, number=number))
            print(f'{i}: {timings[-1]}')

        outer_timings.append((fn.__name__, mean(timings), median(timings)))
        summary.append(
            f'{outer_timings[-1][0]}: '
            f'mean={outer_timings[-1][1]:.5f}  '
            f'median={outer_timings[-1][2]:.5f}  '
            f'stdev={stdev(timings):.5f}')
        print(summary[-1], end='\n\n')

    ordered_means = sorted(outer_timings, key=lambda x: x[1])
    ordered_medians = sorted(outer_timings, key=lambda x: x[2])

    outer_mean = mean([_[1] for _ in outer_timings])
    outer_median = median([_[2] for _ in outer_timings])
    outer_stdev = (stdev([_[1] for _ in outer_timings]),
                   stdev([_[2] for _ in outer_timings]))

    print(f"""{'=' * 72}
{'\n'.join(summary)}

Mean over runs: {outer_mean:.5f} --> {', '.join([_[0] for _ in ordered_means])}
Median over runs: {outer_median:.5f} --> {', '.join([_[0] for _ in ordered_medians])}
Stdev over means runs: {outer_stdev[0]:.5f}
Stdev over medians runs: {outer_stdev[1]:.5f}

""")
