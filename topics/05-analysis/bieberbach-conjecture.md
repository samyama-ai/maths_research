---
id: 05-analysis/bieberbach-conjecture
title: "Bieberbach Conjecture"
topic: 05-analysis
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bieberbach Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/bieberbach-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $\mathbb{D} = \{z \in \mathbb{C} : |z| < 1\}$ and let $S$ denote the class of **schlicht** functions: functions $f$ holomorphic and injective on $\mathbb{D}$ with the normalization
$$f(z) = z + a_2 z^2 + a_3 z^3 + \cdots , \qquad f(0)=0,\ f'(0)=1 .$$

**Bieberbach's conjecture (1916).** For every $f \in S$ and every $n \ge 2$,
$$|a_n| \le n ,$$
with equality for some $n$ if and only if $f$ is a rotation of the Koebe function
$$k(z) = \frac{z}{(1-z)^2} = \sum_{n\ge 1} n z^n .$$

A complete proof must establish the bound for **all** $n$ simultaneously and for the full class $S$ (no smoothness, boundedness, starlikeness or symmetry hypotheses), together with the equality characterization. A disproof would exhibit a single univalent $f$ and index $n$ with $|a_n| > n$.

**Status.** Proved by **Louis de Branges** in 1984 (published 1985). The page is retained because (a) the proof route — Milin's conjecture plus the Askey–Gasper inequality — remains the only known one and is still being simplified, and (b) the natural strengthenings and companion coefficient problems (Zalcman, Krzyż, bounded univalent coefficients, Bombieri's local conjecture) remain open.

## 2. Mathematical Foundations

**The class $\Sigma$ and the area theorem.** Let $\Sigma$ be the family of $g(\zeta) = \zeta + b_0 + b_1\zeta^{-1} + b_2\zeta^{-2}+\cdots$ univalent on $|\zeta|>1$. Then
$$\sum_{n=1}^{\infty} n\,|b_n|^2 \le 1 ,$$
because the omitted set has nonnegative area (Gronwall, 1914).

**Square-root transform.** If $f\in S$, then $f(z^2)$ is nonvanishing on $\mathbb{D}\setminus\{0\}$ and admits an odd univalent square root
$$h(z) = \sqrt{f(z^2)} = z + c_3 z^3 + c_5 z^5 + \cdots \in S .$$
This device converts coefficient statements about $S$ into statements about odd univalent functions.

**Loewner theory.** Every $f\in S$ is a limit, locally uniformly, of solutions of the Loewner ODE. For a single-slit map with driving function $\kappa(t)$, $|\kappa(t)|=1$, the family $f(z,t)=e^{t}z+\cdots$ satisfies
$$\frac{\partial f}{\partial t}(z,t) \;=\; z\,\frac{\partial f}{\partial z}(z,t)\,\frac{1+\kappa(t)z}{1-\kappa(t)z}, \qquad f(z,0)=f(z).$$
Single-slit maps are dense in $S$, and $S$ is compact in the topology of locally uniform convergence, so bounds proved on a dense subclass pass to $S$.

**Logarithmic coefficients.** For $f\in S$ define $\gamma_n$ by
$$\log\frac{f(z)}{z} \;=\; 2\sum_{n=1}^{\infty}\gamma_n z^n .$$

**The chain of conjectures.**

- **Robertson (1936).** For odd $h(z)=\sum_{k\ge 0} c_{2k+1}z^{2k+1}\in S$ with $c_1=1$,
 $$\sum_{k=0}^{n-1}|c_{2k+1}|^2 \le n \quad (n\ge 1).$$
- **Milin (1971).** For every $f\in S$ and $n\ge 1$,
 $$\sum_{k=1}^{n}(n+1-k)\Big(k|\gamma_k|^2-\frac1k\Big) \;\le\; 0 .$$

Milin $\Rightarrow$ Robertson $\Rightarrow$ Bieberbach, the first implication via the **Lebedev–Milin second inequality**: if $\varphi=\sum_{k\ge1}\alpha_k z^k$ and $e^{\varphi}=\sum_{k\ge0}\beta_k z^k$, then
$$\sum_{k=0}^{n}|\beta_k|^2 \le (n+1)\exp\!\left(\frac{1}{n+1}\sum_{m=1}^{n}\sum_{k=1}^{m}\big(k|\alpha_k|^2-\tfrac1k\big)\right).$$

