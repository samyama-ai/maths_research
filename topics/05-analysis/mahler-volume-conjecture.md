---
id: 05-analysis/mahler-volume-conjecture
title: "Mahler Volume Conjecture"
topic: 05-analysis
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mahler Volume Conjecture

> **Topic:** Real & Complex Analysis · **ID:** `05-analysis/mahler-volume-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

For a convex body $K\subset\mathbb{R}^n$ (compact, convex, with nonempty interior) containing the origin, the **polar body** is
$$K^{\circ}=\{y\in\mathbb{R}^n:\ \langle x,y\rangle\le 1\ \ \forall x\in K\},$$
and the **Mahler volume** (volume product) is $\mathcal{P}(K)=|K|\,|K^{\circ}|$, where $|\cdot|$ is Lebesgue measure.

**Symmetric Mahler conjecture.** If $K=-K$, then
$$\mathcal{P}(K)\ \ge\ \mathcal{P}\big([-1,1]^n\big)=\frac{4^n}{n!},$$
with equality conjecturally exactly for the **Hanner polytopes** (built from segments by iterated $\ell_1$/$\ell_\infty$ sums).

**Non-symmetric (simplex) conjecture.** For general $K$, with the minimum over translates,
$$\mathcal{P}_s(K)=\min_{z\in\operatorname{int}K}|K|\,|(K-z)^{\circ}|\ \ge\ \mathcal{P}_s(\Delta^n)=\frac{(n+1)^{n+1}}{(n!)^2},$$
with equality only for simplices.

A resolution requires a proof valid in all dimensions $n$, or a single convex body violating the bound. The quantity is invariant under $GL_n(\mathbb{R})$ (since $(TK)^\circ=T^{-\top}K^\circ$), so the problem lives on the compact Banach–Mazur compactum; minimizers exist, and the content is identifying them.

## 2. Mathematical Foundations

Let $\|x\|_K=\inf\{t>0: x\in tK\}$ be the Minkowski gauge. Then $\|\cdot\|_{K^\circ}=h_K$, the support function, and $K^{\circ\circ}=K$ for $0\in K$ closed convex. For $K=-K$, $\|\cdot\|_K$ is a norm and $\mathcal{P}(K)$ is an isometric invariant of the normed space $X_K=(\mathbb{R}^n,\|\cdot\|_K)$ measuring "distance from the Euclidean ball".

**Upper bound (Blaschke–Santaló, proved).**
$$\mathcal{P}_s(K)\ \le\ \mathcal{P}(B_2^n)=\omega_n^2,\qquad \omega_n=\frac{\pi^{n/2}}{\Gamma(1+\tfrac n2)},$$
with equality iff $K$ is an ellipsoid (Petty 1985; Meyer–Pajor 1990 via Steiner symmetrization).

**Lower bounds (Mahler side, open).** Known:
$$\frac{\pi^n}{n!}\ \le\ \mathcal{P}(K)\qquad (K=-K),$$
Kuperberg (2008) — off the conjecture by the factor $(\pi/4)^n$. The Bourgain–Milman theorem (1987) is the weaker isomorphic statement $\mathcal{P}(K)\ge c^n\,\omega_n^2$ for an absolute $c>0$.

**Hanner polytopes.** $H$ is Hanner if $H$ is a symmetric segment, or $H=H_1\oplus_1 H_2=\operatorname{conv}(H_1\times\{0\}\cup\{0\}\times H_2)$, or $H=H_1\oplus_\infty H_2=H_1\times H_2$, with $H_i$ Hanner. Polarity swaps the two operations: $(H_1\oplus_1H_2)^\circ=H_1^\circ\oplus_\infty H_2^\circ$. Since $|A\times B|=|A||B|$ and $|A\oplus_1 B|=\binom{k+m}{k}^{-1}|A||B|$ for $A\subset\mathbb{R}^k$, $B\subset\mathbb{R}^m$, induction gives $\mathcal{P}(H)=4^n/n!$ for **every** Hanner polytope. Non-uniqueness of the conjectured minimizer (there are $\sim$exponentially many Hanner types) rules out symmetrization/uniqueness-based proofs.

**Functional form.** For even log-concave $f:\mathbb{R}^n\to[0,\infty)$ with Legendre-type dual $\mathcal{L}f(y)=\inf_x e^{-\langle x,y\rangle}/f(x)$, the conjecture $\int f\int\mathcal{L}f\ge 4^n$ is equivalent to the body case (Fradelizi–Meyer), placing Mahler inside a reverse-Prékopa–Leindler framework.

## 3. History & State of the Art (SOTA)

- **1939.** Kurt Mahler introduces the volume product in the geometry-of-numbers context and proves both planar cases: $\mathcal{P}(K)\ge 8$ for symmetric planar bodies, and $\ge 27/4$ for general planar bodies.
- **1949.** Santaló establishes the sharp upper bound in all dimensions, fixing the "other end" of the problem.
- **1981–86.** Saint-Raymond proves the symmetric conjecture for **unconditional** bodies (invariant under all coordinate sign flips); Meyer (1986) gives a short proof and the Hanner equality characterization for that class; Reisner (1986) proves it for **zonoids**.
- **1987.** Bourgain–Milman: $\mathcal{P}(K)\ge c^n\omega_n^2$, settling the isomorphic version and making $\mathcal{P}(K)^{1/n}$ order-correct.
- **2008.** Kuperberg's Gauss-linking-integral proof gives the best explicit constant to date, $\pi^n/n!$.
- **2012.** Nazarov reproves Bourgain–Milman by $\bar\partial$/Hörmander $L^2$ estimates on the tube domain $\mathbb{R}^n+iK$, with a constant of the form $c^n4^n/n!$, $c=(\pi/4)^3$ — analytically new, numerically weaker than Kuperberg.
- **2020.** Iriyeh–Shibata prove the symmetric conjecture in $\mathbb{R}^3$ (Duke Math. J.), the first new dimension in 80 years; Fradelizi–Hubard–Meyer–Roldán-Pensado–Zvavitch (2022) give a shorter proof via measure equipartitions.

Status: proven for $n\le 3$ (symmetric), $n\le 2$ (general), and for wide symmetry-rich classes; open for $n\ge 4$ symmetric and $n\ge 3$ general.

## 4. Partial Results / Verified Cases

| Class / regime | Result |
|---|---|
| $n=2$, symmetric | $\mathcal{P}\ge 8$, equality iff parallelogram (Mahler 1939) |
| $n=2$, general | $\mathcal{P}_s\ge 27/4$, equality iff triangle (Mahler 1939; Meyer–Reisner shadow-system proof) |
| $n=3$, symmetric | $\mathcal{P}\ge 32/3$ (Iriyeh–Shibata 2020; second proof 2022) |
| Unconditional bodies, all $n$ | $\mathcal{P}\ge 4^n/n!$ (Saint-Raymond 1981; Meyer 1986) |
| Zonoids / zonotopes, all $n$ | $\mathcal{P}\ge 4^n/n!$, equality iff cube (Reisner 1986; Gordon–Meyer–Reisner) |
| Bodies with $\ge n$ independent hyperplane symmetries | Barthe–Fradelizi (2013) |
| Symmetric polytopes with $\le 2n+2$ vertices (or facets) | Lopez–Reisner (1998) |
| Bodies of revolution | Meyer–Reisner (2006) |
| Local minimality | Cube is a local minimum in Banach–Mazur distance (Nazarov–Petrov–Ryabogin–Zvavitch 2010); all Hanner polytopes are local minima (Kim 2014); simplex is a local minimum (Kim–Reisner 2011) |
| Global lower bound, all $n$ | $\mathcal{P}(K)\ge\pi^n/n!$ (Kuperberg 2008) — gap factor $(4/\pi)^n$ |

## 5. Principal Obstacles

- **Symmetrization fails.** The Santaló inequality falls to Steiner symmetrization because symmetrization *increases* $\mathcal{P}$ toward the ball. No symmetrization drives a body toward a cube: the conjectured minimizers are the maximally "unsymmetric" extreme points, and there is a large, disconnected family of them.
- **Non-uniqueness of extremizers.** In dimension $n$ the number of combinatorially distinct Hanner polytopes grows exponentially. Any variational argument must produce a degenerate, multi-valley landscape rather than an isolated critical point — which defeats rigidity/stability schemes that work for Santaló.
- **Local ≠ global.** Local minimality of Hanner polytopes is known, but $\mathcal{P}$ on the Banach–Mazur compactum is neither convex nor quasi-convex along shadow systems in a way that forces global control; there is no known monotone flow connecting an arbitrary body to a Hanner polytope.
- **Analytic methods lose exponential constants.** Hörmander $L^2$-estimates and Bergman-kernel bounds control $\mathcal{P}$ through a plurisubharmonic weight on the tube domain $\mathbb{R}^n+iK$; the constant degrades geometrically per dimension, so these methods are structurally $c^n$-lossy and cannot reach a sharp value.
- **Fourier-analytic obstruction.** Unlike the Busemann–Petty problem, $\mathcal{P}$ is not expressible through a linear transform (spherical Radon/cosine) of the body; polarity is a nonlinear involution that interacts badly with harmonic-analytic decompositions.
- **Combinatorial link.** Mahler for polytopes implies (Kalai-type) $3^n$ face-count phenomena; any proof must implicitly encode a hard combinatorial extremal statement.

## 6. The Gap

Proven: sharp bounds when the body has an abundance of linear symmetries (unconditional, zonoid, revolution, many-hyperplane-symmetry) or when $n\le 3$; and a general bound off by $(4/\pi)^n\approx 1.273^n$. Conjectured: the sharp constant for *arbitrary* symmetric bodies in every dimension.

The exact missing step: **an inductive or variational mechanism that reduces a general symmetric $K\subset\mathbb{R}^n$ to lower-dimensional data without assuming a symmetry that aligns with a coordinate decomposition.** The known proofs in $n\le 3$ split $K$ by hyperplanes/equipartitions and estimate slices; the resulting inequalities become false or unmanageable for $n\ge 4$ because the number of section-and-cone terms grows and no single hyperplane simultaneously bisects the needed measures. Closing the gap means either (i) a dimension-free multiplicative recursion respecting $\oplus_1/\oplus_\infty$ duality, or (ii) an analytic identity whose sharp case is exactly the Hanner class.

## 7. Current Research (as of June 2026)

- **Complex-analytic route.** Berndtsson's Bergman-kernel refinements of Nazarov's argument, and Błocki's work on the Hörmander approach, aim at improving the constant $c$ and possibly reaching $4^n/n!$ for special classes. *(frontier — verify)* Sharp-constant claims in this line remain partial.
- **Symplectic route disrupted.** Artstein-Avidan–Karasev–Ostrover (2014) showed Viterbo's capacity–volume conjecture implies symmetric Mahler, via $\mathrm{c}_{EHZ}(K\times K^\circ)=4$. Haim-Kislev and Ostrover's 2024 counterexample to Viterbo's conjecture in $\mathbb{R}^4$ removes this as a proof pathway; it does **not** disprove Mahler, and the identity $\mathrm{c}_{EHZ}(K\times K^\circ)=4$ survives. *(frontier — verify current scope of the counterexample.)*
- **Dimension 4.** Groups around Kent State (Zvavitch), Université Gustave Eiffel (Fradelizi, Meyer), and Tokyo (Iriyeh, Shibata) are pushing equipartition/section methods toward $n=4$ and toward the non-symmetric three-dimensional simplex case. *(frontier — verify)*
- **Computational.** Numerical searches over polytopes with bounded vertex counts (Alexander–Fradelizi–Zvavitch and successors) find no body below $4^n/n!$ through moderate $n$, supporting the conjecture and its equality set.
- **Functional/entropic.** Reverse Blaschke–Santaló for log-concave functions, transport and Bianchi–Egnell-type stability, and $L_p$/Orlicz volume products.

## 8. Future Work

- Find a **shadow-system or linear-parameter deformation** along which $\mathcal{P}$ is concave, with endpoints in the Hanner class — the mechanism that closed $n=2$, generalized correctly.
- Prove the conjecture for **all polytopes with at most $C n$ vertices**, extending Lopez–Reisner beyond $2n+2$.
- Establish a **quantitative stability** result: $\mathcal{P}(K)\ge (1+c\,\delta(K,\mathcal{H}))\,4^n/n!$ where $\delta$ is Banach–Mazur distance to the Hanner family; this would upgrade local minimality to a global statement given compactness plus a covering argument.
- Settle the **isomorphic sharp constant**: is $\liminf_n\big(\mathcal{P}(K)n!/4^n\big)^{1/n}=1$ uniformly? Improving Kuperberg's $\pi/4$ toward $1$ by any analytic means would be a major advance.
- Resolve the **non-symmetric case in $\mathbb{R}^3$**, expected to be within reach of the equipartition technique.

## 9. Key References

- **[Foundational]** K. Mahler. *Ein Übertragungsprinzip für konvexe Körper.* Časopis pro pěstování matematiky a fysiky 68 (1939), 93–102.
- **[Foundational]** K. Mahler. *Ein Minimalproblem für konvexe Polygone.* Mathematica (Zutphen) B 7 (1939), 118–127.
- **[Foundational]** L. A. Santaló. *Un invariante afín para los cuerpos convexos del espacio de $n$ dimensiones.* Portugaliae Mathematica 8 (1949), 155–161.
- **[Foundational]** J. Saint-Raymond. *Sur le volume des corps convexes symétriques.* Séminaire d'Initiation à l'Analyse (Choquet), 1980/81, Univ. Paris VI.
- **[Foundational]** M. Meyer. *Une caractérisation volumique de certains espaces normés de dimension finie.* Israel J. Math. 55 (1986), 317–326.
- **[Foundational]** S. Reisner. *Zonoids with minimal volume-product.* Math. Zeitschrift 192 (1986), 339–346.
- **[Foundational]** J. Bourgain, V. Milman. *New volume ratio properties for convex symmetric bodies in $\mathbb{R}^n$.* Inventiones Math. 88 (1987), 319–340.
- **[Foundational]** M. Meyer, A. Pajor. *On the Blaschke–Santaló inequality.* Archiv der Mathematik 55 (1990), 82–93.
- **[SOTA]** G. Kuperberg. *From the Mahler conjecture to Gauss linking integrals.* Geometric and Functional Analysis 18 (2008), 870–892.
- **[SOTA]** F. Nazarov, F. Petrov, D. Ryabogin, A. Zvavitch. *A remark on the Mahler conjecture: local minimality of the unit cube.* Duke Math. J. 154 (2010), 419–430.
- **[SOTA]** F. Nazarov. *The Hörmander proof of the Bourgain–Milman theorem.* Geometric Aspects of Functional Analysis, Lecture Notes in Math. 2050, Springer (2012), 335–343.
- **[SOTA]** S. Artstein-Avidan, R. Karasev, Y. Ostrover. *From symplectic measurements to the Mahler conjecture.* Duke Math. J. 163 (2014), 2003–2022.
- **[SOTA]** J. Kim. *Minimal volume product near Hanner polytopes.* J. Functional Analysis 266 (2014), 2360–2402.
- **[SOTA]** H. Iriyeh, M. Shibata. *Symmetric Mahler's conjecture for the volume product in the three-dimensional case.* Duke Math. J. 169 (2020), 1077–1134.
- **[SOTA]** M. Fradelizi, A. Hubard, M. Meyer, E. Roldán-Pensado, A. Zvavitch. *Equipartitions and Mahler volumes of symmetric convex bodies.* American J. Math. 144 (2022), 1201–1219.
- **[SOTA]** P. Haim-Kislev, Y. Ostrover. *A counterexample to Viterbo's conjecture.* arXiv:2405.16513 (2024).
- **[Survey]** M. Fradelizi, M. Meyer, A. Zvavitch. *Volume product.* In: Harmonic Analysis and Convexity (A. Koldobsky, A. Volberg, eds.), De Gruyter, 2023.
- **[Survey]** M. A. Lopez, S. Reisner. *A special case of Mahler's conjecture.* Discrete & Computational Geometry 20 (1998), 163–177.
- **[Survey]** R. Schneider. *Convex Bodies: The Brunn–Minkowski Theory,* 2nd ed., Cambridge University Press, 2014.

## 10. Worked Example / Concrete Special Case

**Dimension 2, the $\ell_p$ family.** For $B_p^n=\{x:\sum|x_i|^p\le 1\}$, $|B_p^n|=\dfrac{\big(2\Gamma(1+\frac1p)\big)^n}{\Gamma(1+\frac np)}$ and $(B_p^n)^\circ=B_q^n$ with $\frac1p+\frac1q=1$. In $n=2$:
$$\mathcal{P}(B_p^2)=\frac{4\Gamma(1+\tfrac1p)^2}{\Gamma(1+\tfrac2p)}\cdot\frac{4\Gamma(1+\tfrac1q)^2}{\Gamma(1+\tfrac2q)}.$$

- $p=1$: $|B_1^2|=4\Gamma(2)^2/\Gamma(3)=2$, $|B_\infty^2|=4$, so $\mathcal{P}=8=\dfrac{4^2}{2!}$ — the conjectured minimum, attained.
- $p=2$: $|B_2^2|=4\Gamma(1.5)^2/\Gamma(2)=4\cdot(\sqrt\pi/2)^2=\pi$, so $\mathcal{P}=\pi^2\approx 9.8696$ — the Santaló maximum.
- $p=4$ ($q=4/3$): $|B_4^2|=4\Gamma(1.25)^2/\Gamma(1.5)\approx 3.7081$, $|B_{4/3}^2|=4\Gamma(1.75)^2/\Gamma(2.5)\approx 2.5416$, so $\mathcal{P}\approx 9.424$ — strictly between the two extremes, as required.

**A non-$\ell_p$ check: the regular hexagon.** Let $H$ have circumradius $1$, so $|H|=\tfrac{3\sqrt3}{2}$. Each edge lies at distance $\tfrac{\sqrt3}{2}$ from the origin, hence $H^\circ$ is the hexagon rotated by $30^\circ$ with circumradius $2/\sqrt3$, giving
$$|H^\circ|=\frac{3\sqrt3}{2}\Big(\frac{2}{\sqrt3}\Big)^2=2\sqrt3,\qquad \mathcal{P}(H)=\frac{3\sqrt3}{2}\cdot 2\sqrt3=9.$$
So $8<9<\pi^2$: the hexagon sits between the square (Mahler extremal) and the disk (Santaló extremal), consistent with Mahler's planar theorem that no symmetric planar body beats the parallelogram.

**Why $n\ge 4$ resists.** Repeating the hexagon-style computation in higher dimensions requires comparing $|K|$ to $|K^\circ|$ through slices. In $\mathbb{R}^3$ the proofs bisect $K$ by three suitably chosen planes (an equipartition) and bound the eight resulting cone-pairs. In $\mathbb{R}^4$ one needs a simultaneous equipartition by four hyperplanes; the corresponding Borsuk–Ulam-type existence statement is not available in the required form, and the number of cone terms rises from $8$ to $16$ with weaker per-term estimates. That is the concrete technical wall.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*