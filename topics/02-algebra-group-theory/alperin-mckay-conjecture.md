---
id: 02-algebra-group-theory/alperin-mckay-conjecture
title: "Alperin-McKay Conjecture"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alperin-McKay Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/alperin-mckay-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G$ be a finite group, $p$ a prime, and $B$ a $p$-block of $G$ with defect group $D$. Let $b$ be the Brauer correspondent of $B$ in $N_G(D)$, i.e. the unique block of $N_G(D)$ with $b^G = B$.

**Conjecture (Alperin, 1976).**
$$|\mathrm{Irr}_0(B)| \;=\; |\mathrm{Irr}_0(b)|,$$
where $\mathrm{Irr}_0(B)$ denotes the set of irreducible ordinary characters of height zero in $B$.

A complete proof must establish this equality for every finite group, every prime, and every block. The conjecture is a *counting* statement: no canonical bijection $\mathrm{Irr}_0(B) \to \mathrm{Irr}_0(b)$ is asserted, and constructing one naturally is a strictly harder open problem. A disproof requires one explicit block with $|\mathrm{Irr}_0(B)| \neq |\mathrm{Irr}_0(b)|$.

Applied to the principal block with $D \in \mathrm{Syl}_p(G)$ and $p$ odd, the conjecture implies the McKay conjecture $|\mathrm{Irr}_{p'}(G)| = |\mathrm{Irr}_{p'}(N_G(P))|$; it is thus the block-theoretic refinement of McKay.

## 2. Mathematical Foundations

Fix a $p$-modular system $(K, \mathcal{O}, k)$ with $K$ of characteristic $0$ big enough for $G$, $\mathcal{O}$ a complete DVR, $k = \mathcal{O}/J(\mathcal{O})$ of characteristic $p$.

**Blocks.** The group algebra decomposes into indecomposable two-sided ideals
$$\mathcal{O}G = B_1 \oplus \cdots \oplus B_r,$$
each $B_i$ a *block* with primitive central idempotent $e_i$. Every $\chi \in \mathrm{Irr}(G)$ lies in exactly one block, so $\mathrm{Irr}(G) = \bigsqcup_i \mathrm{Irr}(B_i)$.

**Defect and height.** Write $|G|_p = p^a$. The block $B$ has defect group $D$, a $p$-subgroup determined up to $G$-conjugacy by Brauer's theory of the defect; set $|D| = p^d$. Equivalently, $d = \max\{\nu_p(|D|)\}$ and
$$\min\{\nu_p(\chi(1)) : \chi \in \mathrm{Irr}(B)\} = a - d .$$
For $\chi \in \mathrm{Irr}(B)$ the *height* $h(\chi) \ge 0$ is defined by
$$\chi(1)_p = p^{\,a-d+h(\chi)}, \qquad \mathrm{Irr}_0(B) = \{\chi \in \mathrm{Irr}(B) : h(\chi) = 0\}.$$

