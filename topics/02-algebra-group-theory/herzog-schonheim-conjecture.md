---
id: 02-algebra-group-theory/herzog-schonheim-conjecture
title: "Herzog-Schonheim Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Herzog–Schönheim Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/herzog-schonheim-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a group and let $H_1,\dots,H_k$ be subgroups of finite index with $k>1$. Suppose the left cosets
$$G=\bigsqcup_{i=1}^{k} a_iH_i ,\qquad a_iH_i\cap a_jH_j=\varnothing\ (i\neq j),$$
form a **partition** (an exact, or disjoint, cover) of $G$.

**Conjecture (Herzog–Schönheim, 1974).** The indices $n_i=[G:H_i]$ cannot be pairwise distinct; i.e. there exist $i\neq j$ with $[G:H_i]=[G:H_j]$.

A proof must handle every group and every such partition. A disproof requires one explicit group $G$, subgroups $H_1,\dots,H_k$ and coset representatives $a_1,\dots,a_k$ with $k>1$, distinct indices, and $G=\bigsqcup a_iH_i$. The subgroups need not be normal and need not be distinct as sets; only the index multiset is at issue.

## 2. Mathematical Foundations

**Coset partitions.** For $H\le G$ with $[G:H]=n<\infty$, a left coset $aH$ has "density" $1/n$ in the sense of the normalised counting measure on any finite quotient through which it factors. Counting in a finite group, or Neumann's lemma in general, gives the **Mirsky–Newman relation**
$$\sum_{i=1}^{k}\frac{1}{[G:H_i]}=1 .$$
If additionally the $n_i$ are pairwise distinct, then $(n_1<\dots<n_k)$ is a **strict Egyptian-fraction representation of $1$**, forcing $n_1=2$ and $k\ge 3$ (since $1/2+1/3<1$ and $1/2+1/3+1/6=1$).

**Reduction to finite groups.** Put $H=\bigcap_{i=1}^k H_i$; then $[G:H]<\infty$, and the normal core
$$N=\operatorname{Core}_G(H)=\bigcap_{g\in G} gHg^{-1}$$
is normal of finite index with $N\le H_i$ for all $i$. Since each $H_i$ is a union of cosets of $N$, the partition descends to
$$G/N=\bigsqcup_{i=1}^{k}\overline{a_i}\,(H_i/N),\qquad [G/N:H_i/N]=[G:H_i].$$
Hence **the conjecture for all groups is equivalent to the conjecture for finite groups**.

**Neumann's lemma** (B. H. Neumann, 1954). If $G=\bigcup_{i=1}^k a_iH_i$ then the cosets with $[G:H_i]=\infty$ may be deleted and the cover still holds; moreover $[G:\bigcap_{[G:H_i]<\infty}H_i]<\infty$. This justifies the finite-index hypothesis being harmless rather than restrictive.

**The classical case $G=\mathbb{Z}$.** Subgroups of finite index are $n\mathbb{Z}$, cosets are residue classes $a\bmod n$. A partition is an *exact covering system*. The **Davenport–Mirsky–Newman–Rado theorem** states that in any exact cover of $\mathbb Z$ by $k>1$ classes, the largest modulus occurs at least twice. Proof sketch: for $|z|<1$,
$$\frac{1}{1-z}=\sum_{i=1}^{k}\frac{z^{a_i}}{1-z^{n_i}} .$$
If the largest modulus $n_k$ were unique, letting $z\to e^{2\pi i/n_k}$ makes exactly one term on the right blow up while the left side and all other terms stay bounded — contradiction. This is the archetype the general conjecture asks to replicate.

**Subnormality.** $H\le G$ is *subnormal* if there is a chain $H=H_0\trianglelefteq H_1\trianglelefteq\dots\trianglelefteq H_r=G$. In a finite nilpotent group every subgroup is subnormal; subnormality is the technical hypothesis under which the $\mathbb{Z}$-style induction survives.

## 3. History & State of the Art (SOTA)

