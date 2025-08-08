# tinybench - my benchmark boilerplate to quick test stuff

`I also have this as a snippet, but having it as a package seems more
useful.`

Tinybench runs a given list of functions using `timeit` and spits out some
basic statistics on them.

## Synopsis

```console
from tinybench import bench

def f1(): ...  # implementation version 1
def f2(): ...  # implementation version 2

bench(f1, f2)
```

## Usage

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

## Installation

This module is not specialized and thorough enough for pypi, it's only on my
github.  Install it with

```
pip install git+https://github.com/dickerdackel/tinybench
```

## Support / Contributing

Issues can be opened on [Github](https://github.com/dickerdackel/tinybench/issues)

## License

This software is provided under the MIT license.

See LICENSE file for details.
