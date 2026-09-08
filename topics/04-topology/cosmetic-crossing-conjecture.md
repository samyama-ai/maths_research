---
id: 04-topology/cosmetic-crossing-conjecture
title: "Cosmetic Crossing Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cosmetic Crossing Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/cosmetic-crossing-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

A crossing change on a knot $K \subset S^3$ is **nugatory** (trivial for an obvious reason) if the crossing is supported by a disk that separates the diagram: the crossing circle bounds an embedded disk in the complement of $K$. A nugatory crossing change never alters the knot type. The conjecture asserts the converse.

**Conjecture (Cosmetic Crossing / Nugatory Crossing Conjecture).** Let $K \subset S^3$ be a knot and let $K'$ be obtained from $K$ by a single crossing change. If $K' = K$ as oriented knots (ambient isotopy, orientation-preserving in $S^3$), then the crossing change is nugatory.

Equivalently: no knot admits a *cosmetic crossing* — a non-nugatory crossing whose change is invisible up to isotopy. It appears as Problem 1.58 in Kirby's problem list, attributed to X.-S. Lin. A proof must handle every knot and every crossing disk; a disproof requires one explicit pair $(K, D)$ with $K_D \cong K$ and $\partial D$ essential in $S^3 \setminus K$. The link version is false-by-convention only if orientations are dropped; the oriented statement for links is also conjectured, and known for split links.

## 2. Mathematical Foundations

Let $K \subset S^3$ be a knot. A **crossing disk** for $K$ is an embedded disk $D \subset S^3$ with
$$D \cap K = \{p, q\}, \qquad \operatorname{lk}(\partial D, K) = 0,$$
where $K$ intersects $\operatorname{int} D$ transversally in two points of opposite sign. The curve $L = \partial D$ is the **crossing circle**. Changing the crossing at $D$ is the same as $(-1)$-twisting along $D$, i.e. performing $\mp 1$ surgery on $L$:
$$K_D \subset S^3_{\mp 1}(L) \cong S^3 .$$
More generally, $-1/n$ surgery on $L$ gives the **generalized crossing change** of order $n$, adding $n$ full twists.

The crossing is **nugatory** iff $L$ bounds an embedded disk in $S^3 \setminus K$, i.e. $L$ is inessential in the complement; equivalently $S^3 \setminus (K \cup L)$ is reducible or $L$ is boundary-parallel in a punctured-sphere sense.

Since $K_D \cong K$ makes all classical invariants agree, obstructions must come from the *pair*. Two frameworks dominate:

1. **Sutured/foliation theory.** For a minimal-genus Seifert surface $S$ for $K$ of genus $g(K)$, one may isotope $D$ so that $D \cap S$ is a single arc or a curve system; the crossing change becomes twisting along a simple closed curve $c \subset S$ with $\operatorname{lk}(c, c) = 0$ in the Seifert form. Gabai's theorem that a taut foliation certifies minimal genus, and $g(K_D) = g(K)$, constrains $c$.
2. **Seifert form.** For $g(K) = 1$ with basis $\{x, y\}$ of $H_1(S) \cong \mathbb{Z}^2$, the Seifert matrix may be normalized to
$$V = \begin{pmatrix} a & b+1 \\ b & c\end{pmatrix}, \qquad V - V^{T} = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix},$$
and with $n := ac - b(b+1)$,
$$\Delta_K(t) \doteq \det(V - tV^{T}) = n t^{2} - (2n - 1)t + n .$$
So $\Delta_K \doteq 1$ exactly when $n = 0$.

3. **Branched covers.** A crossing change on $K$ lifts to a surgery on a knot in the double branched cover $\Sigma_2(K)$; a cosmetic crossing yields a *cosmetic surgery* pair there, attackable by Heegaard Floer $d$-invariants and the Casson–Walker invariant.

A crossing change is also realized by a genus-one cobordism in $S^3 \times I$, so concordance invariants ($\tau$, $s$, $\nu^+$) move by at most $1$ — enough to bound, never to exclude, since a cosmetic change moves them by $0$.

