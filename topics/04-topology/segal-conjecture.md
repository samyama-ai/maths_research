---
id: 04-topology/segal-conjecture
title: "Segal Conjecture"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Segal Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/segal-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G$ be a finite group, $A(G)$ its Burnside ring, and $I = \ker(A(G) \xrightarrow{\ \deg\ } \mathbb{Z})$ the augmentation ideal. Segal's conjecture (c. 1970) asserts that the natural completion map

$$\alpha^* : \pi^{*}_{G}(S^{0})^{\wedge}_{I} \longrightarrow \pi^{*}_{S}(BG_{+})$$

from the $I$-adically completed $\mathbb{Z}$-graded equivariant stable cohomotopy of a point to the stable cohomotopy of the classifying space $BG$ (with disjoint basepoint) is an isomorphism in every degree. Equivalently, in spectrum form: the map of $G$-fixed-point spectra induced by $EG_+ \to S^0$,

$$\big(\mathbb{S}_{G}\big)^{\wedge}_{I} \;\xrightarrow{\ \simeq\ }\; F(BG_{+}, \mathbb{S}) = D(BG_{+}),$$

identifies the $I$-completed $G$-equivariant sphere with the Spanier–Whitehead dual of $BG_+$. It is the stable-cohomotopy analogue of the Atiyah–Segal completion theorem $K_G^*(\mathrm{pt})^{\wedge}_{J} \cong K^*(BG)$ for the representation-ring augmentation ideal $J$.

A complete proof requires the isomorphism in **all** degrees for **all** finite groups; a disproof would exhibit one group and one degree where $\alpha^*$ fails to be injective or surjective. The conjecture was proved by **Gunnar Carlsson (1984)**; it remains listed here because the natural extensions — compact Lie groups, infinite discrete groups, and the "$\mathrm{THH}$-Segal conjecture" for ring spectra — are open or only partially settled.

## 2. Mathematical Foundations

**Burnside ring.** $A(G)$ is the Grothendieck group of finite $G$-sets under disjoint union, with product induced by $\times$. It is free abelian on orbits $[G/H]$, $H$ ranging over conjugacy classes of subgroups. The mark homomorphism
$$\phi: A(G) \hookrightarrow \prod_{(H)} \mathbb{Z}, \qquad \phi_H([X]) = |X^{H}|$$
is injective with finite cokernel. The augmentation is $\deg = \phi_{\{e\}}$.

**Segal–tom Dieck theorem.** For $G$ finite, $\pi^{0}_{G}(S^{0}) \cong A(G)$, and more generally the tom Dieck splitting gives
$$\pi_{*}^{G}(\mathbb{S}) \;\cong\; \bigoplus_{(H)} \pi_{*}^{s}\big( (BW_{G}H)_{+} \big), \qquad W_{G}H = N_{G}H/H .$$

**$I$-adic completion.** For a $G$-spectrum $X$, $X^{\wedge}_{I}$ denotes completion of $\pi_*^G$-modules at $I$; concretely $I = \big( [G/H] - |G/H| \big)_{H \le G}$ and $I$-adic topology agrees with the $\prod_p$-adic topology in a range controlled by the primes dividing $|G|$.

**Equivalent geometric form.** With $EG$ a free contractible $G$-CW complex, $\alpha$ is induced by $EG_+ \to S^0$; taking function spectra and fixed points,
$$F(EG_+, \mathbb{S})^{G} \simeq F(BG_+, \mathbb{S}), \qquad \mathbb{S}^{G} = \mathbb{S}_G,$$
so the conjecture says $\alpha: \mathbb{S}_G \to F(EG_+,\mathbb{S})^G$ is $I$-adic completion.

**Reduction to $p$-groups.** By a transfer/induction argument the statement for $G$ follows from the statement for all $p$-Sylow subgroups; a further induction on the subgroup lattice reduces to elementary abelian $p$-groups $(\mathbb{Z}/p)^{n}$ — the technical heart.

## 3. History & State of the Art (SOTA)

