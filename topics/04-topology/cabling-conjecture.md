---
id: 04-topology/cabling-conjecture
title: "Cabling Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Cabling Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/cabling-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (González-Acuña–Short, 1986).** Let $K \subset S^3$ be a knot and let $S^3_{r}(K)$ denote the result of Dehn surgery on $K$ along the slope $r \in \mathbb{Q} \cup \{\infty\}$. If $S^3_r(K)$ is *reducible* — i.e. contains an embedded 2-sphere that does not bound a ball — then $K$ is a cable knot, $K = C_{p,q}(K')$ for some knot $K'$ and coprime $p \geq 2$, $q$, and $r = pq$ is the slope of the cabling annulus.

Equivalently: the only way to produce a reducible manifold by surgery on a knot in $S^3$ is the obvious way, by filling along the boundary slope of an essential annulus in the knot exterior.

The unknot is excluded only in the trivial sense that $S^3_0(\text{unknot}) = S^1 \times S^2$ is reducible; by Gabai's Property R theorem this is the unique reducible surgery on the unknot, so the conjecture is stated for nontrivial $K$.

A complete proof must show that every nontrivial non-cable knot has *irreducible* surgeries at all slopes. A disproof requires one hyperbolic knot $K$ and one integer $n$ with $S^3_n(K)$ reducible.

## 2. Mathematical Foundations

Let $E(K) = S^3 \setminus \nu(K)$ be the knot exterior, a compact orientable 3-manifold with $\partial E(K) \cong T^2$. Fix the standard meridian–longitude basis $(\mu, \lambda)$ with $\lambda$ null-homologous in $E(K)$. A **slope** is an isotopy class of essential simple closed curve on $\partial E(K)$, parametrised as $r = p/q \leftrightarrow p\mu + q\lambda$. Dehn filling gives
$$S^3_{p/q}(K) \;=\; E(K) \cup_{h} (S^1 \times D^2), \qquad h(\partial D^2) = p\mu + q\lambda .$$

The **distance** between slopes is $\Delta(r_1, r_2) = |p_1 q_2 - p_2 q_1|$.

**Cable knots.** Given a knot $K' \subset S^3$ with tubular neighbourhood $\nu(K') \cong S^1\times D^2$, and coprime integers $p \geq 2$, $q$, the $(p,q)$-cable $C_{p,q}(K')$ is the curve on $\partial \nu(K')$ homologous to $p[\lambda'] + q[\mu']$. The annulus
$$A \;=\; \partial \nu(K') \setminus \nu\!\left(C_{p,q}(K')\right)$$
is essential in $E(C_{p,q}(K'))$, and $\partial A$ has slope $pq$ on $\partial E(C_{p,q}(K'))$. Filling along $pq$ caps $A$ into a 2-sphere, and

