---
id: 04-topology/bridge-number-additivity
title: "Bridge Number Additivity under Connected Sum"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bridge Number Additivity under Connected Sum

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/bridge-number-additivity` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

For a knot $K \subset S^3$, let $b(K)$ denote its **bridge number**: the minimum, over all embeddings of $K$ isotopic to it that are in Morse position with respect to a height function $h: S^3 \setminus \{\pm\infty\} \to \mathbb{R}$, of the number of local maxima of $h|_K$.

**Schubert's additivity theorem.** For all knots $K_1, K_2 \subset S^3$,
$$b(K_1 \\# K_2) \;=\; b(K_1) + b(K_2) - 1 .$$
Equivalently, the **reduced bridge number** $\bar b(K) := b(K) - 1$ is a monoid homomorphism from the connected-sum monoid of knots to $(\mathbb{Z}_{\ge 0}, +)$.

The inequality $\le$ is elementary (stack the two bridge presentations and merge one maximum). The content is the lower bound $b(K_1 \\# K_2) \ge b(K_1) + b(K_2) - 1$: no bridge presentation of a composite knot can be more efficient than the "obvious" one built from presentations of its factors.

The classical case is settled. The page is catalogued as *solved-recently* because the modern, fully verified proofs are recent (Schultens 2003; Taylor–Tomova 2018), and because the natural generalizations — higher-genus bridge numbers $b_g$, bridge spectra, knots in arbitrary 3-manifolds, spatial graphs — are only partly resolved and remain the live open problem. What counts as a resolution of the general problem: a proof or counterexample for additivity of $b_g$ for every $g \ge 1$, and an identification of exactly which "complexity" invariants of knots in 3-manifolds are additive under connected sum.

## 2. Mathematical Foundations

**Bridge position.** Let $\Sigma \subset S^3$ be a sphere separating $S^3$ into balls $B_+, B_-$. A knot $K$ is in **$n$-bridge position** with respect to $\Sigma$ if $K$ intersects $\Sigma$ transversally in $2n$ points and $K \cap B_\pm$ is a collection of $n$ arcs simultaneously isotopic, rel endpoints, into $\Sigma$ (a **trivial tangle**). Then
$$b(K) = \min\{\, n : K \text{ admits an } n\text{-bridge position} \,\}.$$
$\Sigma$ is a **bridge sphere** for $K$.

**Basic facts.**
- $b(K) = 1 \iff K$ is the unknot.
- $b(K) \le c(K)$ where $c$ is crossing number; $b(K) \le \frac{1}{2}(c(K)+1)$ for alternating knots is not generally sharp, but $b(K) - 1$ is bounded by the number of Seifert-type "levels".
- $b(K) \ge \mathrm{br}(K)$-type lower bounds come from the meridional rank and from the bridge distance.
- **Torus knots:** $b(T_{p,q}) = \min(p,q)$ (Schubert 1954; modern proof by Schultens 2007).

**Connected sum.** Given oriented knots $K_1, K_2$, choose a sphere $S$ meeting $K_1 \\# K_2$ transversally in exactly $2$ points; $S$ is a **decomposing sphere**, and the pair $(S^3, K_1\\#K_2)$ is recovered by summing $(S^3,K_1)$ and $(S^3,K_2)$ along $S$. A knot is **prime** if every such sphere is trivial.

**Thin position and width.** For $K$ in Morse position with critical values $c_1 < \dots < c_m$ and regular values $r_i \in (c_i, c_{i+1})$, the **width** is
$$w(K) = \min \sum_{i=1}^{m-1} \big| K \cap h^{-1}(r_i) \big|,$$
the minimum taken over isotopy classes of Morse embeddings (Gabai 1987). Bridge position is the special case where all maxima precede all minima; $w(K) \ge 2b(K)^2 - \text{(correction)}$ in general, and $w(K) = 2b(K)^2$ when $K$ is in bridge position with $b$ bridges.

**Higher-genus bridge number.** Let $\Sigma_g \subset S^3$ be a genus-$g$ Heegaard surface. $b_g(K)$ is the minimum number of arcs in each handlebody, all trivial (boundary-parallel into $\Sigma_g$). The sequence
$$\mathbf{b}(K) = \big(b_0(K), b_1(K), b_2(K), \dots\big)$$
is the **bridge spectrum**; it is strictly decreasing until it reaches $0$ at $g = g(K)$, the Heegaard genus of the knot exterior plus one. Doll (1992) set up this theory for links in arbitrary closed orientable 3-manifolds.

**Net extent (Taylor–Tomova).** For a $(3\text{-manifold},\text{graph})$ pair $(M,T)$ with a multiple bridge surface $\mathcal{H}$, the **net extent** is
$$\mathrm{netext}(M,T) = \sum_{H \in \mathcal{H}} \Big( \tfrac{1}{2}|H \cap T| - \chi(H) \Big)^{\pm},$$
suitably signed over thick and thin surfaces. Its minimum over all multiple bridge surfaces is an invariant, and for $K \subset S^3$ one has $\mathrm{netext}(S^3,K) = 2\big(b(K) - 1\big)$.

## 3. History & State of the Art (SOTA)

- **1954.** Horst Schubert introduces the bridge number ("Brückenzahl") in *Über eine numerische Knoteninvariante* (Math. Z. 61) and proves both additivity under connected sum and the satellite inequality $b(K) \ge n \cdot b(C)$ for a satellite $K$ with companion $C$ and winding number $n$. The proof is a long, delicate cut-and-paste argument on normal surfaces; it was widely regarded as correct but very hard to check.
- **1987.** Gabai introduces thin position for knots, giving a new combinatorial framework for minimizing intersections with level spheres.
- **1992.** Doll defines $b_g$ and bridge spectra for links in 3-manifolds and asks about their behaviour under connected sum.
- **1995–2000.** Morimoto shows tunnel number can *drop* under connected sum ($t(K_1\\#K_2) < t(K_1)+t(K_2)$); Scharlemann–Schultens quantify the degeneration. This makes clear that additivity is not automatic for Heegaard-type complexity.
- **2003.** Jennifer Schultens gives a short, modern, fully verifiable proof of Schubert's additivity theorem using thin position and the theory of essential meridional planar surfaces. This is the standard reference today.
- **2013.** Blair–Tomova prove that Gabai width is **not** additive, correcting the expectation that all such complexity measures behave like $b$.
- **2018.** Taylor–Tomova construct net extent and related invariants, proving additivity under connected sum for knots, links and spatial graphs in arbitrary compact orientable 3-manifolds — recovering Schubert's theorem as a corollary and extending it far beyond $S^3$.

## 4. Partial Results / Verified Cases

- **$g = 0$, knots in $S^3$: fully proved.** Schubert (1954), Schultens (2003), and Taylor–Tomova (2018) give three independent proofs of $b(K_1\\#K_2) = b(K_1)+b(K_2)-1$.
- **Links in $S^3$.** Additivity extends to connected sums of links along a component, with the same $-1$ correction.
- **Knots in arbitrary compact orientable 3-manifolds.** Net extent is additive under connected sum of pairs $(M_1,T_1)\\#(M_2,T_2)$ (Taylor–Tomova 2018); for $M_i = S^3$ this specializes to bridge number.
- **Spatial graphs.** The Taylor–Tomova invariants are additive for connected sums of graphs in 3-manifolds, where no analogue of Schubert's original argument was known.
- **Torus knots and iterated torus knots.** $b(T_{p,q}) = \min(p,q)$; Zupan (2014) computes the full bridge spectrum $\mathbf{b}$ for iterated torus knots, giving explicit values of $b_g$ for $g \ge 1$ against which additivity can be tested.
- **$2$-bridge knots.** Since $2$-bridge knots are prime, $b(K)=2$ forces $K$ prime — the smallest nontrivial instance of the theorem, and a case provable by elementary means (Schubert's classification of $2$-bridge knots).
- **Negative companion result.** $b_g$ is *sub*additive in the sense $b_{g_1+g_2}(K_1\\#K_2) \le b_{g_1}(K_1)+b_{g_2}(K_2)-1$ (Doll 1992); equality is known only in scattered families.

## 5. Principal Obstacles

- **Bridge surfaces are not unique.** A knot may admit many non-isotopic minimal bridge spheres, so one cannot simply "choose the right one" and cut. Uniqueness is known only in restricted settings (e.g. Scharlemann–Tomova for $2$-bridge knots).
- **The decomposing sphere is uncontrolled.** The essential step is to isotope the decomposing sphere $S$ so that $S \cap \Sigma$ is a single circle. Innermost-disk arguments produce new intersections as fast as they remove them; Schubert handled this by a normal-surface bookkeeping that is hard to audit, and Schultens replaced it with thin position of the *pair* $(K, S)$.
- **Thin position is not connected-sum compatible.** Blair–Tomova's counterexamples show width degenerates: a thin presentation of $K_1\\#K_2$ need not restrict to thin presentations of the factors. So thin position alone cannot prove additivity — it must be combined with an argument that essential meridional surfaces survive thinning.
- **Higher genus destroys the "trivial tangle" rigidity.** For $g \ge 1$, arcs can be trivial in a handlebody in ways that interact with the handles; compression bodies admit annuli that block the innermost-disk induction. This is exactly the mechanism behind Morimoto's tunnel number degeneration, and it is why $b_g$ additivity resists the $g=0$ proofs.
- **No homological or gauge-theoretic lower bound.** Bridge number has no known Floer-theoretic or Khovanov-theoretic lower bound sharp enough to force additivity; the meridional rank (Cappell–Shaneson) conjecture would give one but is itself open, and known counterexamples in the graph setting warn against optimism.

## 6. The Gap

Proven: $b = b_0$ is additive-with-$-1$ for knots, links and graphs in any compact orientable 3-manifold, via net extent.

Not proven: whether
$$b_{g_1+g_2}(K_1 \\# K_2) \;=\; \min_{\substack{h_1+h_2 = g_1+g_2}} \big( b_{h_1}(K_1) + b_{h_2}(K_2) \big) - 1$$
holds for $g_1+g_2 \ge 1$, i.e. whether the whole bridge spectrum is determined by the spectra of the factors. The exact barrier: the net-extent machinery assigns *positive* weight $\frac12|H\cap T| - \chi(H)$ to thick surfaces, and this weight is additive only when the summand surfaces are spheres. For $\chi(H) < 0$ the same sum can be realized by a genus-$g$ surface intersecting $T$ in fewer points, so a genuinely new bridge surface for $K_1\\#K_2$ may exist that is not built from bridge surfaces of the factors. Ruling out such a "hidden" surface — or constructing one — is the step to be crossed.

## 7. Current Research (as of June 2026)

- **Taylor–Tomova school (Colby College / Univ. of Iowa).** Extending the additive-invariant framework — net extent, width for graphs, multiple bridge surfaces — to knotted graphs, tangles, and knots in non-prime manifolds.
- **Zupan and collaborators (Univ. of Nebraska–Lincoln).** Bridge spectra, bridge trisections of surfaces in $4$-manifolds, and the analogous additivity question for the **bridge trisection number** of knotted surfaces; the $4$-dimensional analogue $b(\mathcal{S}_1 \\# \mathcal{S}_2) = b(\mathcal{S}_1)+b(\mathcal{S}_2)-1$ is an active target *(frontier — verify)*.
- **Blair, Campisi, and coauthors.** Bridge distance and its interaction with connected sum; high-distance bridge surfaces force uniqueness, which yields additivity in a bounded range of $g$ *(frontier — verify)*.
- **Meridional rank programme.** Renewed activity on the Cappell–Shaneson conjecture ($\text{meridional rank} = b$) for arborescent, twisted torus, and iterated cable knots; a positive answer for a class immediately gives additivity there by Grushko-type rank additivity.
- **Computational.** Bridge numbers for knots up to 16 crossings are tabulated in KnotInfo, providing exhaustive verification of the additive formula on all composites of tabulated primes within that range.

## 8. Future Work

1. **Decide $b_1$ additivity.** Either prove $b_1(K_1\\#K_2) = \min\{b_1(K_1)+b_0(K_2),\, b_0(K_1)+b_1(K_2)\} - 1$ or produce a counterexample, likely among Morimoto-style knots where tunnel number already degenerates.
2. **Axiomatize additivity.** Characterize which functions of a multiple bridge surface yield additive invariants; Taylor–Tomova's weight $\frac12|H\cap T|-\chi(H)$ should be one point in a family.
3. **Four-dimensional analogue.** Settle additivity of the bridge trisection number for connected sums of knotted surfaces in $S^4$.
4. **Sharpen the satellite inequality.** Determine when $b(K) = n\,b(C)$ holds with equality for satellites, which would combine with additivity into a full "multiplicativity" package.
5. **Lower bounds from Floer theory.** Find a knot-homology invariant that bounds $b$ from below and is additive by construction.

## 9. Key References

- **[Foundational]** Horst Schubert. *Über eine numerische Knoteninvariante.* Mathematische Zeitschrift 61 (1954), 245–288.
- **[Foundational]** Horst Schubert. *Die eindeutige Zerlegbarkeit eines Knotens in Primknoten.* Sitzungsberichte der Heidelberger Akademie der Wissenschaften, Math.-Nat. Kl. (1949), 57–104.
- **[Foundational]** David Gabai. *Foliations and the topology of 3-manifolds III.* Journal of Differential Geometry 26 (1987), 479–536.
- **[Key proof]** Jennifer Schultens. *Additivity of bridge numbers of knots.* Mathematical Proceedings of the Cambridge Philosophical Society 135 (2003), 539–544.
- **[SOTA / Recent]** Scott A. Taylor and Maggy Tomova. *Additive invariants for knots, links and graphs in 3-manifolds.* Geometry & Topology 22 (2018), 3235–3286.
- **[SOTA / Recent]** Ryan Blair and Maggy Tomova. *Width is not additive.* Geometry & Topology 17 (2013), 93–156.
- **[Structural]** Helmut Doll. *A generalized bridge number for links in 3-manifolds.* Mathematische Annalen 294 (1992), 701–717.
- **[Structural]** Kanji Morimoto. *There are knots whose tunnel numbers go down under connected sum.* Proceedings of the American Mathematical Society 123 (1995), 3527–3532.
- **[Structural]** Martin Scharlemann and Jennifer Schultens. *Annuli in generalized Heegaard splittings and degeneration of tunnel number.* Mathematische Annalen 317 (2000), 783–820.
- **[Computation]** Alexander Zupan. *Bridge spectra of iterated torus knots.* Communications in Analysis and Geometry 22 (2014), 931–963.
- **[Related]** Jennifer Schultens. *Bridge numbers of torus knots.* Mathematical Proceedings of the Cambridge Philosophical Society 143 (2007), 621–625.
- **[Survey / Textbook]** Peter Cromwell. *Knots and Links.* Cambridge University Press, 2004.
- **[Survey / Textbook]** Jennifer Schultens. *Introduction to 3-Manifolds.* Graduate Studies in Mathematics 151, American Mathematical Society, 2014.

## 10. Worked Example / Concrete Special Case

**Claim.** The square knot $K = 3_1 \\# \overline{3_1}$ (trefoil summed with its mirror) has $b(K) = 3$.

*Upper bound.* The trefoil $3_1$ is a $2$-bridge knot: $b(3_1) = 2$, realized by a bridge sphere $\Sigma_1$ meeting it in $4$ points, with $2$ trivial arcs above and $2$ below. Same for $\overline{3_1}$ with sphere $\Sigma_2$. Stack the two presentations vertically. Cutting one bridge of the lower copy and one bridge of the upper copy and splicing gives a Morse embedding with $2 + 2 - 1 = 3$ maxima. Hence
$$b(3_1 \\# \overline{3_1}) \le b(3_1) + b(\overline{3_1}) - 1 = 3 .$$

*Lower bound, elementarily.* Suppose $b(K) \le 2$. Since $K \ne$ unknot, $b(K) = 2$, so $K$ is a $2$-bridge knot. By Schubert's classification, every $2$-bridge knot is the double branched cover data of a lens space $L(p,q)$ with $p$ odd, and $2$-bridge knots are **prime**: the double branched cover of $S^3$ over a $2$-bridge knot is a lens space, which is irreducible, whereas the double branched cover over a composite knot contains an essential $2$-sphere (the lift of the decomposing sphere) and is therefore reducible — a connected sum of two lens spaces. For the square knot the double branched cover is $L(3,1) \\# L(3,2)$, reducible. Contradiction. Hence $b(K) \ge 3$, and $b(K) = 3$.

*Where the general argument is harder.* The above uses the classification of $2$-bridge knots, available only at $n = 2$. For $b(K_1)=b(K_2)=3$ one must rule out $b(K_1\\#K_2) \le 4$ with no classification to hand. Schultens' proof instead argues: put $K_1\\#K_2$ in a minimal bridge position with sphere $\Sigma$, take a decomposing sphere $S$ realizing the connected sum, and isotope $S$ to minimize $|S \cap \Sigma|$ together with the number of critical points of $h|_S$. A thin-position/innermost-disk analysis shows the minimum is achieved when $S \cap \Sigma$ is a single circle and $S$ has exactly two critical points. Then $\Sigma$ cuts along $S$ into bridge spheres $\Sigma_i$ for $K_i$, with
$$\tfrac12|\Sigma \cap K| \;=\; \tfrac12|\Sigma_1 \cap K_1| + \tfrac12|\Sigma_2 \cap K_2| - 1 \;\ge\; b(K_1) + b(K_2) - 1 .$$

*The net-extent bookkeeping.* In Taylor–Tomova's language, $\mathrm{netext}(S^3,K) = 2(b(K)-1)$, so the square knot has net extent $4 = 2 + 2$, matching $\mathrm{netext}(S^3,3_1) = 2$ for each trefoil summand. Additivity of net extent under connected sum is the statement being verified, and this instance is its smallest nontrivial check.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*