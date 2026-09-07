---
id: 04-topology/composite-knot-crossing-number-conjecture
title: "Composite Knot Crossing Number Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Composite Knot Crossing Number Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/composite-knot-crossing-number-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $c(K)$ denote the crossing number of a knot $K \subset S^3$: the minimum number of double points over all regular planar diagrams of $K$. Let $K_1 \\# K_2$ denote the connected sum.

**Conjecture (additivity of crossing number).**
$$c(K_1 \\# K_2) = c(K_1) + c(K_2) \quad \text{for all knots } K_1, K_2 .$$
More generally, $c(K_1 \\# \cdots \\# K_n) = \sum_{i=1}^n c(K_i)$.

The inequality $\le$ is elementary: place minimal diagrams side by side and splice. The open half is
$$c(K_1 \\# K_2) \;\ge\; c(K_1) + c(K_2),$$
i.e. *no* diagram of the composite knot can be cheaper than the naive spliced one. A complete solution is either a proof of this lower bound for all pairs, or an explicit pair $(K_1,K_2)$ with a diagram of $K_1 \\# K_2$ having fewer than $c(K_1)+c(K_2)$ crossings. Even the weakest nontrivial instance is open: it is not known that $c(K \\# 3_1) = c(K)+3$ for every knot $K$, nor even that $c(K \\# K) > c(K)$.

The conjecture is folklore, at least implicit since the 19th-century tabulations of Tait, Kirkman and Little; it appears as Problem 1.67 in Kirby's problem list.

## 2. Mathematical Foundations

**Diagrams.** A diagram $D$ of $K$ is the image of a generic projection $S^3 \setminus \{pt\} \to \mathbb{R}^2$ with over/under data at each transverse double point; $c(D)$ is the number of double points, and
$$c(K) = \min\{\, c(D) : D \text{ a diagram of } K \,\}.$$

**Connected sum.** Given oriented knots $K_1,K_2$, choose a smooth 2-sphere $S \subset S^3$ meeting $K_1 \\# K_2$ transversely in exactly two points; the summands are recovered by capping each side. By the Schubert/Milnor uniqueness theorem the knot monoid $(\mathcal{K}, \\#)$ is free commutative on the prime knots, so the decomposition is well defined.

**Additive companions.** Several invariants *are* additive, which is the source of the conjecture's plausibility:
$$g(K_1\\#K_2)=g(K_1)+g(K_2), \qquad b(K_1\\#K_2)=b(K_1)+b(K_2)-1,$$
for Seifert genus $g$ (Schubert 1949) and bridge number $b$ (Schubert 1954). Not everything is additive: tunnel number can drop, $t(K_1\\#K_2) \le t(K_1)+t(K_2)+1$ with strict subadditivity examples, and unknotting number additivity is itself open.

**Kauffman bracket / Jones bounds.** For the Kauffman bracket $\langle D\rangle$ of a connected diagram with $c$ crossings,
$$\operatorname{span}\langle D\rangle \;\le\; 4c(D) ,$$
with equality iff $D$ is *adequate* (no state circle of the all-$A$ or all-$B$ state touches itself at a crossing). Since $V_K(t)$ is a normalization of $\langle D\rangle$ by $(-A)^{-3w(D)}$ with $t=A^{-4}$,
$$\operatorname{span} V_K \;\le\; c(K),$$
with equality for reduced alternating (Kauffman–Murasugi–Thistlethwaite, 1987) and more generally for adequate knots (Lickorish–Thistlethwaite, 1988). Multiplicativity $V_{K_1\\#K_2}=V_{K_1}\cdot V_{K_2}$ and additivity of span for Laurent polynomials give the additive lower bound whenever both summands are span-sharp.

**Geometric bound (Lackenby).** Using thin position and normal-surface/ Dehn-surgery arguments on the composite sphere,
$$c(K_1 \\# \cdots \\# K_n) \;\ge\; \frac{1}{152}\sum_{i=1}^{n} c(K_i).$$

## 3. History & State of the Art (SOTA)

- **1870s–1900s.** Tait, Kirkman and Little tabulate knots assuming, without proof, that minimal diagrams behave additively and that reduced alternating diagrams are minimal (the "Tait conjectures").
- **1949–1954.** Schubert proves unique prime decomposition, additivity of genus, and additivity of bridge number $-1$, establishing the template the crossing conjecture is modeled on.
- **1987.** Kauffman, Murasugi and Thistlethwaite independently prove, via the Jones polynomial, that a reduced alternating diagram is minimal, so $c(K)=\operatorname{span}V_K$ for alternating $K$. Additivity for alternating summands follows immediately.
- **1988.** Lickorish–Thistlethwaite extend span-sharpness to adequate (in particular semi-adequate, and all Montesinos/pretzel adequate) knots.
- **2003–2004.** Gruber, and independently Diao, establish additivity for connected sums of torus knots by combinatorial/braid-index arguments.
- **2009.** Lackenby, *The crossing number of composite knots*, proves the first universal linear lower bound with constant $1/152$, valid for arbitrarily many summands.
- **2014.** Lackenby, *The crossing number of satellite knots*, proves $c(\text{satellite}) \ge c(\text{companion})/10^{13}$ — the composite case is the degenerate satellite case, and the machinery (thin position for the composite sphere, sweep-outs, parallel-surface counting) is the same.
- **2018–2020.** Malyutin shows that additivity of crossing number is *incompatible* with the widely believed statement that hyperbolic knots are generic among all knots in the natural crossing-number counting — so the conjecture has nontrivial consequences for knot census asymptotics.

**Status:** open in general; proven for large, natural classes; only a constant-factor lower bound universally.

## 4. Partial Results / Verified Cases

- **Alternating summands.** If $K_1,\dots,K_n$ are alternating, $c(\\# K_i)=\sum c(K_i)$ (Kauffman–Murasugi–Thistlethwaite 1987). The composite of alternating knots is alternating, and Menasco's theorem identifies the composite sphere in the diagram.
- **Adequate summands.** Same conclusion for adequate knots (Lickorish–Thistlethwaite 1988), since a connected sum of adequate diagrams is adequate and $\operatorname{span}\langle\cdot\rangle$ adds.
- **Torus knots.** Additivity for connected sums of torus knots (Diao 2004; Gruber 2003). E.g. $c(T_{3,4}\\#T_{3,5})=8+10=18$.
- **Mixed adequate/arbitrary.** If $K_1$ is adequate and $K_2$ arbitrary, combining span-sharpness with Lackenby's bound gives $c(K_1\\#K_2)\ge c(K_1)+c(K_2)/152$ — the "full price" is paid for the adequate summand.
- **Universal constant.** $c(K_1\\#\cdots\\#K_n)\ge \frac{1}{152}\sum c(K_i)$ for all knots and all $n$ (Lackenby 2009).
- **Small-crossing verification.** Prime knots are tabulated to 19 crossings (Burton, *The next 350 million knots*, 2020; Hoste–Thistlethwaite–Weeks to 16). Every composite knot whose summands have total crossing number $\le 19$ is a connected sum of knots which are alternating, adequate, or torus knots except for a short explicit list; for those, additivity is confirmed by direct invariant computation (Jones span, HOMFLY breadth, braid index). No counterexample exists in any tabulated range.
- **Positive braids.** Crossing number is additive for connected sums of positive braid closures, since $c$ equals $b + s - 1$-type expressions computable from the HOMFLY breadth (Bennequin/Morton–Franks–Williams sharpness for positive braids).

## 5. Principal Obstacles

- **Crossing number is not a complement invariant with additive structure.** $g$ and $b$ are minima of geometric complexity over surfaces/positions that can be cut along the composite sphere; a minimal *diagram* has no known normal form compatible with that sphere. Cutting a diagram along a composite sphere gives two diagrams, but the sphere may intersect the projection plane in a complicated curve, so the crossings need not split.
- **Polynomial bounds are not sharp off adequate knots.** $\operatorname{span}V_K \le c(K)$ is the only general polynomial lower bound of the right order, and the deficit $c(K)-\operatorname{span}V_K$ is unbounded (e.g. non-alternating knots with trivial Jones polynomial candidates, and Kanenobu-type families). Multiplicativity of $V$ therefore transmits additivity only where the bound is already tight.
- **No lower bound of the correct linear order.** All universal lower bounds ($1/152$, or $10^{-13}$ in the satellite setting) come from counting parallel copies of an essential surface against a sweep-out; the counting loses a large constant with no known route to $1$.
- **Hyperbolic geometry is uncooperative.** Volume is *additive*-like under connected sum ($\mathrm{vol}$ of the hyperbolic pieces adds), but the comparison $\mathrm{vol}(S^3\setminus K)\le v_8 (c(K)-5)$ (Lackenby–Agol–Thurston) runs the wrong way; there is no lower bound of volume by crossing number, since volume is bounded on families with $c\to\infty$ (twisted torus knots, satellites).
- **Machine search is exponentially bounded.** Deciding $c(K)\le n$ is not known to be in NP with a small certificate; exhaustive diagram search is doubly exponential, and Reidemeister moves may require crossing increases (no monotone simplification), so counterexample hunts cannot be exhaustive beyond ~20 crossings.

## 6. The Gap

Proven: additivity when both summands lie in a class where a *diagrammatic* invariant certifies minimality (adequate, torus, positive braid) — i.e. where a computable lower bound $L(K)$ satisfies $L(K)=c(K)$ *and* $L(K_1\\#K_2)\ge L(K_1)+L(K_2)$.

Wanted: the same for arbitrary summands. The precise missing step is a **sharp additive lower bound**: an invariant $L$ with $L \le c$ universally, $L$ additive under $\\#$, and $L$ within $o(c)$ of $c$. Equivalently, one must upgrade Lackenby's constant from $1/152$ to $1$. Every known proof of the constant-factor bound counts intersections of the composite sphere with a sweep-out of a diagram-induced handle structure, and each of the several "wasteful" steps (Euler-characteristic bookkeeping, normalization of the thin position, discarding non-essential product regions) costs a multiplicative factor. Closing the gap requires either a loss-free version of this counting, or an entirely new certificate of diagram minimality valid for non-adequate knots.

## 7. Current Research (as of June 2026)

- **Improving Lackenby's constant.** Refinements of the thin-position/normal-surface argument aiming to replace $1/152$ by a small explicit fraction such as $1/5$ or $1/2$ have circulated in preprint form *(frontier — verify)*. No published proof of a constant near $1$ exists.
- **Khovanov-homological width bounds.** Groups at Warwick, Bonn and Regensburg study whether homological width or $sl_N$-homology support gives an additive-and-sharper substitute for $\operatorname{span}V$; Khovanov homology of a connected sum is a tensor product over the base ring, so additivity of any width-type invariant is automatic — the open half is sharpness against $c$ *(frontier — verify)*.
- **Census asymptotics.** Following Malyutin, work on whether hyperbolic knots are generic by crossing number is now understood as constraining additivity: a proof of genericity would disprove additivity for *some* pair. This raises the possibility that the conjecture is false, contrary to classical expectation.
- **Machine-assisted search.** Reinforcement-learning and SAT/ILP diagram-simplification pipelines (Burton's *Regina*, knot-tabulation groups at Monash and Sydney) test composite diagrams of tabulated summands up to ~24 crossings for cheaper representatives; nothing sub-additive found *(frontier — verify)*.

## 8. Future Work

- Prove additivity for **all semi-adequate knots**, or for a class defined by Turaev-genus zero/one, extending the state-surface method beyond adequacy.
- Prove the special case $c(K\\#K)=2c(K)$, where the extra symmetry of the composite sphere might be exploited.
- Find a *sharp* additive lower bound from the Kauffman state surface: the Turaev surface gives $c(K)\ge$ genus-corrected span bounds; making the correction term additive is a concrete target.
- Establish or refute genericity of hyperbolic knots, which by Malyutin's dichotomy resolves part of the landscape either way.
- Determine the complexity of computing $c(K)$; an NP-certificate for minimality would make computational refutation feasible at 25–30 crossings.

## 9. Key References

- **[Foundational]** H. Schubert. *Über eine numerische Knoteninvariante.* Mathematische Zeitschrift 61, 245–288, 1954.
- **[Foundational]** L. H. Kauffman. *State models and the Jones polynomial.* Topology 26(3), 395–407, 1987.
- **[Foundational]** K. Murasugi. *Jones polynomials and classical conjectures in knot theory.* Topology 26(2), 187–194, 1987.
- **[Foundational]** M. B. Thistlethwaite. *A spanning-tree expansion of the Jones polynomial.* Topology 26(3), 297–309, 1987.
- **[Foundational]** W. Menasco. *Closed incompressible surfaces in alternating knot and link complements.* Topology 23(1), 37–44, 1984.
- **[Key partial result]** W. B. R. Lickorish, M. B. Thistlethwaite. *Some links with non-trivial polynomials and their crossing-numbers.* Commentarii Mathematici Helvetici 63, 527–539, 1988.
- **[Key partial result]** Y. Diao. *The additivity of crossing numbers.* Journal of Knot Theory and Its Ramifications 13(7), 857–866, 2004.
- **[Key partial result]** H. Gruber. *Estimates for the minimal crossing number.* Preprint, arXiv:math/0303273, 2003.
- **[SOTA]** M. Lackenby. *The crossing number of composite knots.* Journal of Topology 2(4), 747–768, 2009.
- **[SOTA]** M. Lackenby. *The crossing number of satellite knots.* Algebraic & Geometric Topology 14(4), 2379–2409, 2014.
- **[SOTA]** A. V. Malyutin. *On the question of genericity of hyperbolic knots.* International Mathematics Research Notices, 2020.
- **[Computational]** B. A. Burton. *The next 350 million knots.* Proceedings of the 36th International Symposium on Computational Geometry (SoCG), 2020.
- **[Survey]** C. C. Adams. *The Knot Book.* American Mathematical Society, 2004.
- **[Survey]** P. Cromwell. *Knots and Links.* Cambridge University Press, 2004.
- **[Problem list]** R. Kirby (ed.). *Problems in Low-Dimensional Topology.* AMS/IP Studies in Advanced Mathematics 2.2, 1997 (Problem 1.67).

## 10. Worked Example / Concrete Special Case

**Claim.** For the square knot $SK = 3_1 \\# \overline{3_1}$ (trefoil connect-sum its mirror), $c(SK)=6$.

*Upper bound.* Splicing two 3-crossing trefoil diagrams gives a 6-crossing diagram, so $c(SK)\le 6$.

*Lower bound via the Jones polynomial.* The right-handed trefoil has
$$V_{3_1}(t) = -t^{-4} + t^{-3} + t^{-1},$$
so $\operatorname{span}V_{3_1} = (-1) - (-4) = 3$. Its mirror satisfies $V_{\overline{3_1}}(t)=V_{3_1}(t^{-1}) = -t^{4}+t^{3}+t$, again of span $3$. Multiplicativity under connected sum gives
$$V_{SK}(t) = \left(-t^{-4}+t^{-3}+t^{-1}\right)\left(-t^{4}+t^{3}+t\right).$$
Top term: $(-t^{-1})\cdot$ nothing cancels — the extreme monomials are $(-t^{-4})(t)= -t^{-3}$ at the bottom and $(t^{-1})(-t^{4}) = -t^{3}$ at the top, and since the extreme coefficients of a product of Laurent polynomials are the products of the extreme coefficients (no cancellation possible), 
$$\operatorname{span}V_{SK} = 3+3 = 6 .$$
Applying $\operatorname{span}V_K \le c(K)$ yields $c(SK)\ge 6$. Hence $c(SK)=6=c(3_1)+c(\overline{3_1})$. The same computation gives $c(3_1\\#3_1)=6$ for the granny knot.

**Where the argument dies.** The step $\operatorname{span}V_K \le c(K)$ was used as an *equality* for each summand — legitimate only because trefoils are alternating. Take instead $K_1 = K_2 = 8_{19}=T_{3,4}$, a non-alternating knot with $c=8$ but $\operatorname{span}V_{8_{19}} = 5$. The Jones argument only delivers $c(8_{19}\\#8_{19}) \ge 10$, four short of the conjectured $16$. Additivity here is nonetheless known — but by the torus-knot argument of Diao/Gruber, not by any polynomial span. Replace one summand by a knot that is neither alternating, adequate, nor a torus knot (e.g. a suitable Kinoshita–Terasaka or twisted-torus knot) and the best available statement collapses to Lackenby's $c(K_1 \\# K_2)\ge (c(K_1)+c(K_2))/152$ — which for two 8-crossing summands asserts only $c \ge 1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*