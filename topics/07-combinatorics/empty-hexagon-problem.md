---
id: 07-combinatorics/empty-hexagon-problem
title: "Empty Hexagon Problem"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Empty Hexagon Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/empty-hexagon-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $S \subset \mathbb{R}^2$ be a finite set of points in **general position** (no three collinear). A subset $H \subseteq S$ of size $k$ is an **empty convex $k$-gon** (or **$k$-hole**) if $H$ is in convex position and the open convex hull $\operatorname{int}(\operatorname{conv} H)$ contains no point of $S$.

Erdős (1978) asked: does every sufficiently large planar point set in general position contain an empty convex hexagon? Equivalently, is
$$h(6) \;=\; \min\{\, n : \text{every } n\text{-point set in general position contains a } 6\text{-hole} \,\}$$
finite?

Two questions sit here, with different status:

1. **Existence** — is $h(6) < \infty$? *Answered yes* independently by Nicolás (2007) and Gerken (2008).
2. **Exact value** — *Answered* by Heule and Scheucher (2024): $h(6) = 30$. Every set of $30$ points in general position contains a $6$-hole, and Overmars' $29$-point set contains none.

A complete resolution of the exact-value question requires both a $29$-point witness with no $6$-hole (a finite, checkable object) and a proof that no $30$-point configuration avoids one — the latter being a statement over all $30$-point *order types*, of which there are astronomically many. Residual open parts: a human-surveyable proof of $h(6)=30$, the asymptotic count of $6$-holes, and $k$-hole questions in higher dimensions.

## 2. Mathematical Foundations

**Order types.** The combinatorics of holes depends only on the **chirotope** $\chi_S : S^3 \to \{+1,-1\}$,
$$\chi_S(p,q,r) \;=\; \operatorname{sgn} \det \begin{pmatrix} q_x - p_x & r_x - p_x \\ q_y - p_y & r_y - p_y \end{pmatrix},$$
the orientation of each ordered triple. Two sets with the same $\chi$ (up to relabelling and global sign) have the same convex-position and emptiness structure. So $h(k)$ is a statement about **rank-3 uniform oriented matroids** that are *realizable*; the SAT encodings work in the larger, purely combinatorial class of **signotopes** / abstract order types, which is why they yield valid upper bounds.

**Hole numbers.** Define $h(k)\in\mathbb{N}\cup\{\infty\}$ as above, and let $ES(k)$ be the Erdős–Szekeres number: the least $n$ such that every $n$ points in general position contain $k$ points in convex position (holes not required). Trivially $ES(k) \le h(k)$.

**Known values.**
$$h(3)=3,\quad h(4)=5,\quad h(5)=10,\quad h(6)=30,\quad h(k)=\infty \ \ (k \ge 7).$$

**Erdős–Szekeres side.** The classical bounds are
$$2^{k-2}+1 \;\le\; ES(k) \;\le\; \binom{2k-5}{k-2}+1 ,$$
the lower bound from Erdős–Szekeres (1961), the upper from Tóth–Valtr (2005); Suk (2017) improved this to $ES(k) \le 2^{k+o(k)}$. The conjecture $ES(k)=2^{k-2}+1$ is verified up to $k=6$ ($ES(6)=17$, Szekeres–Peters 2006).

**Horton sets.** Horton (1983) built arbitrarily large sets with no $7$-hole. Recursively, $H_{2m}$ splits into an "even" set $E$ and "odd" set $O$ such that $E$ lies *high above* $O$: every line through two points of $E$ passes above all of $O$, and every line through two points of $O$ passes below all of $E$. This mutual-visibility obstruction kills all $7$-holes, hence $h(k)=\infty$ for $k\ge 7$.

**Counting.** Let $X_k(n)$ be the minimum number of $k$-holes over $n$-point sets. Bárány–Füredi (1987) give $X_3(n) \ge n^2 - O(n\log n)$; Valtr (2008) proved $X_6(n) \ge n^2/229$ for large $n$, while Bárány–Valtr (2004) give constructions with $X_k(n) = O(n^2)$ for $k\le 6$. So $X_6(n) = \Theta(n^2)$ with a large constant gap.

## 3. History & State of the Art (SOTA)

