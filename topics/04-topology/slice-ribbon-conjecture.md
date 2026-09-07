---
id: 04-topology/slice-ribbon-conjecture
title: "Slice-Ribbon Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Slice-Ribbon Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/slice-ribbon-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Fox, 1962).** Every smoothly slice knot in $S^3$ is a ribbon knot.

A knot $K \subset S^3 = \partial B^4$ is **smoothly slice** if it bounds a smoothly embedded disk $D \hookrightarrow B^4$ with $\partial D = K$. It is **ribbon** if it bounds an immersed disk in $S^3$ whose only singularities are ribbon singularities, equivalently if it bounds a smooth disk in $B^4$ with no local maxima of the radial Morse function.

Ribbon $\Rightarrow$ slice is elementary: push the ribbon disk into $B^4$ to resolve the singularities. The conjecture asserts the converse. A proof would show every slice disk can be isotoped to have no critical points of index $2$ (equivalently, to be presented by a handle decomposition with only $0$- and $1$-handles). A disproof requires exhibiting a single knot $K$ that bounds a smooth disk in $B^4$ but admits no ribbon presentation — which requires a *sliceness certificate* plus an obstruction to ribbonness, and no useful obstruction to ribbonness is currently known.

The statement is specific to the **smooth** category. In the topological locally flat category it is false in spirit and vacuously uninformative: Freedman's theorem gives that every knot with Alexander polynomial $\Delta_K(t) \doteq 1$ is topologically slice, and infinitely many such knots (Endo 1995) are not smoothly slice, hence not ribbon.

## 2. Mathematical Foundations

**Ribbon singularity.** Let $f: D^2 \looparrowright S^3$ be a generic immersion. A double-point arc $A \subset f(D^2)$ is a *ribbon singularity* if its two preimages $A_1, A_2 \subset D^2$ satisfy: $A_1 \subset \operatorname{int} D^2$ and $A_2$ is properly embedded with $\partial A_2 \subset \partial D^2$. Then $K = f(\partial D^2)$ is a ribbon knot.

**Radial Morse formulation.** Let $r: B^4 \to [0,1]$ be the radial function. A slice disk $D$ is *ribbon* iff $r|_D$ can be made Morse with no index-$2$ critical points. Equivalently, $K$ is ribbon iff there is a sequence
$$U_{k} \;\xrightarrow{\ \text{fusion bands}\ } \; K,$$
where $U_k$ is a $k$-component unlink and $k-1$ bands are attached; the minimal such $k-1$ is the **fusion number** $\mathrm{fus}(K)$.

**Concordance group.** Slice knots form the kernel of $\mathcal{K} \to \mathcal{C}$, where $\mathcal{C}$ is the smooth knot concordance group. Ribbon knots generate a subgroup $\mathcal{R} \le \mathcal{C}$; the conjecture is $\mathcal{R} = 0$ *as a set-level statement*: $\{\text{ribbon}\} = \{\text{slice}\}$.

**Classical obstructions to sliceness.**
- *Fox–Milnor:* if $K$ is slice then $\Delta_K(t) \doteq f(t)\,f(t^{-1})$ for some $f \in \mathbb{Z}[t,t^{-1}]$. In particular $\det(K) = |\Delta_K(-1)|$ is a perfect square.
- *Signatures:* $\sigma_\omega(K) = 0$ for all $\omega \in S^1$ of prime power order (Tristram–Levine).
- *Arf invariant:* $\mathrm{Arf}(K) = 0$.
- *Casson–Gordon invariants:* metabelian $\rho$-invariants of prime-power branched covers obstruct sliceness beyond algebraic concordance.
- *Gauge-theoretic:* if $K$ is slice then $\tau(K) = s(K)/2 = \Upsilon_K \equiv 0$, and $V_0(K) = V_0(\overline{K}) = 0$ in Heegaard Floer $d$-invariants.

**Double branched cover.** Let $\Sigma_2(K)$ be the double cover of $S^3$ branched over $K$. If $K$ is slice, $\Sigma_2(K)$ bounds a rational homology $4$-ball $W$ (the double cover of $B^4$ branched over the slice disk), so
$$|H_1(\Sigma_2(K))| = \det(K) = n^2, \qquad \lambda(\Sigma_2(K)) \text{ metabolic.}$$
Donaldson's diagonalization theorem $Q_X \cong \langle -1 \rangle^{\oplus n}$ for negative definite closed $X$, applied to $W \cup_{\Sigma} (\text{plumbing})$, is the engine behind essentially every affirmative case in Section 4.

**Homotopy-ribbon.** $K$ is *homotopy-ribbon* if it bounds a slice disk $D$ with $\pi_1(S^3 \setminus K) \to \pi_1(B^4 \setminus D)$ surjective. Then ribbon $\Rightarrow$ homotopy-ribbon $\Rightarrow$ slice, and both implications are open in reverse.