## 3. History & State of the Art (SOTA)

- **1980s.** The question circulates as Lin's problem; recorded as Problem 1.58 in Kirby's 1995/1997 problem list.
- **1989.** Scharlemann–Thompson, *Link genus and the Conway moves*, settle the unknot: a crossing change on the unknot producing the unknot is nugatory. Their method (sutured manifold theory after Gabai) sets the template.
- **1999.** Torisu proves the conjecture for **2-bridge knots**, via a careful analysis of crossing circles against the bridge sphere plus Gordon–Luecke.
- **2012.** Kalfagianni proves it for **fibred knots** (Crelle), using Gabai's theorems on Thurston norm and the sutured decomposition of a fibre.
- **2012.** Balm–Friedl–Kalfagianni–Powell, *Cosmetic crossings and Seifert genus*, prove it for **genus-one knots with $\Delta_K \not\doteq 1$**, and verify it for all knots of at most $9$ crossings.
- **2017.** Lidman–Moore (Trans. AMS) prove it for knots whose double branched cover is an **L-space** — this covers all **alternating** knots and all **Montesinos** knots — by translating to cosmetic surgery and using $d$-invariants.
- **2022.** J. Wang proves the **split-link** case using Kronheimer–Mrowka instanton Floer homology ($I^\natural$ / singular instanton knot homology).

State of the art: the conjecture is a theorem on large, structurally defined families (fibred, alternating, Montesinos, 2-bridge, small genus with nontrivial Alexander polynomial), and open for a generic knot — notably for satellites and for genus-one knots with trivial Alexander polynomial.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Unknot | No cosmetic crossings | Scharlemann–Thompson 1989 |
| 2-bridge knots | No cosmetic crossings | Torisu 1999 |
| Fibred knots (any genus) | No cosmetic crossings | Kalfagianni 2012 |
| Genus-one knots with $\Delta_K(t) \not\doteq 1$ | No cosmetic crossings | Balm–Friedl–Kalfagianni–Powell 2012 |
| Knots with $\le 9$ crossings | Verified case-by-case | Balm–Friedl–Kalfagianni–Powell 2012 |
| $\Sigma_2(K)$ an L-space; in particular alternating and Montesinos knots | No cosmetic crossings | Lidman–Moore 2017 |
| Split links | Conjecture holds | J. Wang 2022 |
| Symmetric unions (large families) | No cosmetic crossings | Moore 2016 |
| Generalized crossing changes of order $|n| \ge 2$ on many classes | Excluded by genus/surgery arguments | Kalfagianni 2012; Balm–Kalfagianni |

Also known: a cosmetic crossing change cannot alter the Seifert genus, so any cosmetic crossing on $K$ must be *genus-preserving* — which is what makes genus $1$ tractable and genus $\ge 2$ non-fibred knots hard.

## 5. Principal Obstacles

- **Invariants are blind by hypothesis.** If $K_D \cong K$, every knot invariant of $K$ and $K_D$ agrees. No polynomial, Floer group, or concordance invariant of the knot alone can obstruct; one must work with the *link* $K \cup L$ or the crossing disk, which is not determined by $K$.
- **Reduction to cosmetic surgery.** The natural translation turns the problem into: a knot in a solid torus with two distinct slopes giving the same filled knot. This is exactly the difficulty of the Cosmetic Surgery Conjecture, itself open; the Heegaard Floer route (Ozsváth–Szabó, Ni–Wu) yields strong but not complete constraints, and needs an L-space or similarly rigid hypothesis to close.
- **Sutured manifold theory needs a fibration or a thin surface.** Gabai's machinery is decisive when a minimal-genus Seifert surface is unique and rigid (fibred case) or has tiny $H_1$ (genus one). For high-genus, non-fibred knots the surface is neither unique nor forced to intersect $D$ in a controlled arc system, and the sutured decomposition branches uncontrollably.
- **Trivial Alexander polynomial kills the linear algebra.** In genus one the Seifert-form argument produces the numerical invariant $n = ac - b(b+1)$; when $n = 0$ the obstruction vanishes identically. Untwisted Whitehead doubles sit precisely here.
- **Satellites and JSJ structure.** For satellite knots the crossing disk can live in a companion solid torus and interact with the JSJ decomposition; no general argument transfers a solution from the companion or the pattern to the satellite.
- **Instanton/Khovanov methods are qualitative.** Wang's split-link proof exploits a genuinely global structure (splitness detected by instanton homology); there is no known analogue of "splitness" to exploit for a prime knot.