- **1935** — Erdős and Szekeres publish "A combinatorial problem in geometry", founding the subject (the "Happy Ending problem").
- **1978** — Erdős poses the empty-polygon variant. Harborth proves $h(5)=10$ in the same year, exhibiting a $9$-point set with no $5$-hole.
- **1983** — Horton settles $k \ge 7$ negatively: $h(7)=\infty$. This made $k=6$ the sole undecided case for 25 years.
- **1980s–90s** — Partial attacks: bounds on the size of point sets forced to contain $6$-holes under extra hypotheses; Valtr and Bárány develop the counting theory.
- **2003** — Overmars, by exhaustive computer search over order types, finds a set of $29$ points with no $6$-hole, establishing $h(6) \ge 30$.
- **2007–2008** — **Existence resolved.** Nicolás ("The empty hexagon theorem", *DCG* 38, 2007) and independently Gerken ("Empty convex hexagons in planar point sets", *DCG* 39, 2008) prove $h(6)<\infty$. Gerken's argument: any set containing a convex $9$-gon contains a $6$-hole, giving $h(6) \le ES(9) \le \binom{13}{7}+1 = 1717+1$. Valtr later simplified the proof; the best human-proof bound stood near $h(6) \le 463$ (Koshelev, 2007–09).
- **2024** — **Exact value.** Heule and Scheucher, "Happy ending: an empty hexagon in every set of 30 points" (TACAS 2024, LNCS 14570), encode the $30$-point case as propositional satisfiability, exploit symmetry breaking, and obtain UNSAT with a DRAT proof of roughly $17$ TiB, verified by `cake_lpr`. Combined with Overmars: $h(6)=30$.
- **2024** — Subercaseaux, Heule and Scheucher formally verify the encoding-to-geometry reduction in **Lean 4** (ITP 2024), closing the gap between "SAT instance is unsatisfiable" and "no such point set exists".

## 4. Partial Results / Verified Cases

| Statement | Status | Source |
|---|---|---|
| $h(3)=3$, $h(4)=5$ | Elementary | Klein/Erdős–Szekeres 1935 |
| $h(5)=10$ | Proved | Harborth 1978 |
| $h(6)\ge 30$ | Explicit $29$-point set | Overmars 2003 |
| $h(6)<\infty$ | Proved | Nicolás 2007; Gerken 2008 |
| $h(6)\le 463$ | Human proof | Koshelev 2009 |
| $h(6)=30$ | Computer proof, Lean-verified | Heule–Scheucher 2024 |
| $h(k)=\infty$, $k\ge 7$ | Proved | Horton 1983 |
| Every set with a convex $9$-gon has a $6$-hole | Proved | Gerken 2008 |
| $X_6(n)\ge n^2/229$ | Proved | Valtr 2008 |
| Squared-Horton / dense sets | $6$-holes exist in random sets a.s. with density $\Theta(n)$ per point | Bárány–Füredi 1987; Fabila-Monroy et al. |
| $ES(6)=17$ | Computer proof | Szekeres–Peters 2006 |
| $3$-D analogue: every large set has an empty "convex polytope" on $k$ vertices? | Known for $k \le 5$; open for $k\ge 6$ | Valtr; Bárány–Füredi |

## 5. Principal Obstacles

- **Search-space explosion.** The number of realizable order types of $n$ points grows as $2^{\Theta(n\log n)}$; for $n = 30$ this is far beyond enumeration. Overmars' exhaustive method topped out near $n=29$.
- **Realizability is hard.** Deciding whether an abstract order type is realizable by actual points is $\exists\mathbb{R}$-complete (Mnëv universality). SAT/oriented-matroid methods therefore only prove *upper* bounds on $h$: an unsatisfiable abstract instance implies no realization, but a satisfiable abstract instance may have no geometric model. Lower bounds still need explicit coordinates.
- **Gerken-type case analysis does not scale.** The human proofs proceed by peeling convex layers and splitting on the position of interior points relative to a convex $9$-gon. The number of subcases grows superexponentially when one tries to reduce the starting convex polygon from $9$ to $8$ or $7$ vertices, and the $6$-hole may be forced only via a global, not local, argument.
- **No stability/extremal principle.** Unlike Ramsey-type problems where random constructions match, the only near-extremal $6$-hole-free sets known are the sporadic $29$-point set and small Horton-like perturbations; there is no parametric family to interpolate, so probabilistic and entropy methods have no target measure.
- **Proof size, not proof idea, is the bottleneck for $h(6)=30$.** The DRAT certificate is $\sim 17$ TiB. This is a valid proof, but it carries no reusable structural insight, so it does not transfer to $ES(7)$ or higher-dimensional analogues.