**Brauer correspondence.** For a $p$-subgroup $D$, the Brauer homomorphism $\mathrm{Br}_D : (kG)^D \to kC_G(D)$ induces a bijection between blocks $b$ of $N_G(D)$ with defect group $D$ and blocks $B = b^G$ of $G$ with defect group $D$ (Brauer's First Main Theorem). This makes the right-hand side of the conjecture a genuinely *local* invariant: it depends only on $N_G(D)$.

**Related statements.**
- *Brauer's height zero conjecture (BHZ):* $\mathrm{Irr}(B) = \mathrm{Irr}_0(B)$ iff $D$ is abelian. Now a theorem (2024).
- *Alperin weight conjecture:* $|\mathrm{IBr}(B)| = $ number of $B$-weights.
- *Broué's abelian defect group conjecture:* for $D$ abelian, $D^b(B) \simeq D^b(b)$ as derived categories — this implies AM for such blocks, since a perfect isometry preserves height-zero counts.
- *Isaacs–Navarro / Navarro refinements:* AM should hold with degrees matched modulo $p$ up to sign, and equivariantly for the action of $\mathrm{Gal}(\mathbb{Q}_{|G|}/\mathbb{Q})$.

**Reduction.** Späth (2013) proved: if every finite non-abelian simple group satisfies the *inductive Alperin–McKay (iAM) condition* at $p$, then AM holds for all finite groups at $p$. The iAM condition demands, for each block of the universal covering group, an $\mathrm{Aut}(S)_B$-equivariant bijection compatible with central characters and with Clifford theory of the relevant character triples ($\sim_c$ ordering).

## 3. History & State of the Art (SOTA)

- **1972.** McKay observes $|\mathrm{Irr}_{2'}(G)| = |\mathrm{Irr}_{2'}(N_G(P))|$ for simple groups with $P \in \mathrm{Syl}_2$.
- **1966.** Dade's classification of blocks with cyclic defect groups yields the first infinite family where the equality holds.
- **1976.** Alperin, in *The main problem of block theory* (Park City conference), states the block-wise form and proposes it as the organising problem of modular representation theory.
- **1976–1980.** Olsson verifies it for symmetric and alternating groups; Okuyama–Wajima settle $p$-solvable groups.
- **1990.** Broué's abelian defect group conjecture supplies a categorical mechanism (perfect isometries, splendid equivalences) implying AM for abelian $D$.
- **2007.** Isaacs–Malle–Navarro reduce McKay to a condition on simple groups; the template for Späth's later work.
- **2013.** Späth's reduction theorem for AM (*J. reine angew. Math.* 680).
- **2016–2022.** Verification of iAM for large families: cyclic defect blocks of quasi-simple groups (Koshitani–Späth), defining-characteristic blocks of groups of Lie type, and a Jordan decomposition for iAM (Ruhstorfer, *Adv. Math.* 2022).
- **2022.** Ruhstorfer announces AM for $p = 2$ for all finite groups.
- **2024.** Malle–Navarro–Schaeffer Fry–Tiep prove Brauer's height zero conjecture (*Annals* 200), using AM at $p=2$ as an input.
- **2024–2025.** Cabanes–Späth announce a proof of the McKay conjecture for all primes; the block-wise AM statement for odd $p$ remains open in general.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Blocks with cyclic defect group $D \cong C_{p^n}$ | Proved; $|\mathrm{Irr}_0(B)| = e + \frac{p^n-1}{e}$ with $e = |N_G(D,b_D)/DC_G(D)|$ | Dade 1966 |
| $p$-solvable $G$ | Proved, all $p$ | Okuyama–Wajima 1980 |
| Symmetric groups $S_n$, alternating groups | Proved, all $p$ (blocks parametrised by $p$-cores/weights) | Olsson 1976 |
| $p = 2$, all finite groups | Proved (iAM verified for all simple groups at $p=2$) | Ruhstorfer 2022 |
| Klein four defect group $D \cong C_2 \times C_2$ | Proved; $|\mathrm{Irr}_0(B)| = 3$ always | Craven–Eaton–Kessar–Linckelmann 2011 |
| Blocks with abelian $D$ where Broué's conjecture is known (e.g. principal blocks with $D$ abelian and $p$-nilpotent normaliser; $\mathrm{SL}_2(q)$; many unipotent blocks) | Proved via perfect isometry | Broué 1990 and successors |
| Defect $\le 2$ ($|D| \le p^2$) | Proved | Consequence of classification of small-defect blocks; see Sambale 2014 |
| 2-blocks of defect $\le 4$, minimal nonabelian defect groups | Proved | Sambale 2014 (LNM 2127) |
| Unipotent and quasi-isolated blocks of groups of Lie type, $p$ good | Extensively verified | Kessar–Malle 2013; Ruhstorfer 2022 |
| Sporadic simple groups | iAM verified block-by-block by computation in GAP/CHEVIE for all but a few large cases | Breuer et al., ongoing |

## 5. Principal Obstacles

- **No canonical bijection.** The conjecture predicts an equality of cardinalities with no known intrinsic map. Every proof strategy must either construct a bijection ad hoc (fragile, non-functorial) or count both sides independently (only feasible with a classification of the block).
- **Local–global gap.** $\mathrm{Irr}_0(B)$ is a global object; $\mathrm{Irr}_0(b)$ is computable from $N_G(D)$. There is no functor from $\mathrm{mod}\,B$ to $\mathrm{mod}\,b$ that induces the count in general; Broué's equivalence supplies one only for abelian $D$, and even there it is proved case by case.
- **Nonabelian defect groups.** For nonabelian $D$, no categorical equivalence is even conjectured; Broué's framework simply does not extend, and heights can be positive so the height-zero subset is not a natural block-theoretic invariant of any module category shadow.
- **Cost of the inductive condition.** iAM is much stronger than AM for the simple group itself: it requires equivariance under $\mathrm{Aut}(S)$ *and* compatibility of central/Clifford data. Verifying it for groups of Lie type at odd $p$ needs precise control of the action of diagonal, field and graph automorphisms on Lusztig series and on $\ell$-modular Deligne–Lusztig characters — exactly where multiplicity-one statements and Jordan decomposition are hardest.
- **Bad primes and non-connected centralisers.** For $p$ dividing $|Z(G^F)|$ or $p$ bad for the root system, Jordan decomposition of blocks is not known to be compatible with the automorphism action; disconnected centralisers break the standard parametrisation.
- **Dependence on CFSG.** Every general strategy currently routes through the classification of finite simple groups, so no proof is self-contained.

## 6. The Gap

The reduction theorem converts the conjecture into a finite (but enormous) checklist: verify iAM for each simple group $S$ and prime $p$. What is settled is $p = 2$ in full, plus, for odd $p$: alternating groups, sporadic groups, groups of Lie type in defining characteristic, and blocks admitting a suitable Jordan decomposition.

The remaining gap is precisely: **iAM for blocks of quasi-simple groups of Lie type at odd primes $\ell \neq p$ (non-defining characteristic), especially non-unipotent and quasi-isolated blocks at bad primes, with full equivariance under the outer automorphism group and correct behaviour on central characters.** The parallel McKay statement was reached by Cabanes–Späth via a "$\ell$-adic" parametrisation of $\mathrm{Irr}_{\ell'}$ of $N$ and a character-triple argument; upgrading that argument block-wise requires tracking which height-zero characters lie in a given block $B$ — a condition invisible to the McKay-level bookkeeping.

## 7. Current Research (as of June 2026)

- **Späth's school (Bergische Universität Wuppertal).** Systematic verification of iAM and its Galois-equivariant strengthening; Cabanes–Späth's McKay machinery is being adapted to blocks. *(frontier — verify)*
- **Ruhstorfer (Wuppertal/Kaiserslautern).** Jordan decomposition for AM; extension of the $p=2$ argument to odd primes via $\ell$-adic cohomology of Deligne–Lusztig varieties and Bonnafé–Dat–Rouquier equivalences.
- **Malle, Navarro, Schaeffer Fry, Tiep.** Post-BHZ programme: consequences and refinements (Galois–AM, Isaacs–Navarro congruences, characterisations of defect groups from character degrees).
- **Linckelmann, Kessar (City, University of London).** Structural finiteness (Donovan's conjecture, block invariant bounds) that would make block-by-block verification of small defect uniform.
- **Computational.** GAP character-table library and CHEVIE checks for sporadic and small Lie-type groups; Sambale's classification programme for blocks of small defect.

## 8. Future Work

- Prove a block-wise refinement of the Cabanes–Späth McKay theorem by showing their bijections respect Brauer blocks and central characters.
- Establish Broué's conjecture (or a splendid Rickard equivalence) for quasi-isolated blocks with abelian defect at bad primes — this would settle a large residual family.
- Find a *natural* bijection: Navarro's Galois-refinement suggests candidate maps determined by fields of values, which may pin down the correspondence uniquely.
- Develop a defect-group-agnostic invariant (e.g. a cohomological or fusion-system-level count) whose equality with the local side is provable without CFSG.
- Extend AM to blocks of finite reductive groups over $\overline{\mathbb{F}}_q$ uniformly in $q$, using Lusztig induction commuting with Brauer correspondence.

## 9. Key References

- **[Foundational]** J. L. Alperin. *The main problem of block theory.* In: Proceedings of the Conference on Finite Groups (Park City, Utah, 1975), Academic Press, 1976, pp. 341–356.
- **[Foundational]** J. McKay. *Irreducible representations of odd degree.* Journal of Algebra 20 (1972), 416–418.
- **[Foundational]** E. C. Dade. *Blocks with cyclic defect groups.* Annals of Mathematics 84 (1966), 20–48.
- **[Foundational]** T. Okuyama, M. Wajima. *Character correspondence and $p$-blocks of $p$-solvable groups.* Osaka Journal of Mathematics 17 (1980), 801–806.
- **[Foundational]** J. B. Olsson. *McKay numbers and heights of characters.* Mathematica Scandinavica 38 (1976), 25–42.
- **[Foundational]** M. Broué. *Isométries parfaites, types de blocs, catégories dérivées.* Astérisque 181–182 (1990), 61–92.
- **[Key]** M. Isaacs, G. Malle, G. Navarro. *A reduction theorem for the McKay conjecture.* Inventiones Mathematicae 170 (2007), 33–101.
- **[Key]** B. Späth. *A reduction theorem for the Alperin–McKay conjecture.* Journal für die reine und angewandte Mathematik 680 (2013), 153–189.
- **[Key]** D. Craven, C. W. Eaton, R. Kessar, M. Linckelmann. *The structure of blocks with a Klein four defect group.* Mathematische Zeitschrift 268 (2011), 441–476.
- **[Key]** R. Kessar, G. Malle. *Quasi-isolated blocks and Brauer's height zero conjecture.* Annals of Mathematics 178 (2013), 321–384.
- **[SOTA / Recent]** L. Ruhstorfer. *Jordan decomposition for the Alperin–McKay conjecture.* Advances in Mathematics 394 (2022), 108031.
- **[SOTA / Recent]** L. Ruhstorfer. *The Alperin–McKay conjecture for the prime 2.* arXiv:2204.06373 (2022).
- **[SOTA / Recent]** G. Malle, G. Navarro, A. A. Schaeffer Fry, P. H. Tiep. *Brauer's Height Zero Conjecture.* Annals of Mathematics 200 (2024), 557–608.
- **[SOTA / Recent]** M. Cabanes, B. Späth. *The McKay conjecture on character degrees.* arXiv preprint, 2024.
- **[Survey]** G. Navarro. *Character Theory and the McKay Conjecture.* Cambridge Studies in Advanced Mathematics 175, Cambridge University Press, 2018.
- **[Survey]** B. Sambale. *Blocks of Finite Groups and Their Invariants.* Lecture Notes in Mathematics 2127, Springer, 2014.

## 10. Worked Example / Concrete Special Case

Take $G = A_5$ and $p = 5$. Here $|G| = 60 = 2^2 \cdot 3 \cdot 5$, so $a = 1$.

**Global side.** $\mathrm{Irr}(A_5)$ has degrees $1, 3, 3, 4, 5$. The character of degree $5$ has $\nu_5(5) = 1 = a$, so it forms a block of defect $0$. The remaining four characters lie in the principal block $B_0$, whose defect group is $D = P \in \mathrm{Syl}_5(A_5)$, $D \cong C_5$, $d = 1$. For $\chi \in \mathrm{Irr}(B_0)$,
$$\chi(1)_5 = 5^{\,a-d+h(\chi)} = 5^{\,h(\chi)}.$$
Degrees $1, 3, 3, 4$ are all prime to $5$, so every one has height $0$:
$$|\mathrm{Irr}_0(B_0)| = 4.$$

This matches Dade's cyclic-defect formula. With $D = C_5$, $C_G(D) = D$ and $N_G(D) \cong D_{10}$ (dihedral of order $10$), the inertial index is
$$e = |N_G(D)/C_G(D)| = 10/5 = 2, \qquad e + \frac{|D|-1}{e} = 2 + \frac{4}{2} = 4 .$$

**Local side.** $N_G(D) = D_{10}$ has $O_{5'}(D_{10}) = 1$ and a normal Sylow $5$-subgroup, so it has a single $5$-block $b$ (the principal one), with defect group $D$ and $b^G = B_0$. Its irreducible characters have degrees $1, 1, 2, 2$ — four characters, all of degree prime to $5$, hence all of height $0$:
$$|\mathrm{Irr}_0(b)| = 4 .$$

**Conclusion.** $|\mathrm{Irr}_0(B_0)| = |\mathrm{Irr}_0(b)| = 4$: the conjecture holds here. Two features are worth noting. First, the global degrees $\{1,3,3,4\}$ and the local degrees $\{1,1,2,2\}$ are entirely different — only the *counts* agree, which is why no naive degree-preserving bijection can exist. Second, reduction mod $5$ of the degrees gives $\{1, 3, 3, 4\} \equiv \{1, 3, 3, 4\}$ and $\{1,1,2,2\}$; matching $\pm$ classes mod $5$ gives $\{\pm 1, \pm 2\}$ on both sides, which is exactly the Isaacs–Navarro refinement in action.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*