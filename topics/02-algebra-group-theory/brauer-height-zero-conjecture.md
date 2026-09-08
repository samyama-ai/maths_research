---
id: 02-algebra-group-theory/brauer-height-zero-conjecture
title: "Brauer's Height Zero Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Brauer's Height Zero Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/brauer-height-zero-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G$ be a finite group, $p$ a prime, and $B$ a $p$-block of $G$ with defect group $D$.

**Brauer's Height Zero Conjecture (BHZ).** Every irreducible ordinary character in $B$ has height zero if and only if $D$ is abelian.

Equivalently, writing $|G|_p = p^a$ and $|D| = p^d$: $\chi(1)_p = p^{a-d}$ for all $\chi \in \operatorname{Irr}(B)$ $\iff$ $D$ is abelian.

The conjecture is a *local–global* statement: an invariant of the ordinary character theory of $G$ (a global object) is claimed to detect the isomorphism type — here, commutativity — of a $p$-local subgroup-theoretic object. Stated by Richard Brauer in 1955, it was open for 69 years. A complete proof requires both implications for all finite groups, all primes, and all blocks; both directions are now theorems, but every known proof uses the Classification of Finite Simple Groups (CFSG).

**Status.** Proved. The direction "all heights zero $\Rightarrow$ $D$ abelian" is Kessar–Malle (*Annals*, 2013); the converse "$D$ abelian $\Rightarrow$ all heights zero" was completed by Malle–Navarro–Schaeffer Fry–Tiep (*Annals*, 2024). The page is retained because the quantitative refinements (Eaton–Moretó, Malle–Navarro), the CFSG-free question, and the structural strengthenings remain open.

## 2. Mathematical Foundations

Let $(K, \mathcal{O}, k)$ be a $p$-modular system: $\mathcal{O}$ a complete discrete valuation ring with residue field $k = \mathcal{O}/J(\mathcal{O})$ of characteristic $p$, and $K = \operatorname{Frac}(\mathcal{O})$ of characteristic $0$, both $K$ and $k$ large enough for $G$.

**Blocks.** The group algebra decomposes into indecomposable two-sided ideals,
$$\mathcal{O}G = B_1 \oplus B_2 \oplus \cdots \oplus B_r,$$
corresponding to the primitive idempotents $e_1,\dots,e_r$ of $Z(\mathcal{O}G)$. Each $B_i$ is a **block**. Every $\chi \in \operatorname{Irr}(G)$ and every $\varphi \in \operatorname{IBr}(G)$ lies in exactly one block, giving $\operatorname{Irr}(B)$ and $\operatorname{IBr}(B)$.

**Defect groups.** For a block $B$ with idempotent $e_B$, the defect group $D \le G$ is a minimal subgroup such that $B$ is a direct summand of $\operatorname{Ind}_{D\times D}^{G\times G}$ of a $\mathcal{O}[D\times D]$-module (equivalently, $B$ is $D$-projective as an $\mathcal{O}[G\times G]$-module). $D$ is a $p$-subgroup, determined up to $G$-conjugacy. Write $|D| = p^d$; $d$ is the **defect** of $B$. For the principal block $B_0(G)$ (the one containing the trivial character), $D \in \operatorname{Syl}_p(G)$.

**Heights.** With $|G|_p = p^a$, Brauer's theory gives $\chi(1)_p \ge p^{a-d}$ for all $\chi \in \operatorname{Irr}(B)$. The **height** $h(\chi) \ge 0$ is defined by
$$\chi(1)_p = p^{\,a - d + h(\chi)}.$$
Brauer proved $h(\chi) = 0$ for at least one $\chi \in \operatorname{Irr}(B)$, and $h(\chi) \le d$ always; more sharply $p^{h(\chi)} \le |D : Z(D)|^{1/2}$ in many settings.