## 3. History & State of the Art (SOTA)

- **1961–62.** Fox introduces ribbon knots and poses the question as Problem 25 in *Some problems in knot theory* (Topology of 3-Manifolds, Prentice–Hall, 1962).
- **1966.** Fox–Milnor publish the determinant/Alexander-polynomial condition, the first slicing obstruction.
- **1975.** Casson–Gordon construct their invariants, showing algebraic sliceness is strictly weaker than sliceness.
- **1983.** Casson–Gordon (*A loop theorem for duality spaces and fibred ribbon knots*, Invent. Math. 74): if a fibered knot is homotopy-ribbon, its fiber surface monodromy extends over a handlebody. This is the sharpest structural constraint known in the fibered case.
- **2007.** Lisca proves the conjecture for **2-bridge knots** (*Lens spaces, rational balls and the ribbon conjecture*, Geom. Topol. 11), simultaneously settling the Casson–Harer question of which lens spaces bound rational homology balls.
- **2011.** Greene–Jabuka settle **odd 3-strand pretzel knots** $P(p,q,r)$ (Amer. J. Math. 133).
- **2012–15.** Lecuona extends to large families of **Montesinos knots** and to **pretzel knots** with mixed parities.
- **2010.** Gompf–Scharlemann–Thompson (Geom. Topol. 14) produce fibered candidates for counterexamples arising from the square knot; Abe–Jong–Luecke–Osoinach (2013) later show they are ribbon.
- **2019–2023.** Manolescu–Piccirillo generate candidate counterexamples from zero-surgery homeomorphisms; Nakamura and others rule out several by trace-embedding arguments.
- **2022–24.** Dai–Kang–Mallick–Park–Stoffregen prove the **$(2,1)$-cable of the figure-eight knot is not smoothly slice**, eliminating the most prominent conjectural counterexample family and validating a knot-Floer-theoretic obstruction ($\iota$-complexes / involutive Heegaard Floer for satellites).

Status: no counterexample, no general proof, and no obstruction to ribbonness that is not already an obstruction to sliceness.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| 2-bridge (rational) knots $b(p,q)$ | Slice $\Rightarrow$ ribbon; complete list of slice ones | Lisca 2007 |
| 3-strand pretzel $P(p,q,r)$, $p,q,r$ odd | Slice $\Rightarrow$ ribbon; only $P(p,-p,q)$-type are slice | Greene–Jabuka 2011 |
| Pretzel $P(p,q,r)$, general parities | Conjecture holds | Lecuona 2015 |
| Large families of Montesinos knots | Conjecture holds | Lecuona 2012 |
| Knots with $\le 12$ crossings | Every slice knot in the table is ribbon (all 12-crossing cases resolved; the last holdouts settled via twisted Alexander polynomials / Casson–Gordon) | Herald–Kirk–Livingston 2010; Cha–Livingston KnotInfo |
| Generalized square knots $T_{p,q} \\# \overline{T_{p,q}}$ | Slice $\Rightarrow$ ribbon | Meier–Zupan 2019 |
| Certain iterated torus knots / cables | Rational-homology-ball obstructions force ribbonness | Aceto 2020; Aceto–Golla–Larson–Lecuona |
| Symmetric unions | All are ribbon (a source of examples, not a proof) | Lamm 2000s |

Computationally: KnotInfo/KnotAtlas record sliceness status for all knots up to 12 crossings and most 13-crossing knots; every knot verified slice there has an explicit ribbon presentation, typically of fusion number $1$.

## 5. Principal Obstacles

- **No obstruction to ribbonness exists.** Every known invariant that vanishes for ribbon knots ($\Delta$-factorization, signatures, $\tau$, $s$, $\Upsilon$, $V_0$, Casson–Gordon, $d$-invariants of branched covers) vanishes for slice knots too, because they are all built from the $4$-manifold topology of the slice complement, which does not see handle indices. A counterexample would need an invariant sensitive to the *Morse/handle structure* of the disk, not to its concordance class.
- **Handle cancellation is 4-dimensional.** Turning a slice disk into a ribbon disk means cancelling all index-$2$ critical points. This is exactly the type of statement blocked by the failure of the Whitney trick in dimension $4$: the algebraic cancellation data is available, but no geometric cancellation theorem exists.
- **Gauge theory is category-blind to indices.** Donaldson- and Floer-theoretic arguments constrain which $3$-manifolds bound rational homology balls, hence which knots can be slice; they say nothing about the handle decomposition of the bounding object.
- **The proved cases rely on lattice combinatorics.** Lisca's and Greene–Jabuka's proofs reduce to classifying which linear/star-shaped negative-definite lattices embed in $\mathbb{Z}^n$. That reduction requires $\Sigma_2(K)$ to bound a *plumbed* $4$-manifold — true for Montesinos knots, false in general.
- **Entanglement with the smooth Poincaré conjecture.** Several candidate counterexample families (Gompf–Scharlemann–Thompson; Meier–Zupan) are simultaneously candidates for exotic homotopy $4$-spheres; disproving slice-ribbon in those families would carry $4$-dimensional smooth-structure consequences, so the difficulty is not incidental.