**Askey–Gasper inequality (1976).** For $\alpha>-2$ and $-1\le x\le 1$,
$$\sum_{k=0}^{n} \frac{P_k^{(\alpha,0)}(x)}{\binom{k+\alpha}{k}} \;\ge\; 0 ,$$
where $P_k^{(\alpha,\beta)}$ are Jacobi polynomials. This positivity is precisely what makes de Branges' weight system monotone.

## 3. History & State of the Art (SOTA)

- **1916** — Ludwig Bieberbach proves $|a_2|\le 2$ and remarks that $|a_n|\le n$ may hold generally (*Sitzungsber. Preuss. Akad. Wiss.*). His $|a_2|\le2$ yields the Koebe $1/4$-theorem and the distortion theorems.
- **1923** — Charles Loewner introduces the parametric method and proves $|a_3|\le 3$.
- **1925** — Littlewood proves $|a_n| \le e\,n < 2.72\,n$ for all $n$.
- **1932–36** — Littlewood–Paley conjecture $|c_{2k+1}|\le1$ for odd schlicht functions is disproved by Fekete and Szegő (1933), who compute the sharp bound for $|c_5|$; Robertson then formulates the correct quadratic substitute.
- **1955** — Garabedian and Schiffer prove $|a_4|\le4$ using variational methods and Grunsky-type inequalities.
- **1968–72** — $n=6$ (Pederson; Ozawa, independently) and $n=5$ (Pederson–Schiffer).
- **1972–78** — Asymptotic constants: FitzGerald gets $|a_n| < \sqrt{7/6}\,n \approx 1.081\,n$ by exponentiating Grunsky inequalities; Horowitz sharpens to $|a_n| < (209/140)^{1/6} n \approx 1.0657\,n$.
- **1984/85** — **de Branges** proves Milin's conjecture, hence Bieberbach's, in *A proof of the Bieberbach conjecture*, Acta Math. **154** (1985). The argument was verified at the Leningrad (Steklov) seminar of Milin, Emel'yanov and others in spring 1984.
- **1985–91** — Simplifications: FitzGerald–Pommerenke give a Loewner-theoretic proof avoiding operator theory; Weinstein (1991) gives a two-page proof using a generating-function identity for Legendre polynomials, later shown by Wilf and by Ekhad–Zeilberger to be equivalent to Askey–Gasper positivity.

## 4. Partial Results / Verified Cases

Before 1984, all of the following were established and remain the standard reference points:

| Result | Author(s), year |
|---|---|
| $|a_2|\le2$ | Bieberbach 1916 |
| $|a_3|\le3$ | Loewner 1923 |
| $|a_4|\le4$ | Garabedian–Schiffer 1955 |
| $|a_6|\le6$ | Pederson 1968; Ozawa 1969 |
| $|a_5|\le5$ | Pederson–Schiffer 1972 |
| $|a_n|\le e n$ | Littlewood 1925 |
| $|a_n| < 1.081\,n$ | FitzGerald 1972 |
| $|a_n| < 1.0657\,n$ | Horowitz 1978 |