## 6. The Gap

The *existence* and *exact value* gaps are closed. What remains is a three-part gap:

1. **Comprehensibility gap.** Between the human-checkable bound $h(6)\le 463$ and the machine bound $h(6)=30$ lies a factor of ~15 that no human argument reaches. Closing it means finding a structural theorem — e.g. "every $30$-point set contains a convex $7$-gon with at most $r$ interior points, and such a configuration always yields a $6$-hole" — whose case tree a person can traverse.
2. **Counting gap.** $X_6(n)=\Theta(n^2)$ but the constants differ by roughly two orders of magnitude ($1/229$ vs. the $O(1)$ upper constructions). The precise constant $\lim X_6(n)/n^2$ is open.
3. **Dimensional gap.** In $\mathbb{R}^d$, $d\ge3$, the analogous hole numbers $h_d(k)$ are unknown for $k\ge 6$; even whether $h_3(6)<\infty$ is open, since Horton's construction lifts to give no obvious obstruction.

## 7. Current Research (as of June 2026)

- **SAT-based discrete geometry** (Heule at CMU; Scheucher at TU Berlin; Subercaseaux). Following $h(6)=30$ and $ES(7)$-adjacent work, the same encode–symmetry-break–verify pipeline is being aimed at $ES(7)=33$ (conjectured) and at hole counts $X_5, X_6$ for moderate $n$. *(frontier — verify)*
- **Formal verification.** Lean 4 mathlib-adjacent developments of order types and of the Erdős–Szekeres and empty-hexagon theorems, extending Subercaseaux–Heule–Scheucher (ITP 2024). Marić's earlier Isabelle verification of $ES(6)=17$ is the template.
- **Chromatic and colored variants.** $k$-holes in two-colored point sets (Aichholzer, Hackl, Vogtenhuber, and coauthors): whether every large enough bichromatic set has a monochromatic $4$- or $5$-hole remains open.
- **Random and dense settings.** Expected numbers of $k$-holes in uniform samples from a convex body (Fabila-Monroy, Huemer, Mitsche); asymptotics of $E[X_6]$ refined for $k \le 6$.
- **Higher dimensions.** Work on $d$-dimensional holes and on "convex position with few interior points" (Valtr school, Prague).

## 8. Future Work

- Produce a *surveyable* proof of $h(6)\le 30$ — Heule has explicitly framed proof compression (extracting short human lemmas from DRAT cores) as the goal.
- Determine $\lim_{n\to\infty} X_6(n)/n^2$; even improving Valtr's $1/229$ to a constant above $1/10$ would be a substantial advance.
- Settle $ES(7)$; the conjectured value $2^5+1=33$ is the next SAT-tractable target.
- Decide $h_3(6)$ and, more generally, whether Horton-type obstructions exist in $\mathbb{R}^d$.
- Resolve monochromatic-hole questions for $2$-colored sets, where even $k=4$ has resisted.

## 9. Key References

