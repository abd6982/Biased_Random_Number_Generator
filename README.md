## Pseudo Random Number Generator

This is an implementation of the **Linear Congruential Generator (LCG)** algorithm.

The LCG algorithm yields a sequence of pseudo-randomized numbers calculated with a discontinuous piecewise linear equation. The function follows the following *recurrence relation*:

X<sub>n+1</sub> = (aX<sub>n</sub> + c) mod m

where X is the sequence of pseudo-random values, and

m, 0 < m (the modulus)<br>
a, 0 < a < m (the multiplier)<br>
c, 0 <= c < m (the increment)<br>
X<sub>0</sub>, 0 <= X<sub>0</sub> < m

*m* is often a prime just less than a power of 2 (here the Mersenne Prime 2<sup>31</sup>-1 is used).<br>When c&ne;0, correctly chosen parameters allow a period equal to *m*, for all seed values. This will occur if and only if:

1. *m* and *c* are relatively prime,
2. a-1 is divisible by all prime factors of m,
3. a-1 is divisible by 4 if m is divisible by 4.

There are various combinations of *a*, *m*, and *c*. I have used the combination used by the **GNU C Library**.

##### a = 1103515245, c = 12345, m = 2<sup>31</sup> - 1

## Implementation

The generator takes multiple arguments:

1. **upper limit** - numbers generated are less than or equal to upper limit
2. **lower limit** - numbers generated are greater than or equal to lower limit
3. **n** - the number of random numbers required
4. **optional seed value** - can be used for reproducible results

## The bias

To introduce the bias, I developed the following technique:

Aside from the provided upper limit, we calculate a mid_limit ,i.e., upper_limit / 2. In the current iteration of the generation, a number *n*; 1 <= n <= 20 is generated. If the number generated is a multiple of 4 (i.e. 5 possible numbers) then we generate a smaller number using mid_limit and lower_limit. Otherwise, we generate the number using upper_limit and mid_limit.

Now the probability of generating a large number is 75% and of small number is 25%.

(We generated 20 numbers initially to distribute evenly the chances of generating small or large numbers.)

## How to use

Clone the repository. Run the *rand-test.py* file. The *randgen.py* file contains two functions - rand() which generates random values and calculate_ratio() which calculates the fraction of large and small numbers generated. Provide inputs in the following format:

The first three arguments are upper_limit, lower_limit and the number_of_randoms. Fourth is the optional seed argument.

eg. **python rand-test.py 400 200 10**

This combination of inputs will generate 10 random numbers between 200 and 400.

eg. **python rand-test.py 400 200 10 5**

This combination of inputs will generate 10 random numbers between 200 and 400 using 5 as the seed.
