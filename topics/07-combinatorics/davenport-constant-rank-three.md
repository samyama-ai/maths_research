---
id: 07-combinatorics/davenport-constant-rank-three
title: "Davenport Constant of Finite Abelian Groups of Rank Three"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Davenport Constant of Finite Abelian Groups of Rank Three

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/davenport-constant-rank-three` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a finite abelian group. The **Davenport constant** $\mathsf D(G)$ is the smallest $\ell$ such that every sequence of $\ell$ elements of $G$ (repetition allowed, order irrelevant) has a non-empty subsequence summing to $0$.

Write $G \cong C_{n_1} \oplus C_{n_2} \oplus C_{n_3}$ with $1 < n_1 \mid n_2 \mid n_3$, i.e. $G$ has rank $3$, and set
$$\mathsf D^*(G) \;=\; 1 + \sum_{i=1}^{3} (n_i - 1).$$
It is elementary that $\mathsf D(G) \ge \mathsf D^*(G)$.

**Open problem.** Is $\mathsf D(G) = \mathsf D^*(G)$ for *every* finite abelian group of rank three? In particular, is
$$\mathsf D(C_n \oplus C_n \oplus C_n) = 3n - 2 \quad \text{for all } n \ge 2\,?$$

A complete solution requires either (a) a proof, for all $n_1 \mid n_2 \mid n_3$, that every sequence of length $n_1+n_2+n_3-2$ over $C_{n_1}\oplus C_{n_2}\oplus C_{n_3}$ has a non-empty zero-sum subsequence, or (b) an explicit rank-three group together with a zero-sum-free sequence of length $\mathsf D^*(G)$ (equivalently a minimal zero-sum sequence of length $\mathsf D^*(G)+1$). Counterexamples are known in rank $\ge 4$, so the answer is not forced either way by general principles.

## 2. Mathematical Foundations

**Sequences as monoid elements.** A *sequence* over $G$ is an element of the free abelian monoid $\mathcal F(G)$; write $S = g_1 \cdot \ldots \cdot g_\ell = \prod_{g \in G} g^{[\mathsf v_g(S)]}$, with length $|S| = \ell$ and sum $\sigma(S) = \sum_i g_i$. $S$ is *zero-sum* if $\sigma(S)=0$, *zero-sum free* if no non-empty subsequence has sum $0$, and *minimal zero-sum* if $\sigma(S)=0$ and no proper non-empty subsequence is zero-sum. Then
$$\mathsf D(G) = 1 + \max\{|S| : S \in \mathcal F(G) \text{ zero-sum free}\} = \max\{|S| : S \text{ minimal zero-sum}\}.$$

**Lower bound.** Let $(e_1,\dots,e_r)$ be a basis with $\operatorname{ord}(e_i)=n_i$. The sequence
$$S_0 \;=\; \Big(\prod_{i=1}^{r} e_i^{[\,n_i-1\,]}\Big)\cdot\Big(\textstyle\sum_{i=1}^{r} e_i\Big)$$
is minimal zero-sum of length $\mathsf D^*(G)$, whence $\mathsf D(G)\ge \mathsf D^*(G)$.

**Standard general bounds.**
- $\mathsf D(G) \le |G|$, with equality iff $G$ is cyclic; $\mathsf D(C_n)=n$.
- Superadditivity: $\mathsf D(G_1 \oplus G_2) \ge \mathsf D(G_1) + \mathsf D(G_2) - 1$.
- Character/group-ring bound (van Emde Boas–Kruyswijk, Meshulam; sharpened form used by Alford–Granville–Pomerance): with $n=\exp(G)$,
$$\mathsf D(G) \;\le\; n\left(1 + \log\frac{|G|}{n}\right).$$
For $G$ of rank three this reads $\mathsf D(G) \le n_3\big(1+\log(n_1n_2)\big)$, which exceeds $n_1+n_2+n_3-2$ by a factor growing like $\log$.

**Related invariants.** $\eta(G)$ (shortest length forcing a short zero-sum subsequence, of length $\le \exp(G)$) and the Erdős–Ginzburg–Ziv constant $\mathsf s(G)$; for rank-two groups $\mathsf s(G)=\eta(G)+\exp(G)-1$. **Property B** for $C_n^2$: every minimal zero-sum sequence over $C_n\oplus C_n$ of maximal length $2n-1$ contains some element with multiplicity $n-1$. Property B is the inverse-theoretic input on which most rank-three inductions rest.

**Why the constant matters.** If $H$ is a Krull monoid with class group $G$ and every class contains a prime divisor (e.g. the multiplicative monoid of a ring of integers with ideal class group $G$), then $\mathsf D(G)$ is exactly the maximal number of atoms in a factorization of an atom's product relation — the sharp bound on the length of irreducible factorizations.

## 3. History & State of the Art (SOTA)

- **1960s.** The constant is named after H. Davenport, who raised the question in the context of factorizations in algebraic number fields; the same quantity had been studied by K. Rogers (1963).
- **1969.** J. E. Olson proves the two decisive positive results: $\mathsf D(G)=\mathsf D^*(G)$ for all finite abelian $p$-groups (part I) and for all groups of rank $\le 2$ (part II).
- **1969.** P. van Emde Boas and D. Kruyswijk, in the Mathematisch Centrum report series, compute $\mathsf D$ for many small groups, establish the logarithmic upper bound, and record the first evidence that $\mathsf D=\mathsf D^*$ can fail.
- **1992.** A. Geroldinger and R. Schneider exhibit infinite families with $\mathsf D(G) > \mathsf D^*(G)$; the known families have rank $\ge 4$ (e.g. groups of the form $C_2^{\,r-1}\oplus C_{2n}$ with $r\ge 4$ and $n\ge 3$ odd). No rank-three counterexample has ever been found.
- **1994.** Alford–Granville–Pomerance use the logarithmic bound on $\mathsf D(G)$ as a key lemma in the proof that there are infinitely many Carmichael numbers — the best-known external application.
- **2007–2010.** Reiher proves Property B for prime $n$; Gao–Geroldinger–Grynkiewicz reduce Property B for general $n$ to the prime case, completing it. This unlocks inverse results in rank two that feed rank-three inductions.
- **2007.** Bhowmik and Schlage-Puchta settle the family $C_3\oplus C_3\oplus C_{3n}$.
- **2011 onward.** W. A. Schmid solves the *inverse* problem for $C_2\oplus C_2\oplus C_{2n}$ (classifying all maximal-length minimal zero-sum sequences), which is the model for how rank-three cases are expected to be handled.

**SOTA summary:** $\mathsf D = \mathsf D^*$ is a theorem for $p$-groups, rank $\le 2$, and a handful of rank-three families with small $n_1=n_2$; it is a conjecture, supported by all computations, for rank three in general.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $G$ a $p$-group of any rank (so $C_{p^a}^3$, $C_{p^a}\oplus C_{p^b}\oplus C_{p^c}$) | $\mathsf D(G)=\mathsf D^*(G)$ | Olson 1969 (I) |
| $\operatorname{rank}(G)\le 2$ | $\mathsf D(C_{m}\oplus C_{mn}) = m+mn-1$ | Olson 1969 (II) |
| $C_2\oplus C_2\oplus C_{2n}$, all $n\ge 1$ | $\mathsf D = 2n+2$; full inverse classification | van Emde Boas–Kruyswijk; Schmid 2011 |
| $C_3\oplus C_3\oplus C_{3n}$, all $n\ge 1$ | $\mathsf D = 3n+4$ | Bhowmik–Schlage-Puchta 2007 |
| $C_n^3$ with $n$ a prime power | $\mathsf D = 3n-2$ | Olson 1969 (I) |
| Rank-three groups of small order | $\mathsf D = \mathsf D^*$ by exhaustive/structured computation; no counterexample found | van Emde Boas–Kruyswijk 1969 and later computations |
| Rank $\ge 4$ | $\mathsf D > \mathsf D^*$ for infinite families | Geroldinger–Schneider 1992 |

The first genuinely open cases are small: $C_6^3$ ($\mathsf D^* = 16$), $C_5\oplus C_5\oplus C_{5n}$ with $n$ not a power of $5$, and $C_2\oplus C_6\oplus C_{6n}$-type groups where $n_1<n_2$ and $|G|$ is not a prime power.

## 5. Principal Obstacles

- **Olson's group-algebra argument is $p$-adic.** The $p$-group proof works in $\mathbb F_p[G]$, where $(1-g)^{p^k}=1-g^{p^k}$ and the augmentation ideal is nilpotent with computable nilpotency index. For $|G|$ divisible by two primes no single characteristic supports this filtration, and the Sylow decomposition does not recombine: $\mathsf D$ is not additive over Sylow subgroups ($\mathsf D(C_6)=6 \ne \mathsf D(C_2)+\mathsf D(C_3)-1=4$).
- **The rank-two proof is inherently two-dimensional.** Olson's rank-$\le 2$ argument, and its later reproofs, use the fact that a subgroup of index $n_2$ has cyclic quotient, so one can run a Davenport-Erdős-type induction along a single cyclic direction. In rank three the quotient $G/H$ by a cyclic $H$ is again rank two, and the induction requires knowing not only $\mathsf D(G/H)$ but the *structure* of all extremal sequences — the inverse problem.
- **Inverse problems in rank two are only partly solved.** Property B gives structure for maximal-length minimal zero-sum sequences over $C_n^2$, but rank-three inductions need control of sequences of length close to but below $2n-1$, where no classification exists.
- **Fourier/character methods lose a constant factor.** The logarithmic bound $\mathsf D(G)\le \exp(G)(1+\log(|G|/\exp(G)))$ is essentially optimal for the method (it is tight in order of magnitude for groups of large rank), and $\log(n_1n_2)$ swamps the target $n_1+n_2-1$.
- **Counterexamples exist nearby.** Because $\mathsf D > \mathsf D^*$ genuinely happens in rank $4$, any proposed proof must use a property that fails at rank $4$; purely "soft" arguments are therefore ruled out. This is the sharpest structural obstruction: the statement is *not* a general phenomenon, only a low-rank one.
- **Brute force is hopeless.** Certifying $\mathsf D(G)=\mathsf D^*(G)$ by search requires ruling out zero-sum-free sequences of length $n_1+n_2+n_3-2$ over a group of order $n_1n_2n_3$; the search space grows superexponentially, so only very small groups are decidable directly.

## 6. The Gap

Proven: $\mathsf D=\mathsf D^*$ when $|G|$ is a prime power (any rank), when $\operatorname{rank}(G)\le 2$ (any order), and for rank-three families in which the two smaller invariants are fixed and tiny ($n_1=n_2\in\{2,3\}$).

Conjectured: $\mathsf D=\mathsf D^*$ for rank three with $n_1,n_2$ arbitrary and $|G|$ divisible by at least two primes.

The precise missing step is an *upper bound* argument for $\mathsf D(C_{n_1}\oplus C_{n_2}\oplus C_{n_3})$ that is uniform in $n_1$. All existing proofs eliminate $n_1$ by case analysis whose complexity grows with $n_1$: for $n_1=2$ and $n_1=3$ the number of configurations of a hypothetical long zero-sum-free sequence modulo a cyclic subgroup is finite and small; for $n_1\ge 4$ (and $n_1n_2$ not a prime power) the case tree has no known finite description. Crossing the gap means replacing that enumeration with a structural theorem: a classification of zero-sum-free sequences over $C_{n_1}\oplus C_{n_2}$ of length $\ge n_1+n_2-1-k$ for all $k$ up to $n_1$, which is exactly the unsolved "higher-order inverse problem" in rank two.

## 7. Current Research (as of June 2026)

- **Graz school (Geroldinger, Zhong, and collaborators).** Continues to develop the factorization-theoretic side: the *set of distances*, elasticity, and unions of sets of lengths of Krull monoids, all controlled by $\mathsf D(G)$ and $\eta(G)$. Rank-three cases are the standing obstruction to arithmetic characterization results for class groups.
- **Nankai school (Gao and collaborators).** Works on $\eta(G)$, $\mathsf s(G)$ and the EGZ constant for groups $C_2^r\oplus C_n$ and $C_n^3$; sharp values of $\eta(C_n^3)$ would transfer to Davenport bounds. *(frontier — verify)* Several recent preprints claim improved upper bounds for $\mathsf s(C_n^3)$ using the polynomial method combined with Reiher-type inverse input.
- **Inverse problems for $C_2\oplus C_2\oplus C_{2n}$ and $C_3^2\oplus C_{3n}$.** Extensions of Schmid's classification to $n_1=n_2=4,5$ are being attempted; the ingredient still lacking is a rank-two inverse result at length $2n-3$.
- **Computational verification.** SAT/ILP and orderly-generation searches over rank-three groups of moderate order (typically $|G|$ into the low thousands) continue to confirm $\mathsf D=\mathsf D^*$; no counterexample has surfaced. *(frontier — verify)*
- **Polynomial method / Combinatorial Nullstellensatz.** Effective for prime exponent (Kemnitz-type statements) but so far unable to handle composite $\exp(G)$, which is precisely the open regime.

## 8. Future Work

1. **Settle $\mathsf D(C_6^3)=16$.** The smallest open instance with two prime divisors; a proof method that scales would be the template for $C_n^3$ with $n=pq$.
2. **Prove the higher-order inverse theorem in rank two:** classify zero-sum-free sequences over $C_m\oplus C_n$ of length $m+n-1-k$ for small $k$. Geroldinger and Grynkiewicz have repeatedly flagged this as the enabling lemma.
3. **Find the rank threshold.** Determine the exact set $\mathcal D = \{G : \mathsf D(G)=\mathsf D^*(G)\}$; a proof that $\mathcal D$ contains all rank-three groups but not all rank-four groups must isolate the mechanism that breaks at rank four (currently unidentified).
4. **Coprime-splitting bounds.** Develop a genuine "Chinese remainder" technique for $\mathsf D$: currently only the weak inequality $\mathsf D(G_1\oplus G_2)\ge \mathsf D(G_1)+\mathsf D(G_2)-1$ is available, and no matching upper bound.
5. **Transfer from $\eta$ and $\mathsf s$.** Sharp values $\eta(C_n^3)$, $\mathsf s(C_n^3)$ would constrain long zero-sum-free sequences; conversely, rank-three Davenport results would settle several EGZ questions.

## 9. Key References

- **[Foundational]** J. E. Olson. *A combinatorial problem on finite abelian groups, I.* Journal of Number Theory 1 (1969), 8–10.
- **[Foundational]** J. E. Olson. *A combinatorial problem on finite abelian groups, II.* Journal of Number Theory 1 (1969), 195–199.
- **[Foundational]** P. van Emde Boas, D. Kruyswijk. *A combinatorial problem on finite abelian groups III.* Report ZW-1969-008, Mathematisch Centrum, Amsterdam, 1969.
- **[Foundational]** A. Geroldinger, R. Schneider. *On Davenport's constant.* Journal of Combinatorial Theory, Series A 61 (1992), 147–152.
- **[Application]** W. R. Alford, A. Granville, C. Pomerance. *There are infinitely many Carmichael numbers.* Annals of Mathematics 139 (1994), 703–722.
- **[Survey]** W. Gao, A. Geroldinger. *Zero-sum problems in finite abelian groups: a survey.* Expositiones Mathematicae 24 (2006), 337–369.
- **[Monograph]** A. Geroldinger, F. Halter-Koch. *Non-Unique Factorizations: Algebraic, Combinatorial and Analytic Theory.* Chapman & Hall/CRC, 2006.
- **[SOTA]** G. Bhowmik, J.-C. Schlage-Puchta. *Davenport's constant for groups of the form $\mathbb Z_3 \oplus \mathbb Z_3 \oplus \mathbb Z_{3d}$.* In: Additive Combinatorics, CRM Proceedings and Lecture Notes 43, American Mathematical Society, 2007, 307–326.
- **[SOTA]** W. Gao, A. Geroldinger, D. J. Grynkiewicz. *Inverse zero-sum problems III.* Acta Arithmetica 141 (2010), 103–152.
- **[SOTA]** W. A. Schmid. *The inverse problem associated to the Davenport constant for $C_2\oplus C_2\oplus C_{2n}$, and applications to the arithmetical characterization of class groups.* Electronic Journal of Combinatorics 18 (2011).
- **[Related]** C. Reiher. *On Kemnitz' conjecture concerning lattice-points in the plane.* The Ramanujan Journal 13 (2007), 333–337.
- **[Monograph]** D. J. Grynkiewicz. *Structural Additive Theory.* Developments in Mathematics 30, Springer, 2013.

## 10. Worked Example / Concrete Special Case

Take $G = C_2 \oplus C_2 \oplus C_6$, so $(n_1,n_2,n_3)=(2,2,6)$, $|G|=24$, and
$$\mathsf D^*(G) = 1 + (2-1)+(2-1)+(6-1) = 8.$$

**Lower bound $\mathsf D(G)\ge 8$.** Fix a basis $e_1,e_2,e_3$ with orders $2,2,6$ and set
$$S_0 = e_1 \cdot e_2 \cdot e_3^{[5]} \cdot (e_1+e_2+e_3), \qquad |S_0| = 1+1+5+1 = 8.$$
Its sum is $2e_1 + 2e_2 + 6e_3 = 0$, so $S_0$ is zero-sum.

*Minimality.* A subsequence has the form $T = e_1^{a} e_2^{b} e_3^{c}$ or $T' = e_1^{a} e_2^{b} e_3^{c}\cdot(e_1+e_2+e_3)$ with $0\le a,b\le 1$, $0\le c \le 5$.
- $\sigma(T) = a e_1 + b e_2 + c e_3 = 0$ forces $a\equiv b \equiv 0 \pmod 2$ and $c \equiv 0 \pmod 6$, so $a=b=c=0$: only the empty subsequence.
- $\sigma(T') = (a+1)e_1 + (b+1)e_2 + (c+1)e_3 = 0$ forces $a+1\equiv 0 \pmod 2 \Rightarrow a=1$; likewise $b=1$; and $c+1\equiv 0\pmod 6 \Rightarrow c=5$. That is $T'=S_0$ itself.

So $S_0$ is a minimal zero-sum sequence of length $8$, and deleting any one term gives a zero-sum-free sequence of length $7$. Hence $\mathsf D(G)\ge 8$.

**Upper bound.** Applying the theorem for $C_2\oplus C_2\oplus C_{2n}$ with $n=3$ gives $\mathsf D(G)\le 8$, so $\mathsf D(C_2\oplus C_2\oplus C_6)=8=\mathsf D^*(G)$. Note that the generic character bound would only give $\mathsf D(G)\le 6(1+\log 4)\approx 14.3$, i.e. $\lfloor 14.3\rfloor = 14$ — far from $8$. This gap between $8$ and $14$ is exactly the difficulty of Section 5 in miniature.

**Contrast with the next-smallest open case.** For $G=C_6\oplus C_6\oplus C_6$ the same construction gives a minimal zero-sum sequence $e_1^{[5]}e_2^{[5]}e_3^{[5]}(e_1+e_2+e_3)$ of length $16=\mathsf D^*(G)$, so $\mathsf D(C_6^3)\ge 16$. Since $6$ is not a prime power, Olson's theorem does not apply; the character bound gives only $\mathsf D \le 6(1+\log 36)\approx 27.5$. Whether $\mathsf D(C_6^3)=16$ is, as of 2026, open.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*