- **1969.** Atiyah–Segal prove the $K$-theory completion theorem, the template.
- **c. 1970.** Segal formulates the cohomotopy analogue (ICM Nice address, *Equivariant stable homotopy theory*), noting the case $G=\mathbb{Z}/2$ already implies deep facts about stunted projective spaces.
- **1980.** **Lin's theorem** (with computations by Davis–Mahowald–Adams): the case $G = \mathbb{Z}/2$, equivalent to $\big(\varprojlim_n \Sigma^{\infty}\mathbb{RP}^{\infty}_{-n}\big)^{\wedge}_{2} \simeq \mathbb{S}^{-1}{}^{\wedge}_{2}$.
- **1980.** Gunawardena proves $G = \mathbb{Z}/p$, $p$ odd.
- **1981.** Ravenel extends to cyclic $p$-groups $\mathbb{Z}/p^{n}$.
- **1985 (circulated 1981–83).** Adams–Gunawardena–Miller prove the elementary abelian case $(\mathbb{Z}/p)^{n}$ via the Singer construction and an $\mathrm{Ext}$-level Lannes-type argument over the Steenrod algebra.
- **1984.** **Carlsson** completes the proof for all finite $G$ (Annals of Math. 120), by an induction over the poset of subgroups reducing the general case to elementary abelian ones; simultaneous with Miller's proof of the Sullivan conjecture, using overlapping unstable-module technology.
- **1987.** Caruso–May–Priddy give an alternative, more structural treatment of the elementary abelian case; Feshbach establishes a compact-Lie version with a corrected statement.
- **2018–present.** The conjecture is recast in the Nikolaus–Scholze formalism: for $G=C_p$, "the Segal conjecture for a ring spectrum $R$" means the cyclotomic Frobenius $\varphi: \mathrm{THH}(R) \to \mathrm{THH}(R)^{tC_p}$ is an equivalence in large degrees. For $R = \mathbb{S}$ this is exactly Lin's theorem.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $G = \mathbb{Z}/2$ | Full isomorphism; $\pi^0_s(B\mathbb{Z}/2) \cong \mathbb{Z}^{\wedge}_2$ | Lin (1980) |
| $G = \mathbb{Z}/p$, $p$ odd | Full isomorphism | Gunawardena (1980) |
| $G = \mathbb{Z}/p^{n}$ | Full isomorphism | Ravenel (1981) |
| $G = (\mathbb{Z}/p)^{n}$, all $n$ | Full isomorphism | Adams–Gunawardena–Miller (1985) |
| All finite $G$ | Theorem | Carlsson (1984) |
| $G$ compact Lie | Modified statement; answer involves the family of subgroups, not a single $I$-completion | Feshbach (1987) |
| $\mathrm{THH}$ form, $R = \mathbb{S}$, $\mathbb{F}_p$, $\mathrm{BP}\langle n\rangle$, $y(n)$ | Frobenius is an equivalence in a range | Nikolaus–Scholze (2018); Angelini-Knoll–Quigley (2021); Hahn–Wilson (2022) |

Degreewise, the $\mathbb{Z}/2$ case reads: $\pi^{-i}_{s}(B\mathbb{Z}/2_{+}) \cong \big(\pi_{i}^{\mathbb{Z}/2}(\mathbb{S})\big)^{\wedge}_{I}$ for all $i \ge 0$, verified against the Adams spectral sequence through the classical stable stems.

## 5. Principal Obstacles

- **The proof is computational, not conceptual.** The elementary abelian case rests on an $\mathrm{Ext}$-group calculation over the Steenrod algebra $A$ (the Singer construction $R_+ M$ and the fact that $\mathrm{Ext}^{s,t}_{A}(R_+\mathbb{F}_p, \mathbb{F}_p) \cong \mathrm{Ext}^{s,t}_{A}(\mathbb{F}_p,\mathbb{F}_p)$ in a shifted range). No proof avoids an Adams spectral sequence input, so the theorem gives little insight into *why* $I$-completion sees $BG$.
- **Compact Lie groups break the naive statement.** For $G = S^{1}$, $A(S^{1}) \cong \mathbb{Z}$, so the left side is essentially trivial, while $\pi^{*}_{s}(BS^{1}_{+}) = \pi^{*}_{s}(\mathbb{CP}^{\infty}_{+})$ is large. Any correct generalization must complete along the whole family of (finite) subgroups; the bookkeeping is the obstruction.
- **Infinite discrete groups.** For $G$ infinite discrete there is no Burnside ring with finite mark homomorphism, and $BG$ can be arbitrarily complicated; even formulating a completion is unclear. This is where the analogy with Baum–Connes / Farrell–Jones stalls.
- **Ranges, not equivalences, in the $\mathrm{THH}$ setting.** For $R$ beyond $\mathbb{S}$ and $\mathbb{F}_p$, the Frobenius $\varphi$ is an equivalence only above a connectivity bound whose size is computed case by case; there is no general criterion on $R$ implying the Segal property.
- **Failure of transfer arguments off the finite case.** Carlsson's induction uses finiteness of the subgroup poset and Sylow transfers; both fail for compact Lie and profinite groups.

## 6. The Gap

For finite groups there is no gap: Carlsson's theorem is the general statement. The live boundary is threefold.

