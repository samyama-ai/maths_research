---
id: 02-algebra-group-theory/mullineux-conjecture
title: "Mullineux Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mullineux Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/mullineux-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $p$ be a prime and $F$ a field of characteristic $p$. The irreducible $F\mathfrak{S}_n$-modules are the modules $D^\lambda$ indexed by $p$-regular partitions $\lambda \vdash n$ (partitions with no part repeated $p$ or more times). Tensoring with the sign representation $\mathrm{sgn}$ permutes the irreducibles, so there is an involution $\lambda \mapsto \mathsf{m}_p(\lambda)$ on $p$-regular partitions with

$$D^\lambda \otimes \mathrm{sgn} \;\cong\; D^{\mathsf{m}_p(\lambda)}.$$

**Mullineux's conjecture (1979).** The involution $\mathsf{m}_p$ is computed by an explicit combinatorial algorithm on Young diagrams — the *Mullineux map* $M_p$ defined by successive removal of $p$-rims and the transformation of the resulting *Mullineux symbol* (Section 2). That is, $\mathsf{m}_p = M_p$ for all primes $p$ and all $n$.

A complete solution requires a proof that the representation-theoretic involution agrees with the purely combinatorial map for every $p$ and $n$; a disproof would exhibit one $p$-regular $\lambda$ with $D^\lambda\otimes\mathrm{sgn}\not\cong D^{M_p(\lambda)}$. **The conjecture is a theorem** (Ford–Kleshchev, 1997). What remains open are its analogues and refinements: spin/super versions, higher-level Ariki–Koike versions, and structural questions about fixed points and $\ell$-adic behaviour.

## 2. Mathematical Foundations

**Partitions and diagrams.** For $\lambda=(\lambda_1\ge\lambda_2\ge\cdots)\vdash n$, the Young diagram is $[\lambda]=\{(i,j): 1\le j\le \lambda_i\}$. The **rim** of $\lambda$ is
$$R(\lambda)=\{(i,j)\in[\lambda] : (i+1,j+1)\notin[\lambda]\},$$
read as a lattice path from the rightmost node of row 1 down to the last node of the last row.

**The $p$-rim.** Traverse $R(\lambda)$ in that order. The first $p$-segment is the first $p$ nodes met; each subsequent segment begins with the first rim node lying in a row strictly below the last row used by the previous segment, and again takes up to $p$ nodes. The **$p$-rim** $R_p(\lambda)$ is the union of all segments. Set
$$a_1=|R_p(\lambda)|,\qquad r_1=\\#\{\text{rows meeting } R_p(\lambda)\}.$$
Removing $R_p(\lambda)$ leaves a partition; iterating until the empty partition produces the **Mullineux symbol**
$$G_p(\lambda)=\begin{pmatrix} a_1 & a_2 & \cdots & a_k\\ r_1 & r_2 & \cdots & r_k\end{pmatrix},\qquad \sum_i a_i=n .$$
Mullineux showed $G_p$ is a bijection from $p$-regular partitions of $n$ onto symbols satisfying $a_i-a_{i+1}\ge r_i-r_{i+1}\ge 0$, $0\le a_i - a_{i+1} < p$ (with $0<a_k$, $r_k\ge 1$).

**The Mullineux map.** Define $M_p(\lambda)$ to be the $p$-regular partition with
$$G_p\bigl(M_p(\lambda)\bigr)=\begin{pmatrix} a_1 & \cdots & a_k\\ s_1 & \cdots & s_k\end{pmatrix},\qquad s_i=a_i-r_i+\varepsilon_i,\quad \varepsilon_i=\begin{cases}0,& p\mid a_i,\\ 1,& p\nmid a_i.\end{cases}$$
$M_p$ is an involution, preserves the $p$-core up to conjugation, and satisfies $M_p(\lambda)=\lambda'$ (conjugate) when $\lambda$ has at most $p-1$ parts or $\lambda_1 \le p-1$.

**The Kleshchev map.** Give node $(i,j)$ the residue $\mathrm{res}(i,j)\equiv j-i \pmod p$. Kleshchev's modular branching rules define **good** removable nodes of each residue; $D^\lambda\!\downarrow_{\mathfrak{S}_{n-1}}$ has socle $\bigoplus_i D^{\lambda - A_i}$ over good nodes $A_i$. Recursively removing good nodes gives a residue sequence $(i_1,\dots,i_n)$, and one defines $\mathsf{K}_p(\lambda)$ as the partition with the negated sequence $(-i_1,\dots,-i_n)$. Branching theory gives immediately $D^\lambda\otimes\mathrm{sgn}\cong D^{\mathsf{K}_p(\lambda)}$, so the conjecture is equivalent to the *purely combinatorial* identity
$$M_p=\mathsf{K}_p .$$
In crystal language, $\mathsf{K}_p$ is the unique automorphism of the $\widehat{\mathfrak{sl}}_p$-crystal $B(\Lambda_0)$ induced by the Dynkin diagram automorphism $i\mapsto -i$.