## 6. The Gap

Proven statements all supply one of three rigidities: (i) a fibration, (ii) $\operatorname{rank} H_1(S) = 2$ with $\Delta_K \ne 1$, or (iii) an L-space double branched cover. The general statement needs neither.

The exact step to cross: given a knot $K$ and a crossing disk $D$ with $\partial D$ essential in $S^3 \setminus K$, show that $\pm 1$ surgery on $\partial D$ *must* change the isotopy class of $K$ — with no hypothesis on $g(K)$, on the Alexander polynomial, or on $\Sigma_2(K)$. Concretely, the two smallest unclosed frontiers are:

1. **Genus one, $\Delta_K \doteq 1$** (e.g. untwisted Whitehead doubles $D_\pm(J,0)$ of a nontrivial knot $J$): here $n = 0$ and every current obstruction is vacuous.
2. **Non-fibred knots of genus $\ge 2$ whose double branched cover is not an L-space** — the generic case, where minimal-genus Seifert surfaces are non-unique.

## 7. Current Research (as of June 2026)

- **Instanton-theoretic extensions.** Following Wang's split-link theorem, work aims to replace splitness with weaker decompositions (connected sums, tangle sums) using singular instanton homology and Kronheimer–Mrowka excision. *(frontier — verify)*
- **Heegaard Floer surgery obstructions.** Refinements of Ni–Wu-type inequalities and $d$-invariant surgery formulas, aiming to drop the L-space hypothesis in Lidman–Moore. Groups at Michigan State (Kalfagianni), Georgia Tech / UC Davis (Moore), and NC State (Lidman) have been central.
- **Genus-one with trivial Alexander polynomial.** Attacks combining the Casson invariant of $\Sigma_2(K)$ with the geometry of once-punctured torus fibres; also twisted Alexander polynomials and metabelian representations as replacements for the vanishing classical obstruction. *(frontier — verify)*
- **Quantum / Khovanov constraints.** Reduced Khovanov and annular Khovanov homology of $K \cup L$ as a candidate obstruction to $\pm1$ twisting along $L$. *(frontier — verify)*
- **Cosmetic surgery interplay.** Progress on the cosmetic surgery conjecture (Hanselman-type bounds relating $g(K)$ and thickness) is being imported to bound which knots could host a cosmetic crossing. *(frontier — verify)*

## 8. Future Work

- Prove the genus-one case unconditionally: classify curves $c$ on a once-punctured torus Seifert surface with $\operatorname{lk}(c,c) = 0$ whose twisting preserves the knot when $\Delta_K \doteq 1$.
- Establish a satellite reduction theorem: if the conjecture holds for companion and pattern, it holds for the satellite.
- Extend Kalfagianni's fibred-knot argument to knots with *unique* minimal-genus Seifert surface (a strictly larger class than fibred).
- Push computational verification past $9$ crossings by enumerating crossing disks up to isotopy in complements, using SnapPy/Regina and normal-surface algorithms.
- Prove the oriented conjecture for all links, generalizing Wang's split case.

## 9. Key References