- **1950s.** Erdős' covering systems; the Mirsky–Newman/Davenport–Rado theorem settles $G=\mathbb{Z}$ by analytic means. Znám (1969) and Newman sharpen it: if the moduli of an exact cover are distinct, the least prime $p\mid n_k$ forces $n_k$ to repeat at least $p$ times.
- **1954.** B. H. Neumann's structure theory of groups covered by finitely many cosets supplies the finite-index and core reductions.
- **1974.** Marcel Herzog and Jochanan Schönheim pose the general group-theoretic version as Research Problem No. 9 in the *Canadian Mathematical Bulletin* — the conjecture in its current form.
- **1986–1988.** Berger, Felzenbaum and Fraenkel prove the conjecture for **finite nilpotent groups**, and refine the Newman–Znám bounds for disjoint covering systems.
- **2004–2006.** Zhi-Wei Sun proves it whenever all $H_i$ are **subnormal** in $G$, and develops the theory of uniform ($m$-fold) covers of groups, deriving index inequalities such as $k\ge 1+\text{(smallest prime divisor bounds)}$ for covers by cosets.
- **2019.** Margolis and Schnabel introduce *harmonic subgroup lattices* and verify the conjecture computationally for all finite groups of order $<1440$, and study reductions for finitely generated groups.

No counterexample is known; no proof is known beyond the structural classes below.

## 4. Partial Results / Verified Cases

| Class / range | Result | Source |
|---|---|---|
| $G=\mathbb{Z}$ (exact covering systems) | Largest modulus repeats; distinct moduli impossible | Davenport, Mirsky, Newman, Rado (c. 1950) |
| $G$ finitely generated abelian | Follows from the $\mathbb{Z}$ case + core reduction | classical |
| $G$ finite nilpotent (includes all $p$-groups) | Conjecture true | Berger–Felzenbaum–Fraenkel, 1986 |
| All $H_i$ subnormal in $G$ | Conjecture true | Sun, 2004 |
| $k\le 3$ | True: $\{2,3,6\}$ is the only distinct-index Egyptian solution and it is excluded (Section 10) | elementary |
| $|G|<1440$ (all finite groups) | Verified by computer search over subgroup lattices | Margolis–Schnabel, 2019 |
| Indices $n_i$ all powers of one prime $p$ | True (density/counting forces repetition, since $\sum p^{-e_i}=1$ with distinct $e_i$ is impossible for $p\ge2$ unless $e_i$ repeat) | elementary |
| Uniform / $m$-fold covers | Structural index inequalities; conjecture confirmed in several sub-cases | Sun, 2004, 2006 |

Note that Sun's subnormal theorem strictly contains the nilpotent theorem, and the abelian case; the first genuinely open configurations sit in groups with non-subnormal (e.g. self-normalising, non-normal) subgroups of composite index.

## 5. Principal Obstacles

- **No Fourier/generating-function analogue.** The $\mathbb{Z}$ proof evaluates a rational generating function at roots of unity. The indicator function $\mathbf 1_{aH}$ is a linear combination of characters only when $H\trianglelefteq G$; for non-normal $H$ the natural object $\mathbf 1_{aH}$ lives in the permutation module $\mathbb{C}[G/H]$, whose decomposition varies with $H$, so the pole-isolation argument has no target to isolate.
- **Subnormality is exactly where induction stops.** Every known proof lifts a partition to a quotient or restricts it to a normal subgroup. If $H_i$ is not subnormal, $H_iN/N$ can have index unrelated to $[G:H_i]$ in any intermediate quotient, and the induction loses control of the index multiset.
- **Combinatorial explosion.** After the core reduction, the problem is finite but unbounded: the number of strict Egyptian representations of $1$ grows super-exponentially in $k$ (already $\{2,3,10,15\}$, $\{2,4,6,12\}$, $\{2,3,7,42\}$, …), and each must be excluded against *every* subgroup lattice that could host it. Brute force stalls beyond order $\sim 10^3$.
- **No global invariant.** For $\mathbb{Z}$ the modulus is an invariant of the coset. In general the same index can be realised by lattice-inequivalent subgroups, so index alone carries too little information; "harmonic lattice" invariants capture some of it but are not known to be complete.

