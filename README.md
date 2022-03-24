# exact_skellam

An exact sampler for generating symmetric Skellam variates in python. 

A symmetric Skellam variate is the difference between two independent Poisson variates of the same variance

The algorithm for generating exact Poisson is based on Algorithm 1 by Duchon and Duvignau 2016 (see https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i4p22/pdf).

and the observation that the sum of Bernoulli variates is Poisson distributed by Devorye 1986 (see page 487http://www.eirene.de/Devroye.pdf).

We adopt the convention that </pre><code>range(m)</code></pre>, which uniformly samples an integer from 0 to m, is the only accessible randomness.
