# exact_skellam

An exact sampler for generating symmetric Skellam random variates in python. 

The algorithm is based on https://www.combinatorics.org/ojs/index.php/eljc/article/view/v23i4p22/pdf

The implementation is based on https://github.com/peteroupc/peteroupc.github.io/blob/master/randomfunc.md#Poisson_Distribution

We adopt the convention that </pre><code>range(m)</code></pre>, which uniformly samples an integer from 0 to m, is the only accessible randomness.