## 6. The Gap

Proven: partitions in which each $H_i$ admits a subnormal chain to $G$ (Sun), plus finite verification to order $1440$. Conjectured: all partitions of all groups.

The precise missing step is a **non-subnormal descent lemma**: given $G=\bigsqcup a_iH_i$ with distinct indices $n_1=2<n_2<\dots<n_k$, produce a proper section $\bar G$ of $G$ and an induced partition whose index multiset is again distinct and strictly smaller — without assuming that any $H_i$ is normalised by anything. Equivalently, one wants a weight function $w$ on cosets, invariant under left translation and multiplicative along the lattice, whose value on $a_iH_i$ depends only on $[G:H_i]$ and satisfies $\sum_i w(a_iH_i)\neq w(G)$ when indices are distinct. Neither object is known to exist.

## 7. Current Research (as of June 2026)

- **Lattice-theoretic reformulation.** Margolis (Vrije Universiteit Brussel / Murcia) and Schnabel (Ort Braude) reduce the conjecture to a purely order-theoretic property of subgroup lattices ("harmonic" lattices), which decouples it from the group's representation theory. Extending their $|G|<1440$ verification is a live computational programme in GAP.
- **Covering systems school.** Sun's group at Nanjing continues on covers and $m$-covers of groups, index inequalities, and links to Erdős-style covering-system problems (minimum modulus, odd covers) — the latter reinvigorated by Hough's resolution of the minimum modulus problem (2015) and the Balister–Bollobás–Morris–Sahasrabudhe–Tiba distortion method.
- **Frontier.** Attempts to attack the first open index patterns ($\{2,3,10,15\}$, $\{2,4,6,12\}$) inside metabelian and Frobenius groups, and to bound the order of a minimal counterexample by its subgroup-lattice height *(frontier — verify)*.
- **Automated search.** SAT/ILP encodings of the coset-partition constraints over concrete groups of order up to $\sim10^4$ *(frontier — verify)*.

## 8. Future Work

- Prove the conjecture for **finite supersolvable** or **finite solvable** groups — the natural next class beyond nilpotent, where chief series exist but subnormality fails.
- Establish it for all $k\le 5$ or $k\le 6$ by exhausting the finitely many distinct Egyptian patterns and excluding each by lattice arguments.
- Show a minimal counterexample must be non-solvable, or bound $|G|$ for a minimal counterexample in terms of $\max_i n_i$.
- Develop a representation-theoretic invariant of coset partitions (e.g. via the Burnside ring of $G$, where $[G/H_i]$ are canonical generators and $\sum_i [G/H_i]$-type relations are computable).
- Settle the "harmonic lattice" question: is every finite subgroup lattice harmonic?

## 9. Key References

