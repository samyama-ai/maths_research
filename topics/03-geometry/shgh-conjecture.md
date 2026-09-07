---
id: 03-geometry/shgh-conjecture
title: "SHGH Conjecture"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# SHGH Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/shgh-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Fix $n$ **general** points $p_1,\dots,p_n \in \mathbb{P}^2$ over an algebraically closed field of characteristic $0$, a degree $d \ge 0$, and multiplicities $m_1,\dots,m_n \ge 0$. Let
$$\mathcal{L} = \mathcal{L}_d(m_1,\dots,m_n)$$
be the linear system of plane curves of degree $d$ having multiplicity at least $m_i$ at $p_i$. Each condition "multiplicity $\ge m$ at a point" imposes at most $\binom{m+1}{2}$ linear conditions on the $\binom{d+2}{2}$ coefficients, so
$$\dim \mathcal{L} \;\ge\; e(\mathcal{L}) := \max\Big\{-1,\; \binom{d+2}{2}-1-\sum_{i=1}^{n}\binom{m_i+1}{2}\Big\}.$$
Call $\mathcal{L}$ **special** if $\dim\mathcal{L} > e(\mathcal{L})$, i.e. the multiplicity conditions are not independent beyond what dimension count forces.

**SHGH Conjecture (Segre–Harbourne–Gimigliano–Hirschowitz).** $\mathcal{L}_d(m_1,\dots,m_n)$ is special **if and only if** it has a *multiple rational curve of self-intersection $-1$ in its base locus*. Equivalently, in the Harbourne–Hirschowitz formulation: if $h^1$ of the corresponding line bundle is nonzero, then there is a $(-1)$-curve $C$ on the blow-up with $\mathcal{L}\cdot C \le -2$.

A complete resolution requires either a proof valid for **all** $(d;m_1,\dots,m_n)$ with $n$ arbitrary, or a single explicit system that is special with no such $(-1)$-curve obstruction. The conjecture is known to be false if "general" is weakened (special position of points), so genericity is essential.

## 2. Mathematical Foundations

Let $\pi: X_n \to \mathbb{P}^2$ be the blow-up at $p_1,\dots,p_n$, with exceptional divisors $E_1,\dots,E_n$ and $H = \pi^*\mathcal{O}(1)$. Then
$$\operatorname{Pic}(X_n) = \mathbb{Z}H \oplus \bigoplus_{i=1}^n \mathbb{Z}E_i,\qquad H^2=1,\; E_i^2=-1,\; H\cdot E_i = 0,$$
and $K_{X_n} = -3H+\sum_i E_i$. Put $L = dH - \sum_i m_i E_i$. Then $H^0(X_n,L) \cong \mathcal{L}_d(m_1,\dots,m_n)$ (as vector spaces, $\dim\mathcal{L}=h^0-1$), and by Riemann–Roch
$$\chi(L)=\frac{L\cdot(L-K)}{2}+1=\binom{d+2}{2}-\sum_i\binom{m_i+1}{2}.$$
Since $h^2(L)=0$ whenever $d\ge -1$ (Serre duality plus $L-K$ effective in the relevant range), speciality is exactly $h^1(X_n,L)>0$.

**$(-1)$-curves.** An irreducible curve $C\subset X_n$ with $C^2=-1$ and $p_a(C)=0$, equivalently $C^2=C\cdot K=-1$. Examples: $E_i$; the line class $H-E_i-E_j$; the conic $2H-E_{i_1}-\dots-E_{i_5}$; the cubic $3H-2E_{i_1}-E_{i_2}-\dots-E_{i_7}$.

**Harbourne–Hirschowitz statement.** $h^1(X_n,L)>0 \iff \exists$ a $(-1)$-curve $C$ with $L\cdot C \le -2$.

**Segre statement.** If $\mathcal{L}$ is special, its general member is non-reduced (some multiple curve appears in every member).

**Gimigliano/Harbourne statement (standard classes).** For $n\ge 3$ the standard Cremona transformation based at $p_1,p_2,p_3$ acts on classes by
$$(d;m_1,m_2,m_3,m_4,\dots)\mapsto (d+k;\,m_1+k,\,m_2+k,\,m_3+k,\,m_4,\dots),\qquad k=d-m_1-m_2-m_3,$$
generating (with permutations) the Weyl group $W_n$ of the root system $E_n$ acting on $K^\perp \subset \operatorname{Pic}(X_n)$. This action preserves $h^0$ and $h^1$. A class with $m_1\ge\dots\ge m_n\ge 0$ is **standard** if $d\ge m_1+m_2+m_3$. Every effective class with nonnegative multiplicities reduces under $W_n$ to a standard one or to a negative degree, so SHGH is equivalent to: **every standard class is non-special.**