## 6. The Gap

Proven cases are exactly those where $\Sigma_2(K)$ bounds a plumbing tree, so that "bounds a rational homology ball" becomes a finite lattice-embedding problem whose solutions can be matched one-to-one with explicit band moves. The general statement covers knots with $\Sigma_2(K)$ an arbitrary rational homology sphere, where no such finite reduction is available.

The precise missing step: given a slice disk $D \subset B^4$ with $k$ index-$2$ critical points, produce an ambient isotopy reducing $k$ to $0$ — or produce a computable invariant $\iota(K)$ with $\iota(\text{ribbon}) = 0$ and $\iota(K) \ne 0$ for some slice $K$. Neither the "geometric cancellation" nor the "new invariant" branch has a working prototype.

## 7. Current Research (as of June 2026)

- **Involutive and knot Floer obstructions for satellites.** The Dai–Kang–Mallick–Park–Stoffregen technique that killed the $(2,1)$-cable of $4_1$ is being applied to other cables and Whitehead doubles; the hope is a family where sliceness holds but ribbonness provably fails. No success yet. *(frontier — verify)*
- **Zero-surgery homeomorphism candidates.** Manolescu–Piccirillo's construction produces knots $K$ with $S^3_0(K) \cong S^3_0(K')$ where $K'$ is slice; each is a potential counterexample to slice-ribbon or a source of exotic definite $4$-manifolds. Nakamura's trace-embedding criterion has eliminated several. *(frontier — verify)*
- **Ribbon-number and fusion-number bounds.** Work bounding $\mathrm{fus}(K)$ below via Heegaard Floer and Khovanov homology (Juhász–Miller–Zemke; Kang; Sundberg–Swann) aims at a genuinely ribbon-specific invariant.
- **Alternating and quasi-alternating knots.** The conjecture is open beyond 2-bridge; Greene's lattice-theoretic characterization of alternating links is the natural tool.
- **Fibered knots.** Casson–Gordon's handlebody-extension criterion combined with Meier–Zupan's Dehn-surgery methods; the generalized square knot case is settled, general fibered case open.
- Active groups: Boston College (Greene), Georgia Tech, MPIM Bonn, Zaragoza (Lecuona), KIAS/Seoul (Park, Kang), Indiana/Brandeis (Livingston, Cha collaborations).

## 8. Future Work

1. **Construct a ribbon-specific invariant.** Most promising: an invariant of the *ribbon disk complement* $\pi_1(B^4 \setminus D)$ — ribbon disk groups are exactly those with a Wirtinger-type presentation of deficiency $1$ where meridians normally generate. Finding a group-theoretic property failing for some slice disk complement would settle it.
2. **Push lattice methods past plumbings.** Extend Lisca-type classification from linear/star-shaped graphs to arbitrary rational homology spheres with small $|H_1|$.
3. **Attack alternating knots.** A proof for all alternating knots would be the first infinite non-plumbing-based family.
4. **Systematic search at 14–16 crossings.** Slice knots whose ribbon status is undetermined would sharpen the empirical evidence, currently exhausted at 12 crossings.
5. **Homotopy-ribbon intermediate.** Prove or disprove slice $\Rightarrow$ homotopy-ribbon first; this weaker statement is more tractable and would already be a major advance.

## 9. Key References

