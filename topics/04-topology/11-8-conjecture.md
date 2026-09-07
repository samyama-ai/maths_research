---
id: 04-topology/11-8-conjecture
title: "11/8 Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# 11/8 Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/11-8-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (11/8).** Let $X$ be a closed, oriented, smooth **spin** 4-manifold. Then

$$b_2(X) \;\ge\; \tfrac{11}{8}\,|\sigma(X)|,$$

where $b_2$ is the second Betti number and $\sigma$ the signature.

By Rokhlin's theorem $\sigma(X) \equiv 0 \pmod{16}$, and by Hasse–Minkowski classification the intersection form of a spin 4-manifold is even and (if indefinite) isomorphic to

$$Q_X \;\cong\; 2m\,(-E_8) \oplus n\,H, \qquad m \ge 0,\ n \ge 0,$$

with $\sigma = -16m$, $b_2 = 16m + 2n$, $b_2^+ = n$, $b_2^- = 16m+n$. In these coordinates the conjecture is exactly

$$n \;\ge\; 3m \qquad\text{for all } m\ge 1 .$$

A complete proof must show no smooth closed spin 4-manifold realizes $2m(-E_8)\oplus nH$ with $n < 3m$; a disproof requires the construction of a single such smooth manifold (a "small exotic" spin geography point). The bound is **smooth-only**: Freedman realizes every even unimodular form topologically, so the conjecture is false in the topological category. The constant $11/8$ is sharp — connected sums of $K3$ surfaces attain equality.

## 2. Mathematical Foundations

**Intersection form.** For closed oriented $X^4$, the cup pairing $Q_X: H^2(X;\mathbb{Z})/\mathrm{tors} \times H^2(X;\mathbb{Z})/\mathrm{tors} \to \mathbb{Z}$ is symmetric unimodular. $X$ is *spin* iff $w_2(X)=0$ iff $Q_X$ is even ($Q_X(x,x)\in 2\mathbb{Z}$) when $H_1$ has no 2-torsion.

**Rokhlin (1952).** $X$ closed smooth spin $\Rightarrow$ $16 \mid \sigma(X)$.

**Donaldson (1983).** A definite intersection form of a smooth closed 4-manifold is diagonalizable; hence $2m(-E_8)$ alone ($n=0$, $m\ge1$) is not smoothable, giving $n\ge 1$.

**Seiberg–Witten / Bauer–Furuta.** For a spin$^c$ structure the monopole map
$$\mu(A,\phi) \;=\; \bigl(d^+a,\; D_A\phi,\; \dots\bigr)$$
is a proper, $S^1$-equivariant nonlinear Fredholm map between Hilbert bundles. For a spin structure the quaternionic structure on the spinor bundle upgrades the symmetry group to
$$Pin(2) \;=\; S^1 \cup j\,S^1 \subset Sp(1),$$
acting on the spinors through the quaternionic representation $\mathbb{H}$ and on the self-dual forms through the sign representation $\tilde{\mathbb{R}}$ ($S^1$ trivial, $j \mapsto -1$).

Finite-dimensional approximation (Furuta; Bauer–Furuta) converts $\mu$ into a stable $Pin(2)$-equivariant map of representation spheres. For $X$ spin with $b_1=0$, $\sigma=-16m$, $b_2^+=n$ the Bauer–Furuta invariant is a stable class represented by

$$f:\; S^{m\mathbb{H}} \longrightarrow S^{n\tilde{\mathbb{R}}},$$

whose restriction to $Pin(2)$-fixed points $S^0 \to S^0$ has degree $\pm 1$ (the index of the Dirac operator contributes $-\sigma/16 = m$ copies of $\mathbb{H}$; the cokernel of $d^+$ contributes $n$ copies of $\tilde{\mathbb{R}}$).

**Furuta's problem.** For which $(m,n)$ does such an $f$ exist? The 11/8 conjecture would follow from nonexistence whenever $n < 3m$.

**Furuta's 10/8 theorem (2001).** Existence forces
$$n \;\ge\; 2m+1 \quad (m\ge 1), \qquad\text{i.e.}\qquad b_2(X) \;\ge\; \tfrac{10}{8}|\sigma(X)| + 2 .$$
The proof applies $Pin(2)$-equivariant $K$-theory: the $K_{Pin(2)}$-degree of $f$ lies in $R(Pin(2))$, and Adams-operation divisibility of the class $\prod$ over the quaternionic weights forces the inequality.