- **[Problem source]** R. Kirby (ed.). *Problems in low-dimensional topology.* In *Geometric Topology* (Athens, GA, 1993), AMS/IP Studies in Advanced Mathematics 2.2, American Mathematical Society, 1997. (Problem 1.58.)
- **[Foundational]** M. Scharlemann, A. Thompson. *Link genus and the Conway moves.* Commentarii Mathematici Helvetici 64 (1989), 527–535. [DOI](https://doi.org/10.1007/bf02564693)
- **[Foundational]** D. Gabai. *Foliations and the topology of 3-manifolds II, III.* Journal of Differential Geometry 26 (1987), 461–478 and 479–536. [DOI](https://doi.org/10.4310/jdg/1214441488)
- **[Partial results]** I. Torisu. *On nugatory crossings for knots.* Mathematical Proceedings of the Cambridge Philosophical Society 126 (1999), 435–446. [DOI](https://doi.org/10.1016/s0166-8641(97)00238-1)
- **[Partial results]** E. Kalfagianni. *Cosmetic crossings of fibred knots.* Journal für die reine und angewandte Mathematik (Crelle's Journal) 669 (2012), 151–164.
- **[Partial results]** C. Balm, S. Friedl, E. Kalfagianni, M. Powell. *Cosmetic crossings and Seifert genus.* Journal of Knot Theory and Its Ramifications 21 (2012), no. 11, 1250120.
- **[SOTA]** T. Lidman, A. H. Moore. *Cosmetic surgery in L-spaces and nugatory crossings.* Transactions of the American Mathematical Society 369 (2017), 3639–3654. [DOI](https://doi.org/10.1090/tran/6839)
- **[SOTA / Recent]** J. Wang. *The cosmetic crossing conjecture for split links.* Geometry & Topology 26 (2022). [DOI](https://doi.org/10.2140/gt.2022.26.2941)
- **[Partial results]** A. H. Moore. *Symmetric unions without cosmetic crossing changes.* In *Advances in the Mathematical Sciences* (Association for Women in Mathematics Series, vol. 6), Springer, 2016. [DOI](https://doi.org/10.1007/978-3-319-34139-2_3)
- **[Background]** P. Kronheimer, T. Mrowka. *Khovanov homology is an unknot-detector.* Publications mathématiques de l'IHÉS 113 (2011), 97–208. [DOI](https://doi.org/10.1007/s10240-010-0030-y)
- **[Background]** P. Ozsváth, Z. Szabó. *Knot Floer homology and rational surgeries.* Algebraic & Geometric Topology 11 (2011), 1–68. [DOI](https://doi.org/10.2140/agt.2011.11.1)

## 10. Worked Example / Concrete Special Case

**Claim.** The figure-eight knot $4_1$ admits no cosmetic crossing change — twice over, and by two different mechanisms.

*Route 1 (genus-one Seifert form).* $4_1$ has genus $1$; its Seifert surface is a once-punctured torus with Seifert matrix
$$V = \begin{pmatrix} 1 & 1 \\ 0 & -1 \end{pmatrix}, \qquad V - V^{T} = \begin{pmatrix} 0 & 1 \\ -1 & 0\end{pmatrix}.$$
In the normalization of Section 2, $a = 1$, $b = 0$, $c = -1$, so
$$n = ac - b(b+1) = (1)(-1) - 0 = -1,$$
and
$$\Delta_{4_1}(t) \doteq n t^{2} - (2n-1)t + n = -t^{2} + 3t - 1 \doteq -t + 3 - t^{-1},$$
matching the classical value. Since $n = -1 \neq 0$, $\Delta_{4_1} \not\doteq 1$, and the Balm–Friedl–Kalfagianni–Powell theorem applies: every crossing change on $4_1$ that returns $4_1$ is nugatory.

*Route 2 (fibredness).* $4_1$ is fibred, with monodromy $\begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$ acting on $H_1$ of the fibre. Kalfagianni's theorem gives the same conclusion independently. (And $4_1$ is alternating and 2-bridge, so Torisu 1999 and Lidman–Moore 2017 also cover it.)

*Where the argument breaks.* Take instead $K = D_+(J, 0)$, the untwisted positive-clasped Whitehead double of the trefoil $J = 3_1$. Then $g(K) = 1$ and $\Delta_K(t) \doteq 1$, i.e. $n = 0$, so the polynomial $n t^2 - (2n-1)t + n$ collapses to $t$ and carries no information. $K$ is not fibred, is not alternating, and $\Sigma_2(K)$ is not known to be an L-space. Every proof strategy in Section 4 fails on this single knot: it is the smallest honest test case for the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*