These three formulations were shown to be equivalent by Ciliberto and Miranda. SHGH implies **Nagata's conjecture**: for $n\ge 10$ general points and any curve of degree $d$ with multiplicities $m_i$, $d > \frac{1}{\sqrt n}\sum_i m_i$.

## 3. History & State of the Art (SOTA)

- **1959–61.** Nagata, solving Hilbert's 14th problem, proved the $\sqrt n$ inequality for $n=k^2\ge 16$ and conjectured it in general (*Amer. J. Math.* 81, 1959). Beniamino Segre, in the 1961 Turin conference volume, stated the "non-reduced general member" criterion for speciality — the earliest form of the conjecture.
- **1986.** Harbourne, studying anticanonical rational surfaces and Hilbert functions of fat points, formulated the $(-1)$-curve criterion and proved the case $n\le 9$ using the anticanonical class.
- **1987.** Gimigliano's Queen's University thesis gave the Cremona/standard-class classification and conjectural list of special systems.
- **1989.** Hirschowitz (*J. reine angew. Math.* 397) independently stated the conjecture and proved it for all $m_i\le 3$ via the **méthode d'Horace** (differential Horace / specialization to a line).
- **1998–2000.** Ciliberto–Miranda introduced **degeneration of the plane** to a union of surfaces, proving the homogeneous case ($m_1=\dots=m_n=m$) for $m\le 12$.
- **1999.** Evain proved the homogeneous case for $n=4^h$ points, any $m$, by a $2$-adic recursive specialization.
- **2007.** Yang, and independently Dumnicki–Jarnicki, gave algorithmic/combinatorial proofs for bounded multiplicities, reaching $m_i\le 11$.
- **2011.** Ciliberto–Miranda settled the homogeneous case $n=10$ (*J. Algebraic Geom.* 20), the first genuinely infinite non-anticanonical family; $n=10$ is the boundary case of Nagata's conjecture.

The name "SHGH" was popularized by Ciliberto–Miranda's 2001 NATO survey. No formulation has been disproved and no new formulation has superseded the three above.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $n\le 9$ general points, any $d,m_i$ | Proved (anticanonical $-K$ is nef; $X_n$ is a weak del Pezzo) | Harbourne 1986; Gimigliano 1987 |
| $m_i\le 3$ for all $i$, any $n,d$ | Proved | Hirschowitz 1989 |
| $m_i\le 11$ for all $i$, any $n,d$ | Proved | Yang 2007; Dumnicki–Jarnicki 2007 |
| Homogeneous $m_i=m\le 12$ | Proved | Ciliberto–Miranda 1998, 2000 |
| Homogeneous, $n=4^h$ points | Proved for all $m$ | Evain 1999 |
| Homogeneous, $n=10$ | Proved for all $m$ | Ciliberto–Miranda 2011 |
| Homogeneous, $n$ a perfect square $\ge 16$ | Nagata inequality (hence emptiness half) known | Nagata 1959 |
| Quasi-homogeneous $(d;m,\dots,m,k)$, various ranges | Proved in wide ranges | Ciliberto–Miranda; Laface–Ugaglia; Roé |
| $d \ge \sum_i m_i - 1$ (few conditions relative to degree) | Non-special, elementary | classical |
| Double points in $\mathbb{P}^r$ (analogue) | Alexander–Hirschowitz theorem, fully proved | Alexander–Hirschowitz 1995 |

Computer verification: Dumnicki's reduction algorithms and Yang's methods confirm non-speciality for millions of standard classes with $d$ in the hundreds; no counterexample has appeared in any systematic search.

## 5. Principal Obstacles

- **Infinitely many $(-1)$-curves.** For $n\ge 10$ the Weyl group $W_n$ is infinite, so $X_n$ carries infinitely many $(-1)$-classes and the effective cone is not rational polyhedral (indeed not even closed in general). Any proof must control an infinite obstruction set uniformly; no finiteness/termination argument is available.
- **Vanishing theorems do not apply.** Kawamata–Viehweg and Kodaira-type vanishing require $L-K$ nef and big. For $n\ge 10$, deciding nefness of $dH-\sum m_iE_i$ is *equivalent* to Nagata's conjecture — the tool presupposes the conclusion.
- **Semicontinuity is one-directional.** Horace-type specializations move points to a line or conic; $h^0$ can only jump up, so one gets upper bounds on speciality only when the specialized system is itself computable. Specializing enough points to force a computation typically makes the specialized system special, and the induction collapses.
- **Degeneration combinatorics explode.** Ciliberto–Miranda's plane degenerations reduce a class to a matching problem on a "$k$-transversal" configuration; the number of cases grows superexponentially in $m$, which is exactly why the method stalls near $m=12$ rather than at a conceptual barrier.
- **Cremona reduction is not a descent.** Reduction to standard classes is a *reformulation*, not a simplification: standard classes form the hard core, and there is no induction parameter that strictly decreases within them.
- **No characteristic-free or moduli-theoretic mechanism.** Speciality is a genericity statement about a $2n$-dimensional configuration space; there is no known deformation-theoretic invariant detecting the very general locus directly.

