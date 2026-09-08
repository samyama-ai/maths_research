---
id: 05-analysis/borwein-conjecture
title: "Borwein Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Borwein Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/borwein-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

For $n \ge 1$ define the polynomial
$$P_n(q) \;=\; \prod_{j=1}^{n}\bigl(1-q^{3j-2}\bigr)\bigl(1-q^{3j-1}\bigr) \;\in\; \mathbb{Z}[q].$$
Because $P_n$ has integer exponents, it can be split ("dissected") by residue of the exponent modulo $3$:
$$P_n(q) \;=\; A_n(q^3) \;-\; q\,B_n(q^3) \;-\; q^2\,C_n(q^3),$$
which defines $A_n, B_n, C_n \in \mathbb{Z}[t]$ uniquely.

**First Borwein conjecture (P. Borwein, c. 1990).** All coefficients of $A_n$, $B_n$ and $C_n$ are non-negative, for every $n \ge 1$.

**Second Borwein conjecture.** The same holds for the square: writing $P_n(q)^2 = \alpha_n(q^3) - q\,\beta_n(q^3) - q^2\gamma_n(q^3)$, the polynomials $\alpha_n,\beta_n,\gamma_n$ have non-negative coefficients.

**Third Borwein conjecture (modulus 5).** Writing
$$\prod_{j=1}^{n}\bigl(1-q^{5j-4}\bigr)\bigl(1-q^{5j-3}\bigr)\bigl(1-q^{5j-2}\bigr)\bigl(1-q^{5j-1}\bigr) \;=\; \sum_{i=0}^{4} \varepsilon_i\, q^{i} A^{(5)}_{n,i}(q^5), \qquad \varepsilon_0 = 1,\ \varepsilon_{1..4}=-1,$$
all five polynomials $A^{(5)}_{n,i}$ have non-negative coefficients.

A complete resolution means, for each conjecture, either a proof valid for all $n$ or an explicit $n$ and exponent $m$ where the relevant coefficient is negative. The first conjecture is now a theorem (Wang, 2019/2022); the second, third, and the wider Bressoud generalization remain open, which is why this entry is catalogued as **open**.

## 2. Mathematical Foundations

**Gaussian binomials.** For $0 \le k \le n$,
$$\begin{bmatrix} n \\ k\end{bmatrix}_q \;=\; \frac{(q;q)_n}{(q;q)_k\,(q;q)_{n-k}}, \qquad (a;q)_n = \prod_{i=0}^{n-1}(1-aq^i),$$
a polynomial in $q$ with non-negative coefficients (it generates partitions inside a $k \times (n-k)$ box).

**Finite $q$-binomial theorem.**
$$\prod_{j=1}^{n}\bigl(1 - x q^{\,j-1}\bigr) \;=\; \sum_{k=0}^{n} (-1)^k q^{\binom{k}{2}} \begin{bmatrix} n \\ k \end{bmatrix}_q x^k .$$
Substituting $q \mapsto q^3$ with $x = q$ and $x = q^2$ gives the two halves of $P_n$:
$$\prod_{j=1}^{n}(1-q^{3j-2}) = \sum_{k}(-1)^k q^{3\binom{k}{2}+k}\begin{bmatrix} n\\k\end{bmatrix}_{q^3}, \qquad \prod_{j=1}^{n}(1-q^{3j-1}) = \sum_{l}(-1)^l q^{3\binom{l}{2}+2l}\begin{bmatrix} n\\l\end{bmatrix}_{q^3}.$$
Since $3\binom{k}{2}+k+3\binom{l}{2}+2l \equiv k+2l \equiv k-l \pmod 3$, the mod-3 components are
$$A_n(q^3) = \!\!\sum_{k\equiv l\ (3)}\!\! (-1)^{k+l} q^{3(\binom{k}{2}+\binom{l}{2})+k+2l}\begin{bmatrix} n\\k\end{bmatrix}_{q^3}\begin{bmatrix} n\\l\end{bmatrix}_{q^3},$$
and analogously for $B_n$ ($k-l\equiv 1$) and $C_n$ ($k-l\equiv 2$). Each is a *massively cancelling alternating sum* of manifestly non-negative objects: the difficulty is entirely one of cancellation control.

