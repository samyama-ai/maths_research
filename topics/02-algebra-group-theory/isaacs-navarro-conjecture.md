---
id: 02-algebra-group-theory/isaacs-navarro-conjecture
title: "Isaacs-Navarro Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Isaacs-Navarro Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/isaacs-navarro-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite group, $p$ a prime, $P \in \mathrm{Syl}_p(G)$ and $N = N_G(P)$. Write
$$\mathrm{Irr}_{p'}(G) = \{\chi \in \mathrm{Irr}(G) : p \nmid \chi(1)\}.$$
The McKay conjecture asserts $|\mathrm{Irr}_{p'}(G)| = |\mathrm{Irr}_{p'}(N)|$. Isaacs and Navarro (2002) conjectured that this bijection can be taken to preserve character degrees modulo $p$ up to sign. For an integer $k$ set
$$\mathcal{M}_k(G) = \{\chi \in \mathrm{Irr}_{p'}(G) : \chi(1) \equiv \pm k \pmod p\}.$$

**Conjecture (Isaacs–Navarro).** For every finite group $G$, every prime $p$ and every integer $k$,
$$|\mathcal{M}_k(G)| \;=\; |\mathcal{M}_k(N_G(P))|.$$

Equivalently, there is a bijection $\Omega : \mathrm{Irr}_{p'}(G) \to \mathrm{Irr}_{p'}(N)$ with $\Omega(\chi)(1) \equiv \pm \chi(1) \pmod p$ for all $\chi$. A proof must produce such a bijection (or the counting identity) for all $G$; a disproof requires a single $G$, $p$, $k$ with unequal counts.

The statement is vacuous for $p = 2$ (all $p'$-degrees are $\equiv 1$) and for $p = 3$ (all $p'$-degrees are $\equiv \pm 1$), so it has content only for $p \ge 5$, where $k$ ranges over $1, \dots, (p-1)/2$.

## 2. Mathematical Foundations

**Characters.** $\mathrm{Irr}(G)$ is the set of irreducible $\mathbb{C}$-characters; $\sum_{\chi \in \mathrm{Irr}(G)} \chi(1)^2 = |G|$ and $\chi(1) \mid |G|$.

**Blocks.** $\mathrm{Irr}(G)$ partitions into $p$-blocks $B$ with defect groups $D \le_G P$. If $|G|_p = p^a$ and $|D| = p^d$, every $\chi \in \mathrm{Irr}(B)$ satisfies $\chi(1)_p = p^{a-d+h(\chi)}$ with $h(\chi) \ge 0$ the *height*. Write $\mathrm{Irr}_0(B)$ for the height-zero characters. Brauer's first main theorem gives a bijection $B \mapsto b$ between blocks of $G$ with defect group $D$ and blocks of $N_G(D)$ with defect group $D$.

**Blockwise (Alperin–McKay) refinement.** For a block $B$ with defect group $D$ and Brauer correspondent $b$ in $N_G(D)$, put
$$\mathcal{M}_k(B) = \Big\{\chi \in \mathrm{Irr}_0(B) : \frac{\chi(1)}{p^{\,a-d}} \equiv \pm k \pmod p \Big\}.$$
Isaacs and Navarro also conjecture $|\mathcal{M}_k(B)| = |\mathcal{M}_k(b)|$, which refines Alperin–McKay ($|\mathrm{Irr}_0(B)| = |\mathrm{Irr}_0(b)|$) exactly as the global form refines McKay. Taking $B$ over all blocks of maximal defect recovers Section 1.

**Why $\pm$ and not $=$.** A strict congruence $\Omega(\chi)(1) \equiv \chi(1) \pmod p$ fails: for $G = \mathrm{SL}_2(5)$, $p=5$, $G$ has $p'$-degrees $1,2,3,4$ while $N = P \rtimes C_4$ of order $20$ has $p'$-degrees $1,1,1,1,4$ — the multisets of residues differ, but the multisets of $\pm$-classes do not. The sign ambiguity is intrinsic and matches the $\pm$ appearing in degree formulas for groups of Lie type (Weyl-group signs, $\varepsilon_G = (-1)^{\sigma(G)}$ in Deligne–Lusztig theory) and in the hook-length formula for $S_n$.

**Related refinements.** Isaacs–Navarro also proposed a $p$-adic strengthening comparing $\chi(1)_{p'}$ and $\Omega(\chi)(1)_{p'}$ modulo $p$ together with fields of values; Navarro's Galois–McKay conjecture instead requires $\Omega$ to commute with a suitable $\sigma \in \mathrm{Gal}(\mathbb{Q}_{|G|}/\mathbb{Q})$. These are logically distinct refinements of McKay.

## 3. History & State of the Art (SOTA)

- **1972.** McKay observes $|\mathrm{Irr}_{2'}(G)| = |\mathrm{Irr}_{2'}(N_G(P))|$ for simple groups; Alperin and Isaacs extend the statement to arbitrary $G$ and all primes.
- **1973.** Isaacs proves McKay for groups of odd order, via a canonical $\pi$-special correspondence.
- **2002.** Isaacs and Navarro, *New refinements of the McKay conjecture for arbitrary finite groups* (Ann. of Math. 156), state the $\pm k$ refinement, prove it for $p$-solvable groups, and verify it computationally for the sporadic simple groups and other small cases.
- **2004.** Navarro states the Galois refinement (Ann. of Math. 160), an independent strengthening.
- **2007.** Isaacs, Malle and Navarro reduce McKay to an inductive condition on simple groups (Invent. Math. 170). Späth (2013) supplies the analogous reduction for Alperin–McKay.
- **2016.** Malle and Späth prove McKay for $p = 2$ (Ann. of Math. 184) — a case where the Isaacs–Navarro refinement carries no extra information.
- **2024–2025.** Cabanes and Späth announce a proof of the McKay conjecture for all primes. This does **not** settle Isaacs–Navarro: the bijections produced are not controlled modulo $p$ on degrees.

State of the art: the conjecture is a theorem for $p$-solvable groups and verified for large libraries of simple and quasi-simple groups; no reduction theorem to simple groups in the style of Isaacs–Malle–Navarro has been published for the $\pm k$ refinement.

## 4. Partial Results / Verified Cases

- **$p$-solvable groups:** proved by Isaacs and Navarro (2002), using the Glauberman/Isaacs correspondence and $\pi$-special character theory. Turull (2008) strengthened the $p$-solvable case to a correspondence preserving local Schur indices and fields of values, which implies the degree congruence.
- **$p = 2$ and $p = 3$:** trivially equivalent to McKay, hence theorems (Malle–Späth 2016 for $p=2$; the $p=3$ case follows from McKay, now available via Cabanes–Späth).
- **Blocks of defect zero and defect one:** for defect zero $\mathrm{Irr}_0(B)$ is a singleton on both sides; for cyclic defect groups the Brauer-tree description of $\mathrm{Irr}_0(B)$ (Dade) gives $e$ exceptional-free characters with degrees congruent modulo $p$ to $\pm$ the corresponding degrees in $N_G(D)$, so the blockwise form holds.
- **Sporadic groups:** verified for all 26 sporadic simple groups and their automorphism groups by direct computation in GAP/CHEVIE character-table libraries.
- **Symmetric and alternating groups:** the $p'$-degree characters of $S_n$ are indexed by partitions with empty $p$-core removed iteratively (Macdonald's criterion: $p \nmid \chi_\lambda(1)$ iff the base-$p$ digits of the hook structure are compatible), and the resulting degrees satisfy the required $\pm k$ matching against $N_{S_n}(P) \cong (C_p \wr \cdots) \rtimes \dots$; the conjecture is known here for all $n$ and all $p$.
- **Groups of Lie type:** verified for $\mathrm{GL}_n(q)$, $\mathrm{SL}_2(q)$, $\mathrm{PSL}_2(q)$, groups of small rank, and for $p$ the defining characteristic (where $N = B$, a Borel subgroup, and $\mathrm{Irr}_{p'}(G)$ consists of the semisimple characters, whose degrees are $\equiv \pm 1$ or explicitly computable modulo $p$).
- **Self-normalizing Sylow case:** if $N_G(P) = P$ with $P$ abelian of order $p$, both sides have $p-1$ characters distributed evenly across the $(p-1)/2$ classes $\{\pm k\}$.

## 5. Principal Obstacles

- **No reduction theorem.** McKay was cracked by reducing to an *inductive McKay condition* on simple groups, checkable case by case. For the $\pm k$ refinement, the Clifford-theoretic bookkeeping must additionally track degrees modulo $p$ through central extensions and through $\mathrm{Aut}(S)$-equivariance. Degrees multiply by ramification indices $e$ and by orbit lengths $|A : A_\chi|$ under induction/restriction; these factors are $p'$-integers but need not be $\pm 1$ modulo $p$, so the congruence is not preserved by the standard Clifford-correspondence steps.
- **Bijections are non-canonical.** All known proofs of McKay for large classes produce bijections via Jordan decomposition or via $d$-Harish-Chandra series, defined only up to choices. Degrees are then controlled only up to unipotent-degree factors $\pm |W|_{p'}$-type expressions, and existing arguments do not pin down the residue.
- **Deligne–Lusztig degrees modulo $p$.** For $G$ of Lie type in non-defining characteristic $p \mid q^e - 1$, $\chi(1)$ is a product of cyclotomic-polynomial values $\Phi_i(q)$ and unipotent degrees; reducing such products modulo $p$ requires evaluating $\Phi_i(q) \bmod p$ where $q$ has order $e$ modulo $p$. This is arithmetically delicate and depends on $e$, $p$ and the isogeny type simultaneously — a uniform computation is missing.
- **The sign is not intrinsic.** Because only $\pm k$ is asserted, no cohomological or Galois-theoretic invariant is available to *predict* the sign; one cannot bootstrap from a single "correct" normalization.
- **Character-theoretic tools are degree-blind.** Brauer's second main theorem, Dade's cyclic-defect theory and the Broué perfect-isometry framework control heights, fields of values and generalized decomposition numbers, but perfect isometries only preserve degrees up to a global sign per block — exactly the ambiguity the conjecture wants to exploit, yet they give no control for non-abelian defect groups.

## 6. The Gap

Proved: the $p$-solvable case, the small primes, cyclic-defect blocks, and a long but finite list of simple groups. Asserted: all finite groups, all primes $p \ge 5$, all $k$.

The precise missing step is an **inductive Isaacs–Navarro condition** for a simple group $S$ — a statement about $\mathrm{Irr}_{p'}(S)$, its $\mathrm{Aut}(S)$-action, its Schur multiplier, and degrees modulo $p$ — together with a proof that this condition for every simple group implies the conjecture for every finite group. Two sub-gaps:

1. **Clifford theory modulo $p$.** Show that the congruence class $\pm \chi(1) \bmod p$ is stable under the induction/extension operations used in the McKay reduction, or identify a corrected invariant that is.
2. **Uniform Lie-type verification.** Compute $\chi(1) \bmod p$ for all $\chi \in \mathrm{Irr}_{p'}(G^F)$ and all $\psi \in \mathrm{Irr}_{p'}(N_{G^F}(P))$ in terms of $e = \mathrm{ord}_p(q)$ and the relative Weyl group $W(\Phi_e)$, uniformly in the root datum.

## 7. Current Research (as of June 2026)

- **Wuppertal school (Späth, Ruhstorfer, and collaborators)** and **Paris (Cabanes)** — after the announced proof of McKay (Cabanes–Späth, arXiv 2024) the machinery of $e$-Harish-Chandra series and $\ell$-adic equivariance is being revisited to see which refinements the same bijections carry. *(frontier — verify)* Whether the Cabanes–Späth bijections can be normalized to satisfy the $\pm k$ congruence is open.
- **Valencia (Navarro, Rizo, Vallejo, Val Ors)** — Galois-theoretic refinements, $p$-rationality of $p'$-degree characters, and the interaction between the Galois–McKay and Isaacs–Navarro statements. No general implication either way is known *(frontier — verify)*.
- **Kaiserslautern (Malle)** — height-zero characters of Lie-type groups and explicit degree congruences; the main source of Lie-type verifications.
- **Computational verification** via GAP, CHEVIE and the CTblLib character-table library continues to extend the checked range to quasi-simple groups of moderate rank.
- Blockwise strengthenings tied to Brauer's height-zero conjecture (proved by Malle–Kessar–Schacht–Späth for the remaining direction, 2024) are being tested for compatibility with $\mathcal{M}_k(B)$ counts *(frontier — verify)*.

## 8. Future Work

- Formulate and prove a reduction theorem: "if every finite non-abelian simple group satisfies the inductive Isaacs–Navarro condition, the conjecture holds." This is the consensus prerequisite, mirroring Isaacs–Malle–Navarro (2007).
- Determine the logical relations among McKay, Galois–McKay, Isaacs–Navarro and Turull's Schur-index refinement — in particular whether the Galois–McKay conjecture implies the $\pm k$ counts for $p \ge 5$.
- Establish the blockwise form for abelian defect groups, where Broué's abelian defect group conjecture predicts a derived equivalence that should induce a degree-congruent bijection on height-zero characters.
- Produce a uniform Lie-type degree computation modulo $p$ in terms of $e$ and $\Phi_e$-tori, replacing case-by-case checks.
- Extend computer verification to all quasi-simple groups of Lie rank $\le 4$ for $5 \le p \le 100$.

## 9. Key References

- **[Foundational]** I. M. Isaacs, G. Navarro. *New refinements of the McKay conjecture for arbitrary finite groups.* Annals of Mathematics (2) **156** (2002), 333–344. [DOI](https://doi.org/10.2307/3597192)
- **[Foundational]** J. McKay. *Irreducible representations of odd degree.* Journal of Algebra **20** (1972), 416–418. [DOI](https://doi.org/10.1016/0021-8693(72)90066-x)
- **[Foundational]** I. M. Isaacs. *Character Theory of Finite Groups.* Academic Press, 1976 (reprinted AMS Chelsea, 2006).
- **[Structural]** I. M. Isaacs, G. Malle, G. Navarro. *A reduction theorem for the McKay conjecture.* Inventiones Mathematicae **170** (2007), 33–101. [DOI](https://doi.org/10.1007/s00222-007-0057-y)
- **[Related refinement]** G. Navarro. *The McKay conjecture and Galois automorphisms.* Annals of Mathematics (2) **160** (2004), 1129–1140. [DOI](https://doi.org/10.4007/annals.2004.160.1129)
- **[Related refinement]** A. Turull. *Strengthening the McKay conjecture to include local fields and local Schur indices.* Journal of Algebra **319** (2008), 4853–4868. [DOI](https://doi.org/10.1016/j.jalgebra.2005.12.035)
- **[SOTA]** G. Malle, B. Späth. *Characters of odd degree.* Annals of Mathematics (2) **184** (2016), 869–908. [DOI](https://doi.org/10.4007/annals.2016.184.3.6)
- **[SOTA]** B. Späth. *A reduction theorem for the Alperin–McKay conjecture.* Journal für die reine und angewandte Mathematik **680** (2013), 153–189. [DOI](https://doi.org/10.1515/crelle.2012.035)
- **[SOTA / frontier]** M. Cabanes, B. Späth. *The McKay Conjecture on character degrees.* Preprint, arXiv:2410.20392 (2024).
- **[Survey]** G. Navarro. *Character Theory and the McKay Conjecture.* Cambridge Studies in Advanced Mathematics **175**, Cambridge University Press, 2018.
- **[Survey]** G. Malle. *Height 0 characters of finite groups of Lie type.* Representation Theory **11** (2007), 192–220. [DOI](https://doi.org/10.1090/s1088-4165-07-00312-3)
- **[Background]** I. G. Macdonald. *On the degrees of the irreducible representations of symmetric groups.* Bulletin of the London Mathematical Society **3** (1971), 189–192. [DOI](https://doi.org/10.1112/blms/3.2.189)

## 10. Worked Example / Concrete Special Case

**$G = A_5$, $p = 5$.** $|G| = 60 = 2^2 \cdot 3 \cdot 5$, so $P = \langle (12345) \rangle \cong C_5$ and $N = N_G(P) \cong D_{10}$ of order $10$.

Character degrees of $A_5$: $1, 3, 3, 4, 5$. Removing the degree divisible by $5$:
$$\mathrm{Irr}_{5'}(A_5) \text{ has degrees } 1,\,3,\,3,\,4 .$$
$D_{10}$ has degrees $1, 1, 2, 2$, all prime to $5$. McKay: $4 = 4$. ✓

Now sort by $\pm k$ modulo $5$, with $k \in \{1,2\}$:

| $\pm k \bmod 5$ | degrees in $A_5$ | $|\mathcal{M}_k(A_5)|$ | degrees in $D_{10}$ | $|\mathcal{M}_k(D_{10})|$ |
|---|---|---|---|---|
| $\pm 1 \equiv \{1,4\}$ | $1,\;4$ | 2 | $1,\;1$ | 2 |
| $\pm 2 \equiv \{2,3\}$ | $3,\;3$ | 2 | $2,\;2$ | 2 |

Both classes match, so the Isaacs–Navarro conjecture holds for $(A_5, 5)$. Note that the *unsigned* refinement fails: $A_5$ has no $5'$-degree character with degree $\equiv 2$, while $D_{10}$ has two — the $\pm$ is essential.

**Second check: $G = \mathrm{PSL}_2(7)$, $p = 7$.** $|G| = 168$, degrees $1,3,3,6,7,8$; $N_G(P) = C_7 \rtimes C_3$ of order $21$ with degrees $1,1,1,3,3$. Both sides have five $7'$-degree characters.

- $\pm 1 \equiv \{1,6\} \pmod 7$: $G$ contributes $1, 6, 8$ (since $8 \equiv 1$) $\Rightarrow 3$; $N$ contributes $1,1,1 \Rightarrow 3$.
- $\pm 2 \equiv \{2,5\}$: $0$ on both sides.
- $\pm 3 \equiv \{3,4\}$: $G$ contributes $3,3 \Rightarrow 2$; $N$ contributes $3,3 \Rightarrow 2$.

The counts agree class by class. Any explicit bijection must send $\{1,6,8\} \to \{1,1,1\}$ and $\{3,3\} \to \{3,3\}$; the conjecture asserts such a matching exists for every finite group, with no known construction in general.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*