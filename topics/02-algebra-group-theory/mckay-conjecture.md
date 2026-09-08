---
id: 02-algebra-group-theory/mckay-conjecture
title: "McKay Conjecture"
topic: 02-algebra-group-theory
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# McKay Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/mckay-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G$ be a finite group, $p$ a prime, and $P \in \mathrm{Syl}_p(G)$ a Sylow $p$-subgroup. Write $\mathrm{Irr}(G)$ for the set of irreducible ordinary (complex) characters of $G$, and
$$\mathrm{Irr}_{p'}(G) \;=\; \{\chi \in \mathrm{Irr}(G) \;:\; p \nmid \chi(1)\}.$$

**McKay Conjecture.** For every finite group $G$ and every prime $p$,
$$|\mathrm{Irr}_{p'}(G)| \;=\; |\mathrm{Irr}_{p'}(N_G(P))|.$$

The count of irreducible characters of degree prime to $p$ is a purely local invariant: it is determined by the normalizer of a Sylow $p$-subgroup. A complete proof must establish the equality for all finite groups; a disproof requires one explicit pair $(G,p)$ with unequal counts.

**Status note.** Cabanes and Späth announced a proof in 2024, completing the Isaacs–Malle–Navarro reduction programme by verifying the inductive McKay condition for all finite simple groups. The page is marked *partially-solved* because that proof is still under referee scrutiny at the time of writing, and because the standard refinements (Alperin–McKay, blockwise and Galois versions, Dade's conjecture) remain open.

## 2. Mathematical Foundations

**Characters.** For $\chi \in \mathrm{Irr}(G)$, $\chi(1) \mid |G|$, and $\sum_{\chi \in \mathrm{Irr}(G)} \chi(1)^2 = |G|$. Writing $|G|_p$ for the $p$-part, the *$p$-defect* of $\chi$ is $d(\chi)$ with $\chi(1)_p = |G|_p / p^{d(\chi)}$; so $\mathrm{Irr}_{p'}(G)$ is exactly the set of characters of maximal defect $d(\chi) = \log_p |G|_p$.

**Blocks.** $\mathrm{Irr}(G)$ partitions into $p$-blocks $B$, each with a defect group $D \leq G$ determined up to conjugacy. The Brauer correspondence $B \mapsto b$ sends blocks of $G$ with defect group $D$ to blocks of $N_G(D)$. Writing $\mathrm{Irr}_0(B)$ for the height-zero characters of $B$ (those $\chi \in \mathrm{Irr}(B)$ with $\chi(1)_p = |G:D|_p$), the **Alperin–McKay conjecture** asserts
$$|\mathrm{Irr}_0(B)| \;=\; |\mathrm{Irr}_0(b)|,$$
which reduces to McKay on summing over blocks of maximal defect (defect group $P$), since $\mathrm{Irr}_{p'}(G) = \bigsqcup_{B: D(B)=P} \mathrm{Irr}_0(B)$.

**Galois refinement (Navarro, 2004).** Let $\mathcal{G} = \mathrm{Gal}(\mathbb{Q}_{|G|}/\mathbb{Q})$ and, for $p$-power root of unity data, let $\mathcal{H} \leq \mathcal{G}$ be the subgroup of $\sigma$ acting on $p'$-roots of unity by $\zeta \mapsto \zeta^{p^k}$ for some integer $k$. Navarro conjectured the McKay bijection can be chosen $\mathcal{H}$-equivariant:
$$\left|\mathrm{Irr}_{p'}(G)^{\sigma}\right| = \left|\mathrm{Irr}_{p'}(N_G(P))^{\sigma}\right| \quad \text{for all } \sigma \in \mathcal{H}.$$

**Reduction machinery.** For $S$ a finite non-abelian simple group with universal covering group $X$, and $Q \in \mathrm{Syl}_p(X)$, the *inductive McKay condition* $\mathrm{iMK}(S,p)$ requires an $\mathrm{Aut}(X)_Q$-equivariant bijection
$$\Omega : \mathrm{Irr}_{p'}(X) \longrightarrow \mathrm{Irr}_{p'}(N_X(Q))$$
compatible with central characters and with Clifford theory: for each $\chi$, the character triples $(\mathrm{Aut}(X)_{Q,\chi} \ltimes X, X, \chi)$ and $(\mathrm{Aut}(X)_{Q,\chi} \ltimes N_X(Q), N_X(Q), \Omega(\chi))$ must be *order-preserving isomorphic*, written $\chi \sim_X \Omega(\chi)$. The relation $\sim$ controls extendability and the behaviour of characters in arbitrary overgroups.

**Theorem (Isaacs–Malle–Navarro, 2007).** If every finite non-abelian simple group $S$ with $p \mid |S|$ satisfies $\mathrm{iMK}(S,p)$, then the McKay conjecture holds for all finite groups at $p$.

This converts a statement about all finite groups into a checklist over the classification of finite simple groups (CFSG).

## 3. History & State of the Art (SOTA)

- **1972.** John McKay observes, for simple groups with cyclic or small Sylow $2$-subgroups, that the number of odd-degree irreducible characters matches that of the Sylow normalizer (*Irreducible representations of odd degree*, J. Algebra 20).
- **1970s.** Alperin extends the statement to all primes and to blocks (Alperin–McKay), placing it in the emerging "local–global" family alongside Brauer's height-zero conjecture and later Alperin's weight conjecture and Dade's conjectures.
- **1976–1990s.** Verification for $p$-solvable groups (Okuyama–Wajima; Wolf), symmetric and general linear groups (Olsson; Fong), and extensive checks against the ATLAS.
- **2004.** Navarro's Galois refinement, which implies e.g. that $|G:N_G(P)|$-type field-of-values data is also local.
- **2007.** Isaacs–Malle–Navarro reduction theorem (Invent. Math. 170) — the pivot of the modern programme.
- **2013.** Späth's reduction theorem for the Alperin–McKay conjecture (Crelle 680) and the blockwise inductive condition.
- **2016.** Malle–Späth prove the McKay conjecture for $p = 2$ in full (Ann. of Math. 184).
- **2017–2023.** Inductive condition verified type-by-type for groups of Lie type: type $A$ and type $C$ (Cabanes–Späth), defining characteristic (Späth 2012; completed by Ruhstorfer), and successive reductions of the remaining classical/exceptional cases via Jordan decomposition of characters and Deligne–Lusztig theory.
- **2024.** Cabanes–Späth announce the verification of $\mathrm{iMK}(S,p)$ for all remaining simple groups, hence a proof of the McKay conjecture for all finite groups and all primes.

## 4. Partial Results / Verified Cases

Unconditionally established cases (independent of the 2024 announcement):

| Class | Result |
|---|---|
| $p$-solvable $G$ | Okuyama–Wajima (1979); Wolf (1978) — bijection built from Isaacs' $B_\pi$-theory |
| $p = 2$, all $G$ | Malle–Späth (2016): $\mathrm{iMK}(S,2)$ for all simple $S$ |
| Abelian Sylow $p$-subgroup | Follows from Broué's abelian defect conjecture where known; verified for blocks with cyclic defect via Dade's theory |
| Cyclic Sylow $p$-subgroup | Classical: Brauer tree theory gives $|\mathrm{Irr}_0(B)| = e + (p^d-1)/e$ on both sides |
| $\mathfrak{S}_n$, $\mathfrak{A}_n$, covering groups | Olsson (1976) via hook/core combinatorics and the Macdonald formula for $|\mathrm{Irr}_{p'}(\mathfrak{S}_n)|$ |
| $\mathrm{GL}_n(q)$, $\mathrm{U}_n(q)$, $p \nmid q$ | Fong–Srinivasan block theory; Cabanes–Späth for the inductive condition in type $A$ (Crelle 728, 2017) |
| Groups of Lie type, defining characteristic $p \mid q$ | Späth (Bull. LMS 44, 2012); Ruhstorfer for the Galois-equivariant refinement |
| Sporadic groups, Tits group | Case-by-case computation (GAP/ATLAS character tables), all 26 sporadics, all primes |
| $|G| < 10^{10}$ scale checks | Verified computationally over the small-groups library and simple-group tables |

Blockwise: the Alperin–McKay conjecture is known for $p$-solvable groups, blocks with cyclic defect groups, symmetric groups, and — via Kessar–Malle's proof of Brauer's height-zero conjecture (Ann. of Math. 178, 2013, one direction; the converse completed 2024 by Malle–Navarro–Schaeffer Fry–Tiep) — for large families of abelian-defect blocks.

## 5. Principal Obstacles

- **No canonical bijection.** McKay asserts equality of cardinalities; no natural map $\mathrm{Irr}_{p'}(G) \to \mathrm{Irr}_{p'}(N_G(P))$ is known in general. Character-theoretic invariants (fields of values, degrees mod $p$) match only conjecturally, so counting arguments cannot be replaced by construction.
- **Failure of induction/restriction.** $N_G(P)$ is not a "large" subgroup in any Mackey-theoretic sense: induction from $N_G(P)$ to $G$ does not preserve irreducibility, and $\mathrm{Irr}_{p'}$ is not stable under standard functors. Brauer character theory sees only $p$-modular data and loses the ordinary degrees.
- **Equivariance is the real difficulty.** The reduction demands bijections commuting with $\mathrm{Aut}(X)_Q$, including diagonal, field and graph automorphisms of groups of Lie type. Jordan decomposition of characters $\mathrm{Irr}(G^F) \leftrightarrow \bigsqcup_{(s)} \mathrm{Irr}(C_{G^*}(s)^{F})$ is not known to be canonical enough to be automorphism-equivariant; disconnected centralizers and the action on Lusztig series obstruct it.
- **Clifford theory obstructions.** The relation $\chi \sim_X \Omega(\chi)$ requires control of projective representations and cohomology classes in $H^2$, which are hard to compute for covering groups of Lie type with non-trivial Schur multipliers ($\mathrm{SL}_n(q)$, $E_6$, $E_7$, exceptional multipliers).
- **CFSG-dependence.** Every route currently known passes through the classification; no structural or character-variety proof exists.

## 6. The Gap

The reduction (Section 2) is a theorem; the residue is entirely the simple-group checklist. Concretely, the gap that had to be crossed after 2016 was:

> For each simple group of Lie type $S = G^F/Z$ in non-defining characteristic $p \nmid q$, construct an $\mathrm{Aut}(X)_Q$-equivariant bijection $\mathrm{Irr}_{p'}(X) \to \mathrm{Irr}_{p'}(N_X(Q))$ satisfying $\sim_X$, uniformly in the Lusztig series and compatible with $e$-Harish-Chandra theory for $e = \mathrm{ord}_p(q)$.

The Cabanes–Späth argument supplies this by combining Broué–Malle–Michel $e$-Harish-Chandra series with a refined Jordan decomposition whose equivariance is controlled by regular embeddings. The open gap now shifts one level up: the same programme for the *blockwise* inductive conditions (Alperin–McKay, Alperin weight, Dade), where local data must be tracked block-by-block rather than only at maximal defect, remains unfinished.

## 7. Current Research (as of June 2026)

- **Refereeing and consolidation** of the Cabanes–Späth proof; expository accounts and simplifications of the type-$D$/$E$ equivariance arguments *(frontier — verify)*.
- **Alperin–McKay and Galois–McKay.** Navarro–Späth–Vallejo's reduction for the Galois–McKay ("Navarro") conjecture (Trans. AMS, 2020) is being pushed through the Lie-type cases by Ruhstorfer, Schaeffer Fry, and collaborators; the $p=2$ case is complete.
- **Ruhstorfer's Jordan decomposition for Alperin–McKay** (Adv. Math., 2022) is the main engine for the blockwise programme.
- **Categorical upgrades.** Broué's abelian defect group conjecture, via derived equivalences and Deligne–Lusztig varieties (Bonnafé–Dat–Rouquier, "Derived categories and Deligne–Lusztig varieties II", Ann. of Math. 185, 2017), would yield McKay-type equalities as shadows of equivalences.
- **Groups:** Bochum (Späth, Malle-school), Paris (Cabanes), Valencia (Navarro), Rutgers (Tiep), Denver/ICERM (Schaeffer Fry), Kaiserslautern.

## 8. Future Work

- Prove the inductive Alperin–McKay and inductive Alperin weight conditions for all simple groups, closing the blockwise analogues.
- Establish Dade's projective conjecture, which implies all of the above; a reduction to simple groups exists (Späth) but the simple-group verification is far from complete.
- Find a *canonical* bijection — ideally functorial or arising from a derived equivalence — replacing case analysis, which would remove CFSG-dependence.
- Extend equivariant Jordan decomposition to a genuine categorical statement about $\ell$-adic cohomology of Deligne–Lusztig varieties.
- Explore consequences: local characterizations of Sylow structure (e.g. $|\mathrm{Irr}_{p'}(G)| = p$ iff $P$ cyclic of order $p$ type results).

## 9. Key References

- **[Foundational]** J. McKay. *Irreducible representations of odd degree.* Journal of Algebra **20** (1972), 416–418. [DOI](https://doi.org/10.1016/0021-8693(72)90066-x)
- **[Foundational]** J. L. Alperin. *The main problem of block theory.* In Proceedings of the Conference on Finite Groups (Park City, Utah, 1975), Academic Press, 1976, 341–356. [DOI](https://doi.org/10.1016/b978-0-12-633650-4.50025-4)
- **[Foundational]** I. M. Isaacs. *Character Theory of Finite Groups.* Academic Press, 1976.
- **[Foundational]** G. Navarro. *Characters and Blocks of Finite Groups.* LMS Lecture Note Series 250, Cambridge University Press, 1998.
- **[Key]** I. M. Isaacs, G. Malle, G. Navarro. *A reduction theorem for the McKay conjecture.* Inventiones Mathematicae **170** (2007), 33–101. [DOI](https://doi.org/10.1007/s00222-007-0057-y)
- **[Key]** G. Navarro. *The McKay conjecture and Galois automorphisms.* Annals of Mathematics **160** (2004), 1129–1140. [DOI](https://doi.org/10.4007/annals.2004.160.1129)
- **[Key]** G. Malle, B. Späth. *Characters of odd degree.* Annals of Mathematics **184** (2016), 869–908. [DOI](https://doi.org/10.4007/annals.2016.184.3.6)
- **[Key]** B. Späth. *A reduction theorem for the Alperin–McKay conjecture.* Journal für die reine und angewandte Mathematik (Crelle) **680** (2013), 153–189. [DOI](https://doi.org/10.1515/crelle.2012.035)
- **[SOTA / Recent]** M. Cabanes, B. Späth. *Equivariant character correspondences and inductive McKay condition for type A.* Journal für die reine und angewandte Mathematik (Crelle) **728** (2017), 153–194.
- **[SOTA / Recent]** M. Cabanes, B. Späth. *The McKay conjecture on character degrees.* Preprint, arXiv, 2024.
- **[SOTA / Recent]** L. Ruhstorfer. *Jordan decomposition for the Alperin–McKay conjecture.* Advances in Mathematics **394** (2022), 108031. [DOI](https://doi.org/10.1016/j.aim.2021.108031)
- **[SOTA / Recent]** R. Kessar, G. Malle. *Quasi-isolated blocks and Brauer's height zero conjecture.* Annals of Mathematics **178** (2013), 321–384. [DOI](https://doi.org/10.4007/annals.2013.178.1.6)
- **[Survey]** B. Späth. *Reduction theorems for some global–local conjectures.* In *Local Representation Theory and Simple Groups*, EMS Series of Lectures in Mathematics, European Mathematical Society, 2018, 23–61. [DOI](https://doi.org/10.4171/185-1/2)
- **[Survey]** G. Malle. *Local–global conjectures in the representation theory of finite groups.* In *Representation Theory — Current Trends and Perspectives*, EMS, 2017, 519–539. [DOI](https://doi.org/10.4171/171-1/17)

## 10. Worked Example / Concrete Special Case

Take $G = A_5$, $|G| = 60 = 2^2 \cdot 3 \cdot 5$. Character degrees: $\mathrm{Irr}(A_5) = \{1, 3, 3', 4, 5\}$.

**Case $p = 2$.** $|G|_2 = 4$, and $P \cong C_2 \times C_2$ (generated by $(12)(34)$, $(13)(24)$). Its normalizer is $N_G(P) = A_4$ of order $12$.
- Odd-degree characters of $G$: degrees $1, 3, 3, 5$ — so $|\mathrm{Irr}_{2'}(A_5)| = 4$.
- $\mathrm{Irr}(A_4)$ has degrees $1,1,1,3$ (three linear characters from $A_4/V_4 \cong C_3$, plus the $3$-dimensional one). All odd: $|\mathrm{Irr}_{2'}(A_4)| = 4$. ✔

**Case $p = 5$.** $P = \langle (12345)\rangle \cong C_5$, $N_G(P) \cong D_{10}$ of order $10$.
- Characters of $A_5$ of degree prime to $5$: $1, 3, 3, 4$ — four of them.
- $\mathrm{Irr}(D_{10})$ has degrees $1, 1, 2, 2$; all prime to $5$: four. ✔

**Case $p = 3$.** $P \cong C_3$, $N_G(P) \cong S_3$. Degrees prime to $3$: $1, 4, 5$ — three. $\mathrm{Irr}(S_3)$ has degrees $1,1,2$ — three. ✔

**Why it is not automatic.** For $p=2$ the correspondence is not degree-preserving: $\{1,3,3,5\}$ on the left versus $\{1,1,1,3\}$ on the right. No naive restriction map works either — restricting the degree-$5$ character of $A_5$ to $A_4$ gives $\chi_1 + \chi_3$ (a sum), and restricting the degree-$4$ character gives $1 + \chi_3$. Only the *counts* agree. In block language, $A_5$ at $p=2$ has one block of full defect containing $\{1,3,3,5\}$ plus a defect-zero block $\{4\}$ (degree $4 = |G|_2 \cdot 1$), so $\mathrm{Irr}_0(B) = \mathrm{Irr}_{2'}(A_5)$ has size $4$, matching $\mathrm{Irr}_0(b)$ for the principal block of $A_4$ — the Alperin–McKay statement in miniature.

Verifying $\mathrm{iMK}(A_5, 2)$ additionally requires the bijection to commute with $\mathrm{Aut}(A_5) = S_5$: the two degree-$3$ characters are swapped by the transposition-induced outer automorphism, and correspondingly two of the three linear characters of $A_4$ (the non-trivial ones, complex-conjugate under $S_4$) are swapped. Choosing $1 \mapsto 1_{A_4}$, $5 \mapsto \chi_3$, and $\{3, 3'\} \mapsto \{\lambda, \bar\lambda\}$ gives an $S_5$-equivariant bijection, which is exactly the kind of matching that becomes intractable for groups of Lie type of large rank.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*