**Analytic reformulation.** With $[q^m]$ the coefficient extraction operator, non-negativity is the statement
$$[q^{3m+i}]\,P_n(q) \;=\; \frac{1}{2\pi i}\oint \frac{P_n(q)}{q^{3m+i+1}}\,dq \;\le\; 0 \quad (i=1,2), \qquad \ge 0 \quad (i=0),$$
so the conjecture is an assertion about the sign of a contour integral of a highly oscillatory finite product on $|q|=r$ — a genuinely analytic problem, not merely a combinatorial one.

**Bressoud's generalization.** Bressoud (1996) placed the conjecture inside the family
$$G(N,M;\alpha,\beta,K;q) \;=\; \sum_{j=-\infty}^{\infty} (-1)^j\, q^{\,Kj\left((\alpha+\beta)j+\alpha-\beta\right)/2} \begin{bmatrix} M+N \\ N-Kj\end{bmatrix}_q ,$$
with $K$ a positive integer and $\alpha K, \beta K \in \mathbb{Z}$, conjecturing non-negativity of the coefficients under explicit arithmetic and size restrictions on $(\alpha,\beta,K,M,N)$. The Borwein case is $K=3$, $\alpha=\beta=1/3$, $M=N=n$; the polynomials $G$ also count partitions with prescribed *hook differences*, linking the problem to Andrews–Baxter–Forrester statistics in the solvable-lattice-model literature.

## 3. History & State of the Art (SOTA)

- **c. 1990.** Peter Borwein observes the phenomenon numerically and circulates the conjecture; it is never published by him directly.
- **1995.** G. E. Andrews, *On a conjecture of Peter Borwein* (J. Symbolic Comput. 20, 487–501), publishes the three conjectures, derives $q$-binomial and hypergeometric representations for $A_n, B_n, C_n$, and proves a family of related positivity results together with the limiting ($n \to \infty$) infinite-product statement.
- **1996.** Bressoud embeds the problem in the hook-difference family above, producing the "generalized Borwein conjecture".
- **1999.** Ismail, Kim and Stanton connect the dissection to lattice paths and positive trigonometric sums, giving an alternative analytic route.
- **2001–2005.** Warnaar (Burge transform; refined $q$-trinomial coefficients) and Berkovich–Warnaar (positivity-preserving transformations for $q$-binomials) prove infinitely many cases of Bressoud's conjecture, though not the Borwein case itself.
- **2019 (preprint) / 2022 (published).** Chen Wang, *An analytic proof of the Borwein conjecture* (Adv. Math. 394, 108028), proves the **first** conjecture, by a saddle-point / circle-method analysis of the coefficient integral, valid for $n$ beyond an explicit threshold, with the remaining small $n$ checked by computer.
- **2020s.** The same analytic machinery is being pushed at the second and third conjectures and at Bressoud's family. `*(frontier — verify)*`

## 4. Partial Results / Verified Cases

- **First conjecture: fully proved** (Wang 2022) for all $n \ge 1$ — asymptotic analysis above an explicit $n_0$, exhaustive symbolic computation below it.
- **Infinite-product limit:** the $n \to \infty$ dissection of $\prod_{j\ge1}(1-q^{3j-2})(1-q^{3j-1}) = (q;q)_\infty/(q^3;q^3)_\infty$ has non-negative components; established by Andrews (1995).
- **Bressoud family:** Warnaar (2001, 2003) proved non-negativity of $G(N,M;\alpha,\beta,K;q)$ for infinite subfamilies, notably $K=1,2$ and cases reachable by the Burge transform, and for $\alpha+\beta$ small relative to $K$; Berkovich–Warnaar (2005) extended this via positivity-preserving operators on $q$-binomials.
- **Second and third conjectures:** verified by direct computation for all $n$ in the low hundreds; e.g. for $n=1$, $P_1(q)^2 = 1-2q-q^2+4q^3-q^4-2q^5+q^6$ gives $\alpha_1 = 1+4t+t^2$, $\beta_1 = 2+t$, $\gamma_1 = 1+2t$, all non-negative.
- **Structural refinements:** Andrews' representations give closed forms for the *extreme* coefficients (lowest and highest degree terms of $A_n,B_n,C_n$), which are provably non-negative for all $n$; the difficulty concentrates in the middle range $m \approx \tfrac{1}{2}\deg P_n$.

## 5. Principal Obstacles