## 6. The Gap

Everything proved falls into two shapes: (i) $-K$ effective and nef, so $n\le 9$ and the Mori cone is finite; or (ii) multiplicities or point counts bounded by an absolute constant ($m_i\le 11$, $m\le 12$, $n=10$, $n=4^h$). The general statement requires $n$ **and** $m_i$ simultaneously unbounded, precisely where $X_n$ is of general "hyperbolic" type. The single missing step is an **effective non-vanishing/independence criterion for $h^1$ that does not require knowing the nef cone** — or, dually, a proof that for a standard class $L$ (with $d\ge m_1+m_2+m_3$) one has $h^1(L)=0$. Even the special case "standard homogeneous classes with $n=11$ and $m$ arbitrary" is open, and it is arguably the smallest genuinely unknown instance.

## 7. Current Research (as of June 2026)

- **Degeneration and toric/Newton-polygon methods.** Continuation of Ciliberto–Miranda degenerations combined with Dumnicki's polytope-splitting algorithms; the target is pushing uniform multiplicity bounds past $12$ with machine-assisted case enumeration. Groups: Roma Tor Vergata (Ciliberto), Colorado State (Miranda), Jagiellonian/Kraków (Dumnicki, Szemberg, Tutaj-Gasińska).
- **Negative curves and the bounded negativity conjecture.** Barcelona (Roé), Kraków, and Nebraska (Harbourne) study whether $(-1)$-curves are the only negative irreducible curves on $X_n$ for very general points — a statement implied by SHGH and now attacked through Seshadri constants and Zariski decompositions.
- **Unexpected curves and hypersurfaces.** Cook–Harbourne–Migliore–Nagel's theory (line arrangements, Lefschetz properties) explains speciality for *special* point configurations and is being used to test which mechanisms could conceivably occur generically. *(frontier — verify)*
- **Symbolic powers / containment.** The Dumnicki–Harbourne–Nagel–Seceleanu–Szemberg–Tutaj-Gasińska counterexamples to $I^{(3)}\subseteq I^2$ show how far non-general configurations deviate; the general-point analogue is governed by SHGH.
- **Higher-dimensional and other-surface analogues.** Laface–Ugaglia's programme for $\mathbb{P}^3$, and analogues on Hirzebruch and toric surfaces, used as testbeds for the induction machinery. *(frontier — verify)*

## 8. Future Work

- Prove SHGH for **standard homogeneous classes with $n=11,12$**, the next boundary after Ciliberto–Miranda's $n=10$.
- Replace the case-by-case degeneration bookkeeping with a **limit linear series / tropical** framework where the matching condition becomes a single combinatorial statement about a polyhedral complex.
- Establish **bounded negativity on $X_n$** (all irreducible curves have $C^2 \ge -1$) for very general points; this is strictly weaker than SHGH but would already imply Nagata.
- Develop **asymptotic/multiplier-ideal bounds** matching $\sqrt n$ rather than the current $\approx \sqrt{n}\,(1-O(1/n))$ gap on Nagata-type inequalities.
- Search computationally at large $d$ within standard classes for speciality without a $(-1)$-curve; a counterexample would most plausibly appear near the Nagata boundary $d\approx m\sqrt n$.

## 9. Key References

