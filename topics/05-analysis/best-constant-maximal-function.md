---
id: 05-analysis/best-constant-maximal-function
title: "Rate of Convergence in the Hardy-Littlewood Maximal Constant"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Rate of Convergence in the Hardy-Littlewood Maximal Constant

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/best-constant-maximal-function` · **Status:** open

## 1. Problem Statement / Conjecture

Let $M_n$ denote the centered Hardy–Littlewood maximal operator on $\mathbb{R}^n$ with Euclidean balls. Write

$$A_n = \sup_{\substack{f \in L^1(\mathbb{R}^n) \\ f \neq 0}} \; \sup_{\lambda > 0} \; \frac{\lambda \, |\{x : M_n f(x) > \lambda\}|}{\|f\|_{L^1}}, \qquad
B_n(p) = \|M_n\|_{L^p(\mathbb{R}^n) \to L^p(\mathbb{R}^n)} .$$

Three linked questions are open.

1. **(Stein–Strömberg problem.)** Is $\sup_n A_n < \infty$? Equivalently, is the weak type $(1,1)$ constant for Euclidean balls dimension-free? If not, what is the exact growth rate of $A_n$ as $n \to \infty$?
2. **(Rate.)** Determine the asymptotics of $B_n(p)$ as $p \to 1^+$ with $n$ fixed, and the joint asymptotics of $B_n(p)$ as $n \to \infty$, $p \to 1^+$ simultaneously. Known: $B_n(p) \le C_p$ uniformly in $n$ for each fixed $p>1$, but the blow-up rate of $C_p$ as $p \downarrow 1$ is not known to be dimension-free.
3. **(Exact constants.)** Compute $A_n$ and $B_n(p)$ exactly. Only $n=1$ weak type is settled ($A_1 = \frac{11+\sqrt{61}}{12}$, Melas 2003); $B_1(p)$ is unknown for every $p \in (1,\infty)$.

A complete resolution of (1) means either a proof that $A_n \le C$ with $C$ absolute, or a lower bound $A_n \to \infty$ with a matching upper bound.

## 2. Mathematical Foundations

For $f \in L^1_{\mathrm{loc}}(\mathbb{R}^n)$ and $B(x,r)$ the Euclidean ball,

$$M_n f(x) = \sup_{r>0} \frac{1}{|B(x,r)|}\int_{B(x,r)} |f(y)|\,dy,
\qquad
\widetilde{M}_n f(x) = \sup_{B \ni x} \frac{1}{|B|}\int_B |f|,$$

the **centered** and **uncentered** operators; $M_n \le \widetilde M_n \le 2^n M_n$. For a convex symmetric body $K \subset \mathbb{R}^n$, $M^K$ is defined with dilates $x + tK$.

**Classical theorem (Hardy–Littlewood 1930; Wiener 1939).** $M_n$ is weak $(1,1)$ and bounded on $L^p$ for $p>1$. The Vitali argument gives $A_n \le 3^n$ (or $5^n$ for the uncentered version), and Marcinkiewicz interpolation gives

$$B_n(p) \le \Big( \frac{p}{p-1} A_n \Big)^{1/p} \cdot 2^{1/p'} \cdot \big(\tfrac{p}{p-1}\big)^{\!1/p}\!,$$

so any dimension-free $L^p$ bound near $p=1$ is tied to $A_n$.

**Stein–Strömberg (1983).** Two facts:
$$A_n \le C n \quad (\text{all } n), \qquad B_n(p) \le C_p \quad (p>1, \ C_p \text{ independent of } n).$$
The second uses the heat/Poisson semigroup and Stein's maximal ergodic theorem; the first replaces $3^n$ by a covering argument with linear loss.

**Bourgain–Carbery (1986).** For every symmetric convex body $K$, $\|M^K\|_{L^p \to L^p} \le C_p$ with $C_p$ independent of $n$ and $K$, for $p>3/2$ (Bourgain), and for all $p>1$ for a large class via Carbery's almost-orthogonality principle; Bourgain (1986, Israel J. Math.) extended to all $p>1$ for balls of $\ell^q$ type and later (2014) to the cube.

**Exact one-dimensional constants.**
- Uncentered, $L^p(\mathbb{R})$ (Grafakos–Montgomery-Smith 1997): $\|\widetilde M_1\|_{L^p \to L^p}$ is the unique root $x>1$ of
$$(p-1)x^p - p\,x^{p-1} - 1 = 0 .$$
- Uncentered weak $(1,1)$: constant exactly $2$.
- Centered weak $(1,1)$ (Melas 2003): $A_1$ is the larger root of $12C^2 - 22C + 5 = 0$,
$$A_1 = \frac{11+\sqrt{61}}{12} = 1.5675208\ldots$$
- Dyadic maximal operator: $\|M^{\mathrm{dyad}}\|_{L^p \to L^p} = \frac{p}{p-1}$ exactly, in every dimension.

## 3. History & State of the Art (SOTA)

- **1930.** Hardy and Littlewood prove the $L^p$ maximal theorem on $\mathbb{R}$ ("A maximal theorem with function-theoretic applications", Acta Math.), motivated by a cricket-averages heuristic and by Hardy-space theory.
- **1939.** Wiener gives the covering-lemma proof and the $n$-dimensional weak $(1,1)$ inequality with constant $3^n$.
- **1976–1982.** Stein establishes dimension-free $L^p$ bounds for spherical means and for the ball maximal function, $p>1$.
- **1983.** Stein–Strömberg: $A_n = O(n)$; they explicitly raise whether $A_n = O(1)$.
- **1986.** Bourgain and Carbery independently obtain dimension-free $L^p$ bounds for general symmetric convex bodies in restricted ranges of $p$; Müller (1990) extends to a geometric class.
- **1997–2003.** Sharp constants in dimension one: Grafakos–Montgomery-Smith ($L^p$, uncentered), Melas (weak $(1,1)$, centered) — the latter a 40-page Bellman/extremal-measure analysis in *Annals of Mathematics*.
- **2009–2013.** For **cubes** the answer is negative: Aldaz proves the weak $(1,1)$ constants tend to infinity with $n$; Aubrun and then Iakovlev–Strömberg give quantitative lower bounds.
- **2014–2019.** Bourgain settles dimension-free $L^p$, $p>1$, for the cube; Bourgain–Mirek–Stein–Wróbel transport dimension-free estimates to $\mathbb{Z}^d$ and to variational/jump inequalities.

**SOTA for the headline question:** for Euclidean balls, $c \le A_n \le Cn$ — no improvement on the linear upper bound and no super-constant lower bound in over 40 years.

## 4. Partial Results / Verified Cases

| Setting | Result | Source |
|---|---|---|
| $n=1$, centered, weak $(1,1)$ | $A_1 = (11+\sqrt{61})/12$ | Melas 2003 |
| $n=1$, uncentered, weak $(1,1)$ | constant $=2$, extremal $f = \delta_0$ | classical |
| $n=1$, uncentered, $L^p$, all $p>1$ | root of $(p-1)x^p - px^{p-1}=1$ | Grafakos–Montgomery-Smith 1997 |
| all $n$, dyadic cubes, $L^p$ | $p/(p-1)$ exactly; weak $(1,1)$ constant $1$ | Bellman-function analysis (Melas) |
| all $n$, balls, $p>1$ | $B_n(p) \le C_p$, dimension-free | Stein 1982; Stein–Strömberg 1983 |
| all $n$, symmetric convex $K$, $p > 3/2$ | dimension-free | Bourgain 1986 |
| all $n$, cubes / $\ell^q$ balls, $p>1$ | dimension-free | Bourgain 1986, 2014 |
| all $n$, cubes, weak $(1,1)$ | constants $\to \infty$; $\gtrsim (\log n)^{1-\varepsilon}$ (Aubrun), $\gtrsim n^{1/4}$ (Iakovlev–Strömberg) | Aldaz 2011 |
| metric measure spaces, $n$-microdoubling | weak $(1,1)$ constant $O(\log n)$ | Naor–Tao 2010 |
| radial $f$, all $n$ | $A_n$ bounded uniformly on radial functions | Stein–Strömberg 1983 |

## 5. Principal Obstacles

- **No $L^1$ substitute for the semigroup method.** The dimension-free $L^p$ proofs run through the heat semigroup $e^{t\Delta}$, Stein's maximal ergodic theorem, and $g$-function/square-function arguments. All of these are $L^2$-based and interpolate down only to $p>1$; at $p=1$ square functions carry no information.
- **Covering lemmas lose dimension by construction.** Vitali gives $3^n$; every refinement (Besicovitch, Stein–Strömberg's random-covering step) still has a dimensional deficit, and Naor–Tao showed the localization/random-martingale scheme *cannot* beat $O(\log n)$ in general metric spaces — so a positive answer for balls must use Euclidean geometry, not covering.
- **The cube counterexample does not transfer.** Aldaz's blow-up for cubes exploits the fact that the cube's extreme points concentrate at distance $\sqrt{n}$ from the center; the Euclidean ball is isotropic and its dilates are far better behaved, so the counterexample machinery has no analogue. Conversely, the cube shows any proof of $A_n = O(1)$ must be sensitive to the shape of $K$, ruling out all body-independent arguments.
- **Extremal measures are unmanageable.** Melas's $n=1$ solution required classifying extremizers among sums of Dirac masses and solving a nontrivial optimization; in $\mathbb{R}^n$ the configuration space of extremal measures is not even conjecturally described.
- **Non-linearity of $M$.** $M$ is sublinear, not linear, so no duality, no spectral theory, and no interpolation-with-change-of-measure tricks apply directly to the constant itself.

## 6. The Gap

The proven envelope is $c \le A_n \le Cn$; the conjectured truth is $A_n = O(1)$ (Stein–Strömberg). The gap is a full factor of $n$, and it is not a matter of optimizing constants: no known technique produces *any* sublinear upper bound, and no known construction produces *any* unbounded lower bound for balls. The precise missing step is an $L^1$-endpoint replacement for the $L^2$ square-function machinery — a covering or stopping-time argument in $\mathbb{R}^n$ whose loss depends on the isotropy of the ball rather than on $n$. For the rate question, the gap is the joint limit: dimension-free $C_p$ is known for each fixed $p>1$, but no estimate of the form $C_p \lesssim (p-1)^{-\alpha}$ with $\alpha$ absolute and dimension-free is available.

## 7. Current Research (as of June 2026)

- **Mirek–Stein school (Rutgers, Bonn, IMPAN).** Dimension-free estimates for discrete averages over $\mathbb{Z}^d$, for $\ell^q$ balls, and for $r$-variational and jump inequalities; the program pushes the range of $q$ and $p$ and quantifies dependence on $q$. *(frontier — verify)* recent work isolates for which $\ell^q$ balls the dimension-free $L^p$ range can be extended to $p$ arbitrarily close to $1$.
- **Convex-geometry route.** Attacks via isotropic constants, the Bourgain slicing problem, and concentration of measure on convex bodies; the resolution of slicing (Klartag–Lehec, 2024–2025) has renewed interest in whether isotropic-position arguments give sublinear $A_n$. *(frontier — verify)*
- **Bellman-function / exact-constant community.** Ivanisvili, Slavin, Vasyunin, Volberg: exact constants for dyadic and martingale maximal operators, with attempts to transfer Bellman methods to the continuous centered operator.
- **Lower-bound constructions.** Following Iakovlev–Strömberg, attempts to build high-dimensional configurations of point masses for Euclidean balls; all published attempts yield $O(1)$ so far.
- **Sharp constants in $n=1$ for $L^p$, centered.** Numerical/variational studies continue; no closed form is conjectured.

## 8. Future Work

- Prove or disprove $A_n = o(n)$ — even $A_n = O(n^{1-\varepsilon})$ or $A_n = O(n/\log n)$ would be a genuine break.
- Establish an explicit dimension-free rate $C_p \lesssim (p-1)^{-\alpha}$ for balls, and identify the optimal $\alpha$; the dyadic model suggests $\alpha = 1$.
- Determine the exact value of $A_2$, or any $n \ge 2$; a second data point would test whether $A_n$ increases at all.
- Characterize which symmetric convex bodies $K$ have dimension-free weak $(1,1)$ constants. Balls and cubes sit on opposite sides; the dividing invariant is unidentified.
- Transfer Melas's extremal-measure classification to the uncentered $L^p$ setting in $\mathbb{R}^n$, where the one-dimensional answer is already algebraic.

## 9. Key References

- **[Foundational]** G. H. Hardy and J. E. Littlewood. *A maximal theorem with function-theoretic applications.* Acta Mathematica 54 (1930), 81–116.
- **[Foundational]** E. M. Stein and J.-O. Strömberg. *Behavior of maximal functions in $\mathbf{R}^n$ for large $n$.* Arkiv för Matematik 21 (1983), 259–269.
- **[Foundational]** E. M. Stein. *Singular Integrals and Differentiability Properties of Functions.* Princeton University Press, 1970.
- **[SOTA]** A. D. Melas. *The best constant for the centered Hardy–Littlewood maximal inequality.* Annals of Mathematics 157 (2003), 647–688.
- **[SOTA]** L. Grafakos and S. Montgomery-Smith. *Best constants for uncentred maximal functions.* Bulletin of the London Mathematical Society 29 (1997), 60–64.
- **[SOTA]** J. Bourgain. *On high-dimensional maximal functions associated to convex bodies.* American Journal of Mathematics 108 (1986), 1467–1476.
- **[SOTA]** J. Bourgain. *On the $L^p$-bounds for maximal functions associated to convex bodies in $\mathbb{R}^n$.* Israel Journal of Mathematics 54 (1986), 257–265.
- **[SOTA]** A. Carbery. *An almost-orthogonality principle with applications to maximal functions associated to convex bodies.* Bulletin of the AMS 14 (1986), 269–273.
- **[SOTA]** J. M. Aldaz. *The weak type $(1,1)$ bounds for the maximal function associated to cubes grow to infinity with the dimension.* Annals of Mathematics 173 (2011), 1013–1023.
- **[SOTA]** J. Bourgain. *On the Hardy–Littlewood maximal function for the cube.* Israel Journal of Mathematics 203 (2014), 275–293.
- **[SOTA]** A. Naor and T. Tao. *Random martingales and localization of maximal inequalities.* Journal of Functional Analysis 259 (2010), 731–779.
- **[SOTA]** J. Bourgain, M. Mirek, E. M. Stein, B. Wróbel. *Dimension-free estimates for discrete Hardy–Littlewood averaging operators over the cubes in $\mathbb{Z}^d$.* American Journal of Mathematics 141 (2019), 857–905.
- **[Survey]** L. Grafakos. *Classical Fourier Analysis*, 3rd ed. Springer GTM 249, 2014 (Chapter 2).
- **[Survey]** M. Mirek, E. M. Stein, B. Wróbel. *Dimension-free estimates for maximal functions: a survey* — in *Harmonic Analysis and Applications*, AMS, 2020.

## 10. Worked Example / Concrete Special Case

**(a) The uncentered constant in one dimension is exactly $2$; the centered one is not visible from a single mass.**

Take $f_\varepsilon$ an $L^1$-normalized bump concentrating at $0$; in the limit $f = \delta_0$, $\|f\|_1 = 1$.

*Uncentered:* the best interval containing $x \ne 0$ and containing $0$ has length $|x|$, so $\widetilde M f(x) = 1/|x|$. Hence
$$\{\widetilde M f > \lambda\} = (-1/\lambda, 1/\lambda), \qquad \lambda\,|\{\widetilde M f > \lambda\}| = 2 = 2\|f\|_1 .$$
So the constant $2$ from the Vitali argument is attained.

*Centered:* the ball must be $B(x,r)$ with $r \ge |x|$, so $Mf(x) = \frac{1}{2|x|}$ and
$$\lambda\,|\{Mf > \lambda\}| = \lambda \cdot \frac{1}{\lambda} = 1 = \|f\|_1 .$$
A single Dirac mass gives only the trivial constant $1$. Two symmetric masses $\delta_{-1} + \delta_{1}$ also give ratio exactly $1$ (the two level intervals either separate, giving measure $4s$ at $\lambda = 1/(2s)$, or merge into $[-(2s-1), 2s-1]$, and both cases return $1$). Melas's theorem says the true supremum $\frac{11+\sqrt{61}}{12} \approx 1.5675$ is reached only by **asymmetrically weighted** pairs of masses — which is exactly why the centered problem is hard: the extremizer is not a symmetric, self-similar configuration, and no such configuration is known in $\mathbb{R}^n$.

**(b) An exactly solved rate: $p=2$, uncentered, $n=1$.**

Grafakos–Montgomery-Smith: solve $(p-1)x^p - p x^{p-1} - 1 = 0$ at $p=2$:
$$x^2 - 2x - 1 = 0 \implies x = 1 + \sqrt{2} = 2.41421\ldots$$
so $\|\widetilde M_1\|_{L^2 \to L^2} = 1+\sqrt 2$ exactly. As $p \to 1^+$, substituting $x = p/(p-1)$ into the left side gives $x^{p-1}\big((p-1)x - p\big) - 1 = -1 < 0$, so the root exceeds $p/(p-1)$, and one checks
$$\|\widetilde M_1\|_{L^p \to L^p} = \frac{p}{p-1}\,(1 + o(1)), \qquad p \to 1^+ .$$
That is the model rate. The open problem is whether the same $(p-1)^{-1}$ rate holds for the **centered** operator with a constant **independent of $n$** — which would follow from, and is essentially equivalent in strength to, $\sup_n A_n < \infty$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*