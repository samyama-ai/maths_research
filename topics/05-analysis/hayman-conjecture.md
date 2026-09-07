---
id: 05-analysis/hayman-conjecture
title: "Hayman Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hayman Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/hayman-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $f$ be a transcendental meromorphic function on $\mathbb{C}$ and let $n \ge 1$ be an integer. **Hayman's conjecture** (Problem 1.19 in *Research Problems in Function Theory*, 1967) asserts:

> For every $a \in \mathbb{C} \setminus \{0\}$, the function $f^n f' - a$ has infinitely many zeros.

Equivalently, the differential monomial $f^n f'$ assumes every finite nonzero value infinitely often. Three hypotheses are all necessary:

- **Transcendence.** For rational $f$ the claim is vacuous or false ($f(z)=z$, $n=1$: $ff'=z$ takes each value once).
- **$a \ne 0$.** $f = e^{z}$ gives $f^n f' = e^{(n+1)z}$, which omits $0$.
- **$n \ge 1$.** For $n = 0$ the statement is false: $f = e^{z} + z$ has $f' - 1 = e^z \neq 0$.

A complete solution requires, for each $n \ge 1$ and each $a \neq 0$, either a proof that $N\!\left(r, 1/(f^nf'-a)\right) \to \infty$, or a transcendental meromorphic counterexample. The conjecture is now a **theorem** for all $n \ge 1$; the surviving open problems are the companion Hayman problem for $f' - af^{2}$ and the difference/$q$-difference analogues (Sections 6–7).

## 2. Mathematical Foundations

**Nevanlinna theory.** For $f$ meromorphic on $\mathbb{C}$ set

$$m(r,f) = \frac{1}{2\pi}\int_0^{2\pi} \log^+ \left|f(re^{i\theta})\right| \, d\theta, \qquad N(r,f) = \int_0^r \frac{n(t,f)-n(0,f)}{t}\,dt + n(0,f)\log r,$$

where $n(t,f)$ counts poles with multiplicity in $|z|\le t$, and $T(r,f) = m(r,f)+N(r,f)$. Write $\bar N$ for the counting function ignoring multiplicity and $N(r,1/f)$ for zeros. $f$ is transcendental iff $T(r,f)/\log r \to \infty$. Write $S(r,f)$ for any quantity that is $o(T(r,f))$ outside a set of finite measure.

**Lemma on the logarithmic derivative.** $m(r, f'/f) = S(r,f)$; hence $T(r,f') \le 2T(r,f) + S(r,f)$.

**Hayman's inequality** (1959) is the quantitative engine. For $f$ transcendental meromorphic, $n \ge 3$, $a\neq0$:

$$T(r,f) \;\le\; \left(2+\frac{1}{n}\right) N\!\left(r,\frac{1}{f}\right) \;+\; \left(2+\frac{2}{n}\right) N\!\left(r,\frac{1}{f^nf'-a}\right) + S(r,f),$$

together with **Hayman's alternative**: a transcendental meromorphic $f$ either takes $0$ infinitely often or $f^{(k)}$ takes every $a \ne 0$ infinitely often.

**Reduction to a derivative.** Setting $F = \dfrac{f^{\,n+1}}{n+1}$ gives $F' = f^n f'$, and every zero of $F$ has multiplicity divisible by $n+1$. So the conjecture says: if $F$ is a meromorphic function all of whose zeros and poles have multiplicity $\ge n+1$ (with $F^{1/(n+1)}$ single-valued), then $F' - a$ has infinitely many zeros.

**Zalcman's rescaling lemma** (1975; Pang's refinement). A family $\mathcal{F}$ of meromorphic functions on a domain $D$ is not normal at $z_0$ iff there exist $f_k \in \mathcal F$, $z_k \to z_0$, $\rho_k \to 0^+$, and $-1 < \alpha < 1$ with

$$g_k(\zeta) := \rho_k^{-\alpha} f_k(z_k + \rho_k \zeta) \longrightarrow g(\zeta)$$

locally uniformly in the spherical metric, $g$ nonconstant meromorphic on $\mathbb{C}$ with bounded spherical derivative $g^{\\#}(\zeta) \le g^{\\#}(0)=1$ (hence $g$ of order $\le 2$). Taking $\alpha = -1/(n+1)$ makes $f^n f'$ scaling-invariant, which is exactly what the $n=1$ proof needs.

## 3. History & State of the Art (SOTA)

- **1959.** Hayman, *Picard values of meromorphic functions and their derivatives* (Ann. of Math. 70), proves the statement for **$n \ge 3$** via his inequality, and proves $f' - af^{n}$ has infinitely many zeros for $n \ge 5$.
- **1964/1967.** *Meromorphic Functions* codifies the machinery; *Research Problems in Function Theory* records the $n=1,2$ cases as Problem 1.19.
- **1967.** Clunie, *On a result of Hayman* (J. London Math. Soc. 42): the conjecture holds for all $n \ge 1$ when $f$ is **entire**.
- **1979.** Mues, *Über ein Problem von Hayman* (Math. Z. 164): settles **$n = 2$** for meromorphic $f$, and lowers the $f'-af^n$ threshold to $n \ge 3$.
- **1995.** The remaining case $n=1$ falls three times independently: Bergweiler–Eremenko (finite order, via singularities of the inverse function, Rev. Mat. Iberoamericana 11), Chen–Fang (Sci. China Ser. A 38), and Zalcman (Bar-Ilan preprint), the latter two by normal-family rescaling. This closes the conjecture as stated.
- **2006–2010s.** Halburd–Korhonen's difference analogue of the logarithmic-derivative lemma opens the **difference Hayman conjecture**; Laine–Yang (2007) prove the entire finite-order case for $f(z)^n f(z+c)$, $n \ge 2$.
- **2019.** Hayman–Lingham, *Research Problems in Function Theory: Fiftieth Anniversary Edition*, records 1.19 as solved and flags the $f'-af^2$ residue as open.

## 4. Partial Results / Verified Cases

| Setting | Range | Result |
|---|---|---|
| $f$ meromorphic transcendental | $n \ge 3$ | Hayman 1959 |
| $f$ entire transcendental | all $n \ge 1$ | Clunie 1967 |
| $f$ meromorphic | $n = 2$ | Mues 1979 |
| $f$ meromorphic, finite order | $n = 1$ | Bergweiler–Eremenko 1995 |
| $f$ meromorphic, arbitrary order | $n = 1$ | Chen–Fang 1995; Zalcman 1995 |
| $f' - a f^{n}$, meromorphic | $n \ge 3$ | Hayman 1959 ($n\ge5$), Mues 1979 ($n=3,4$) |
| $f' - af^{2}$ | $f$ entire; $f$ with finitely many poles | classical; **open in general** |
| Difference: $f(z)^n f(z+c) - a$ | $f$ entire, finite order, $n \ge 2$ | Laine–Yang 2007 |
| Difference: $f(z)^n f(z+c) - a$ | $f$ meromorphic, $n \ge 6$ (typical thresholds) | Liu–Yang and successors |
| $q$-difference: $f(z)^n f(qz) - a$ | $f$ of zero order, $n \ge 2$ | Zheng–Chen and successors |

Quantitatively, in the proven cases one gets more than infinitude: for $n\ge 3$ Hayman's inequality forces $\delta(a, f^nf') \le 1 - \tfrac{n}{2n+2}$, i.e. a positive **density** of $a$-points, not merely infinitely many.

## 5. Principal Obstacles

- **Loss of the pole term at $n=1$.** Hayman's inequality carries a coefficient $2 + 1/n$ on $N(r,1/f)$; the derivation of the error control degrades precisely as $n \downarrow 1$, and at $n=1$ the pole contribution of $f'$ no longer absorbs into $S(r,f)$. Nevanlinna theory alone therefore cannot reach $n=1$: the second fundamental theorem gives a deficiency budget of $2$, and $f$, $f^nf'-a$ and the poles consume it exactly.
- **Multiplicity is too weak.** In the reduction $F=f^{n+1}/(n+1)$, the useful hypothesis is that zeros of $F$ have multiplicity $\ge n+1$. At $n=1$ this is only multiplicity $2$, the borderline at which the standard "zeros are heavy" counting arguments become equalities.
- **Poles are not local obstructions.** For entire $f$ (Clunie) one can write $f^nf'-a = e^{h}$ under a Picard-type assumption and use Borel/Hadamard factorisation. With poles, $f^n f' - a$ zero-free gives no factorisation, since a meromorphic zero-free function is $e^h/\prod$ nothing — poles destroy the exponential representation.
- **Infinite order kills asymptotic/singularity methods.** The Bergweiler–Eremenko route counts direct and logarithmic singularities of $f^{-1}$ and needs finite order (Denjoy–Carleman–Ahlfors). It does not extend to $f$ of infinite order.
- **Rescaling limits must be classified.** The Zalcman–Pang route reduces the problem to: *no nonconstant meromorphic $g$ of order $\le 2$ with $g^{\\#}$ bounded satisfies $g^ng' \equiv a$ or $g^ng'\neq a$*. Classifying such rescaling limits is delicate for meromorphic $g$ — one must rule out functions like $g = c\,\wp$-type or $g$ with $g^ng'-a$ zero-free, and the elliptic candidates are exactly the hard ones.
- **In the difference setting there is no chain rule.** $\Delta_c f = f(z+c)-f(z)$ has no product rule and $T(r, f(z+c)) = T(r,f)+S(r,f)$ only for finite order (Halburd–Korhonen, Chiang–Feng), so infinite-order and meromorphic-with-many-poles cases lose the fundamental estimate.

## 6. The Gap

For the conjecture as literally stated by Hayman there is **no gap**: $n\ge 3$ (1959), $n = 2$ (1979) and $n = 1$ (1995) together cover all cases. The residual gaps in the surrounding problem cluster are sharp:

1. **$f' - af^2$.** Hayman's method needs $n\ge5$, Mues reaches $n=3$; $n=2$ remains open for general transcendental meromorphic $f$. The barrier: $f'/f^2 = -(1/f)'$, so the problem becomes "does $g' + a$ have infinitely many zeros for $g = 1/f$?" — a statement about a derivative omitting a *nonzero* value, which is exactly the Picard-type case where $e^z$-like counterexamples cannot be excluded by counting alone.
2. **Difference analogue at small $n$.** For meromorphic finite-order $f$, thresholds of $n\ge 6$ (or $n\ge2$ for entire) are proved; the conjectured sharp threshold is $n \ge 2$ meromorphic and the case $n=1$, $f(z)f(z+c)-a$, is false in general (e.g. $f$ with $f(z)f(z+c)$ a Picard-exceptional pattern), so the exact boundary is unsettled.
3. **Infinite order in the difference setting**, where the logarithmic-difference lemma is unavailable.

## 7. Current Research (as of June 2026)

- **Normal families / Bloch's principle.** The Pang–Zalcman rescaling framework (Bar-Ilan; Fang's school in Nanjing/Shanghai) continues to be the tool of choice for sharpening $f^nf'$-type results to shared-value and small-function versions ($a$ replaced by $a(z)$ with $T(r,a)=S(r,f)$).
- **Singularities of inverse functions.** Bergweiler (Kiel) and Eremenko (Purdue) developed the direct/logarithmic-singularity counting that gave the finite-order $n=1$ case; extensions target $f'-af^2$ for classes with controlled singular values (Speiser and Eremenko–Lyubich class $\mathcal{B}$). *(frontier — verify)*
- **Difference and $q$-difference value distribution.** Groups around Korhonen (Eastern Finland), Laine, and several Chinese groups push thresholds for $f^n f(z+c)$, $f^n \Delta_c f$, and $q$-shifts downward; recent preprints claim $n \ge 2$ meromorphic under a deficiency assumption $\delta(\infty,f)>0$. *(frontier — verify)*
- **Tropical and non-Archimedean analogues.** Nevanlinna theory over $p$-adic fields and tropical Nevanlinna theory (Halburd–Southall, Korhonen–Tohge) yield Hayman-type theorems where the counterexample structure is more rigid.

## 8. Future Work

- Settle $f' - af^{2}$: the most-cited concrete descendant. Suggested route (Bergweiler, Zalcman): classify meromorphic $g$ of order $\le2$ with bounded spherical derivative and $g' + a$ zero-free; the elliptic and $1/(\text{entire})$ families must be eliminated.
- Obtain *quantitative* $n=1$ results: a deficiency bound $\delta(a, ff') \le 1-c$ with explicit $c>0$, matching Hayman's $n\ge3$ inequality. The 1995 proofs are qualitative (via normality/compactness) and yield no density.
- Extend to differential polynomials $f^n f^{(k)}$ and $f^n L[f]$ with $L$ a linear differential operator with small coefficients; thresholds in $n$ are known but not sharp.
- Prove the meromorphic difference Hayman conjecture at the conjectured sharp $n$, and remove the finite-order hypothesis by finding an infinite-order substitute for the logarithmic-difference lemma.

## 9. Key References

- **[Foundational]** W. K. Hayman. *Picard values of meromorphic functions and their derivatives.* Annals of Mathematics (2) **70** (1959), 9–42.
- **[Foundational]** W. K. Hayman. *Meromorphic Functions.* Oxford Mathematical Monographs, Clarendon Press, 1964.
- **[Foundational]** W. K. Hayman. *Research Problems in Function Theory.* Athlone Press, London, 1967. (Problem 1.19)
- **[Partial]** J. Clunie. *On a result of Hayman.* Journal of the London Mathematical Society **42** (1967), 389–392.
- **[Partial]** E. Mues. *Über ein Problem von Hayman.* Mathematische Zeitschrift **164** (1979), 239–259.
- **[SOTA]** W. Bergweiler and A. Eremenko. *On the singularities of the inverse to a meromorphic function of finite order.* Revista Matemática Iberoamericana **11** (1995), 355–373.
- **[SOTA]** H. Chen and M. Fang. *The value distribution of $f^n f'$.* Science in China Series A **38** (1995), 789–798.
- **[Method]** L. Zalcman. *A heuristic principle in complex function theory.* American Mathematical Monthly **82** (1975), 813–817.
- **[Survey]** L. Zalcman. *Normal families: new perspectives.* Bulletin of the American Mathematical Society **35** (1998), 215–230.
- **[Survey]** W. Bergweiler. *Bloch's principle.* Computational Methods and Function Theory **6** (2006), 77–108.
- **[Method]** X. Pang and L. Zalcman. *Normal families and shared values.* Bulletin of the London Mathematical Society **32** (2000), 325–331.
- **[Difference]** R. G. Halburd and R. J. Korhonen. *Difference analogue of the lemma on the logarithmic derivative with applications to difference equations.* Journal of Mathematical Analysis and Applications **314** (2006), 477–487.
- **[Difference]** I. Laine and C.-C. Yang. *Value distribution of difference polynomials.* Proceedings of the Japan Academy, Series A **83** (2007), 148–151.
- **[Survey]** W. K. Hayman and E. F. Lingham. *Research Problems in Function Theory: Fiftieth Anniversary Edition.* Springer, 2019.

## 10. Worked Example / Concrete Special Case

**Claim.** Let $f$ be transcendental entire of finite order with no zeros, and $a \ne 0$. Then $ff' - a$ has infinitely many zeros (the $n=1$ entire case).

*Proof.* Since $f$ is zero-free of finite order, Hadamard factorisation gives $f = e^{g}$ with $g$ a nonconstant polynomial, $\deg g = d \ge 1$. Then

$$ff' = g'\,e^{2g}.$$

Suppose for contradiction that $ff' - a$ has only finitely many zeros. Then $g'e^{2g} - a = P e^{h}$ with $P$ a polynomial and $h$ entire; comparing orders, $\rho(g'e^{2g}) = d$ forces $h$ to be a polynomial of degree $\le d$. Differentiate:

$$\left(g'' + 2g'^2\right) e^{2g} = \left(P' + Ph'\right) e^{h}.$$

Hence

$$e^{\,2g - h} = \frac{P' + Ph'}{g'' + 2g'^{2}},$$

a rational function that is also entire and zero-free, so it is a nonzero constant $c_0$; therefore $2g - h$ is constant and $Pe^{h} = c\,e^{2g}$ for some $c \ne 0$. Substituting back:

$$\left(g' - c\right) e^{2g} = a .$$

If $g' \equiv c$, then $a = 0$, contradiction. Otherwise $Q := g'-c$ is a nonzero polynomial, and $Q e^{2g}$ is a transcendental entire function; by Liouville it cannot equal the constant $a$ (indeed $Qe^{2g}$ is unbounded along any ray where $\operatorname{Re} g \to +\infty$). Contradiction. $\square$

**Where this breaks.** The argument used two things unavailable in general: (i) the factorisation $f = e^g$, valid only because $f$ is entire *and* zero-free; (ii) finite order, to force $h$ polynomial. For meromorphic $f$ of infinite order neither survives, and one must instead rescale: assuming $ff' \ne a$ on $\mathbb{C}$, the family $\{f_k(\zeta) = k^{1/2} f(\zeta/k)\}$ (the $\alpha = -1/2$ normalisation that leaves $f^nf'$ invariant for $n=1$) fails to be normal, and Zalcman's lemma produces a nonconstant meromorphic $g$ of order $\le 2$ with $gg' \ne a$; excluding such $g$ is exactly the content of the 1995 proofs.

**Sharpness check.** With $a=0$ the statement is false: $f=e^{z}$ gives $ff' = e^{2z}$, zero-free. With $f$ rational, $f=z$ gives $ff'=z$, taking each $a$ exactly once — so "transcendental" and "$a \ne 0$" are both indispensable.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*