- **No combinatorial model.** Despite thirty years of effort there is no known set of combinatorial objects, with a statistic, whose generating functions are $A_n, B_n, C_n$. A bijective or sign-reversing-involution proof would be immediate — none has been found, and the coefficients do not match any standard partition statistic.
- **Cancellation of exponential size.** In the $q$-binomial expansion of Section 2, individual terms are of size roughly $\exp(c\sqrt{m})$ or larger while the result is comparatively tiny; naive triangle-inequality bounds lose the sign entirely.
- **Failure of classical positivity machinery.** $q$-binomials are non-negative, but the alternating sum is not a positivity-preserving transform of them; Burge/Bailey-chain techniques (Warnaar, Berkovich) preserve positivity only for parameter ranges that stop just short of the Borwein point $\alpha=\beta=1/3$, $K=3$.
- **Sharp analytic thresholds.** The circle-method proof of the first conjecture works because a single saddle dominates on the major arc and the minor-arc error is provably smaller. For the square ($P_n^2$) and the modulus-5 product, several saddles become comparable, and the required uniform bounds are not merely harder but currently unavailable.
- **Non-monotone coefficients.** The coefficient sequences of $A_n,B_n,C_n$ are not unimodal in an obvious way, so induction on $n$ (adding one factor $(1-q^{3n+1})(1-q^{3n+2})$) does not preserve any known invariant.

## 6. The Gap

The first conjecture is closed. The open boundary is:

1. **From one product to its square.** Wang's method controls $\oint P_n(q) q^{-m-1}dq$; for $P_n^2$ the integrand's phase doubles, the saddle-point equations acquire additional near-degenerate solutions, and no uniform-in-$m$ error bound is known. The exact missing step is a saddle-point analysis of $P_n(q)^2$ that remains valid across the full range $0 \le m \le \deg P_n^2$, including the transition zones between saddles.
2. **From modulus 3 to modulus 5.** With four factors per block the dissection has five components; the analogue of the "dominant saddle" argument must simultaneously separate five residue classes whose leading asymptotics differ only at exponentially small order.
3. **From special cases to Bressoud's family.** Warnaar's transforms prove positivity for parameters where a Bailey-type chain closes. There is no known chain reaching $(\alpha,\beta,K) = (1/3,1/3,3)$-type parameters in general, so proving the full generalized conjecture needs either a new positivity-preserving operator or an analytic proof uniform in $(\alpha,\beta,K)$.

## 7. Current Research (as of June 2026)

- **Vienna (Krattenthaler and collaborators) and Wuhan (Chen Wang).** Extension of the analytic method to the second and third conjectures, and to Bressoud-type parameters; preprints in this line should be checked against the published record. `*(frontier — verify)*`
- **Brisbane (Warnaar) and Florida (Berkovich).** Algebraic route: new positivity-preserving transformations on $q$-binomial and $q$-trinomial coefficients, Bailey lattices, and connections to characters of $\widehat{\mathfrak{sl}}_2$ coset models.
- **Experimental mathematics.** Large-scale coefficient computation (modular arithmetic plus FFT-based polynomial multiplication) to test the second/third conjectures far beyond earlier ranges and to look for near-violations that would sharpen the analytic thresholds.
- **Cylindric partitions / vertex-operator viewpoint.** Attempts to realize $A_n,B_n,C_n$ as principally specialized characters, which would give non-negativity for free.

## 8. Future Work

- Find a combinatorial interpretation of $A_n,B_n,C_n$ — Andrews himself repeatedly named this as the decisive missing ingredient.
- Develop a *uniform* saddle-point framework for finite products $\prod (1-q^{pj-a})$ that handles multiple competing saddles, which would deliver the third conjecture and much of Bressoud's family at once.
- Search for a positivity-preserving transform bridging the gap between Warnaar's proved parameter region and the Borwein point.
- Establish quantitative lower bounds (not just non-negativity) for the middle coefficients; a bound of the form $[q^{3m}]A_n \gg n^{-c}\,\|A_n\|_\infty$ would likely be more stable under squaring than bare positivity.
- Machine-assisted certificate search: express the coefficients as sums of squares or as positive combinations of $q$-binomials with rational-function coefficients (a "$q$-Positivstellensatz").

## 9. Key References