$$S^3_{pq}\!\left(C_{p,q}(K')\right) \;\cong\; L(p,q) \;\\#\; S^3_{q/p}(K').$$

Since $p \geq 2$, neither summand is $S^3$: the surgery is reducible. The conjecture asserts the converse.

**Torus knots.** $T(p,q) = C_{p,q}(\text{unknot})$, and Moser's classification gives $S^3_{pq}(T(p,q)) \cong L(p,q)\,\\#\,L(q,p)$, the only reducible slope.

**Genus and Floer input.** Write $g(K)$ for the Seifert genus, $\widehat{HFK}$ for knot Floer homology, and $d$ for the Heegaard Floer correction term. A knot is an **L-space knot** if some positive surgery $Y$ has $\dim \widehat{HF}(Y) = |H_1(Y;\mathbb{Z})|$. Greene's obstruction runs through **changemaker lattices**: if $S^3_n(K) \cong Y_1 \\# Y_2$, the intersection form of the associated 4-manifold $X_n(K)$ (2-handle on $B^4$) must embed in a diagonal lattice $\mathbb{Z}^N$ with the vector $(\sigma_1,\dots,\sigma_N)$ satisfying the changemaker condition $\sigma_i \leq 1 + \sum_{j<i}\sigma_j$.

## 3. History & State of the Art (SOTA)

- **1971.** Moser classifies all surgeries on torus knots; reducible exactly at slope $pq$. This is the model case.
- **1986.** González-Acuña and Short state the conjecture in *Knot surgery and primeness*, motivated by the question of when surgery yields a non-prime manifold.
- **1987.** Gabai's Property R (via sutured manifold theory and taut foliations) settles the unknot case: $S^3_0(K) \cong S^1\times S^2$ forces $K$ unknotted.
- **1987.** Gordon–Luecke: a reducing slope is **integral**, $r = n \in \mathbb{Z}$. This removes the entire rational-slope dimension from the problem.
- **1990.** Scharlemann proves the conjecture for **satellite knots**, using thin position and sutured manifold theory. Combined with Moser, all non-hyperbolic knots are settled — the conjecture is now purely a statement about hyperbolic knots.
- **1996.** Gordon–Luecke, *Reducible manifolds and Dehn surgery*: sharp combinatorial control on intersection graphs of punctured spheres; a reducing surgery on a hyperbolic knot yields at most two prime summands and contains a lens space summand.
- **2003.** Matignon–Sayari: a reducing slope on a non-cable knot satisfies $|n| \le 2g(K) - 1$.
- **2015.** Greene, *L-space surgeries, genus bounds, and the cabling conjecture*: lattice-theoretic reproof and sharpening of the genus bound, and a full proof for **L-space knots**.

## 4. Partial Results / Verified Cases

| Class / constraint | Result | Source |
|---|---|---|
| Unknot | Only reducible surgery is $0$-surgery | Gabai 1987 |
| Torus knots $T(p,q)$ | Reducible only at $n = pq$ | Moser 1971 |
| Satellite knots (all) | Conjecture holds | Scharlemann 1990 |
| Alternating knots | Conjecture holds | Menasco–Thistlethwaite 1992 |
| Symmetric knots (periodic / strongly invertible) | Conjecture holds | Hayashi–Shimokawa 1998 |
| L-space knots (incl. all knots with lens space surgeries) | Conjecture holds | Greene 2015 |
| Slope restriction | $r \in \mathbb{Z}$, and $|r| \le 2g(K)-1$ for non-cables | Gordon–Luecke 1987; Matignon–Sayari 2003; Greene 2015 |
| Summand count | $S^3_n(K)$ reducible $\Rightarrow$ at most two prime summands, one a lens space | Gordon–Luecke 1996; Hoffman 1998 |
| Small bridge number | Conjecture holds for bridge number $\le 3$ | Hoffman 1998 (great $x$-cycle obstruction) |
| Census knots | No reducible surgeries found for knots up to 16 crossings, via Floer/changemaker screening *(frontier — verify)* | computational folklore |

Only **hyperbolic knots** with $2 \le |n| \le 2g(K)-1$ remain open, and even there $S^3_n(K)$ must be $L(a,b) \\# Y$ with $Y$ an irreducible homology-lens-space piece.

## 5. Principal Obstacles

- **Combinatorial blow-up in the graph method.** The standard approach takes an essential planar surface $P \subset E(K)$ (a punctured reducing sphere) and a second surface (Seifert surface, or a second reducing sphere), and studies the graphs $G_P, G_Q$ of intersection arcs on the two spheres. Gordon–Luecke's parity and Scharlemann-cycle arguments control the case where the number of punctures $|\partial P|$ is small; for large puncture number the graph combinatorics admits too many configurations to enumerate. There is no known a priori bound on $|\partial P|$.
- **Sutured manifold theory does not see reducing spheres.** Gabai's machinery certifies *taut* foliations and irreducibility statements about norm-minimising surfaces; a reducing sphere is not norm-minimising in any useful sense, so the thin-position/sutured argument that resolves the satellite case has no hyperbolic analogue.
- **Geometric methods give the wrong inequality.** Thurston's hyperbolic Dehn filling and the $6$-theorem (Agol, Lackenby) rule out exceptional fillings for slopes of length $> 6$, leaving finitely many slopes — but the surviving slopes are exactly the small-$|n|$ ones the conjecture must handle, and $|n| \le 2g(K)-1$ can be arbitrarily large.
- **Heegaard Floer obstructions are homological, not geometric.** $d$-invariants and changemaker lattices constrain $S^3_n(K) = Y_1 \\# Y_2$ only through $H_1$, $d$, and the Alexander polynomial. For $Y_1 \\# Y_2$ with $Y_2$ a homology sphere, the correction-term obstruction degenerates; L-space knots are precisely where the Floer data is rigid enough to close the argument.
- **No classification of hyperbolic knots by any computable invariant** makes an exhaustive argument impossible; every proof must be structural.

## 6. The Gap

Proven: reducible surgeries are integral, bounded by $2g(K)-1$, produce a lens space summand, and cannot occur on satellite, alternating, symmetric, small-bridge, or L-space knots.

Missing: a single mechanism showing that for a **hyperbolic** knot $K$ and integer $n$ with $2 \le |n| \le 2g(K)-1$, an essential punctured sphere in $E(K)$ with boundary slope $n$ cannot exist. Concretely, the required step is either
1. an a priori bound on the number of punctures $|\partial P|$ of a minimal reducing planar surface, which would make the Gordon–Luecke graph analysis finite; or
2. a Floer- or gauge-theoretic obstruction to $S^3_n(K) \cong L(a,b) \,\\#\, Y$ that does not require $K$ to be an L-space knot — for instance a genus bound forcing $2g(K)-1 < |n|$ directly from $\widehat{HFK}(K)$ in the reducible case.

## 7. Current Research (as of June 2026)

- **Lattice embeddings beyond L-spaces.** Extending Greene's changemaker technology to non-L-space knots using the full $\mathbb{Z}\oplus\mathbb{Z}$-filtered knot Floer complex $CFK^\infty$ rather than just $\widehat{HFK}$ *(frontier — verify)*. Groups at Georgia Tech (Hom), UT Austin, and Princeton are active here.
- **Instanton and $SU(2)$ methods.** Kronheimer–Mrowka-style $SU(2)$ representation obstructions to reducible surgeries; the observation that $\pi_1(S^3_n(K))$ surjects onto a free product $\pi_1(Y_1) * \pi_1(Y_2)$ gives an abundance of irreducible $SU(2)$ representations, potentially contradicting instanton surgery formulas.
- **Refined graph combinatorics.** Continued work on great $x$-cycles and Scharlemann cycles (in the tradition of Hoffman, Matignon, Sayari, Valdez-Sánchez) aiming at bridge-number bounds beyond 3.
- **Computational screening.** Systematic SnapPy/HFK verification that no census hyperbolic knot admits a reducible filling, together with the Berge-style enumeration of lens-space summands *(frontier — verify)*.

## 8. Future Work

- Prove the conjecture for **tunnel number one** or **bridge number four** knots, the natural next combinatorial layer after Hoffman's bridge-number-3 result.
- Prove the strengthened genus bound $|n| \le g(K)$ for reducing slopes, which combined with existing lens-space-summand constraints would sharply restrict candidates.
- Attack the closely related **Cosmetic Surgery** and **Knot Complement**-style rigidity from the same lattice/Floer toolkit; unified progress is plausible since all three concern how much surgery can forget about $K$.
- Settle the analogous statement for knots in arbitrary homology spheres, where counterexamples *do* exist (e.g. in Poincaré sphere settings), to isolate which property of $S^3$ the conjecture really uses.

## 9. Key References

- **[Foundational]** F. González-Acuña, H. Short. *Knot surgery and primeness.* Mathematical Proceedings of the Cambridge Philosophical Society **99** (1986), 89–102.
- **[Foundational]** L. Moser. *Elementary surgery along a torus knot.* Pacific Journal of Mathematics **38** (1971), 737–745.
- **[Foundational]** D. Gabai. *Foliations and the topology of 3-manifolds. II, III.* Journal of Differential Geometry **26** (1987), 461–478 and 479–536.
- **[Foundational]** C. McA. Gordon, J. Luecke. *Only integral Dehn surgeries can yield reducible manifolds.* Math. Proc. Cambridge Philos. Soc. **102** (1987), 97–101.
- **[Key]** M. Scharlemann. *Producing reducible 3-manifolds by surgery on a knot.* Topology **29** (1990), 481–500.
- **[Key]** W. Menasco, M. Thistlethwaite. *Surfaces with boundary in alternating knot exteriors.* Journal für die reine und angewandte Mathematik **426** (1992), 47–65.
- **[Key]** C. McA. Gordon, J. Luecke. *Reducible manifolds and Dehn surgery.* Topology **35** (1996), 385–409.
- **[Key]** C. Hayashi, K. Shimokawa. *Symmetric knots satisfy the cabling conjecture.* Math. Proc. Cambridge Philos. Soc. **123** (1998), 501–529.
- **[Key]** J. Hoffman. *There are no strict great $x$-cycles after a reducing or $P^2$ surgery on a knot.* Journal of Knot Theory and Its Ramifications **7** (1998), 549–569.
- **[SOTA]** D. Matignon, N. Sayari. *Longitudinal slope and Dehn fillings.* Hiroshima Mathematical Journal **33** (2003), 127–136.
- **[SOTA]** J. E. Greene. *L-space surgeries, genus bounds, and the cabling conjecture.* Journal of Differential Geometry **100** (2015), 491–506.
- **[SOTA]** J. Hom, Ç. Karakurt, T. Lidman. *Surgery obstructions and Heegaard Floer homology.* Geometry & Topology **20** (2016), 2219–2251.
- **[Survey]** C. McA. Gordon. *Dehn surgery on knots.* Proceedings of the ICM, Kyoto 1990, Springer, 631–642.
- **[Survey]** S. Boyer. *Dehn surgery on knots.* In *Handbook of Geometric Topology*, Elsevier, 2002, 165–218.

## 10. Worked Example / Concrete Special Case

**The right-handed trefoil $K = T(2,3)$, surgery slope $n = 6$.**

$T(2,3)$ is the $(2,3)$-cable of the unknot $U$, so the conjecture predicts exactly one reducible slope, $r = pq = 2\cdot 3 = 6$. Verify directly.

*Step 1 — the cabling annulus.* Let $V = \nu(U)$ be a solid torus, $K \subset \partial V$ the $(2,3)$-curve. The annulus $A = \partial V \setminus \nu(K)$ has two boundary components on $\partial E(K)$. In the $(\mu,\lambda)$ basis of $K$, $[\partial A] = 6\mu + \lambda$ — the framing induced by $\partial V$ differs from the Seifert framing by $pq = 6$.

*Step 2 — capping off.* Fill along slope $6$. The filling torus contains a meridian disk whose boundary is isotopic to $\partial A$; the two components of $\partial A$ bound disjoint disks in the filling solid torus. Gluing them to $A$ gives an embedded 2-sphere $S$.

*Step 3 — $S$ is essential.* $S$ splits $S^3_6(K)$ into $V$ filled along $\lambda' + \dots$ and the complementary piece. Cutting gives
$$S^3_6(T(2,3)) \;\cong\; L(2,3)\ \\#\ L(3,2) \;\cong\; \mathbb{RP}^3 \ \\#\ L(3,2),$$
matching Moser's formula $S^3_{pq}(T(p,q)) = L(p,q)\\#L(q,p)$ with $p=2$, $q=3$. Neither summand is $S^3$ since $|H_1| = 2$ and $3$ respectively, so $S$ is essential and the surgery is reducible.

*Step 4 — no other reducible slope.* For $p/q \ne 6$, Moser gives
$$S^3_{p/q}(T(2,3)) = \begin{cases} \text{Seifert fibred over } S^2(2,3,|p-6q|), & |p-6q| \ge 1,\\ L(q,\ast) \ (\text{lens space}), & |p-6q| = 0 \text{ excluded},\end{cases}$$
and every small Seifert fibred space with three exceptional fibres is irreducible. So $6$ is the unique reducible slope.

*Step 5 — consistency with the bounds.* $g(T(2,3)) = 1$, so $2g(K)-1 = 1 < 6$: the Matignon–Sayari/Greene bound $|n| \le 2g(K)-1$ is **violated**, which is exactly why the bound must be stated for non-cable knots. This is the sense in which cables are the extremal, and conjecturally the only, examples. For a hypothetical hyperbolic counterexample $K$ with reducible slope $n$, one would need $2 \le |n| \le 2g(K)-1$ and $S^3_n(K) \cong L(a,b)\\#Y$ — no such pair has ever been exhibited.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*