- **[Foundational]** M. Herzog and J. Schönheim. *Research Problem No. 9.* Canadian Mathematical Bulletin **17** (1974), 150.
- **[Foundational]** B. H. Neumann. *Groups covered by permutable subsets.* Journal of the London Mathematical Society **29** (1954), 236–248. [DOI](https://doi.org/10.1112/jlms/s1-29.2.236)
- **[Foundational]** Š. Znám. *On exactly covering systems of arithmetic sequences.* Mathematische Annalen **180** (1969), 227–232. [DOI](https://doi.org/10.1007/bf01350740)
- **[Partial result]** M. A. Berger, A. Felzenbaum and A. S. Fraenkel. *The Herzog–Schönheim conjecture for finite nilpotent groups.* Canadian Mathematical Bulletin **29** (1986), 329–333. [DOI](https://doi.org/10.4153/cmb-1986-050-0)
- **[Partial result]** M. A. Berger, A. Felzenbaum and A. S. Fraenkel. *Improvements to the Newman–Znám result for disjoint covering systems.* Acta Arithmetica **50** (1988), 1–13. [DOI](https://doi.org/10.4064/aa-50-1-1-13)
- **[SOTA]** Z.-W. Sun. *On the Herzog–Schönheim conjecture for uniform covers of groups.* Journal of Algebra **273** (2004), 153–175. [DOI](https://doi.org/10.1016/s0021-8693(03)00526-x)
- **[SOTA]** Z.-W. Sun. *Finite covers of groups by cosets or subgroups.* International Journal of Mathematics **17** (2006), 1047–1064. [DOI](https://doi.org/10.1142/s0129167x06003813)
- **[SOTA / Recent]** L. Margolis and O. Schnabel. *The Herzog–Schönheim conjecture for small groups and harmonic subgroups.* Beiträge zur Algebra und Geometrie **60** (2019), 399–418. [DOI](https://doi.org/10.1007/s13366-018-0419-1)
- **[SOTA / Recent]** L. Margolis and O. Schnabel. *The Herzog–Schönheim conjecture for finitely generated groups.* International Journal of Algebra and Computation, 2019. [DOI](https://doi.org/10.1142/s0218196719500425)
- **[Related]** M. J. Tomkinson. *Groups covered by finitely many cosets or subgroups.* Communications in Algebra **15** (1987), 845–859. [DOI](https://doi.org/10.1080/00927878708823445)
- **[Survey]** Š. Porubský and J. Schönheim. *Covering systems of Paul Erdős: past, present and future.* In *Paul Erdős and His Mathematics I*, Bolyai Society Mathematical Studies **11**, Springer, 2002, 581–627.

## 10. Worked Example / Concrete Special Case

**Claim.** No group $G$ admits a coset partition with the distinct indices $\{2,3,6\}$. This is the smallest possible distinct-index pattern, since $\sum_i 1/n_i=1$ with $n_1<n_2<n_3$ forces $(2,3,6)$.

**Setup.** Suppose $G=a_1H_1\sqcup a_2H_2\sqcup a_3H_3$ with $[G:H_1]=2$, $[G:H_2]=3$, $[G:H_3]=6$. The density relation checks out: $\tfrac12+\tfrac13+\tfrac16=1$.

**Step 1 — translate.** $H_1$ has index $2$, so $G=a_1H_1\sqcup bH_1$ where $bH_1$ is the other coset. Then
$$bH_1=a_2H_2\sqcup a_3H_3 .$$
Left-translating the whole partition by $b^{-1}$ (which permutes cosets and preserves all indices) gives
$$H_1=cH_2\sqcup dH_3,\qquad c=b^{-1}a_2,\ d=b^{-1}a_3 .$$

**Step 2 — absorb.** $cH_2\subseteq H_1$ and $c=c\cdot 1\in cH_2$, so $c\in H_1$. Since $H_1$ is a subgroup, $c^{-1}H_1=H_1$, hence
$$H_2=c^{-1}(cH_2)\subseteq c^{-1}H_1=H_1 .$$
So $H_2$ is a subgroup of $H_1$.

**Step 3 — index contradiction.** By multiplicativity of the index,
$$[G:H_2]=[G:H_1]\cdot[H_1:H_2]\ \Longrightarrow\ 3=2\cdot[H_1:H_2],$$
so $[H_1:H_2]=3/2\notin\mathbb{Z}$. Contradiction. (Equivalently: $2\mid[G:H_2]$ is forced, but $[G:H_2]=3$.) $\blacksquare$

**What the example shows.** The argument works because the index-$2$ subgroup makes one block of the partition *itself a subgroup*, converting a covering statement into a divisibility statement. The general conjecture fails to yield to this because for $k\ge4$ the complement of $a_1H_1$ is a union of $\ge3$ cosets, and no single one of them need contain the identity after translation — the "absorption" step of Step 2 has no analogue. The first genuinely resistant pattern is $\{2,3,10,15\}$ ($\tfrac12+\tfrac13+\tfrac1{10}+\tfrac1{15}=1$), where the same translation gives $H_1=cH_2\sqcup dH_3\sqcup eH_4$ and no index divisibility contradiction follows from a single containment.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*