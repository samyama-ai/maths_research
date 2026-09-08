---
id: 05-analysis/pisot-vijayaraghavan-problem
title: "Pisot-Vijayaraghavan Problem"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Pisot–Vijayaraghavan Problem

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/pisot-vijayaraghavan-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Write $\|x\|$ for the distance from $x \in \mathbb{R}$ to the nearest integer.

**Problem (Pisot–Vijayaraghavan).** Characterize the real numbers $\theta > 1$ for which
$$\lim_{n \to \infty} \|\theta^n\| = 0 .$$

Every Pisot–Vijayaraghavan number (PV number: a real algebraic integer $\theta > 1$ all of whose other Galois conjugates lie strictly inside the unit disc) has this property. The conjecture is that there are no others.

**Conjecture A (unweighted).** If $\theta > 1$ and $\|\theta^n\| \to 0$, then $\theta$ is a Pisot number. In particular no transcendental $\theta$ has this property.

**Conjecture B (weighted, Pisot's conjecture).** If $\theta > 1$, $\lambda > 0$ and $\|\lambda\theta^n\| \to 0$, then $\theta$ is a Pisot number and $\lambda \in \mathbb{Q}(\theta)$.

A complete solution means either a proof of B (which implies A, taking $\lambda = 1$), or the explicit construction of a pair $(\lambda,\theta)$ with $\theta$ non-Pisot and $\|\lambda\theta^n\| \to 0$. Not a single such $\theta$ is known, and no non-Pisot $\theta$ has ever been *proved* to fail the condition unless it is algebraic.

## 2. Mathematical Foundations

**Norm and orbit.** For $\theta>1$, $\lambda>0$ set $\varepsilon_n = \lambda\theta^n - a_n$ where $a_n = \lfloor \lambda\theta^n \rceil$ is the nearest integer, so $\|\lambda\theta^n\| = |\varepsilon_n|$.

**Pisot numbers.** $\theta>1$ is Pisot if it is an algebraic integer with minimal polynomial $P(x)=x^d + c_{d-1}x^{d-1}+\dots+c_0 \in \mathbb{Z}[x]$ whose conjugates $\theta_2,\dots,\theta_d$ satisfy $|\theta_i| < 1$. Then the power trace
$$T_n = \theta^n + \sum_{i=2}^{d}\theta_i^{\,n} \in \mathbb{Z}$$
is a rational integer (it is a symmetric function of the roots), and
$$\|\theta^n\| \le \Big|\sum_{i=2}^{d}\theta_i^{\,n}\Big| \le (d-1)\,\rho^{\,n}, \qquad \rho = \max_{i\ge2}|\theta_i| < 1 ,$$
so convergence is geometric and in particular $\sum_n \|\theta^n\|^2 < \infty$. Denote the set of Pisot numbers by $S$.

**Salem numbers.** $\tau>1$ algebraic integer with all conjugates in $|z|\le 1$ and at least one on $|z|=1$. Then $\{\tau^n\}$ is dense mod $1$ (Salem) and $\|\tau^n\| \not\to 0$; the set is $T$.

**Pisot's converse theorem (1938).** If $\theta>1$, $\lambda>0$ and
$$\sum_{n\ge 0} \|\lambda\theta^n\|^2 < \infty ,$$
then $\theta \in S$ and $\lambda \in \mathbb{Q}(\theta)$. The proof is analytic: with $\varepsilon_n$ as above, the power series $f(z) = \sum_{n\ge0} a_n z^n$ satisfies
$$f(z) = \frac{\lambda}{1-\theta z} - \sum_{n\ge0}\varepsilon_n z^n ,$$
so $f$ is meromorphic on $|z| < 1$ with one simple pole at $1/\theta$ and, by Cauchy–Schwarz, belongs to the Hardy class $H^2$ after removing that pole. Integer coefficients plus $\ell^2$ control let one invoke the Kronecker–Hadamard rationality criterion (a power series with integer coefficients that is bounded in $H^2$ off a pole represents a rational function), giving $f = A/B$ with $A,B\in\mathbb{Z}[z]$, $B(1/\theta)=0$, and $B$ having no other root in $|z|\le1$ — i.e. the reciprocal of a Pisot minimal polynomial.

**Generic behaviour.** Koksma (1935): for Lebesgue-almost every $\theta>1$, $(\theta^n)_{n\ge1}$ is equidistributed mod $1$. Weyl: for fixed $\theta>1$ and a.e. $\lambda$, $(\lambda\theta^n)$ is equidistributed. So the exceptional sets in Conjectures A and B are null; the difficulty is that no measure-theoretic argument identifies *which* null set.

## 3. History & State of the Art

- **Hardy (1919)** proved the algebraic case of Conjecture B: if $\theta>1$ is algebraic and $\|\lambda\theta^n\|\to0$ for some $\lambda>0$, then $\theta\in S$ and $\lambda\in\mathbb{Q}(\theta)$.
- **Pisot (1938)**, in his thesis, replaced "$\theta$ algebraic" by the square-summability hypothesis, obtaining the converse theorem of §2 — still the strongest general result.
- **Vijayaraghavan (1940s)**, independently, studied limit points of $(\{\theta^n\})$ and proved structural facts, e.g. that for $\theta = 3/2$ the set of limit points is infinite, and that $S$ is nowhere dense.
- **Salem (1944)** proved $S$ is a *closed* subset of $\mathbb{R}$ — a striking topological rigidity, and the reason Salem numbers were introduced (as limits of Pisot numbers).
- **Siegel (1944)** proved $\min S = \theta_0 \approx 1.3247179$, the plastic number, root of $x^3-x-1$; the next is $\approx 1.3802776$, root of $x^4-x^3-1$.
- **Dufresnoy–Pisot (1955)** and **Amara (1966)** determined the derived sets $S^{(k)}\cap(1,2)$; the smallest limit point of $S$ is the golden ratio $\varphi$. **Boyd (1977–85)** gave algorithms enumerating all Pisot numbers below $1.9324\ldots$ exhaustively.
- Since then the *characterization* problem itself has not moved: no improvement on Pisot's $\ell^2$ hypothesis is known.

## 4. Partial Results / Verified Cases

| Hypothesis added | Conclusion | Source |
|---|---|---|
| $\theta$ algebraic, $\lambda>0$, $\|\lambda\theta^n\|\to0$ | $\theta \in S$, $\lambda\in\mathbb{Q}(\theta)$ | Hardy 1919 |
| $\sum_n\|\lambda\theta^n\|^2<\infty$ | $\theta\in S$, $\lambda\in\mathbb{Q}(\theta)$ | Pisot 1938 |
| $\|\lambda\theta^n\| \le C\rho^n$, $\rho<1$ | same (special case of above) | — |
| $\theta$ algebraic, neither Pisot nor Salem, $\xi\neq0$ | $\limsup_n\|\xi\theta^n\| \ge c(\theta) > 0$, with explicit $c$ | Dubickas 2006 |
| $\theta = p/q$ in lowest terms, $q>1$, $\xi \neq 0$ | $\limsup_n\{\xi\theta^n\} - \liminf_n\{\xi\theta^n\} \ge 1/p$ | Flatto–Lagarias–Pollington 1995 |
| $\theta = 3/2$, $\{\xi(3/2)^n\}<1/2$ for all $n$ ("Z-numbers") | the set of such $\xi$ is at most countable, of counting function $O(x^{0.7})$ | Mahler 1968 |

So Conjecture B is a theorem for **all algebraic $\theta$** and for **all $\theta$ whatsoever under $\ell^2$ decay**. The open region is exactly: $\theta$ transcendental and the decay slower than square-summable. Structural facts hold unconditionally: $S$ is closed, countable, nowhere dense, Lebesgue-null; $\min S$, $\min S'$, and all of $S\cap(1,2)$ are known explicitly.

Complementary: for **every** $\theta>1$ there exist uncountably many $\lambda$ with $\{\lambda\theta^n\}\in[1/3,2/3]$ for all $n$ (Pollington 1979, de Mathan 1980) — the orbit can always be forced to *avoid* $0$, but no method forces it *into* $0$ for non-Pisot $\theta$.

## 5. Principal Obstacles

- **No algebraic handle on transcendental $\theta$.** Hardy's argument uses the conjugates of $\theta$; there is nothing to conjugate when $\theta$ is transcendental. Every known route to rigidity passes through a minimal polynomial.
- **The $\ell^2$ hypothesis is not removable by soft analysis.** Pisot's proof needs $\sum\varepsilon_n^2<\infty$ to place $f$ in $H^2$ and apply the rationality criterion. Under only $\varepsilon_n\to0$ (say $\varepsilon_n \sim 1/\log n$), $\sum\varepsilon_n z^n$ need not be in any Hardy class with the required boundary control, and the Kronecker-type criterion fails outright: there exist integer power series with $\varepsilon_n\to0$ that are not rational.
- **Lacunary sequences have no useful Fourier structure.** $(\theta^n)$ is lacunary; Weyl sums $\sum_{n\le N} e(\lambda\theta^n)$ admit no nontrivial cancellation estimate for a *fixed* $\lambda$, only in mean over $\lambda$. Metric (a.e.) statements are abundant, pointwise ones essentially absent — the same barrier that leaves $\{(3/2)^n\}$ undecided.
- **No dynamical model.** For $\theta$ integer, $x\mapsto\theta x$ mod $1$ is an expanding endomorphism and Furstenberg-type rigidity applies; for non-integer $\theta$ the map $x\mapsto\theta x$ mod $1$ is a $\beta$-transformation whose invariant structure is understood only when $\theta$ is a Parry number, which already presupposes algebraicity.
- **Transcendence measures are the wrong tool.** Proving a specific $\theta$ transcendental gives no control on $\|\theta^n\|$; conversely a hypothetical bad $\theta$ would have to be constructed, and every known nested-interval construction produces $\liminf\|\theta^n\| = 0$ with $\limsup > 0$, never $\lim = 0$.

## 6. The Gap

Proven: $\varepsilon_n \in \ell^2 \Rightarrow \theta \in S$. Conjectured: $\varepsilon_n \to 0 \Rightarrow \theta \in S$.

The entire gap is the implication
$$\varepsilon_n \to 0 \quad \stackrel{?}{\Longrightarrow} \quad \sum_n \varepsilon_n^2 < \infty ,$$
which is false for arbitrary sequences but is expected to be forced here by the recursion $a_{n+1} = \theta a_n + (\varepsilon_{n+1} - \theta\varepsilon_n)$ tying the integers $a_n$ to $\theta$. Concretely: rule out any $\theta>1$ with, say, $\|\theta^n\| \asymp n^{-1/2}$ or $\|\theta^n\| \asymp 1/\log n$. Even weakening Pisot's hypothesis from $\ell^2$ to $\ell^p$ for some $p>2$ would be a genuine advance; none is known.

## 7. Current Research (as of June 2026)

- **Diophantine bounds for algebraic bases.** Dubickas, Zaïmi, Kaneko and coauthors continue to sharpen explicit lower bounds for $\limsup\|\xi\alpha^n\|$ when $\alpha$ is algebraic and not Pisot/Salem, and for fractional powers $(p/q)^n$; these refine §4 rows 4–5 but stay inside the algebraic case.
- **$\beta$-expansions and spectra.** The Erdős–Joó–Komornik spectra $\{\sum_{i=0}^{n} \epsilon_i\theta^i : \epsilon_i \in \{0,\pm1\}\}$ have positive separation exactly when $\theta$ is Pisot; groups in Hungary, France and China exploit this to characterize $S$ by metric/combinatorial rather than analytic means. *(frontier — verify)*
- **Salem-number frontier.** Whether $S \cup T$ is closed, and whether Salem numbers are dense in $[1,\infty)$, remain open and are pursued alongside Lehmer's problem; progress there would clarify the boundary of the PV condition.
- **Additive-combinatorial attacks on lacunary orbits** (Peres–Schlag-style local-lemma constructions) currently produce only lower bounds on $\|\lambda\theta^n\|$, i.e. results in the direction opposite to the conjecture. *(frontier — verify)*

## 8. Future Work

1. **Weaken $\ell^2$ to $\ell^p$.** Find a rationality criterion for integer power series valid under $\sum|\varepsilon_n|^p<\infty$, $p>2$. This is the most concrete stated target.
2. **Use the linear recursion.** Show directly that $a_{n+1}/a_n \to \theta$ with $\varepsilon_n\to0$ forces $(a_n)$ to satisfy an integer linear recurrence of bounded order — equivalent to $f$ rational, hence to the conjecture.
3. **Settle $\theta=3/2$ first.** Prove $\liminf_n\|(3/2)^n\| > 0$, or even that $(\{(3/2)^n\})$ is dense. Currently neither is known; this is the standard testing ground.
4. **Rigidity for $\beta$-transformations** with transcendental $\beta$: classify $\beta$ whose orbit of $1$ has vanishing distance to $\mathbb{Z}$.

## 9. Key References

- **[Foundational]** G. H. Hardy. *A problem of Diophantine approximation.* Journal of the Indian Mathematical Society, 11 (1919), 162–166.
- **[Foundational]** C. Pisot. *La répartition modulo 1 et les nombres algébriques.* Annali della Scuola Normale Superiore di Pisa, 7 (1938), 205–248.
- **[Foundational]** R. Salem. *A remarkable class of algebraic integers. Proof of a conjecture of Vijayaraghavan.* Duke Mathematical Journal, 11 (1944), 103–108. [DOI](https://doi.org/10.1215/s0012-7094-44-01111-7)
- **[Foundational]** C. L. Siegel. *Algebraic integers whose conjugates lie in the unit circle.* Duke Mathematical Journal, 11 (1944), 597–602. [DOI](https://doi.org/10.1215/s0012-7094-44-01152-x)
- **[Book / Survey]** M.-J. Bertin, A. Decomps-Guilloux, M. Grandet-Hugot, M. Pathiaux-Delefosse, J.-P. Schreiber. *Pisot and Salem Numbers.* Birkhäuser, 1992.
- **[Book]** R. Salem. *Algebraic Numbers and Fourier Analysis.* D. C. Heath, 1963.
- **[Book]** J. W. S. Cassels. *An Introduction to Diophantine Approximation.* Cambridge University Press, 1957.
- **[Survey]** Y. Bugeaud. *Distribution Modulo One and Diophantine Approximation.* Cambridge Tracts in Mathematics 193, Cambridge University Press, 2012.
- **[SOTA]** A. Dubickas. *Arithmetical properties of powers of algebraic numbers.* Bulletin of the London Mathematical Society, 38 (2006), 70–80. [DOI](https://doi.org/10.1017/s0024609305017728)
- **[SOTA]** L. Flatto, J. C. Lagarias, A. D. Pollington. *On the range of fractional parts $\{\xi(p/q)^n\}$.* Acta Arithmetica, 70 (1995), 125–147.
- **[Related]** K. Mahler. *An unsolved problem on the powers of 3/2.* Journal of the Australian Mathematical Society, 8 (1968), 313–321. [DOI](https://doi.org/10.1017/s1446788700005371)
- **[Computational]** D. W. Boyd. *Pisot and Salem numbers in intervals of the real line.* Mathematics of Computation, 32 (1978), 1244–1260. [DOI](https://doi.org/10.1090/s0025-5718-1978-0491587-8)

## 10. Worked Example / Concrete Special Case

**A Pisot base: $\theta = \varphi = \tfrac{1+\sqrt5}{2}$.** Minimal polynomial $x^2-x-1$, conjugate $\psi = \tfrac{1-\sqrt5}{2} = -1/\varphi \approx -0.6180$. The Lucas numbers $L_n = \varphi^n + \psi^n$ are integers ($L_1=1, L_2=3, L_3=4, L_4=7,\dots$), so
$$\|\varphi^n\| \le |\varphi^n - L_n| = |\psi|^n = \varphi^{-n}.$$
Numerically: $\varphi^{5}=11.0902 \Rightarrow \|\cdot\|=0.0902$; $\varphi^{10}=122.9919 \Rightarrow 0.0081$; $\varphi^{20}=15126.99993 \Rightarrow 7\times10^{-5}$. Decay is geometric, so $\sum\|\varphi^n\|^2 \le \sum \varphi^{-2n} < \infty$, and Pisot's converse theorem applies — consistent with $\varphi \in S$.

**A non-Pisot base: $\theta = 3/2$.** Here $(3/2)^n = 3^n/2^n$, and $\|(3/2)^n\| = 2^{-n}\cdot\|3^n\|_{2^n}$ where $\|3^n\|_{2^n}$ is the distance from $3^n$ to the nearest multiple of $2^n$.

| $n$ | $(3/2)^n$ | $\|(3/2)^n\|$ |
|---|---|---|
| 1 | 1.5 | 0.5 |
| 2 | 2.25 | 0.25 |
| 3 | 3.375 | 0.375 |
| 4 | 5.0625 | 0.0625 |
| 5 | 7.59375 | 0.40625 |
| 6 | 11.390625 | 0.390625 |
| 7 | 17.0859375 | 0.0859375 |
| 8 | 25.62890625 | 0.37109375 |
| 9 | 38.443359375 | 0.443359375 |
| 10 | 57.6650390625 | 0.334960938 |

Numerically the values wander over $(0,1/2)$ with no decay; the Flatto–Lagarias–Pollington bound gives unconditionally $\limsup\{(3/2)^n\}-\liminf\{(3/2)^n\}\ge 1/3$, so the orbit cannot concentrate at a single point. Nevertheless **no proof exists** that $\liminf_n\|(3/2)^n\| > 0$: $\|(3/2)^n\|$ could a priori dip to $0$ along a subsequence. Since $3/2$ is algebraic, Hardy's theorem does rule out $\|(3/2)^n\| \to 0$ in the full-limit sense — which is exactly why the open problem lives entirely in the transcendental regime, where neither table nor theorem is available.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*