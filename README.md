# Advent of Code 2023 Solutions

My solutions to AOC in Python. Relatively new to Python so the code might not be very pretty...

This repository uses the `aoc` runner script provided by [advent-of-code-data](https://github.com/wimglenn/advent-of-code-data). 
It runs, tests and submits my solutions for AOC

The `aoc` runner allows you to easily verify your [Advent of Code](https://adventofcode.com/) solutions against multiple datasets, or verify other user's code against your own dataset.

```bash
$ cat ~/.config/aocd/tokens.json  # create this file with some auth tokens
{
    "github": "53616c7465645f5f0775...",
    "google": "53616c7465645f5f7238...",
    "reddit": "53616c7465645f5ff7c8...",
    "twitter": "53616c7465645f5fa524..."
}
$ pip install ~/src/advent-of-code-solutions  # install the directory which contains your setup.py file
...
$ aoc --years 2023   # run it!
   0.53s   2023/1  - Trebuchet?!                         paixaop/default   ✔ part a: 55971             ✔ part b: 54719 
   0.30s   2023/2  - Cube Conundrum                      paixaop/default   ✔ part a: 2285              ✔ part b: 77021 
   0.30s   2023/3  - Gear Ratios                         paixaop/default   ✔ part a: 550934            ✔ part b: 81997870
   1.13s   2023/4  - Scratchcards                        paixaop/default   ✔ part a: 26426             ✔ part b: 6227972    
```

Inside the entry point you can do whatever you need in order to delegate to your code. For example, write out data to a scratch file then run a script, or import a function and just pass in the data directly as an argument. The only requirement is that this entry point should return a tuple of two values, with the answers for that day's puzzle - the rest is up to you.