- **[Foundational]** P. Erdős, G. Szekeres. *A combinatorial problem in geometry.* Compositio Mathematica 2, 463–470, 1935.
- **[Foundational]** P. Erdős. *Some more problems on elementary geometry.* Australian Mathematical Society Gazette 5, 52–54, 1978.
- **[Foundational]** H. Harborth. *Konvexe Fünfecke in ebenen Punktmengen.* Elemente der Mathematik 33, 116–118, 1978.
- **[Foundational]** J. D. Horton. *Sets with no empty convex 7-gons.* Canadian Mathematical Bulletin 26(4), 482–484, 1983.
- **[Key]** M. Overmars. *Finding sets of points without empty convex 6-gons.* Discrete & Computational Geometry 29(1), 153–158, 2003.
- **[Key]** C. M. Nicolás. *The empty hexagon theorem.* Discrete & Computational Geometry 38(2), 389–397, 2007.
- **[Key]** T. Gerken. *Empty convex hexagons in planar point sets.* Discrete & Computational Geometry 39(1–3), 239–272, 2008.
- **[SOTA / Recent]** M. J. H. Heule, M. Scheucher. *Happy ending: an empty hexagon in every set of 30 points.* TACAS 2024, LNCS 14570, Springer, 2024.
- **[SOTA / Recent]** B. Subercaseaux, M. J. H. Heule, M. Scheucher. *Formal verification of the empty hexagon number.* ITP 2024, LIPIcs vol. 309.
- **[Key]** I. Bárány, Z. Füredi. *Empty simplices in Euclidean space.* Canadian Mathematical Bulletin 30(4), 436–445, 1987.
- **[Key]** I. Bárány, P. Valtr. *Planar point sets with a small number of empty convex polygons.* Studia Scientiarum Mathematicarum Hungarica 41(2), 243–266, 2004.
- **[Key]** P. Valtr. *On empty hexagons.* In: Surveys on Discrete and Computational Geometry, Contemporary Mathematics 453, AMS, 433–441, 2008.
- **[Key]** G. Szekeres, L. Peters. *Computer solution to the 17-point Erdős–Szekeres problem.* ANZIAM Journal 48(2), 151–164, 2006.
- **[Key]** A. Suk. *On the Erdős–Szekeres convex polygon problem.* Journal of the AMS 30, 1047–1053, 2017.
- **[Survey]** W. Morris, V. Soltan. *The Erdős–Szekeres problem on points in convex position — a survey.* Bulletin of the AMS 37(4), 437–458, 2000.
- **[Survey]** J. Matoušek. *Lectures on Discrete Geometry.* Graduate Texts in Mathematics 212, Springer, 2002 (Ch. 3: Horton sets).

## 10. Worked Example / Concrete Special Case

**Claim: $h(4)=5$** — every $5$ points in general position contain an empty convex quadrilateral, and $4$ points do not suffice.

*Lower bound.* Take $p_1=(0,0)$, $p_2=(4,0)$, $p_3=(2,4)$, $p_4=(2,1)$. The first three form a triangle and $p_4$ lies inside it (barycentric coordinates $(\tfrac{3}{8},\tfrac{1}{8},\tfrac{1}{2})$, all positive). No $4$ of these points are in convex position, so there is no $4$-hole. Hence $h(4)\ge 5$.

*Upper bound.* Let $|S|=5$, general position. By the Klein/Erdős–Szekeres argument, $S$ contains $4$ points in convex position: if $\operatorname{conv}(S)$ has $4$ or $5$ vertices we are done; if it is a triangle $abc$ with $d,e$ inside, the line $de$ misses one vertex-side — say it leaves $a$ and $b$ on the same side — and then $a,b,d,e$ is convex.

Now pick, among all convex quadrilaterals $Q$ spanned by $S$, one of **minimum area**. Suppose $Q = wxyz$ contains a point $p \in S$ in its interior. The diagonal $wy$ splits $Q$ into triangles $wxy$ and $wyz$; $p$ lies inside one of them, say $wxy$. Then $w x p y$... more directly: $p$ together with three of $\{w,x,y,z\}$ forms a convex quadrilateral of strictly smaller area — replace the vertex of the triangle not containing $p$'s side. Concretely, if $p \in \operatorname{int}(wyz)$ then $w x y p$ is convex and
$$\operatorname{area}(wxyp) = \operatorname{area}(wxy) + \operatorname{area}(wyp) < \operatorname{area}(wxy) + \operatorname{area}(wyz) = \operatorname{area}(Q),$$
contradicting minimality. So the minimum-area convex quadrilateral is empty, and $h(4)=5$. $\blacksquare$

**Why this breaks at $k=6$.** The minimum-area trick works because a quadrilateral splits into exactly two triangles, so any interior point immediately produces a smaller quadrilateral. For $k=6$ an interior point of a convex hexagon need not yield a smaller *hexagon* — it typically yields a pentagon plus a triangle. The area-minimization potential no longer decreases within the class of $6$-gons, and this is precisely the collapse that forces Gerken's $9$-gon-based case analysis and, ultimately, the $17$ TiB certificate for $h(6)=30$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*