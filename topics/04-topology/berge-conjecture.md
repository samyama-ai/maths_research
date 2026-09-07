---
id: 04-topology/berge-conjecture
title: "Berge Conjecture"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Berge Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/berge-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

**Conjecture (Berge, c. 1990).** Let $K \subset S^3$ be a knot and suppose some Dehn surgery on $K$ yields a lens space. Then $K$ is a *doubly primitive* knot (a **Berge knot**), and the surgery slope is the surface slope induced by the genus-2 Heegaard surface witnessing double primitivity.

Equivalently: Berge's twelve families I–XII exhaust all knots in $S^3$ with a lens space surgery.

A complete resolution requires either (a) a proof that every knot with a lens space surgery lies on a genus-2 Heegaard surface of $S^3$ as a doubly primitive curve, or (b) an explicit knot $K$ and slope $p$ with $S^3_p(K)$ a lens space and $K$ not in Berge's list. Conventions: lens spaces include $S^3$ and $\mathbb{RP}^3$ but exclude $S^1\times S^2$ (whose only surgery realization is the unknot, by Gabai's Property R theorem). By the Cyclic Surgery Theorem the slope may be assumed to be an integer $p$ once $K$ is not a torus knot.

## 2. Mathematical Foundations

**Dehn surgery.** For $K\subset S^3$ with tubular neighborhood $N(K)$, meridian $\mu$ and Seifert-framed longitude $\lambda$, and coprime $p,q$,
$$S^3_{p/q}(K) \;=\; \bigl(S^3 \setminus \mathring{N}(K)\bigr) \cup_{\varphi} \bigl(S^1\times D^2\bigr), \qquad \varphi\bigl(\partial D^2\bigr) \simeq p\mu + q\lambda .$$
Then $H_1(S^3_{p/q}(K);\mathbb{Z}) \cong \mathbb{Z}/p\mathbb{Z}$.

**Lens space.** For $\gcd(p,q)=1$, $p>0$,
$$L(p,q) \;=\; S^3/\!\sim, \qquad (z_1,z_2)\sim(\zeta z_1,\ \zeta^{q} z_2),\quad \zeta = e^{2\pi i/p},$$
a genus-1 Heegaard-splitting manifold. $L(p,q)\cong L(p',q')$ iff $p=p'$ and $q'\equiv q^{\pm1} \pmod p$ or $q'\equiv -q^{\pm1}\pmod p$.

**Doubly primitive.** $K\subset S^3$ is doubly primitive if there is a genus-2 Heegaard splitting $S^3 = H_1 \cup_\Sigma H_2$ with $K\subset \Sigma$ and $[K]$ generating $\pi_1(H_i) \cong F_2$ up to conjugacy for $i=1,2$ — i.e. $K$ is part of a free basis in each handlebody. Then attaching a 2-handle along $K$ with the *surface slope* $\gamma = [\Sigma\cap\partial N(K)]$ turns each $H_i$ into a solid torus, so $S^3_\gamma(K)$ is a lens space. Berge's insight is that $\gamma$ is an integer $p$ and the construction is essentially the only known source of examples.

**Dual/simple knots.** The core of the surgery solid torus is a knot $K^* \subset L(p,q)$ lying on the genus-1 Heegaard torus; such *simple* (or *grid number one*) knots are classified by their homology class $[K^*]\in H_1(L(p,q))\cong \mathbb{Z}/p$. Berge's list is most compactly described by which classes $k$ mod $p$ admit an $S^3$ dual.

**Heegaard Floer constraints.** $Y$ is an *L-space* if $\operatorname{rk}\widehat{HF}(Y) = |H_1(Y;\mathbb{Z})|$; lens spaces are L-spaces. If $S^3_p(K)$ is an L-space with $p>0$ then (Ozsváth–Szabó)
$$\Delta_K(t) \;=\; (-1)^{n} + \sum_{j=1}^{n}(-1)^{n-j}\bigl(t^{a_j}+t^{-a_j}\bigr), \qquad a_1 > a_2 > \cdots > a_n > 0,$$
so all nonzero coefficients are $\pm1$ and alternate; moreover $K$ is fibered (Ghiggini, Ni) and $\widehat{HFK}(K,i)\in\{0,\mathbb{Z}\}$ for all $i$.

**Genus bounds.** If $S^3_p(K)$ is a lens space and $K$ is nontrivial, then
$$2g(K)-1 \;\le\; p \qquad \text{(Kronheimer–Mrowka–Ozsváth–Szabó)},$$
and if $K$ is hyperbolic, $p \le 4g(K)+3$ (Rasmussen), against the conjectural Goda–Teragaito window $2g(K)+8 \le p \le 4g(K)-1$.