## 3. History & State of the Art (SOTA)

- **1952** Rokhlin: $16\mid\sigma$ for smooth spin 4-manifolds.
- **1982** Freedman: all even unimodular forms occur topologically; the smooth/topological gap opens.
- **1983** Donaldson: diagonalizability theorem; $n\ge1$.
- **1980s** The ratio $11/8$ is isolated as the conjectural optimum by Y. Matsumoto (*On the bounding genus of homology 3-spheres* and related work), motivated by $K3$ and the Rokhlin invariant; often called the Matsumoto conjecture.
- **1995–2001** Furuta's $10/8$ theorem: $b_2 \ge \frac{10}{8}|\sigma| + 2$, the first bound with the right linear growth.
- **2004** Bauer–Furuta stable cohomotopy refinement; Bauer's connected-sum (smash product) formula makes the invariant computable for connected sums.
- **2013** N. Nakamura: $Pin(2)$-monopole equations give $10/8$-type bounds with local coefficients, extending to non-simply-connected and non-spin settings.
- **2015** J. Lin: $Pin(2)$-equivariant $KO$-theory sharpens Furuta's argument.
- **2022** Hopkins–Lin–Shi–Xu: the **"$10/8+4$" theorem**, currently SOTA.

**SOTA bound (HLSX).** For $X$ closed smooth spin with $\sigma=-16m<0$ and form $2m(-E_8)\oplus nH$:
$$m\ge1 \Rightarrow n\ge 2m+1,\quad m\ge2 \Rightarrow n\ge 2m+2,\quad m\ge3 \Rightarrow n\ge 2m+3,$$
$$m\ge4 \Rightarrow n\ge 2m+4,\quad m\ge5 \Rightarrow n\ge 2m+5 .$$
Asymptotically this is still $b_2 \ge \frac{10}{8}|\sigma| + 10$ — a bounded additive gain over $10/8$, not an improvement of the slope.

## 4. Partial Results / Verified Cases

- **$m \le 5$, i.e. $|\sigma| \le 80$: the 11/8 conjecture is a theorem.** Compare required $n\ge 3m$ with HLSX $n\ge 2m+k$:
  | $m$ | $\sigma$ | needed $n$ | proved $n$ | source |
  |---|---|---|---|---|
  | 1 | $-16$ | 3 | 3 | Furuta 2001 |
  | 2 | $-32$ | 6 | 6 | HLSX 2022 |
  | 3 | $-48$ | 9 | 9 | HLSX 2022 |
  | 4 | $-64$ | 12 | 12 | HLSX 2022 |
  | 5 | $-80$ | 15 | 15 | HLSX 2022 |
  | 6 | $-96$ | 18 | 17 | gap of 1 |
- **$m=0$ (definite or trivial signature):** immediate.
- **Definite case:** Donaldson — no smooth closed spin 4-manifold with definite nonzero form.
- **Complex/Kähler surfaces:** all known smooth spin 4-manifolds, including complete intersections and elliptic surfaces $E(k)$ with $k$ even, satisfy $b_2 \ge \frac{11}{8}|\sigma|$ with equality only for $\\\\#_m K3$-type forms; no counterexample has ever been constructed by any surgery, symplectic, or algebraic-geometric technique.
- **With extra structure:** Nakamura's $Pin(2)$-monopole bounds cover spin 4-manifolds with $\pi_1 = \mathbb{Z}/2$ and local-coefficient variants; Bauer's connected-sum formula gives improved bounds for connected sums of spin manifolds with $b^+>0$ summands.

## 5. Principal Obstacles

