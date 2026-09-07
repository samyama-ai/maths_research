---
id: 04-topology/tunnel-number-additivity-conjecture
title: "Tunnel Number Additivity Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Tunnel Number Additivity Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/tunnel-number-additivity-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

For a knot $K \subset S^3$, the **tunnel number** $t(K)$ is the least number of disjoint properly embedded arcs (tunnels) that must be attached to a regular neighbourhood of $K$ so that the complement of the resulting handlebody is itself a handlebody. The classical conjecture asks whether tunnel number is additive under connected sum:

$$t(K_1 \\# K_2) \;=\; t(K_1) + t(K_2).$$

The upper bound $t(K_1 \\# K_2) \le t(K_1) + t(K_2) + 1$ is elementary. The conjecture's substantive half — **no degeneration**,
$$t(K_1 \\# K_2) \;\ge\; t(K_1) + t(K_2),$$
is **false**: Morimoto (1995) produced counterexamples. What remains open is the quantitative and structural refinement:

1. **(Degeneration ratio)** Define $d(K_1,K_2) = \dfrac{t(K_1)+t(K_2)-t(K_1\\#K_2)}{t(K_1)+t(K_2)}$. What is $\sup d$ over all pairs of knots? Known: $d < 2/5$.
2. **(Structural characterization)** Give a necessary and sufficient condition on $K_1, K_2$ for degeneration to occur. Morimoto's proposed answer (existence of a primitive meridian) is sufficient but not necessary (Kobayashi–Rieck, 2008).
3. **(Super-additivity)** Characterize the pairs with $t(K_1\\#K_2) = t(K_1)+t(K_2)+1$, equivalently the pairs whose exteriors have additive Heegaard genus.

A complete resolution means: a sharp constant in (1), and a checkable topological criterion in (2)–(3).

## 2. Mathematical Foundations

Let $E(K) = S^3 \setminus \mathring{N}(K)$ be the knot exterior, a compact orientable 3-manifold with torus boundary. A **Heegaard splitting** of $E(K)$ is a decomposition
$$E(K) = C_1 \cup_\Sigma C_2,$$
where $C_1$ is a compression body containing $\partial E(K)$, $C_2$ is a handlebody, and $\Sigma = \partial_+ C_1 = \partial C_2$ is the splitting surface. The **Heegaard genus** $g(E(K))$ is the minimum of $g(\Sigma)$. The basic dictionary is

$$\boxed{\,t(K) = g(E(K)) - 1\,}$$

since a system of $t$ tunnels $\tau_1,\dots,\tau_t$ gives $C_1 = N(K) \cup N(\tau_1) \cup \cdots \cup N(\tau_t)$, a genus-$(t+1)$ compression body.

Under connected sum the exteriors amalgamate along an essential annulus $A$ (the **swallow–follow** annulus) with $\partial A$ meridional:
$$E(K_1 \\# K_2) = E(K_1) \cup_A E(K_2).$$
Stacking minimal splittings across $A$ yields
$$g(E(K_1\\#K_2)) \le g(E(K_1)) + g(E(K_2)), \qquad\text{i.e.}\qquad t(K_1\\#K_2) \le t(K_1)+t(K_2)+1 .$$

**Primitive meridian.** $K$ has a *primitive meridian* if $E(K)$ admits a minimal-genus splitting $C_1\cup_\Sigma C_2$ and a spanning annulus $A' \subset C_1$ with one boundary component a meridian of $K$ and the other a curve on $\Sigma$ that is **primitive** in $C_2$ — i.e. $\partial A' \cap \Sigma$ intersects some meridian disc of $C_2$ exactly once. If $K_1$ has a primitive meridian then
$$t(K_1 \\# K_2) \le t(K_1) + t(K_2),$$
and often strictly less: the annulus lets one tunnel of $K_2$ be absorbed.

**Small knots.** $K$ is *small* if $E(K)$ contains no closed essential surface; *$m$-small* if it contains no essential surface with meridional boundary. These hypotheses forbid the thin-position phenomena that drive degeneration.

**Thin position / generalized Heegaard splittings** (Scharlemann–Thompson): a decomposition $M = \bigcup_i (C_i \cup_{\Sigma_i} C_i')$ into blocks separated by thin surfaces $F_j$, with complexity $\sum_i (2g(\Sigma_i)-2)$ minimized. Untelescoping a minimal splitting of $E(K_1\\#K_2)$ and comparing the thin surfaces with the swallow–follow annulus is the engine behind every known lower bound.

## 3. History & State of the Art (SOTA)

- **1982** — Norwood proves every two-generator knot is prime; in particular $t(K)=1 \Rightarrow K$ prime, so $t(K_1\\#K_2)\ge 2$ always. This was the first evidence for additivity.
- **1994** — Kobayashi constructs knots with **arbitrarily large** degeneration: for every $n$ there exist $K_1,K_2$ with $t(K_1)+t(K_2)-t(K_1\\#K_2) \ge n$.
- **1995** — Morimoto publishes explicit prime knots with $t(K_1\\#K_2) < t(K_1)+t(K_2)$, refuting additivity outright.
- **1996** — Morimoto–Sakuma–Yokota give tunnel-number-one knots with $t(K_1 \\# K_2) = 3$: the "$1+1=3$" phenomenon, i.e. strict super-additivity, realizing the upper bound.
- **1999–2001** — Scharlemann–Schultens prove $t(K_1\\#\cdots\\#K_n) \ge n$ (Topology, 1999) and then the linear bounds $t(K_1\\#K_2) \ge \tfrac{2}{5}(t(K_1)+t(K_2))$ (Math. Ann., 2000), improved to $\tfrac{3}{5}$ (Trans. AMS, 2001).
- **2000** — Morimoto–Schultens: tunnel number of **small** knots does not go down under connected sum. Morimoto studies super-additivity systematically.
- **2006–2008** — Kobayashi–Rieck: Heegaard genus is additive for $m$-small knots; growth rate of $t(K^{\\# n})$ analysed; Morimoto's conjecture disproved using high-distance splittings.

## 4. Partial Results / Verified Cases

| Class / regime | Result |
|---|---|
| $t(K)=1$ | $K$ prime (Norwood 1982); hence no degeneration at the bottom of the scale |
| $n$ arbitrary knots | $t(K_1\\#\cdots\\#K_n) \ge n$ (Scharlemann–Schultens 1999) |
| General pairs | $t(K_1\\#K_2) \ge \tfrac{3}{5}\big(t(K_1)+t(K_2)\big)$, so $d < 2/5$ |
| Small knots | $t(K_1\\#K_2) \ge t(K_1)+t(K_2)$ (Morimoto–Schultens 2000) |
| $m$-small knots $K_1,\dots,K_n$ | $g(E(\\#_i K_i)) = \sum_i g(E(K_i))$, i.e. $t = \sum_i t(K_i) + (n-1)$: full super-additivity (Kobayashi–Rieck 2006) |
| 2-bridge knots | $t(K_1\\#\cdots\\#K_n) = n$ exactly (see §10) |
| Knots with a primitive meridian | Degeneration occurs; $t(K_1\\#K_2)\le t(K_1)+t(K_2)$ |
| Torus knots, most Montesinos knots | $t=1$; sums behave as in the 2-bridge computation |
| High-distance splittings | Additive genus even without a primitive meridian (Kobayashi–Rieck 2008) |

## 5. Principal Obstacles

- **Heegaard genus is not a local invariant.** A minimal splitting of $E(K_1\\#K_2)$ need not be isotopic to anything built from splittings of the summands; the swallow–follow annulus can be swept across the splitting surface, destroying any inductive bookkeeping.
- **Thin position loses control at the annulus.** Untelescoping produces thin surfaces, but an essential *annulus* has Euler characteristic $0$, so the complexity function $\sum (2g-2)$ gains nothing when a thin surface is isotoped to meet $A$. This is exactly why the Scharlemann–Schultens constant is a fraction like $2/5$ or $3/5$ rather than $1$ — the counting argument leaks a fixed proportion at each annular interface.
- **No lower-bound invariant beyond genus.** Bridge number is additive (Schubert), but $t(K)\le b(K)-1$ only bounds from above. Knot Floer, Khovanov, and the Alexander polynomial give no useful lower bound for $t$; representation-variety and rank arguments bound tunnel number only in special families.
- **Degeneration is a real, unbounded phenomenon.** Kobayashi's construction shows the defect is not a small correction term, so any proof strategy that assumes near-additivity is doomed; only the *ratio* can be controlled.
- **Distance-based rigidity does not scale.** High Hempel distance forces additivity, but connected sums of high-distance knots produce splittings whose distance drops to $\le 2$ (the annulus is a compressing configuration), so the rigidity is not inherited.

## 6. The Gap

Proven: $\tfrac{3}{5}(t_1+t_2) \le t(K_1\\#K_2) \le t_1+t_2+1$. Realized by examples: the upper end (Morimoto–Sakuma–Yokota) and arbitrarily large absolute defects (Kobayashi). **The gap is the sharp constant** $c^\ast = \inf_{K_1,K_2} \frac{t(K_1\\#K_2)}{t(K_1)+t(K_2)} \in [3/5, 1)$; no construction is known that approaches $3/5$, and no argument pushes the bound above $3/5$.

Structurally, the gap is a *criterion*. Morimoto's conjecture supplied one direction (primitive meridian $\Rightarrow$ degeneration) and was refuted in the converse direction by Kobayashi–Rieck (2008), who built knots with additive Heegaard genus that nonetheless fail the hypotheses in the intended equivalence. What is missing is an invariant of $E(K)$ — finer than genus, coarser than the full splitting complex — that is *provably* additive under amalgamation along a meridional annulus and that recovers $t$.

## 7. Current Research (as of June 2026)

- **Generalized Heegaard splittings and graph-manifold amalgamation.** Continuation of the Scharlemann–Schultens–Thompson programme, aiming to replace the $3/5$ counting with a sharp accounting of annular interfaces. *(frontier — verify)* Attempts to reach constant $2/3$ have circulated as preprints without a complete argument.
- **Distance and topological index.** Bachman's topological index and Hempel distance are used to certify that a given splitting is minimal; groups at UC Davis, Oklahoma, and in Japan (Kobayashi's school) pursue the classification of degenerating pairs via distance-$\ge 3$ hypotheses.
- **Growth rate.** Following Kobayashi–Rieck, the invariant $\mathrm{gr}_t(K) = \lim_n \frac{t(K^{\\#n}) - n\,t(K)}{n}$ is studied as a stable proxy for degeneration; showing $\mathrm{gr}_t(K) > -\tfrac{2}{5}t(K)$ for all $K$ would be equivalent to sharpening the ratio bound.
- **Computational tunnel number.** Regina/SnapPy-based enumeration of small-genus splittings verifies additivity for knots up to modest crossing number; the search space grows too fast for genus $\ge 4$.
- **Tunnel number of links and $\theta$-graphs.** Extending the question to spatial graphs, where the amalgamating surface may be a planar surface rather than an annulus.

## 8. Future Work

- Construct a pair with $d(K_1,K_2) > 1/3$, or prove $d \le 1/3$; either would substantially close the interval.
- Find an additive-under-amalgamation invariant: a candidate is a weighted count of thin surfaces in the Scharlemann–Thompson untelescoping, refined by the JSJ structure of $E(K)$.
- Settle super-additivity for all small (not just $m$-small) knots.
- Determine whether degeneration is detected by the tunnel-number-one *stabilization* behaviour, i.e. whether $t(K_1\\#K_2) < t_1+t_2$ forces an essential meridional surface in one summand.
- Extend the theory to Heegaard genus of manifolds glued along tori/annuli in general — the tunnel-number question is the simplest nontrivial instance.

## 9. Key References

- **[Foundational]** R. Norwood. *Every two-generator knot is prime.* Proceedings of the American Mathematical Society, 86 (1982), 143–147.
- **[Foundational]** K. Morimoto. *There are knots whose tunnel numbers go down under connected sum.* Proceedings of the American Mathematical Society, 123 (1995), 3527–3532.
- **[Foundational]** T. Kobayashi. *A construction of arbitrarily high degeneration of tunnel numbers of knots under connected sum.* Journal of Knot Theory and Its Ramifications, 3 (1994), 179–186.
- **[SOTA]** M. Scharlemann, J. Schultens. *The tunnel number of the sum of $n$ knots is at least $n$.* Topology, 38 (1999), 265–270.
- **[SOTA]** M. Scharlemann, J. Schultens. *Annuli in generalized Heegaard splittings and degeneration of tunnel number.* Mathematische Annalen, 317 (2000), 783–820.
- **[SOTA]** M. Scharlemann, J. Schultens. *Comparing Heegaard and JSJ structures of orientable 3-manifolds.* Transactions of the American Mathematical Society, 353 (2001), 557–584.
- **[SOTA]** K. Morimoto, J. Schultens. *Tunnel numbers of small knots do not go down under connected sum.* Proceedings of the American Mathematical Society, 128 (2000), 269–278.
- **[SOTA]** K. Morimoto. *On the super additivity of tunnel number of knots.* Mathematische Annalen, 317 (2000), 489–508.
- **[SOTA]** K. Morimoto, M. Sakuma, Y. Yokota. *Examples of tunnel number one knots which have the property "1+1=3".* Mathematical Proceedings of the Cambridge Philosophical Society, 119 (1996), 113–118.
- **[Recent]** T. Kobayashi, Y. Rieck. *Heegaard genus of the connected sum of $m$-small knots.* Communications in Analysis and Geometry, 14 (2006), 1037–1077.
- **[Recent]** T. Kobayashi, Y. Rieck. *Knot exteriors with additive Heegaard genus and Morimoto's Conjecture.* Algebraic & Geometric Topology, 8 (2008), 953–969.
- **[Recent]** T. Kobayashi, Y. Rieck. *On the growth rate of the tunnel number of knots.* Journal für die reine und angewandte Mathematik, 592 (2006), 63–78.
- **[Survey]** Y. Moriah. *Heegaard splittings of knot exteriors.* Geometry & Topology Monographs, 12 (2007), 191–232.
- **[Survey]** M. Scharlemann. *Heegaard splittings of compact 3-manifolds.* In: Handbook of Geometric Topology, Elsevier, 2002, 921–953.
- **[Background]** J. Schultens. *Introduction to 3-Manifolds.* Graduate Studies in Mathematics 151, American Mathematical Society, 2014.

## 10. Worked Example / Concrete Special Case

**Claim.** If $K_1,\dots,K_n$ are 2-bridge knots, then $t(K_1\\#\cdots\\#K_n)=n$. So for $n=2$ tunnel number is exactly additive: $1+1=2$, *not* $3$.

*Upper bound.* A 2-bridge knot has bridge number $b(K_i)=2$. Schubert's theorem gives additivity of bridge number,
$$b(K_1\\#\cdots\\#K_n) = \sum_{i=1}^n b(K_i) - (n-1) = 2n - (n-1) = n+1 .$$
For any knot, a bridge presentation with $b$ bridges yields $b-1$ tunnels (join the $b$ bridge arcs by $b-1$ vertical arcs; the union is an unknotted handlebody in the bridge sphere's ball decomposition). Hence
$$t(K_1\\#\cdots\\#K_n) \le b(K_1\\#\cdots\\#K_n) - 1 = n .$$

*Lower bound.* Scharlemann–Schultens (1999): $t(K_1\\#\cdots\\#K_n)\ge n$ for any $n$ nontrivial knots. Combining, $t = n$. $\square$

**Take $n=2$, $K_1=K_2=$ trefoil $3_1$.** Then $t(3_1)=1$ and $t(3_1\\# 3_1)=2$. The elementary upper bound allows $3$; the *additivity* value is $2$; and here the tunnel systems genuinely amalgamate without waste because a 2-bridge knot has a primitive meridian — the annulus $A'$ running from the meridian to the unknotting tunnel meets a meridian disc of the opposite handlebody once. Absorbing $K_2$'s tunnel into that primitive annulus is exactly the "free" gluing that converts the generic bound $t_1+t_2+1=3$ into $2$.

**Contrast.** Morimoto–Sakuma–Yokota exhibit tunnel-number-one knots $K$ (in a family of $(1,1)$-knots with no primitive meridian) for which $t(K\\#K')=3=t(K)+t(K')+1$. So both endpoints $2$ and $3$ are realized by sums of *tunnel-number-one* knots — the invariant $t$ alone cannot predict the outcome. That failure of locality, made quantitative by Kobayashi's arbitrarily large defects and bounded only by the $3/5$ ratio, is precisely the open content of the conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*