Subclasses where $|a_n|\le n$ was elementary and pre-dates 1984: **starlike** functions ($\operatorname{Re}\,zf'/f>0$, Nevanlinna 1921), **close-to-convex** functions (Reade 1955), functions with **real coefficients** (Dieudonné, Rogosinski 1931), and functions **typically real** on $\mathbb{D}$. For **convex** functions the sharper $|a_n|\le1$ holds (Loewner 1917). Related bounded-coefficient problems remain only partially solved: for $f\in S$ with $|f|\le M$ the sharp $a_n$ bound is known only for small $n$ and large $M$ (Schaeffer–Spencer; Tammi).

## 5. Principal Obstacles

The historical obstacles are instructive because they still block the open successor problems.

- **No linear extremal principle.** $S$ is compact but not convex, and $f\mapsto a_n$ is a nonlinear functional on a nonconvex family. Standard convexity/duality arguments give nothing; extremal functions must be found by Schiffer variation, which produces a quadratic differential ODE for the omitted arc, solvable in closed form only for small $n$.
- **Case-by-case explosion.** Garabedian–Schiffer's $n=4$ proof and Pederson–Schiffer's $n=5$ proof each required heavy Grunsky-inequality computations tuned to the index; the algebra grows superexponentially and no uniform-in-$n$ pattern emerged.
- **Grunsky/exponentiation loss.** Grunsky inequalities are sharp for the Koebe function only in a limiting sense; exponentiating them (FitzGerald, Horowitz) leaves a multiplicative constant $>1$ that no refinement of that method removes — the deficit was structural, not a matter of effort.
- **The wrong linearization.** The Littlewood–Paley conjecture ($|c_{2k+1}|\le1$) was the natural strengthening and is **false** (Fekete–Szegő 1933). This showed that pointwise coefficient bounds on the odd transform cannot carry the argument; only averaged/quadratic forms (Robertson, Milin) survive.
- **Hidden special-function positivity.** The genuine obstruction was that the required monotonicity of de Branges' weight functions $\sigma_k(t)$ is equivalent to a nontrivial Jacobi-polynomial positivity (Askey–Gasper 1976) discovered independently of function theory. Nothing internal to geometric function theory suggested it.

## 6. The Gap

For the Bieberbach conjecture itself, the gap is closed. What separates Section 4 from Section 1 is exactly the step de Branges supplied: from *sharp bounds at finitely many indices plus a constant-factor bound at all indices* to a *single monotone-in-$t$ Loewner functional whose derivative has a fixed sign for all $n$*. Concretely, de Branges introduced weights $\sigma_k(t)$, $1\le k\le n$, with $\sigma_n(t)\equiv 0$ terminal conditions, and showed
$$\frac{d}{dt}\sum_{k=1}^{n}\sigma_k(t)\big(k|\gamma_k(t)|^2 - \tfrac1k\big) \ \ge\ 0$$
along the Loewner flow, provided $\dot\sigma_k(t) \le 0$ — and that last inequality is the Askey–Gasper positivity. The remaining gaps are in the successor problems: the **Zalcman conjecture** $|a_n^2-a_{2n-1}|\le(n-1)^2$ is open in general, and the sharp coefficient bounds for **bounded** univalent functions and for the **Krzyż** problem are unresolved.

## 7. Current Research (as of June 2026)

- **Proof compression and formalization.** Weinstein's proof and its Zeilberger–Ekhad WZ-certified variant are the shortest known; work on machine-checked geometric function theory (Lean/mathlib's growing complex-analysis library) targets Loewner theory and the Koebe $1/4$-theorem as prerequisites, with de Branges not yet formalized *(frontier — verify)*.
- **Logarithmic coefficients.** Sharp bounds on $\sum|\gamma_n|^2$ and on individual $|\gamma_n|$ for subclasses (starlike, close-to-convex, Bazilevič) are an active industry; the sharp bound on $|\gamma_n|$ over all of $S$ for $n\ge3$ is open.
- **Zalcman and generalized Zalcman.** Krushkal established the conjecture for $n\le6$ and asymptotically for large $n$ by holomorphic-motion and Teichmüller-space methods; general $n$ remains open, as does the Ma generalized form $|a_na_m-a_{n+m-1}|$.
- **Bombieri's local conjecture.** Bombieri conjectured that the Koebe function is a local minimum in a strong sense; Greiner and Roth disproved it for the pair $(m,n)=(3,2)$ (*Proc. Amer. Math. Soc.* 129, 2001), and the correct local structure near $k$ is still being mapped.
- **SLE and Loewner analysis.** The Schramm–Loewner evolution has revitalized the driving-function viewpoint; questions about coefficient growth for random and for Hölder-driven Loewner chains are studied at Cambridge, Geneva, Bonn and Helsinki.

## 8. Future Work

