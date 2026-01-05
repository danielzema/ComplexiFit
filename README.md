# ComplexiFit

Calculates the best-fitting time complexity of an algorithm by comparing measured runtimes against common complexity curves.

Currently supporting: ```O(n), O(n*log n), O(n²)```.

---

## How it works

Given measured input sizes `n` and runtimes `C(n)`, plots `C(n)` against common time-complexity curves `f(n)` (`n`, `n * log n`, `n^2`).  

For each candidate `f(n)`, it assumes a model `C(n) ≈ a * f(n) + b` where `a` and `b` are constants. It performs linear regression to compute the coefficient of determination `R²` (variance).  

The best candidate for `C(n)` is the `f(n)` whose model has `R²` closest to `1.0`.

The curves are then plotted using Matplotlib.