**Changemaker lattices.** Greene's method: if $S^3_p(K)=L(p,q)$, Donaldson's diagonalization applied to the two natural 4-manifold fillings forces the linear lattice $\Lambda(p,q)$ to embed in $\mathbb{Z}^{n}$ as the orthogonal complement of a *changemaker vector* $\sigma=(\sigma_1\le\cdots\le\sigma_n)$ with $\sigma_1\in\{0,1\}$ and
$$\sigma_i \;\le\; 1+\sum_{j<i}\sigma_j \quad (2\le i \le n).$$

## 3. History & State of the Art (SOTA)

- **1971.** Moser classifies surgeries on torus knots: $S^3_{p/q}(T_{r,s})$ is a lens space iff $|p-qrs|=1$.
- **1980.** Fintushel–Stern: the $(-2,3,7)$-pretzel knot, a hyperbolic knot, has two lens space surgeries ($18$ and $19$) — the first evidence that the picture is richer than torus knots.
- **1987.** Culler–Gordon–Luecke–Shalen prove the Cyclic Surgery Theorem: for a non-torus knot, cyclic surgery slopes are integral and at most two exist, differing by 1.
- **c. 1990.** Berge circulates *Some knots with surgeries yielding lens spaces*, giving twelve families of doubly primitive knots (I–II torus knots and cables, III–VI Berge–Gabai knots in solid tori, VII–VIII knots on the fiber surfaces of the trefoil and figure-eight, IX–XII sporadic families cut out by congruence conditions mod $p$) and conjecturing completeness. Posted publicly as arXiv:1802.09722 in 2018.
- **2005–2007.** Ozsváth–Szabó extract the alternating Alexander polynomial condition; KMOS prove $p\ge 2g(K)-1$ using monopole Floer homology; Ni proves L-space knots are fibered.
- **2013.** Greene solves the **lens space realization problem**: $L(p,q)$ arises from integral surgery on a knot in $S^3$ iff it arises from a Berge knot, and the knot Floer homology of any such knot matches that of the corresponding Berge knot. This is the strongest general result to date.

## 4. Partial Results / Verified Cases

- **Torus knots** (Moser 1971): fully classified; all are Berge types I–II.
- **Satellite knots** (Bleiler–Litherland 1989; Wang; Wu): a satellite knot with a lens space surgery must be the $(2pq\pm1,2)$-cable of $T_{p,q}$, with slope $4pq\pm1$ — all Berge knots. Combined with the torus case, **the conjecture holds for all non-hyperbolic knots**; only hyperbolic knots remain.
- **Slopes.** Non-integral surgeries on non-torus knots never give lens spaces (CGLS 1987). $\pm1$-surgery on a nontrivial knot never gives a lens space.
- **Genus range.** For hyperbolic $K$: $2g(K)-1\le p\le 4g(K)+3$ (KMOS; Rasmussen 2004), so for fixed genus only finitely many slopes are candidates.
- **Homeomorphism type.** Greene (2013): every lens space realized by integer surgery on any knot is realized by a Berge knot with the *same* $p$ and the *same* knot Floer homology. So no *new lens space* can appear.
- **Knots in solid tori.** Gabai (1989–90): a knot in a solid torus with a nontrivial solid-torus surgery is a 0- or 1-bridge braid; this classifies Berge types III–VI and proves the conjecture's analogue in $S^1\times D^2$.
- **Small complexity.** All knots up to 16 crossings, and the hyperbolic knots in the SnapPy cusped census, that admit lens space surgeries are Berge knots — verified computationally *(frontier — verify)*.
- **Baker–Grigsby–Hedden reformulation:** the conjecture follows if every knot in a lens space with simple ($\operatorname{rk}\widehat{HFK}=p$) knot Floer homology is a simple knot; proven in low genus / low bridge number cases (Baker, "Small genus knots in lens spaces have small bridge number", 2006).

## 5. Principal Obstacles