- Prove the Zalcman conjecture for all $n$, which implies Bieberbach and would give a second, independent route.
- Determine sharp $|a_n|$ for univalent $f$ with $|f|<M$ for all $n$ and all $M$ (Tammi's programme).
- Settle the **Krzyż conjecture**: for $f$ nonvanishing, bounded by 1, and univalent-free, $|a_n|\le 2/e$; known only for $n\le5$.
- Find a proof of Milin's conjecture that does not route through Jacobi-polynomial positivity, or conversely explain conceptually why Askey–Gasper appears.
- Formalize de Branges' theorem in a proof assistant.

## 9. Key References

- **[Foundational]** L. Bieberbach. *Über die Koeffizienten derjenigen Potenzreihen, welche eine schlichte Abbildung des Einheitskreises vermitteln.* Sitzungsber. Preuss. Akad. Wiss., 1916, 940–955.
- **[Foundational]** C. Loewner. *Untersuchungen über schlichte konforme Abbildungen des Einheitskreises. I.* Mathematische Annalen **89** (1923), 103–121. [DOI](https://doi.org/10.1007/bf01448091)
- **[Foundational]** P. R. Garabedian, M. Schiffer. *A proof of the Bieberbach conjecture for the fourth coefficient.* J. Rational Mech. Anal. **4** (1955), 427–465. [DOI](https://doi.org/10.21236/ad0047020)
- **[Foundational]** I. M. Milin. *Univalent Functions and Orthonormal Systems.* American Mathematical Society, Translations of Mathematical Monographs 49, 1977.
- **[SOTA]** L. de Branges. *A proof of the Bieberbach conjecture.* Acta Mathematica **154** (1985), 137–152.
- **[SOTA]** R. Askey, G. Gasper. *Positive Jacobi polynomial sums II.* American Journal of Mathematics **98** (1976), 709–737. [DOI](https://doi.org/10.2307/2373813)
- **[SOTA]** L. Weinstein. *The Bieberbach conjecture.* International Mathematics Research Notices **1991**, no. 5, 61–64.
- **[SOTA]** C. H. FitzGerald, C. Pommerenke. *The de Branges theorem on univalent functions.* Transactions of the American Mathematical Society **290** (1985), 683–690. [DOI](https://doi.org/10.1090/s0002-9947-1985-0792819-9)
- **[Recent]** R. Greiner, O. Roth. *On support points of univalent functions and a disproof of a conjecture of Bombieri.* Proceedings of the American Mathematical Society **129** (2001), 3657–3664. [DOI](https://doi.org/10.1090/s0002-9939-01-05994-9)
- **[Survey]** P. L. Duren. *Univalent Functions.* Grundlehren der mathematischen Wissenschaften 259, Springer, 1983.
- **[Survey]** C. Pommerenke. *Univalent Functions.* Vandenhoeck & Ruprecht, Göttingen, 1975.
- **[Survey]** A. Baernstein, D. Drasin, P. Duren, A. Marden (eds.). *The Bieberbach Conjecture: Proceedings of the Symposium on the Occasion of the Proof.* AMS Mathematical Surveys 21, 1986.

## 10. Worked Example / Concrete Special Case

**Goal: prove $|a_2|\le2$ from the area theorem, and check sharpness.**

Let $f(z)=z+a_2z^2+a_3z^3+\cdots \in S$. Form the odd square-root transform
$$h(z)=\sqrt{f(z^2)} = z\sqrt{1+a_2z^2+a_3z^4+\cdots} = z\Big(1+\tfrac{a_2}{2}z^2+O(z^4)\Big) = z+\tfrac{a_2}{2}z^3+\cdots,$$
which is univalent (if $h(z_1)=h(z_2)$ then $f(z_1^2)=f(z_2^2)$, so $z_1=\pm z_2$; oddness rules out the minus sign unless $z_1=z_2=0$).

Invert to land in $\Sigma$: put $\zeta = 1/z$ and
$$g(\zeta) = \frac{1}{h(1/\zeta)} = \frac{1}{\zeta^{-1}+\frac{a_2}{2}\zeta^{-3}+\cdots} = \zeta\Big(1-\tfrac{a_2}{2}\zeta^{-2}+\cdots\Big) = \zeta - \frac{a_2}{2}\,\zeta^{-1}+\cdots .$$
So $b_0=0$, $b_1=-a_2/2$. The area theorem gives $\sum n|b_n|^2\le1$, hence $|b_1|\le1$, i.e.
$$\Big|\frac{a_2}{2}\Big|\le 1 \quad\Longrightarrow\quad |a_2|\le 2 .$$

**Sharpness.** For the Koebe function $k(z)=z(1-z)^{-2}$, differentiating $\sum_{n\ge1}nz^n$ term-by-term confirms $a_n=n$, so $a_2=2$. Its square-root transform is $h(z)=z/(1-z^2)$ and $g(\zeta)=\zeta-\zeta^{-1}$, for which $\sum n|b_n|^2 = 1$ exactly — the omitted set of $g$ is the segment $[-2,2]$, of zero area. Equality in the area theorem forces $b_n=0$ for $n\ge2$, which pins $g$, hence $f$, to a rotation of $k$.

**Milin's inequality at $n=1$, as a sanity check.** With $\log(f(z)/z)=2\sum\gamma_kz^k$ we get $2\gamma_1=a_2$. Milin's conjecture at $n=1$ reads $|\gamma_1|^2-1\le0$, i.e. $|a_2|\le2$ — the same statement. At $n=2$ it reads $2(|\gamma_1|^2-1)+(2|\gamma_2|^2-\tfrac12)\le0$ with $2\gamma_2=a_3-\tfrac12a_2^2$, and for $f=k$ ($\gamma_k=1/k$) the left side is $2(1-1)+(2\cdot\tfrac14-\tfrac12)=0$: the Koebe function saturates every instance, which is exactly the rigidity de Branges' monotone functional detects.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*