- **[Foundational]** M. Nagata. *On the 14-th problem of Hilbert.* American Journal of Mathematics 81 (1959), 766–772.
- **[Foundational]** B. Segre. *Alcune questioni su insiemi finiti di punti in geometria algebrica.* Atti del Convegno Internazionale di Geometria Algebrica, Torino, 1961, 15–33.
- **[Foundational]** B. Harbourne. *The geometry of rational surfaces and Hilbert functions of points in the plane.* Canadian Mathematical Society Conference Proceedings 6 (1986), 95–111.
- **[Foundational]** A. Gimigliano. *On linear systems of plane curves.* PhD thesis, Queen's University, Kingston, Ontario, 1987.
- **[Foundational]** A. Hirschowitz. *Une conjecture pour la cohomologie des diviseurs sur les surfaces rationnelles génériques.* Journal für die reine und angewandte Mathematik 397 (1989), 208–213.
- **[SOTA]** C. Ciliberto, R. Miranda. *Degenerations of planar linear systems.* Journal für die reine und angewandte Mathematik 501 (1998), 191–220.
- **[SOTA]** C. Ciliberto, R. Miranda. *Linear systems of plane curves with base points of equal multiplicity.* Transactions of the American Mathematical Society 352 (2000), 4037–4050.
- **[SOTA]** L. Evain. *La fonction de Hilbert de la réunion de $4^h$ gros points génériques de $\mathbb{P}^2$.* Journal of Algebraic Geometry 8 (1999), 787–796.
- **[SOTA]** S. Yang. *Linear systems in $\mathbb{P}^2$ with base points of bounded multiplicity.* Journal of Algebraic Geometry 16 (2007), 19–38.
- **[SOTA]** M. Dumnicki, W. Jarnicki. *New effective bounds on the dimension of a linear system in $\mathbb{P}^2$.* Journal of Symbolic Computation 42 (2007), 621–635.
- **[SOTA / Recent]** C. Ciliberto, R. Miranda. *Homogeneous interpolation on ten points.* Journal of Algebraic Geometry 20 (2011), 685–726.
- **[Survey]** C. Ciliberto, R. Miranda. *The Segre and Harbourne–Hirschowitz conjectures.* In: Applications of Algebraic Geometry to Coding Theory, Physics and Computation, NATO Science Series II, vol. 36, Kluwer, 2001, 37–51.
- **[Survey]** C. Ciliberto, B. Harbourne, R. Miranda, J. Roé. *Variations on Nagata's conjecture.* Clay Mathematics Proceedings 18 (2013), 185–203.
- **[Survey]** R. Miranda. *Linear systems of plane curves.* Notices of the American Mathematical Society 46 (1999), 192–202.
- **[Related]** J. Alexander, A. Hirschowitz. *Polynomial interpolation in several variables.* Journal of Algebraic Geometry 4 (1995), 201–222.
- **[Related]** B. Harbourne, J. Roé. *Linear systems with multiple base points in $\mathbb{P}^2$.* Advances in Geometry 4 (2004), 41–59.

## 10. Worked Example / Concrete Special Case

Take $d=4$, $n=5$, $m_1=\dots=m_5=2$: quartics with five general double points.

**Expected dimension.**
$$\binom{6}{2}-1-5\binom{3}{2} = 15-1-15 = -1,$$
so $e(\mathcal{L})=-1$: one expects **no** such quartic.

**Actual dimension.** Five general points lie on a unique smooth conic $Q$ (five points impose independent conditions on the $6$-dimensional space of conics). The quartic $2Q$ (the conic doubled) has multiplicity exactly $2$ at each $p_i$. Conversely any quartic with five double points must contain $Q$: restricting to $Q\cong\mathbb{P}^1$, a quartic cuts a divisor of degree $8$, but the five double points force degree $\ge 10$, so $Q$ is a component; the residual cubic still has multiplicity $\ge 1$ at each $p_i$ and meets $Q$ in $\ge 6 > 6-?$ — repeating, $Q$ splits off twice and the residual conic through the five points is $Q$ again. Hence $\mathcal{L}=\{2Q\}$ and $\dim\mathcal{L}=0$.

$$\dim\mathcal{L}=0 \;>\; -1 = e(\mathcal{L}) \quad\Longrightarrow\quad \mathcal{L}\ \text{is special},\qquad h^0=1,\ \chi=0 \Rightarrow h^1=1.$$

**The $(-1)$-curve obstruction.** On $X_5$, let $C = 2H-E_1-\dots-E_5$ be the strict transform of $Q$. Then
$$C^2 = 4-5 = -1,\qquad C\cdot K = 2(-3)+5 = -1,$$
so $C$ is a $(-1)$-curve. With $L = 4H-2\sum_i E_i$,
$$L\cdot C = 4\cdot 2 - \sum_{i=1}^5 2\cdot 1 = 8-10 = -2 \le -2 .$$
This is exactly the Harbourne–Hirschowitz condition, and indeed $L = 2C$: the multiple $(-1)$-curve sits in the base locus with multiplicity $2$, the general member is non-reduced (Segre's form), and the "lost" condition is accounted for by
$$h^1(L) = \binom{-L\cdot C-1}{2} = \binom{1}{2}\ \text{-type correction} = 1 .$$

**Cremona check.** Reducing $(4;2,2,2,2,2)$ with $k = 4-2-2-2 = -2$ gives $(2;0,0,0,2,2)$, then $(2;2,2,0,0,0)$ after ordering — a conic with two double points, i.e. a double line through two points: degree $2$ minus two multiplicity-$2$ conditions, $\binom{4}{2}-1-2\cdot 3 = -1$ expected, actual $0$ (the doubled line $\overline{p_1p_2}$). Speciality is preserved by the Weyl action, as the theory predicts. SHGH asserts that **every** special system in the plane decomposes this way — and it is exactly this "every" that is unproven once $n\ge 10$ and multiplicities are unbounded.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*