**Brauer correspondence.** For $D \le P \le G$ with $N_G(D) \le H \le G$, blocks of $H$ with defect group $D$ correspond bijectively to blocks of $G$ with defect group $D$ (Brauer's first main theorem), via $b \mapsto b^G$. Local–global conjectures compare $B$ with its **Brauer correspondent** $b$ in $N_G(D)$.

**Related conjectures used in the proof.**
- *Alperin–McKay (AM):* $|\operatorname{Irr}_0(B)| = |\operatorname{Irr}_0(b)|$, where $\operatorname{Irr}_0$ denotes height-zero characters and $b$ is the Brauer correspondent in $N_G(D)$.
- *Nilpotent blocks (Broué–Puig, Puig):* if $B$ is nilpotent with defect group $D$, then $B$ is Morita equivalent to $\mathcal{O}D$, so $\operatorname{Irr}(B)$ is in bijection with $\operatorname{Irr}(D)$ and $k(B) = k(D)$, $l(B)=1$.
- *Knörr / Külshammer–Puig:* control of blocks under normal subgroups and central extensions, used in all reduction arguments.

**Generalizations (still open).** Eaton–Moretó conjecture: for a block $B$ with defect group $D$, the minimal positive height in $\operatorname{Irr}(B)$ equals the minimal positive height in $\operatorname{Irr}(D)$. Malle–Navarro: $B$ has a unique height, i.e. $\operatorname{Irr}(B)$ has bounded height data, relates to $|D:D'|$.

## 3. History & State of the Art (SOTA)

- **1955.** Brauer states the conjecture at the Tokyo–Nikko symposium on algebraic number theory (published 1956), in a list of problems on group representations; it appears again in his 1963 problem list ("Problem 12" and neighbours).
- **1959.** Brauer–Feit-style height bounds and the cyclic-defect theory (Brauer, Dade 1966) settle blocks with cyclic $D$: there heights are all zero iff $|D| = p$, consistent with BHZ.
- **1984.** Gluck–Wolf prove the key character-theoretic theorem for $p$-solvable groups: if $\chi(1)_p$ divides $\theta(1)_p \cdot |G:N|_p$-type constraints hold over normal subgroups then Sylow subgroups are abelian. This yields BHZ for $p$-solvable $G$.
- **1988.** Berger–Knörr reduce the direction "$D$ abelian $\Rightarrow$ heights zero" to quasi-simple groups — the first genuine reduction theorem for BHZ.
- **2013.** Kessar–Malle, *Quasi-isolated blocks and Brauer's height zero conjecture* (*Annals of Math.* 178), prove the direction **"all heights zero $\Rightarrow$ $D$ abelian"** for all finite groups, by verifying it for quasi-simple groups — the hard case being quasi-isolated blocks of groups of Lie type, handled with Lusztig's Jordan decomposition and Bonnafé–Rouquier Morita equivalences.
- **2013.** Navarro–Tiep (*Annals of Math.* 178) prove BHZ for $2$-blocks of maximal defect: $P \in \operatorname{Syl}_2(G)$ is abelian iff all $\chi \in \operatorname{Irr}(B_0(G))$ have odd degree.
- **2014.** Navarro–Späth (*J. Eur. Math. Soc.*) reduce the remaining direction "$D$ abelian $\Rightarrow$ heights zero" to the **inductive Alperin–McKay condition** for simple groups.
- **2017.** Kessar–Malle verify BHZ for all blocks of quasi-simple groups (*J. Algebra* 475).
- **2022.** Ruhstorfer proves the inductive AM condition at $p=2$ for groups of Lie type in defining characteristic, removing the largest remaining family.
- **2024.** Malle–Navarro–Schaeffer Fry–Tiep, *Brauer's Height Zero Conjecture* (*Annals of Math.* 200), complete the proof, with $p=2$ the last case.

## 4. Partial Results / Verified Cases

Cases proved before the general theorem, each still the standard reference for its class:

| Class | Result | Source |
|---|---|---|
| $D$ cyclic | Full block theory known; $k(B)=e+ (|D|-1)/e$, heights zero iff $|D|=p$ | Dade (1966) |
| $p$-solvable $G$ | Both directions | Gluck–Wolf (1984) + Berger–Knörr (1988) |
| Nilpotent blocks | $B \sim_{\mathrm{Morita}} \mathcal{O}D$, so BHZ is $\operatorname{Irr}(D)$ linear iff $D$ abelian | Broué–Puig (1980), Puig (1988) |
| $p$-solvable, $D$ abelian | Heights zero via Fong reduction | Fong; Gluck–Wolf |
| Direction "$\Rightarrow$" (heights zero forces $D$ abelian), all $G$, all $p$ | Theorem | Kessar–Malle (2013) |
| $p=2$, maximal defect ($D \in \operatorname{Syl}_2(G)$) | Theorem | Navarro–Tiep (2013) |
| Blocks of quasi-simple groups, all $p$ | Theorem | Kessar–Malle (2013, 2017) |
| $|D| \le p^3$; defect $\le 2$; $D$ metacyclic, $D \cong D_8, Q_8, SD_{16}$ | Explicit block classifications confirm BHZ | Sambale (2014), Brauer, Olsson |
| $p$-blocks with $D$ abelian and $|D| \le p^4$, small $k(B)$ | Computational verification in GAP/Magma character-table libraries | Sambale; Breuer's block library |
| Symmetric groups $S_n$, all $p$ | Abacus/core combinatorics gives heights explicitly; $D$ abelian iff $n < p^2$ in the relevant weight range ($w<p$) | Olsson; James–Kerber |
| General $G$, all $p$ (both directions) | Theorem, conditional on CFSG | Malle–Navarro–Schaeffer Fry–Tiep (2024) |

## 5. Principal Obstacles

- **No direct bridge from characters to $D$.** Heights are computed from $\chi(1)_p$, a global datum; $D$ is defined by a relative-projectivity condition. No functorial construction takes $\operatorname{Irr}(B)$ to $D$, so every proof proceeds by reduction plus classification, never by an intrinsic argument.
- **Reduction leaves a hard residue.** Berger–Knörr and Navarro–Späth reduce to quasi-simple groups, but the resulting statement is *not* BHZ for simple groups; it is the inductive AM condition, which asks for an $\operatorname{Aut}(S)$-equivariant, cohomology-compatible bijection $\operatorname{Irr}_0(B) \to \operatorname{Irr}_0(b)$ preserving Clifford-theoretic data. Verifying this needs precise control of character extensions to $\operatorname{Aut}(S)$ and of the associated $2$-cocycles.
- **Groups of Lie type at $p=2$.** For $S$ of Lie type in defining characteristic $p=2$, Deligne–Lusztig theory does not give the unipotent blocks in the form needed; automorphism groups include graph and field automorphisms whose action on $\operatorname{Irr}_0$ was unknown. This was the last blocking obstruction and needed Ruhstorfer's new equivariant Jordan-decomposition machinery.
- **Quasi-isolated blocks.** For $\ell$-blocks of exceptional groups $E_7, E_8, F_4$, blocks with quasi-isolated defect data resist Bonnafé–Rouquier reduction to Levi subgroups; Kessar–Malle had to compute them case by case for $\ell \in \{2,3,5\}$.
- **CFSG dependence.** Every step of the reduction assumes CFSG; no non-classification proof is known even for $p$-solvable groups beyond Gluck–Wolf, which itself uses CFSG-dependent results on orbit sizes in coprime actions.
- **Fusion-theoretic invisibility.** Heights are not invariants of the fusion system $\mathcal{F}_D(G)$ alone; blocks with isomorphic fusion systems can have different height distributions, so the local theory of fusion systems cannot detect BHZ on its own.

## 6. The Gap

For BHZ itself the gap is closed. The residual gaps are:

1. **CFSG-free proof.** No argument for either direction avoids the classification, even in the maximal-defect case. Closing this requires an intrinsic mechanism linking $\chi(1)_p$ to commutativity of $D$.
2. **Alperin–McKay in general.** MNST's proof at $p=2$ uses the inductive AM condition only for the relevant families; the full inductive AM condition for all simple groups and all primes is still unverified, so AM itself remains open.
3. **Quantitative refinement.** BHZ says: minimal positive height exists iff $D$ nonabelian. Eaton–Moretó predicts *which* height: $\min\{h(\chi) > 0 : \chi \in \operatorname{Irr}(B)\} = \min\{h(\psi) > 0 : \psi \in \operatorname{Irr}(D)\}$. Only the "$\le$" inequality is known in special cases; no reduction theorem to simple groups exists for it.
4. **Structural strengthening.** Whether "all heights zero" forces a Morita or derived equivalence between $B$ and its Brauer correspondent (Broué's abelian defect group conjecture) is open and strictly stronger.

## 7. Current Research (as of June 2026)

- **Kaiserslautern / Valencia / Rutgers–Denver axis.** Malle, Navarro, Schaeffer Fry and Tiep continue with the block-theoretic consequences of the 2024 theorem: characterizing $D' $, $|D:Z(D)|$ and nilpotency of $B$ by degree divisibility in $\operatorname{Irr}(B)$.
- **Inductive conditions.** Späth's programme on inductive AM/McKay–Navarro conditions for all simple groups; Ruhstorfer's equivariant Jordan decomposition and Bonnafé–Dat–Rouquier's Morita equivalences are the main tools. Verification for exceptional types at bad primes is the active frontier *(frontier — verify)*.
- **Eaton–Moretó.** Partial results for $p$-solvable groups and for principal blocks; work by Moretó, Sambale, and Rizo on lower bounds for $k(B)$ and height distributions.
- **Fusion systems and $\ell$-blocks.** Kessar–Linckelmann's work on Külshammer–Puig classes and the "block $\Rightarrow$ fusion + cohomology class" paradigm, aiming at Donovan's and Broué's conjectures.
- **Computational verification.** Breuer's GAP block libraries and Sambale's tables continue to test the refined conjectures for $|D| \le p^5$.

## 8. Future Work

- Find a proof of the "abelian $\Rightarrow$ height zero" direction that does not route through AM, ideally via a Morita-theoretic invariant of $B$.
- Complete the inductive AM condition for all simple groups; this would give the Alperin–McKay conjecture and re-derive BHZ uniformly for all $p$.
- Prove a reduction theorem for the Eaton–Moretó conjecture analogous to Navarro–Späth's for BHZ.
- Determine whether $B$ with all heights zero must be *isotypic* to its Brauer correspondent (a case of Broué's conjecture), which would upgrade the numerical statement to a categorical one.
- Explore whether the derived length or nilpotency class of $D$ is read off from the multiset $\{h(\chi)\}$, as Brauer's Problem 12 asks.

## 9. Key References

- **[Foundational]** R. Brauer. *Number theoretical investigations on groups of finite order.* Proceedings of the International Symposium on Algebraic Number Theory, Tokyo & Nikko 1955, Science Council of Japan, 1956, pp. 55–62.
- **[Foundational]** R. Brauer. *Representations of finite groups.* In: Lectures on Modern Mathematics, Vol. I, Wiley, 1963, pp. 133–175.
- **[Foundational]** T. R. Berger, R. Knörr. *On Brauer's height 0 conjecture.* Nagoya Mathematical Journal 109 (1988), 109–116.
- **[Foundational]** D. Gluck, T. R. Wolf. *Defect groups and character heights in blocks of solvable groups, II.* Journal of Algebra 87 (1984), 222–246.
- **[Foundational]** M. Broué, L. Puig. *A Frobenius theorem for blocks.* Inventiones Mathematicae 56 (1980), 117–128.
- **[SOTA / Recent]** G. Malle, G. Navarro, A. A. Schaeffer Fry, P. H. Tiep. *Brauer's Height Zero Conjecture.* Annals of Mathematics 200 (2024), 557–608. arXiv:2209.04736.
- **[SOTA / Recent]** R. Kessar, G. Malle. *Quasi-isolated blocks and Brauer's height zero conjecture.* Annals of Mathematics 178 (2013), 321–384.
- **[SOTA / Recent]** R. Kessar, G. Malle. *Brauer's height zero conjecture for quasi-simple groups.* Journal of Algebra 475 (2017), 43–60.
- **[SOTA / Recent]** G. Navarro, B. Späth. *On Brauer's height zero conjecture.* Journal of the European Mathematical Society 16 (2014), 695–747.
- **[SOTA / Recent]** G. Navarro, P. H. Tiep. *Characters of relative $p'$-degree over normal subgroups.* Annals of Mathematics 178 (2013), 1135–1171.
- **[SOTA / Recent]** L. Ruhstorfer. *The Alperin–McKay conjecture for the prime 2.* Preprint, arXiv:2204.06373, 2022.
- **[Survey]** B. Sambale. *Blocks of Finite Groups and Their Invariants.* Lecture Notes in Mathematics 2127, Springer, 2014.
- **[Survey]** G. Navarro. *Character Theory and the McKay Conjecture.* Cambridge Studies in Advanced Mathematics 175, Cambridge University Press, 2018.
- **[Survey]** C. W. Eaton, A. Moretó. *Extending Brauer's height zero conjecture to blocks with nonabelian defect groups.* International Mathematics Research Notices 2014, no. 20, 5581–5601.

## 10. Worked Example / Concrete Special Case

Take $p = 2$ and compare two groups of order divisible by $8$.

**(a) $G = A_5$, $p = 2$.** $|G| = 60 = 2^2 \cdot 3 \cdot 5$, so $a = 2$ and $P \in \operatorname{Syl}_2(A_5)$ is the Klein four-group $V_4$ — abelian. Character degrees: $1, 3, 3, 4, 5$. The principal $2$-block $B_0$ contains $\{1, 3, 3, 5\}$ (the degree-$4$ character is $2$-defect zero and forms its own block with $D=1$). Defect group of $B_0$ is $P$, so $d = 2$ and
$$\chi(1)_2 = 2^{\,a-d+h(\chi)} = 2^{h(\chi)}.$$
Since $1, 3, 3, 5$ are all odd, $h(\chi) = 0$ for every $\chi \in \operatorname{Irr}(B_0)$. BHZ predicts exactly this from $P$ abelian. ✔

**(b) $G = SL_2(3)$, $p = 2$.** $|G| = 24 = 2^3 \cdot 3$, $a = 3$, and $P \in \operatorname{Syl}_2(G)$ is the quaternion group $Q_8$ — nonabelian. Degrees: $1,1,1,2,2,2,3$. The principal $2$-block is the unique block of full defect $d=3$ and contains all characters except the degree-$3$ one (which has $2$-defect zero: $3$ is odd but $\chi(1)_2 = 1 = 2^{a-d}$ only if $d = 3$; in fact $\operatorname{Irr}(B_0) = \{1,1,1,2,2,2\}$ and the degree-$3$ character lies in a block of defect $0$ — no: $3 \nmid$ ... here $\chi(1)_2 = 1$, and $\chi$ lies in the block of defect $3$ as well, giving $k(B_0)=7$ for the unique $2$-block of $SL_2(3)$, since $O_2(G) = Q_8$ forces a single $2$-block). Heights: for $\chi(1) \in \{1,1,1,3\}$, $h = 0$; for $\chi(1) = 2$, $\chi(1)_2 = 2 = 2^{3-3+1}$, so $h(\chi) = 1 > 0$. A positive height appears, matching BHZ's prediction from $Q_8$ nonabelian. ✔

**Reading the conjecture off (b).** $Q_8$ has $\operatorname{Irr}(Q_8)$ with degrees $1,1,1,1,2$, so the minimal positive height in the defect group is $1$; the minimal positive height in $B_0$ is also $1$. This equality is exactly what the Eaton–Moretó refinement asserts in general and what remains open — BHZ only guarantees that *some* positive height occurs, not that it equals $1$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*