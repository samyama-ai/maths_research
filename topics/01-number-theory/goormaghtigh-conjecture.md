---
id: 01-number-theory/goormaghtigh-conjecture
title: "Goormaghtigh Conjecture"
topic: 01-number-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Goormaghtigh Conjecture

> **Topic:** Number Theory · **ID:** `01-number-theory/goormaghtigh-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Goormaghtigh conjecture states that there are exactly two non-trivial solutions to the exponential Diophantine equation:
$$ \frac{x^m - 1}{x - 1} = \frac{y^n - 1}{y - 1} $$
where $x, y, m$, and $n$ are integers satisfying the inequalities $x > y > 1$ and $m, n > 2$.

In bases $x$ and $y$, this fraction evaluates to a number whose digit representation consists entirely of $1$s. Thus, the conjecture posits that the only integers which are repunits (repeated units) of length strictly greater than 2 in two distinct bases are $31$ and $8191$. 

The two known non-trivial solutions are:
1. $(x, y, m, n) = (5, 2, 3, 5)$, which yields the integer $31$.
2. $(x, y, m, n) = (90, 2, 3, 13)$, which yields the integer $8191$.

A complete proof of the conjecture requires showing that no other quadruples $(x, y, m, n)$ exist in the integers meeting the specified bounds.

## 2. Mathematical Foundations

The conjecture belongs to the study of exponential Diophantine equations and properties of numbers in various base representations.

A positive integer $N$ is called a **repunit** in base $b$ (where $b \ge 2$) if it can be expressed as:
$$ N = \sum_{i=0}^{k-1} b^i = 1 + b + b^2 + \dots + b^{k-1} = \frac{b^k - 1}{b - 1} $$
where $k$ is the length of the repunit. 

The Goormaghtigh equation essentially equates two repunits in distinct bases:
$$ R_m(x) = R_n(y) $$
where $R_k(b) = \frac{b^k-1}{b-1}$. The constraint $x > y > 1$ directly forces $n > m > 2$ for equality to hold.

The problem relies heavily on the theory of **linear forms in logarithms** (Baker's method) and **Padé approximations** to hypergeometric functions to establish bounds on the variables. 

## 3. History & State of the Art (SOTA)

The problem was originally posed by the Belgian mathematician René Goormaghtigh in 1917 in the journal *L'Intermédiaire des Mathématiciens*. Goormaghtigh observed the two solutions (31 and 8191) but lacked the machinery to prove their exclusivity.

Historically, the study of the Goormaghtigh equation is intimately tied to the development of Baker's theory of linear forms in logarithms in the 1960s and 1970s. This theory allows mathematicians to extract effective bounds for solutions of certain exponential Diophantine equations. 

Balasubramanian and Shorey (1980) applied Baker's method to prove that for any given fixed $m$ and $n$, the equation has at most finitely many solutions. Conversely, they proved that for fixed $x$ and $y$, there are only finitely many solutions $(m, n)$.

State of the art results predominantly rely on combining modern, sharpened bounds for linear forms in two or three logarithms with lattice basis reduction algorithms (such as LLL) to computationally rule out large swathes of parameter space.

## 4. Partial Results / Verified Cases

Several specific sub-cases of the conjecture have been proven completely:
- **Multiplicatively dependent bases:** Bugeaud (1999) proved that if $x$ and $y$ are multiplicatively dependent (i.e., $x^a = y^b$ for some non-zero integers $a, b$), the equation has no solutions aside from the trivial identity $x=y, m=n$.
- **Fixed variable values:** The conjecture has been verified for small fixed values of the parameters. For instance, if $m = 3$ and $y = 2$, the only solutions are precisely $x = 5, n = 5$ and $x = 90, n = 13$, matching the conjecture.
- **Fixed length combinations:** If $(m, n) = (3, 4)$, it is known there are no solutions. 
- **Prime restrictions:** If $n$ is constrained to be prime and $m=3$, specific finite bounds for $x$ and $y$ have been derived, and computational sweeps up to massive limits have yielded no new solutions.

## 5. Principal Obstacles

The fundamental bottleneck in resolving the Goormaghtigh conjecture globally lies in the fact that the primary tool—Baker's method of linear forms in logarithms—produces upper bounds on $m$ and $n$ that are astronomical (often on the order of $10^{18}$ to $10^{30}$) when $x$ and $y$ are unbounded. 

While algorithmic tools like the LLL lattice reduction algorithm can exhaust parameter spaces of size $10^{30}$ when the bases $x$ and $y$ are fixed, these algorithms require explicit numerical inputs for the logarithms involved ($\log x, \log y$). Without fixed $x$ and $y$, the search space is a four-dimensional manifold of variables extending towards infinity, rendering purely computational verification impossible.

Furthermore, the **modular approach** (using Galois representations and Ribet's level-lowering on Frey-Hellegouarch curves), which famously solved Fermat's Last Theorem, struggles here. To apply it, one must manipulate the Goormaghtigh equation into a ternary equation of the form $A + B = C$. Rearranging yields:
$$ x^m(y-1) - y^n(x-1) = x - y $$
Because the right-hand side ($x-y$) is not a constant and varies with the unknowns, the conductor of the associated Frey curve fluctuates wildly, preventing the extraction of a finite set of modular forms to check against.

## 6. The Gap

The exact boundary between current partial results and the full resolution of the conjecture is the lack of an **absolute, effectively computable upper bound** for all four variables $(x, y, m, n)$ simultaneously. 

Currently, we can fix two variables and bound the other two, or fix one variable and severely constrain the others. Crossing the gap requires either a novel descent argument that proves no infinite families of solutions can exist as $x$ and $y$ grow asymptotically with $n$, or a fundamentally new Diophantine approximation technique that yields absolute bounds small enough to be exhaustively checked.

## 7. Current Research (as of June 2026)

Active research primarily focuses on tightening the analytic bounds of logarithmic linear forms. Key avenues include:
- **$p$-adic bounds:** Utilizing $p$-adic linear forms in logarithms (following Yu's bounds) to attack the prime divisors of the variables, effectively bounding the greatest prime factor of solutions.
- **Hypergeometric methods:** Applying Padé approximations to hypergeometric functions for specific values of $m$ and $n$ to establish bounds entirely independent of Baker's method.
- *(frontier — verify)* **Multi-dimensional Modular Method:** Some groups are attempting to associate the equation $x^m(y-1) - y^n(x-1) = x - y$ with abelian varieties of higher dimension (e.g., hyperelliptic curves over totally real fields) where the variability of $x-y$ can be absorbed by the larger moduli space, though the arithmetic geometry involved remains highly speculative.

## 8. Future Work

Leading number theorists have suggested that instead of waiting for continuous marginal improvements to logarithmic bounds, future strategies should:
1. Identify a clever algebraic substitution that maps the four-variable Goormaghtigh equation into a finite family of Thue-Mahler equations.
2. Formulate a generalized ABC-conjecture argument. A proof of the explicit/effective ABC conjecture would immediately reduce the Goormaghtigh equation to a finite, computationally tractable number of cases by lower-bounding the radical of $x^m y^n (x-y)$.

## 9. Key References

- **[Foundational]** R. Goormaghtigh. *L'Intermédiaire des Mathématiciens*, 24, 88. Gauthier-Villars, 1917.
- **[SOTA / Recent]** Y. Bugeaud, M. Mignotte. *On the Diophantine equation $(x^n - 1)/(x - 1) = (y^m - 1)/(y - 1)$ II*. Proceedings of the American Mathematical Society, 128(10): 2779-2781, 2000.
- **[SOTA / Recent]** R. Balasubramanian, T. N. Shorey. *On the equation $a (x^m-1)/(x-1) = b (y^n-1)/(y-1)$*. Mathematica Scandinavica, 46: 177-182, 1980.
- **[Survey]** T. N. Shorey, R. Tijdeman. *Exponential Diophantine Equations*. Cambridge Tracts in Mathematics 87. Cambridge University Press, 1986.

## 10. Worked Example / Concrete Special Case

To clearly see how a number can be a repunit of length greater than 2 in two different bases, let us explicitly verify the first known solution: 
$(x, y, m, n) = (5, 2, 3, 5)$.

**Left-hand side (Base $x=5$, Length $m=3$):**
$$ \frac{5^3 - 1}{5 - 1} = \frac{125 - 1}{4} = \frac{124}{4} = 31 $$
This corresponds to the polynomial evaluation $1 + 5 + 5^2 = 1 + 5 + 25 = 31$. 
In base 5 notation, the number $31$ is written as $111_5$.

**Right-hand side (Base $y=2$, Length $n=5$):**
$$ \frac{2^5 - 1}{2 - 1} = \frac{32 - 1}{1} = 31 $$
This corresponds to the polynomial evaluation $1 + 2 + 2^2 + 2^3 + 2^4 = 1 + 2 + 4 + 8 + 16 = 31$.
In base 2 notation, the number $31$ is written as $11111_2$.

Because both equations evaluate to $31$, the equality holds. The Goormaghtigh conjecture states that aside from this case and the massive $8191$ case (which is $111_{90}$ and $1111111111111_2$), no other integers possess this dual-repunit property for lengths greater than 2.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*