- **[Foundational]** R. H. Fox. *Some problems in knot theory.* In "Topology of 3-Manifolds and Related Topics" (M. K. Fort, ed.), Prentice–Hall, 1962, 168–176.
- **[Foundational]** R. H. Fox and J. W. Milnor. *Singularities of 2-spheres in 4-space and cobordism of knots.* Osaka J. Math. 3 (1966), 257–267.
- **[Foundational]** A. J. Casson and C. McA. Gordon. *A loop theorem for duality spaces and fibred ribbon knots.* Inventiones Mathematicae 74 (1983), 119–137.
- **[Foundational]** A. J. Casson and C. McA. Gordon. *Cobordism of classical knots.* In "À la Recherche de la Topologie Perdue", Progr. Math. 62, Birkhäuser, 1986, 181–199.
- **[SOTA]** P. Lisca. *Lens spaces, rational balls and the ribbon conjecture.* Geometry & Topology 11 (2007), 429–472.
- **[SOTA]** J. Greene and S. Jabuka. *The slice-ribbon conjecture for 3-stranded pretzel knots.* American Journal of Mathematics 133 (2011), 555–580.
- **[SOTA]** A. G. Lecuona. *On the slice-ribbon conjecture for Montesinos knots.* Transactions of the AMS 364 (2012), 233–285.
- **[SOTA]** A. G. Lecuona. *On the slice-ribbon conjecture for pretzel knots.* Algebraic & Geometric Topology 15 (2015), 2133–2173.
- **[SOTA / Recent]** I. Dai, S. Kang, A. Mallick, J. Park, M. Stoffregen. *The $(2,1)$-cable of the figure-eight knot is not smoothly slice.* arXiv:2207.14196, 2022.
- **[SOTA / Recent]** C. Manolescu and L. Piccirillo. *From zero surgeries to candidates for exotic definite four-manifolds.* arXiv:2102.04391, 2021.
- **[SOTA / Recent]** J. Meier and A. Zupan. *Generalized square knots and homotopy 4-spheres.* arXiv:1904.08527, 2019.
- **[Recent]** R. E. Gompf, M. Scharlemann, A. Thompson. *Fibered knots and potential counterexamples to the Property 2R and slice-ribbon conjectures.* Geometry & Topology 14 (2010), 2305–2347.
- **[Recent]** T. Abe, I. D. Jong, J. Luecke, J. Osoinach. *Infinitely many knots admitting the same integer surgery and a four-dimensional extension.* International Mathematics Research Notices (2015), 4699–4728.
- **[Recent]** C. Herald, P. Kirk, C. Livingston. *Metabelian representations, twisted Alexander polynomials, knot slicing, and mutation.* Mathematische Zeitschrift 265 (2010), 925–949.
- **[Survey]** R. Kirby (ed.). *Problems in low-dimensional topology.* AMS/IP Stud. Adv. Math. 2.2, 1997 (Problem 1.33).
- **[Survey]** C. Livingston and A. H. Moore. *KnotInfo: Table of Knot Invariants.* knotinfo.math.indiana.edu, accessed 2026.
- **[Book]** J. C. Cha and K. H. Ko / see also D. Rolfsen, *Knots and Links*, Publish or Perish, 1976 (Ch. 8, ribbon and slice knots).

## 10. Worked Example / Concrete Special Case

**The knot $6_1$.** This is the two-bridge knot $b(9,7)$, the smallest nontrivial ribbon knot after $6_1$'s cousin the square knot $3_1 \\# \overline{3_1}$.

*Step 1 — Fox–Milnor test.* Its Alexander polynomial is
$$\Delta_{6_1}(t) \;=\; 2t^2 - 5t + 2 \;\doteq\; 2t - 5 + 2t^{-1}.$$
Set $f(t) = 2t - 1$. Then
$$f(t)f(t^{-1}) = (2t-1)(2t^{-1}-1) = 4 - 2t - 2t^{-1} + 1 = 5 - 2t - 2t^{-1} \;\doteq\; \Delta_{6_1}(t).$$
So the Fox–Milnor condition is satisfied and sliceness is not obstructed. The determinant is
$$\det(6_1) = |\Delta_{6_1}(-1)| = |2 + 5 + 2| = 9 = 3^2,$$
a perfect square, as required.

*Step 2 — Double branched cover.* $\Sigma_2(6_1) = L(9,7)$. Lisca's classification of lens spaces bounding rational homology balls says $L(p,q)$ bounds iff $(p,q)$ lies in an explicit family; $L(9,7)$ does, via $9 = 3^2$ with $q = 7 \equiv -3+1$ fitting the $L(m^2, mk\pm1)$ pattern with $m=3, k=1$: $mk+1 = 4$ and $L(9,4) \cong L(9,7)$ since $4 \cdot 7 = 28 \equiv 1 \pmod 9$. Hence the Donaldson obstruction vanishes.

*Step 3 — Explicit ribbon disk.* $6_1$ has fusion number $1$: take the $2$-component unlink $U_1 \sqcup U_2$ and attach a single band $b$ that passes once through the disk bounded by $U_1$ and twists so the resulting knot is $6_1$. Concretely, $6_1$ is the *twisted double* of the unknot with $2$ full twists and framing $-2$ — a knot of the form obtained by pushing one strand of a trivial band through the other. The resulting immersed disk in $S^3$ has exactly one ribbon singularity arc, and pushing the interior into $B^4$ resolves it into a smooth disk with critical points of index $0$ (two minima) and index $1$ (one saddle), and none of index $2$.

*What the example shows.* Every step of the verification for $6_1$ is a *sliceness* argument (Steps 1–2), and ribbonness had to be certified separately by an explicit construction (Step 3). The conjecture asserts that Step 3 is always available whenever Steps 1–2 (and every other obstruction) pass. For $6_1$ it does; Lisca's theorem guarantees it for all two-bridge knots. Outside plumbing-based families there is no mechanism producing Step 3 from Steps 1–2, and that missing mechanism is precisely the open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*