- **Floer homology is not a complete invariant.** Greene's theorem matches the candidate knot with a Berge knot at the level of $\widehat{HFK}$ and the surgered manifold, but $\widehat{HFK}$ does not determine the knot type. Bridging that gap needs a *geometric* rigidity statement no current Floer package supplies.
- **Hyperbolic geometry gives no leverage.** For hyperbolic $K$, the $6$-theorem and Gromov–Thurston $2\pi$ arguments only bound exceptional slopes by a universal constant ($\le 10$ exceptional slopes), which is far weaker than pinning down a genus-2 Heegaard position.
- **Thin position / sutured methods stall at genus 2.** Gabai's sutured-manifold machinery resolves the solid-torus case, but for a general hyperbolic complement there is no foliation argument forcing $K$ onto a genus-2 Heegaard surface.
- **Gauge-theoretic bounds are one-sided.** Instanton and monopole techniques (KMOS, Greene's Donaldson argument) produce numerical/lattice-theoretic obstructions on $(p,q)$ and $\Delta_K$. They constrain the *output* lens space, not the *input* knot; the changemaker condition is already saturated by Berge knots.
- **Sporadic families resist uniform treatment.** Types IX–XII are defined by explicit congruences with no known conceptual derivation, so any classification proof must reproduce arithmetic accidents rather than a single structural mechanism.
- **Tunnel number.** Doubly primitive knots have tunnel number one; proving that every lens-space-surgery knot has tunnel number one is itself open and appears to be of the same difficulty.

## 6. The Gap

Proven: *the set of lens spaces obtained by surgery on knots in $S^3$ equals the set obtained from Berge knots*, and any realizing knot has the knot Floer homology of a Berge knot (Greene 2013). Conjectured: *the set of knots is the same*.

The precise missing step is a **knot-detection statement**: show that if $K$ is hyperbolic, $S^3_p(K)\cong L(p,q)$, and $\widehat{HFK}(K)\cong\widehat{HFK}(B)$ for the Berge knot $B$ with $S^3_p(B)\cong L(p,q)$, then $K = B$. Dually (Baker–Grigsby–Hedden): show every knot $K^*\subset L(p,q)$ with $\operatorname{rk}\widehat{HFK}(L(p,q),K^*)=p$ and null-homologous lift-free geometry is isotopic to the simple knot in its homology class. All present tools see only the invariants, not the isotopy class.

## 7. Current Research (as of June 2026)

- **Simple-knot detection in lens spaces.** The Baker–Grigsby–Hedden program (grid diagrams for lens spaces, combinatorial $\widehat{HFK}$) remains the main line; progress is case-by-case in bridge number and genus.
- **Census and braid-positivity studies.** Baker–Kegel's analysis of L-space knots in the SnapPy census (AGT, 2024) shows all but one census L-space knot are braid positive, and identifies an L-space knot of tunnel number greater than one — evidence that L-space knots are strictly wilder than Berge knots, while Berge's list survives untouched *(frontier — verify)*.
- **Lattice/changemaker refinements.** Greene-style changemaker arguments have been extended to surgeries yielding connected sums of lens spaces and to the cabling conjecture; groups at Boston College, Georgia Tech and UT Austin continue this program.
- **Instanton-theoretic alternatives.** $SU(2)$ representation-variety methods (Kronheimer–Mrowka; Baldwin–Sivek) give independent constraints on cyclic surgeries and are being tested as a route to rigidity beyond Floer numerics *(frontier — verify)*.
- **Machine search.** Large-scale enumeration of hyperbolic knots via SnapPy/Regina with L-space-knot filters continues to return only Berge knots.

## 8. Future Work

1. Prove the simple-knot conjecture in $L(p,q)$ for all bridge numbers, closing the Baker–Grigsby–Hedden reduction.
2. Establish "tunnel number one" for all knots with a lens space surgery; combined with Berge's analysis of doubly primitive positions this would likely suffice.
3. Upgrade Greene's changemaker classification from a statement about lattices to a statement about the surgery cobordism's smooth structure.
4. Prove the Goda–Teragaito bound $2g+8\le p\le 4g-1$ for hyperbolic knots, sharpening Rasmussen's $p\le 4g+3$ and eliminating boundary cases.
5. Develop a Floer-theoretic invariant sensitive to isotopy class rather than filtered chain homotopy type — the essential missing ingredient.

## 9. Key References

- **[Foundational]** J. Berge. *Some knots with surgeries yielding lens spaces.* Unpublished manuscript, c. 1990; arXiv:1802.09722, 2018.
- **[Foundational]** L. Moser. *Elementary surgery along a torus knot.* Pacific Journal of Mathematics 38 (1971), 737–745.
- **[Foundational]** M. Culler, C. McA. Gordon, J. Luecke, P. B. Shalen. *Dehn surgery on knots.* Annals of Mathematics 125 (1987), 237–300.
- **[Foundational]** R. Fintushel, R. Stern. *Constructing lens spaces by surgery on knots.* Mathematische Zeitschrift 175 (1980), 33–51.
- **[SOTA]** J. Greene. *The lens space realization problem.* Annals of Mathematics 177 (2013), 449–511.
- **[SOTA]** P. Kronheimer, T. Mrowka, P. Ozsváth, Z. Szabó. *Monopoles and lens space surgeries.* Annals of Mathematics 165 (2007), 457–546.
- **[SOTA]** P. Ozsváth, Z. Szabó. *Knot Floer homology and lens space surgeries.* Topology 44 (2005), 1281–1300.
- **[SOTA]** J. Rasmussen. *Lens space surgeries and a conjecture of Goda and Teragaito.* Geometry & Topology 8 (2004), 1013–1031.
- **[SOTA]** K. Baker, E. Grigsby, M. Hedden. *Grid diagrams for lens spaces and combinatorial knot Floer homology.* International Mathematics Research Notices 2008, art. rnn024.
- **[SOTA]** M. Hedden. *On Floer homology and the Berge conjecture on knots admitting lens space surgeries.* Transactions of the AMS 363 (2011), 949–968.
- **[SOTA]** D. Gabai. *Surgery on knots in solid tori.* Topology 28 (1989), 1–6; and *1-bridge braids in solid tori.* Topology and its Applications 37 (1990), 221–235.
- **[SOTA]** S. Bleiler, R. Litherland. *Lens spaces and Dehn surgery.* Proceedings of the AMS 107 (1989), 1127–1131.
- **[SOTA]** Y. Ni. *Knot Floer homology detects fibred knots.* Inventiones Mathematicae 170 (2007), 577–608.
- **[Recent]** K. L. Baker, M. Kegel. *Census L-space knots are braid positive, except one that is not.* Algebraic & Geometric Topology 24 (2024).
- **[Survey]** J. Greene. *Heegaard Floer homology.* Notices of the AMS 68 (2021), 19–33.
- **[Survey]** C. McA. Gordon. *Dehn surgery and 3-manifolds.* In *Low Dimensional Topology*, IAS/Park City Mathematics Series 15, AMS, 2009.

## 10. Worked Example / Concrete Special Case

**The $(-2,3,7)$-pretzel knot $P$.** This is the hyperbolic knot $12n242$, fibered of genus $g(P)=5$.

*Alexander polynomial.*
$$\Delta_P(t) = t^{5}-t^{4}+t^{2}-t+1-t^{-1}+t^{-2}-t^{-4}+t^{-5}.$$
Nonzero coefficients are $\pm1$ and alternate in sign — exactly the Ozsváth–Szabó L-space-knot form, with $(a_1,\dots,a_4)=(5,4,2,1)$ and $n=4$: $\Delta_P = 1 + \sum_{j=1}^{4}(-1)^{4-j}(t^{a_j}+t^{-a_j})$. Its top degree $5=g(P)$ confirms fiberedness.

*Surgeries.* Fintushel–Stern: $S^3_{18}(P)\cong L(18,5)$ and $S^3_{19}(P)\cong L(19,8)$. Note $L(19,8)\cong L(19,7)$ since $8^{-1}\equiv 12$ and $-12\equiv 7 \pmod{19}$.

*Consistency with the bounds.*
- KMOS: $p \ge 2g-1 = 9$. Both $18,19 \ge 9$. ✓
- Rasmussen: $p \le 4g+3 = 23$. Both $\le 23$. ✓
- Goda–Teragaito window: $2g+8 = 18 \le p \le 4g-1 = 19$. $P$ realizes **both endpoints simultaneously** — it is the extremal example, which is why the conjectured window is believed sharp.
- CGLS: the two integer slopes differ by exactly $1$, the maximum allowed for a non-torus knot. ✓

*Berge position.* $P$ lies on the once-punctured torus fiber $F$ of the left-handed trefoil, embedded in $S^3$; pushing $F$ into each side of a genus-2 Heegaard surface built from a neighborhood of $F$ shows $[P]$ is primitive in $\pi_1$ of both handlebodies. So $P$ is a Berge knot of **type VII**, with surface slope $18$; the slope-$19$ surgery arises from the second (type VIII-adjacent) doubly primitive position. The dual knots are the simple knots in $L(18,5)$ and $L(19,8)$ of homology classes $5$ and $8$ respectively.

*What the example does not settle.* Greene's theorem guarantees no *other* knot can produce $L(18,5)$ by $18$-surgery with different Floer homology. It does **not** exclude a hypothetical hyperbolic knot $K\ne P$ with $\widehat{HFK}(K)\cong\widehat{HFK}(P)$ and $S^3_{18}(K)\cong L(18,5)$. Ruling this out — for this one $(p,q)$ pair, let alone in general — is precisely the open gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*