## 3. History & State of the Art (SOTA)

- **1979.** Glyn Mullineux, in two *J. London Math. Soc.* papers, defines $M_p$ via $p$-rims and Mullineux symbols, proves it is an involution preserving $p$-cores, and conjectures $\mathsf{m}_p = M_p$ on the basis of small-$n$ computations.
- **1980s.** Verified by machine for small $n$ and small $p$; Mullineux symbols become a standard combinatorial tool.
- **1991.** Andrews–Olsson prove a partition identity (the *Andrews–Olsson identity*) motivated by counting $M_p$-fixed points, linking the map to additive number theory.
- **1994–1996.** Bessenrodt–Olsson develop residue symbols, an alternative encoding in which $M_p$ becomes a simple "swap and shift" operation. Kleshchev (1995–96) proves the branching rules and reduces the conjecture to $M_p=\mathsf{K}_p$.
- **1997 — solution.** Ford and Kleshchev, *A proof of the Mullineux conjecture* (*Math. Z.* 226), prove the combinatorial identity using an induction on $p$-rim structure combined with the branching rules. Independently, Xu (1997, 1999) supplies a combinatorial verification of the key recursion.
- **1998–1999.** Bessenrodt–Olsson give a shorter residue-symbol proof; Bessenrodt–Olsson–Xu extend to consequences for Schur modules and Hecke algebras at roots of unity.
- **2003.** Brundan–Kujawa give a conceptually different proof via Schur–Weyl duality for the queer Lie superalgebra $\mathfrak{q}(n)$ and $\mathfrak{gl}(m|n)$, realising the sign twist as a symmetry of a superalgebra category.
- **Since.** The map is standard in the graded (KLR/quiver Hecke) theory; Fayers has given a systematic modern treatment relating $M_p$ to regularisation and to the "$p$-restricted vs. $p$-regular" dictionary.

## 4. Partial Results / Verified Cases

- **Full theorem:** all primes $p$, all $n$ (Ford–Kleshchev 1997); reproved by Bessenrodt–Olsson (1998), Brundan–Kujawa (2003).
- **Elementary cases proved by Mullineux (1979):** $\lambda$ with at most $p-1$ rows, or $\lambda_1\le p-1$, where $M_p(\lambda)=\lambda'$; $p$-cores; hook partitions.
- **$p=2$:** trivial, since $\mathrm{sgn}$ is the trivial module and $M_2=\mathrm{id}$.
- **Fixed points:** $M_p(\lambda)=\lambda$ characterises exactly those $D^\lambda$ ($p$ odd) that split on restriction to $\mathfrak{A}_n$ into two non-isomorphic irreducibles (Ford, Benson). The number of $M_p$-fixed $p$-regular partitions of $n$ is governed by Andrews–Olsson-type identities (Andrews–Olsson 1991; Bessenrodt 1991).
- **Hecke algebras:** the analogue for $\mathcal{H}_n(q)$ at a primitive $e$-th root of unity, with $\mathsf{m}_e$ given by $M_e$ ($e$ replacing $p$, $e$ not necessarily prime), holds — proved by Brundan (1998) and via Bessenrodt–Olsson–Xu.
- **Ariki–Koike / higher level:** Jacon–Lecouvey describe the Mullineux involution for $\mathcal{H}_{n}(q;Q_1,\dots,Q_\ell)$ via crystal isomorphisms; the level-1 case reduces to $M_e$.
- **Computation:** $M_p$ is $O(n)$-time from the Mullineux symbol and has been tabulated for $n\le 100$ and all $p\le n$ in standard decomposition-matrix packages (GAP, Magma).

## 5. Principal Obstacles

The historical difficulty, and the residual difficulty in the open analogues, is a *mismatch of granularity*:

- **$p$-rims are global; good nodes are local.** $M_p$ strips $O(p)$-sized rim segments and only records the pair $(a_i,r_i)$; $\mathsf{K}_p$ removes one node at a time and tracks a residue word. No naive induction on $n$ relates them: removing a good node can change the whole Mullineux symbol non-locally.
- **Loss of the character-theoretic handle.** Over $\mathbb{C}$, $S^\lambda\otimes\mathrm{sgn}\cong S^{\lambda'}$ is proved by characters. In characteristic $p$ there is no character theory for the $D^\lambda$; decomposition matrices are themselves unknown in general, so the sign twist cannot be read off from Brauer characters.
- **Conjugation is not available.** $\lambda'$ is usually not $p$-regular, so $M_p$ must be a genuine deformation of transposition; the "correction" terms $\varepsilon_i$ have no representation-theoretic interpretation in isolation.
- **Non-functoriality of the sign twist in super settings.** For double covers $\tilde{\mathfrak{S}}_n$ and quiver Hecke *super*algebras, the sign twist interacts with the $\mathbb{Z}/2$-grading and with type M/Q self-associate modules, so an involution on $p$-bar-regular partitions may pair modules of different types — precisely where clean statements are still incomplete.

## 6. The Gap

For the classical statement, there is no gap: $M_p=\mathsf{K}_p$ is proved. The remaining boundary is:

1. **Spin/projective analogue.** For $\tilde{\mathfrak{S}}_n$ in odd characteristic $p$, irreducible spin modules are indexed by $p$-strict restricted partitions. A Mullineux-type combinatorial description of the sign twist, and of the associated crystal automorphism for $\widehat{\mathfrak{sl}}$ of twisted type $A_{p-1}^{(2)}$, is only partially available.
2. **Explicit closed forms.** No formula computes $M_p(\lambda)$ from $\lambda$ without the iterative $p$-rim (or crystal) recursion; a "one-shot" description would likely yield new information on decomposition numbers.
3. **Fixed-point bijections.** A canonical, statistic-preserving bijection between self-conjugate partitions and $M_p$-fixed $p$-regular partitions of $n$, explaining the Andrews–Olsson identity representation-theoretically, is not fully settled.

## 7. Current Research (as of June 2026)

- **Graded/KLR reformulations.** The Mullineux map is the shadow of the sign automorphism of the cyclotomic KLR algebra $R^{\Lambda_0}_n$; work at Oregon (Kleshchev's school), Queen Mary (Fayers), and Sydney (Mathas) studies how it interacts with graded decomposition numbers and homogeneous cellular bases. *(frontier — verify)*
- **Fayers' systematic account.** Fayers' "regularisation and the Mullineux map" programme relates $M_p$ to Jantzen–Schaper filtrations and to the $\ell$-restricted/regular dictionary, giving new proofs of Mullineux-symbol identities. *(frontier — verify)*
- **Super and spin.** Kleshchev–Livesey and collaborators continue the study of RoCK blocks of double covers, where the analogue of the sign twist and Mullineux-type combinatorics is being pinned down. *(frontier — verify)*
- **Higher-level crystals.** Jacon–Lecouvey's crystal-isomorphism approach continues to be extended to Ariki–Koike and to affine type via canonical bases.
- **Combinatorics of fixed points.** Bijective proofs of the Andrews–Olsson identity and explicit maps between self-conjugate and self-Mullineux partitions remain an active small-scale topic. *(frontier — verify)*

## 8. Future Work

- Produce a spin analogue: a combinatorial involution on $p$-strict restricted partitions realising $\mathrm{sgn}$-twist for $\tilde{\mathfrak{S}}_n$-supermodules, with a proof at the level of twisted-type crystals.
- Determine how $M_p$ acts on *graded* decomposition numbers: is there a symmetry $d_{\lambda\mu}(v)=d_{M(\lambda)\,M(\mu)}(v)$ compatible with the grading (known in special cases; general statement open)?
- Find a non-recursive formula for $M_p$, e.g. through abaci or $p$-quotients, that also computes the effect on Specht filtrations.
- Extend the Brundan–Kujawa superalgebra proof to give a categorification of the involution, i.e. an explicit equivalence of categories inducing $M_p$ on simples.

## 9. Key References

- **[Foundational]** G. Mullineux. *Bijections of $p$-regular partitions and $p$-modular irreducibles of the symmetric groups.* J. London Math. Soc. (2) **20** (1979), 60–66. [DOI](https://doi.org/10.1112/jlms/s2-20.1.60)
- **[Foundational]** G. Mullineux. *On the $p$-cores of $p$-regular diagrams.* J. London Math. Soc. (2) **20** (1979), 222–226. [DOI](https://doi.org/10.1112/jlms/s2-20.2.222)
- **[Foundational]** G. James. *The Representation Theory of the Symmetric Groups.* Lecture Notes in Mathematics 682, Springer, 1978.
- **[Solution]** B. Ford, A. S. Kleshchev. *A proof of the Mullineux conjecture.* Mathematische Zeitschrift **226** (1997), 267–308. [DOI](https://doi.org/10.1007/pl00004340)
- **[Key step]** A. S. Kleshchev. *Branching rules for modular representations of symmetric groups III: some corollaries and a problem of Mullineux.* J. London Math. Soc. (2) **54** (1996), 25–38. [DOI](https://doi.org/10.1112/jlms/54.1.25)
- **[Alternative proof]** C. Bessenrodt, J. B. Olsson. *On residue symbols and the Mullineux conjecture.* J. Algebraic Combinatorics **7** (1998), 227–251. [DOI](https://doi.org/10.1023/a:1008618621557)
- **[Alternative proof]** M. Xu. *On Mullineux' conjecture in the representation theory of symmetric groups.* Communications in Algebra **25** (1997), 1797–1803. [DOI](https://doi.org/10.1080/00927879708825953)
- **[Super-algebraic proof]** J. Brundan, J. Kujawa. *A new proof of the Mullineux conjecture.* J. Algebraic Combinatorics **18** (2003), 13–39. [DOI](https://doi.org/10.1023/a:1025113308552)
- **[Related]** C. Bessenrodt, J. B. Olsson, M. Xu. *On properties of the Mullineux map with an application to Schur modules.* Math. Proc. Cambridge Philos. Soc. **126** (1999), 443–459. [DOI](https://doi.org/10.1017/s0305004199003424)
- **[Combinatorics]** G. E. Andrews, J. B. Olsson. *Partition identities with an application to group representation theory.* J. reine angew. Math. **413** (1991), 198–212. [DOI](https://doi.org/10.1515/crll.1991.413.198)
- **[Higher level]** N. Jacon, C. Lecouvey. *On the Mullineux involution for Ariki–Koike algebras.* Journal of Algebra **321** (2009), 2156–2170. [DOI](https://doi.org/10.1016/j.jalgebra.2008.09.033)
- **[Survey / textbook]** A. S. Kleshchev. *Linear and Projective Representations of Symmetric Groups.* Cambridge Tracts in Mathematics 163, Cambridge University Press, 2005.

## 10. Worked Example / Concrete Special Case

Take $p=3$, $n=4$. The $3$-regular partitions of $4$ are $(4),(3,1),(2,2),(2,1,1)$.

**Mullineux symbol of $(4)$.** The rim is the whole row, read $(1,4),(1,3),(1,2),(1,1)$. The first $3$-segment is $\{(1,4),(1,3),(1,2)\}$; it ends in row 1, and there is no row below, so $R_3((4))$ has $a_1=3$, $r_1=1$. Removing it leaves $(1)$, giving $a_2=1$, $r_2=1$:
$$G_3\bigl((4)\bigr)=\begin{pmatrix}3&1\\1&1\end{pmatrix}.$$
Apply the rule: $3\mid a_1=3\Rightarrow \varepsilon_1=0$, $s_1=3-1+0=2$; $3\nmid a_2=1\Rightarrow\varepsilon_2=1$, $s_2=1-1+1=1$. So
$$G_3\bigl(M_3((4))\bigr)=\begin{pmatrix}3&1\\2&1\end{pmatrix}.$$
**Decode.** For $(2,2)$: the rim is $(1,2),(2,2),(2,1)$ (node $(1,1)$ is not on the rim since $(2,2)\in[\lambda]$), so the $3$-rim is all three nodes over $2$ rows, $a_1=3$, $r_1=2$; the remainder is $(1)$, giving $a_2=1,r_2=1$ — the same symbol. Hence $M_3((4))=(2,2)$.

**Check against representation theory.** $D^{(4)}$ is the trivial module. $S^{(2,2)}$ is the $2$-dimensional representation inflated from $\mathfrak{S}_3$; mod $3$ it is uniserial with factors trivial and sign, so $D^{(2,2)}\cong\mathrm{sgn}$. Thus $D^{(4)}\otimes\mathrm{sgn}\cong D^{(2,2)}$, matching $M_3$. ✓

**The other pair.** $[(2,1,1)]$ has rim $=$ all four nodes, read $(1,2),(1,1),(2,1),(3,1)$: first segment $\{(1,2),(1,1),(2,1)\}$, then a second segment starting in row 3 with the single node $(3,1)$, so $a_1=4$, $r_1=3$ and $G_3=\binom{4}{3}$. Since $3\nmid 4$, $\varepsilon_1=1$ and $s_1=4-3+1=2$, giving $\binom{4}{2}$. For $(3,1)$ the rim is $(1,3),(1,2),(1,1),(2,1)$; the first segment is the three row-1 nodes, the second is $(2,1)$, so $a_1=4$, $r_1=2$ — symbol $\binom{4}{2}$. Hence $M_3((2,1,1))=(3,1)$, and indeed the two $3$-dimensional simples of $F\mathfrak{S}_4$ are interchanged by $\mathrm{sgn}$.

**Kleshchev side (same instance).** Residues $j-i \bmod 3$ on $[(4)]$ are $0,1,2,0$. Removing good nodes gives the residue word $(0,2,1,0)$; negating mod $3$ gives $(0,1,2,0)$, and rebuilding by adding good nodes $(1,1)\to(1,2)\to(2,1)\to(2,2)$ with residues $0,1,2,0$ yields $(2,2)$ — the same answer, illustrating $M_3=\mathsf{K}_3$ in this case.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*