1. **Group-theoretic.** Between "finite $G$" (proved) and "compact Lie / profinite / infinite discrete $G$" (Feshbach's modified theorem; otherwise open). The precise missing step is a completion functor that interpolates between $I$-adic completion at a single group and completion along an infinite family of isotropy subgroups, with an Adams-type convergence statement.
2. **Structural.** Between a $p$-adic $\mathrm{Ext}$ computation and a conceptual proof — e.g. via descent along $\mathbb{S} \to \mathbb{S}^{tC_p}$ or via motivic/synthetic filtrations. Nobody has derived Lin's theorem from a structural principle.
3. **Ring-spectrum-theoretic.** Between "Segal conjecture holds for $\mathrm{BP}\langle n \rangle$ and $y(n)$ in a range" and "Segal conjecture holds for every suitably finite $\mathbb{E}_\infty$-ring of chromatic height $n$", which is the input needed for general redshift statements in algebraic $K$-theory.

## 7. Current Research (as of June 2026)

- **$\mathrm{THH}$/$\mathrm{TC}$ school** (Copenhagen, Bonn, MIT, Münster; Nikolaus, Krause, Hahn, Wilson, Antieau, Bhatt-adjacent groups). The Segal condition is a routine hypothesis in redshift arguments; Hahn–Wilson's proof for $\mathrm{BP}\langle n\rangle$ (Annals 2022) is the reference case. Current effort aims at Segal-type statements for $\mathrm{THH}$ of $p$-adic and prismatic ring spectra. *(frontier — verify)*
- **Chromatic Segal conjectures.** Statements of the form $L_{K(n)}\mathbb{S} \to (L_{K(n)}\mathbb{S})^{tC_p}$, connected to Kuhn's blueshift theorem and to ambidexterity; several 2024–2026 preprints refine the range of degrees. *(frontier — verify)*
- **Motivic and equivariant analogues.** Segal-type completion theorems for motivic sphere spectra over general base fields, extending Gregersen–Rognes-style Singer constructions to the motivic Steenrod algebra. *(frontier — verify)*
- **Profinite and compact Lie refinements.** Continued analysis of Feshbach's family completion, and of Segal-type statements for $p$-compact groups.

## 8. Future Work

- Find a proof of Lin's theorem that does not pass through the Adams $E_2$-term — for example by exhibiting $\mathbb{S}^{\wedge}_p \to \mathbb{S}^{tC_p}$ as a descent/Galois statement in a suitable category.
- Formulate and prove a Segal conjecture for profinite groups $G = \varprojlim G_i$ compatible with continuous cohomology, connecting to Galois descent in $K$-theory.
- Determine an intrinsic finiteness condition on an $\mathbb{E}_\infty$-ring $R$ implying $\mathrm{THH}(R) \to \mathrm{THH}(R)^{tC_p}$ is a high-degree equivalence, replacing case-by-case verification.
- Compute the failure of the naive statement for compact Lie groups quantitatively: describe $\mathrm{coker}(\alpha^*)$ for $G = S^1, SU(2)$ explicitly.

## 9. Key References

- **[Foundational]** G. Segal. *Equivariant stable homotopy theory.* Actes du Congrès International des Mathématiciens (Nice, 1970), Vol. 2, Gauthier-Villars, 1971, pp. 59–63.
- **[Foundational]** M. F. Atiyah and G. Segal. *Equivariant K-theory and completion.* Journal of Differential Geometry 3 (1969), 1–18.
- **[Foundational]** W. H. Lin, D. M. Davis, M. E. Mahowald, J. F. Adams. *Calculation of Lin's Ext groups.* Mathematical Proceedings of the Cambridge Philosophical Society 87 (1980), 459–469.
- **[Foundational]** D. C. Ravenel. *The Segal conjecture for cyclic groups.* Bulletin of the London Mathematical Society 13 (1981), 42–44.
- **[Foundational]** J. F. Adams, J. H. Gunawardena, H. Miller. *The Segal conjecture for elementary abelian $p$-groups.* Topology 24 (1985), 435–460.
- **[Resolution]** G. Carlsson. *Equivariant stable homotopy and Segal's Burnside ring conjecture.* Annals of Mathematics (2) 120 (1984), 189–224.
- **[SOTA / Recent]** J. Caruso, J. P. May, S. B. Priddy. *The Segal conjecture for elementary abelian $p$-groups II: $p$-adic completion in equivariant cohomology.* Topology 26 (1987), 413–433.
- **[SOTA / Recent]** M. Feshbach. *The Segal conjecture for compact Lie groups.* Topology 26 (1987), 1–20.
- **[SOTA / Recent]** T. Nikolaus and P. Scholze. *On topological cyclic homology.* Acta Mathematica 221 (2018), 203–409.
- **[SOTA / Recent]** J. Hahn and D. Wilson. *Redshift and multiplication for truncated Brown–Peterson spectra.* Annals of Mathematics 196 (2022), 1277–1351.
- **[SOTA / Recent]** G. Angelini-Knoll and J. D. Quigley. *The Segal conjecture for topological Hochschild homology of Ravenel spectra.* Journal of Homotopy and Related Structures 16 (2021), 41–60.
- **[Survey]** J. P. C. Greenlees and J. P. May. *Equivariant stable homotopy theory.* In: Handbook of Algebraic Topology, North-Holland, 1995, pp. 277–323.
- **[Survey / Background]** L. G. Lewis, J. P. May, M. Steinberger (with J. E. McClure). *Equivariant Stable Homotopy Theory.* Lecture Notes in Mathematics 1213, Springer, 1986.
- **[Background]** T. tom Dieck. *Transformation Groups.* de Gruyter Studies in Mathematics 8, Walter de Gruyter, 1987.
- **[Companion]** H. Miller. *The Sullivan conjecture on maps from classifying spaces.* Annals of Mathematics (2) 120 (1984), 39–87.

## 10. Worked Example / Concrete Special Case

**Degree $0$, $G = \mathbb{Z}/2$.**

Take $x = [\mathbb{Z}/2]$, the free orbit. Since $\mathbb{Z}/2 \times \mathbb{Z}/2 \cong \mathbb{Z}/2 \sqcup \mathbb{Z}/2$ as $G$-sets, $x^{2} = 2x$, so
$$A(\mathbb{Z}/2) \cong \mathbb{Z}[x]/(x^{2}-2x), \qquad \deg(x) = 2 .$$
The augmentation ideal is $I = (x-2)$, a free $\mathbb{Z}$-module of rank one. Compute
$$(x-2)^{2} = x^{2} - 4x + 4 = 2x - 4x + 4 = -2(x-2),$$
so $I^{n} = 2^{\,n-1} I$ for $n \ge 1$. Hence the $I$-adic topology on $I$ is the $2$-adic topology, and
$$A(\mathbb{Z}/2)^{\wedge}_{I} \;\cong\; \mathbb{Z} \oplus \mathbb{Z}^{\wedge}_{2},$$
where the $\mathbb{Z}$ summand is the image of $\deg$ (split by $1 \mapsto 1$) and $\mathbb{Z}^{\wedge}_{2}$ is $\varprojlim_n I/I^{n} = \varprojlim_n \mathbb{Z}/2^{n-1}$.

On the topological side, $\pi^{0}_{s}(B\mathbb{Z}/2_{+}) = \mathbb{Z} \oplus \pi^{0}_{s}(\mathbb{RP}^{\infty})$, the $\mathbb{Z}$ coming from the disjoint basepoint. The Segal conjecture in degree $0$ therefore predicts
$$\pi^{0}_{s}(\mathbb{RP}^{\infty}) \;\cong\; \mathbb{Z}^{\wedge}_{2}.$$

This is precisely Lin's theorem in degree $0$. Its topological content: with $P_{-n} = \Sigma^\infty \mathbb{RP}^{\infty}_{-n}$ the stunted projective spectra (Thom spectra of $-n$ copies of the tautological line bundle over $\mathbb{RP}^\infty$), the inverse system $\cdots \to P_{-n} \to P_{-n+1} \to \cdots$ satisfies
$$\Big( \varprojlim_{n} P_{-n} \Big)^{\wedge}_{2} \;\simeq\; \big(\mathbb{S}^{-1}\big)^{\wedge}_{2}.$$
A single generator is visible concretely: the transfer $\mathrm{tr}: \Sigma^{\infty}\mathbb{RP}^{\infty}_{+} \to \mathbb{S}$ for the double cover $S^{\infty} \to \mathbb{RP}^{\infty}$ corresponds under $\alpha$ to $x \in A(\mathbb{Z}/2)$, and $\deg(\mathrm{tr}) = 2$ matches $\deg(x)=2$. The $2$-adic completion in the answer is exactly the statement that iterated transfers generate $\pi^{0}_{s}(\mathbb{RP}^{\infty})$ topologically, with $I^{n}$-filtration $= 2^{n-1}$-divisibility. Kahn–Priddy provides the complementary surjection $\pi_{*}^{s}(\mathbb{RP}^{\infty}) \to \pi_{*}^{s}(\mathbb{S})_{(2)}$ in positive degrees, showing the two sides of $\alpha$ are tightly linked in both directions.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*