- **The gauge-theoretic obstruction is bounded, not linear-in-$m$ sharp.** Furuta's $K$-theoretic argument and its $KO$ and stable-homotopy refinements all produce $n \ge 2m + c$ with $c$ a small constant. To reach $n\ge 3m$ one needs an obstruction growing like $m$, not an additive correction. Every known refinement (Adams operations, $KO$-degree, equivariant Mahowald invariants) has so far only increased $c$.
- **The equivariant homotopy problem is genuinely weaker than the geometry.** $Pin(2)$-equivariant maps $S^{m\mathbb{H}}\to S^{n\tilde{\mathbb{R}}}$ are believed to exist for $n$ well below $3m$, so no argument that only remembers the $Pin(2)$-equivariant stable homotopy class of the monopole map can prove 11/8 *(frontier — verify)*. Extra input — the geometry of the moduli space, or a finer group action — appears necessary.
- **Computational explosion.** HLSX reduce the question to $Pin(2)$-equivariant stable stems and Mahowald invariants; the relevant Adams spectral sequence charts grow rapidly, and each additional unit of $c$ costs substantially more homotopy-theoretic computation.
- **No construction technique on the other side.** Logarithmic transforms, knot surgery, rational blowdowns and fiber sums either destroy the spin condition or move $(m,n)$ along the known-realizable ray, so there is no candidate counterexample to test.
- **Non-simply-connected and $b_1>0$ cases** complicate finite-dimensional approximation (the Picard torus enters), requiring families versions of the Bauer–Furuta invariant.

## 6. The Gap

Proven: $n \ge 2m + \min(m,5)$. Conjectured: $n \ge 3m$. The gap is the region

$$2m + 5 \;\le\; n \;<\; 3m, \qquad m \ge 6,$$

which is nonempty and grows linearly. The exact missing step is an obstruction whose strength scales with $m$: one must show that a $Pin(2)$-equivariant stable map $S^{m\mathbb{H}} \to S^{n\tilde{\mathbb{R}}}$ with degree $\pm1$ on fixed points, **and additionally arising as the Bauer–Furuta invariant of a smooth spin 4-manifold**, cannot exist for $n<3m$. The second clause is essential — the purely homotopy-theoretic problem almost certainly has a weaker answer.

## 7. Current Research (as of June 2026)

- **Equivariant stable homotopy theory (Hopkins, Lin, Shi, Xu; MIT/UCSD/Northwestern/Harvard).** Extending the $Pin(2)$-equivariant Mahowald invariant computations past $10/8+4$; the technique is systematic and each new stem yields another constant *(frontier — verify)*.
- **Seiberg–Witten Floer homotopy types (Manolescu, Lin, Stoffregen, Sasahira; UCLA, UCSD, Michigan State).** Cutting spin 4-manifolds along homology 3-spheres and using $Pin(2)$-equivariant Floer homotopy of the pieces to localize the obstruction. This is the most promising route to an $m$-dependent bound.
- **$Pin(2)$-monopole and local-coefficient methods (Nakamura, Kato; Japan).** Bounds for spin 4-manifolds with prescribed fundamental groups; also constraints on embeddings of 3-manifolds.
- **Families gauge theory (Baraglia, Konno; Adelaide/Tokyo).** Bauer–Furuta invariants of families give $10/8$-type results for diffeomorphism groups and for spin families over spheres, occasionally beating the single-manifold bound in constrained settings *(frontier — verify)*.
- **Geography searches.** No group has produced a plausible counterexample; effort on the construction side is minimal, which most experts read as evidence for the conjecture.

## 8. Future Work

- Find an obstruction functorial under connected sum whose strength is additive in $m$ — Bauer's smash-product formula suggests the Bauer–Furuta invariant of $\\\\#_m$ pieces should be more rigid than any single equivariant stem class.
- Determine the exact answer to the pure Furuta problem (smallest $n$ admitting a $Pin(2)$-equivariant map $S^{m\mathbb{H}}\to S^{n\tilde{\mathbb{R}}}$). Even a negative answer clarifies how much extra geometry must be injected.
- Push HLSX to $10/8+k$ for $k=6,7,\dots$, settling $m=6,7$ and testing whether the method saturates.
- Develop a genuinely 4-dimensional (non-linearized) obstruction: use the full moduli space, or higher structured equivariance (e.g. $\mathbb{Z}/4$ or $Sp(1)$ actions on covers).
- Relate 11/8 to 3-manifold invariants: bounds on the bounding genus of homology spheres and on which Brieskorn spheres bound spin 4-manifolds with small $b_2$ are equivalent reformulations for small $m$.

## 9. Key References