- **[Foundational]** G. E. Andrews. *On a conjecture of Peter Borwein.* Journal of Symbolic Computation **20** (1995), 487–501. [DOI](https://doi.org/10.1006/jsco.1995.1061)
- **[Foundational]** G. E. Andrews. *The Theory of Partitions.* Cambridge University Press, 1984 (reissued 1998).
- **[Structural]** D. M. Bressoud. *The Borwein conjecture and partitions with prescribed hook differences.* Electronic Journal of Combinatorics **3** (2), (1996), #R4. [DOI](https://doi.org/10.37236/1262)
- **[Analytic]** M. E. H. Ismail, D. Kim, D. Stanton. *Lattice paths and positive trigonometric sums.* Constructive Approximation **15** (1999), 69–81. [DOI](https://doi.org/10.1007/s003659900097)
- **[SOTA / Algebraic]** S. O. Warnaar. *The generalized Borwein conjecture. I. The Burge transform.* In *q-Series with Applications to Combinatorics, Number Theory and Physics*, Contemporary Mathematics **291**, AMS, 2001, 243–267. [DOI](https://doi.org/10.1090/conm/291/04906)
- **[SOTA / Algebraic]** S. O. Warnaar. *The generalized Borwein conjecture. II. Refined q-trinomial coefficients.* Discrete Mathematics **272** (2003), 215–258. [DOI](https://doi.org/10.1016/s0012-365x(03)00047-5)
- **[SOTA / Algebraic]** A. Berkovich, S. O. Warnaar. *Positivity preserving transformations for q-binomial coefficients.* Transactions of the American Mathematical Society **357** (2005), 2291–2351. [DOI](https://doi.org/10.1090/s0002-9947-04-03680-3)
- **[SOTA / Recent]** C. Wang. *An analytic proof of the Borwein conjecture.* Advances in Mathematics **394** (2022), Paper 108028 (arXiv:1901.10886). [DOI](https://doi.org/10.1016/j.aim.2021.108028)

## 10. Worked Example / Concrete Special Case

**Case $n = 2$.** Expand
$$P_2(q) = (1-q)(1-q^2)(1-q^4)(1-q^5).$$
First $(1-q)(1-q^2) = 1-q-q^2+q^3$ and $(1-q^4)(1-q^5) = 1-q^4-q^5+q^9$. Multiplying and collecting:
$$P_2(q) = 1 - q - q^2 + q^3 - q^4 + 2q^6 - q^8 + q^9 - q^{10} - q^{11} + q^{12}.$$
(Check: coefficients sum to $0$, as they must since $P_2(1)=0$.) Dissecting by exponent mod 3:

| residue | exponents | coefficients | component |
|---|---|---|---|
| $0$ | $0,3,6,9,12$ | $1,1,2,1,1$ | $A_2(t) = 1+t+2t^2+t^3+t^4$ |
| $1$ | $1,4,7,10$ | $-1,-1,0,-1$ | $B_2(t) = 1+t+0\,t^2+t^3$ |
| $2$ | $2,5,8,11$ | $-1,0,-1,-1$ | $C_2(t) = 1+0\,t+t^2+t^3$ |

All three are non-negative, as conjectured. Note that the signs on residues $1$ and $2$ are uniformly negative — this is exactly the pattern the conjecture asserts, and it is far from obvious from the expansion.

**A rigorous global constraint.** Set $q = 1$ in the dissection: $P_n(1)=0$ gives $A_n(1) = B_n(1)+C_n(1)$. Now set $q = \omega$, a primitive cube root of unity. Each block contributes $(1-\omega)(1-\omega^2) = 3$, so $P_n(\omega) = 3^n$, while the dissection gives
$$A_n(1) - \omega B_n(1) - \omega^2 C_n(1) = 3^n .$$
Symmetry of the construction forces $B_n(1) = C_n(1) =: b$, and $-\omega-\omega^2 = 1$, so $A_n(1) + b = 3^n$. With $A_n(1) = 2b$ this yields
$$B_n(1) = C_n(1) = 3^{\,n-1}, \qquad A_n(1) = 2\cdot 3^{\,n-1}.$$
For $n=2$: $B_2(1) = C_2(1) = 3$ and $A_2(1) = 6$ — matching the table. So the *total mass* of each component is known exactly and is positive; the conjecture is the far finer statement that this mass is distributed with no negative coefficient anywhere among the $\Theta(n^2)$ terms.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*