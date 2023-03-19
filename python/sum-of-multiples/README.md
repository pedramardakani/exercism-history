# Sum of Multiples

Welcome to Sum of Multiples on Exercism's Python Track.
If you need help running the tests or submitting your code, check out `HELP.md`.

## Instructions

Given a list of factors and a limit, add up all the unique multiples of the factors that are less than the limit.
All inputs will be greater than or equal to zero.

## Example

Suppose the limit is 20 and the list of factors is [3, 5].
We need to find the sum of all unique multiples of 3 and 5 that are less than 20.

Multiples of 3 less than 20: 3, 6, 9, 12, 15, 18
Multiples of 5 less than 20: 5, 10, 15

The unique multiples are: 3, 5, 6, 9, 10, 12, 15, 18

The sum of the unique multiples is: 3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 = 78

So, the answer is 78.

You can make the following assumptions about the inputs to the
`sum_of_multiples` function:
* All input numbers are non-negative `int`s, i.e. natural numbers
including zero.
* A list of factors must be given, and its elements are unique
and sorted in ascending order.

## Source

### Created by

- @sjakobi

### Contributed to by

- @ackerleytng
- @behrtam
- @bsoyka
- @cmccandless
- @Dog
- @etmoore
- @GascaK
- @ikhadykin
- @julianandrews
- @kotp
- @kytrinyx
- @lekum
- @N-Parsons
- @pheanex
- @tqa236

### Based on

A variation on Problem 1 at Project Euler - https://projecteuler.net/problem=1