- **[Foundational]** V. A. Rokhlin. *New results in the theory of four-dimensional manifolds.* Doklady Akad. Nauk SSSR **84** (1952), 221–224.
- **[Foundational]** M. H. Freedman. *The topology of four-dimensional manifolds.* Journal of Differential Geometry **17** (1982), 357–453.
- **[Foundational]** S. K. Donaldson. *An application of gauge theory to four-dimensional topology.* Journal of Differential Geometry **18** (1983), 279–315.
- **[Foundational]** M. Furuta. *Monopole equation and the $11/8$-conjecture.* Mathematical Research Letters **8** (2001), 279–291.
- **[Foundational]** S. Bauer, M. Furuta. *A stable cohomotopy refinement of Seiberg–Witten invariants: I.* Inventiones Mathematicae **155** (2004), 1–19.
- **[Foundational]** S. Bauer. *A stable cohomotopy refinement of Seiberg–Witten invariants: II.* Inventiones Mathematicae **155** (2004), 21–40.
- **[SOTA / Recent]** M. J. Hopkins, J. Lin, X. D. Shi, Z. Xu. *Intersection forms of spin four-manifolds and the $Pin(2)$-equivariant Mahowald invariant.* Transactions of the American Mathematical Society **375** (2022).
- **[SOTA / Recent]** J. Lin. *$Pin(2)$-equivariant $KO$-theory and intersection forms of spin 4-manifolds.* Algebraic & Geometric Topology **15** (2015), 863–902.
- **[SOTA / Recent]** N. Nakamura. *$Pin(2)$-monopole equations and intersection forms with local coefficients of four-manifolds.* Mathematische Annalen **357** (2013), 915–939.
- **[SOTA / Recent]** C. Manolescu. *$Pin(2)$-equivariant Seiberg–Witten Floer homology and the triangulation conjecture.* Journal of the American Mathematical Society **29** (2016), 147–176.
- **[Survey]** R. E. Gompf, A. I. Stipsicz. *4-Manifolds and Kirby Calculus.* Graduate Studies in Mathematics 20, American Mathematical Society, 1999.
- **[Survey]** A. Scorpan. *The Wild World of 4-Manifolds.* American Mathematical Society, 2005.

## 10. Worked Example / Concrete Special Case

**The $K3$ surface: the extremal point.**

Take $K3 = \{z_0^4+z_1^4+z_2^4+z_3^4=0\}\subset \mathbb{CP}^3$. Its canonical class vanishes, so $w_2=0$ and $K3$ is spin. Standard invariants: $\chi = 24$, $b_1=0$, $b_2=22$, $b_2^+=3$, $b_2^-=19$, $\sigma = 3-19 = -16$. Its intersection form is

$$Q_{K3} \;=\; 2(-E_8)\oplus 3H, \qquad m=1,\ n=3 .$$

Check the conjecture: $\tfrac{11}{8}|\sigma| = \tfrac{11}{8}\cdot 16 = 22 = b_2$. Equality — $K3$ sits exactly on the conjectured boundary.

**The excluded neighbour.** Consider $Q = 2(-E_8)\oplus 2H$: even, unimodular, indefinite, $\sigma=-16$ (Rokhlin-compatible), $b_2 = 20 < 22$. By Freedman there is a closed simply-connected **topological** 4-manifold with this form, and it is unique. Is it smoothable? Here $m=1$, $n=2$. Furuta's theorem requires $n \ge 2m+1 = 3$. Since $2<3$, **no smooth structure exists**. This single case already establishes 11/8 for $m=1$, since $n\in\{0,1,2\}$ are all excluded ($n=0$ also by Donaldson).

**Where it fails today.** Take $m=6$, $\sigma = -96$. The conjecture forbids $n \le 17$; HLSX prove only $n \ge 2\cdot6+5 = 17$. So the single form

$$2\cdot 6\,(-E_8)\oplus 17H, \qquad b_2 = 96+34 = 130, \qquad \tfrac{11}{8}\cdot 96 = 132,$$

is topologically realized (Freedman), is not excluded by any current theorem, and is conjectured to be non-smoothable. It is the smallest open case. For comparison, $\\\\#_6 K3$ realizes $2\cdot6(-E_8)\oplus 18H$ smoothly with $b_2=132$, matching the bound exactly. The whole problem is the two-unit difference between $130$ and $132$, repeated with growing multiplicity as $m$ increases.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*