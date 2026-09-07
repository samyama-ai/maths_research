---
id: 07-combinatorics/kemnitzs-conjecture
title: "Kemnitz's Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kemnitz's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/kemnitzs-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

**Kemnitz's Conjecture (1983).** For every integer $n \ge 1$, any $4n-3$ points of the integer lattice $\mathbb{Z}^2$ (repetitions allowed) contain $n$ points whose centroid is again a lattice point.

Equivalently, given $P_1,\dots,P_{4n-3} \in \mathbb{Z}^2$ there is an index set $I \subseteq \{1,\dots,4n-3\}$ with $|I| = n$ and

$$\frac{1}{n}\sum_{i \in I} P_i \in \mathbb{Z}^2 .$$

The condition depends only on the residues $P_i \bmod n$, so the statement is exactly: every sequence of $4n-3$ elements of $\mathbb{Z}_n^2$ has a zero-sum subsequence of length $n$.

The constant $4n-3$ is optimal (Section 10), so the conjecture asserts $s(\mathbb{Z}_n^2) = 4n-3$ where $s(\cdot)$ is the Erdős–Ginzburg–Ziv constant. A complete proof must handle all $n$; a disproof requires one $n$ and one explicit sequence of $4n-3$ points with no $n$-subset summing to $0$ mod $n$.

**Status:** proved. Christian Reiher (announced 2003, published 2007) and, independently, Svetoslav Savchev and Fang Chen (2007) settled it. The page is retained because the higher-dimensional analogue is wide open.

## 2. Mathematical Foundations

Let $G$ be a finite abelian group, written additively. A *sequence* over $G$ is a finite multiset $S = (g_1,\dots,g_\ell)$; $\sigma(S) = \sum_i g_i$; $S$ is a *zero-sum sequence* if $\sigma(S) = 0$.

**Definition (EGZ constant).**
$$s(G) = \min\{\, \ell \in \mathbb{N} : \text{every sequence over } G \text{ of length } \ell \text{ has a zero-sum subsequence of length } \exp(G) \,\},$$
where $\exp(G)$ is the exponent. Related constants: the Davenport constant $D(G)$ (longest zero-sum-free sequence, plus one) and $\eta(G)$ (shortest length forcing a nonempty zero-sum subsequence of length $\le \exp(G)$).

**Theorem (Erdős–Ginzburg–Ziv, 1961).** $s(\mathbb{Z}_n) = 2n-1$.

Kemnitz's conjecture is the two-dimensional analogue:
$$s(\mathbb{Z}_n^2) = 4n-3, \qquad \exp(\mathbb{Z}_n^2) = n .$$

**Lower bound (Harborth).** For all $d,n$, $s(\mathbb{Z}_n^d) \ge (n-1)2^d + 1$, from the sequence containing each element of $\{0,1\}^d \subset \mathbb{Z}_n^d$ with multiplicity $n-1$. For $d=2$ this gives $4n-3$.

**Multiplicativity.** If $s(\mathbb{Z}_m^d) = (m-1)2^d+1$ and $s(\mathbb{Z}_n^d) = (n-1)2^d+1$, then $s(\mathbb{Z}_{mn}^d) = (mn-1)2^d+1$. Proof sketch for $d=2$: from $4mn-3$ elements repeatedly extract disjoint zero-sum-mod-$m$ blocks of length $m$; their averages form a sequence over $\mathbb{Z}_n^2$ of length $\ge 4n-3$, and a zero-sum $n$-subsequence there lifts to a zero-sum $mn$-subsequence. Hence **it suffices to prove the conjecture for $n = p$ prime.**

**Chevalley–Warning.** If $f_1,\dots,f_k \in \mathbb{F}_p[x_1,\dots,x_N]$ satisfy $\sum_j \deg f_j < N$ and have a common zero, they have another. Applied with $N = 4p-3$ variables and, for a sequence $(a_i,b_i)_{i\le N}$ over $\mathbb{F}_p^2$,
$$f_1 = \sum_{i} a_i x_i^{p-1}, \quad f_2 = \sum_{i} b_i x_i^{p-1}, \quad f_3 = \sum_{i} x_i^{p-1},$$
of total degree $3(p-1) < 4p-3$, one obtains a nonempty subsequence of length $\equiv 0 \pmod p$ with zero sum — length $p$, $2p$, or $3p$. Eliminating the cases $2p$ and $3p$ is the whole difficulty.

## 3. History & State of the Art (SOTA)

- **1961.** Erdős, Ginzburg and Ziv prove the one-dimensional case, $s(\mathbb{Z}_n) = 2n-1$.
- **1973.** Harborth (*Ein Extremalproblem für Gitterpunkte*) introduces $s(\mathbb{Z}_n^d)$ in lattice-point language and proves $(n-1)2^d + 1 \le s(\mathbb{Z}_n^d) \le (n-1)n^d + 1$. For $d = 2$: $4n-3 \le s(\mathbb{Z}_n^2) \le n^3-n^2+1$.
- **1983.** Arnfried Kemnitz (*On a lattice point problem*, Ars Combinatoria 16B) verifies $s(\mathbb{Z}_n^2)=4n-3$ for $n \in \{2,3,5,7\}$ and for $n = 2^a3^b5^c7^d$ by multiplicativity, and conjectures the general case.
- **1995.** Alon and Dubiner prove the first linear bound $s(\mathbb{Z}_n^2) \le 6n - 5$, and $s(\mathbb{Z}_n^d) \le c(d)\, n$ in all dimensions.
- **2000.** Rónyai (Combinatorica) proves $s(\mathbb{Z}_p^2) \le 4p - 2$ for primes $p$ — off by exactly one — via a Chevalley–Warning/polynomial argument with a Cauchy–Davenport step.
- **2002.** Thangadurai and, independently, Gao extend the $4n-2$ bound beyond primes.
- **2003/2007.** **Christian Reiher**, then a 19-year-old undergraduate, closes the gap: $s(\mathbb{Z}_p^2) = 4p-3$ for all primes $p$; with multiplicativity this proves the conjecture for all $n$. Published as *On Kemnitz' conjecture concerning lattice points in the plane*, Ramanujan J. 13 (2007).
- **2007.** Savchev and Chen give an independent, largely elementary proof (Discrete Math. 307).
- **Since.** Attention moved to $d \ge 3$, where even the order of growth of $c(d)$ is open. Elsholtz (2004) showed the naive generalization $s(\mathbb{Z}_n^d) = (n-1)2^d+1$ is false in general.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $d=1$, all $n$ | $s(\mathbb{Z}_n)=2n-1$ | Erdős–Ginzburg–Ziv 1961 |
| $d=2$, $n\in\{2,3,5,7\}$ | $4n-3$, by hand/computation | Kemnitz 1983 |
| $d=2$, $n=2^a3^b5^c7^d$ | $4n-3$, by multiplicativity | Kemnitz 1983 |
| $d=2$, all $n$ | $s(\mathbb{Z}_n^2)\le 6n-5$ | Alon–Dubiner 1995 |
| $d=2$, $p$ prime | $s(\mathbb{Z}_p^2)\le 4p-2$ | Rónyai 2000 |
| $d=2$, all $n$ | $s(\mathbb{Z}_n^2)=4n-3$ — **conjecture proved** | Reiher 2007; Savchev–Chen 2007 |
| $d=3$, $n=3$ | $s(\mathbb{Z}_3^3)=19 > (3-1)2^3+1=17$ | Kemnitz 1983; Elsholtz 2004 |
| $d\ge 3$, odd $n\ge 3$ | $s(\mathbb{Z}_n^d) \ge (n-1)\,2^d\,(9/8)^{\lfloor d/3\rfloor} + 1$ | Elsholtz 2004 |
| $d$ general | $s(\mathbb{Z}_n^d) \le c(d)n$ with $c(d) \le (cd\log d)^d$ | Alon–Dubiner 1995 |
| $n=p$ prime, $d$ large | $s(\mathbb{Z}_p^d) \le (C p)^d$ with $C$ absolute, via slice rank | Fox–Sauermann 2018; Naslund 2020 |

Exact values for $d \ge 3$ are known only in scattered cases ($s(\mathbb{Z}_2^d)$, $s(\mathbb{Z}_3^3)=19$, $s(\mathbb{Z}_3^4)=41$); see Edel–Elsholtz–Geroldinger–Kubertin–Rackham (2007).

## 5. Principal Obstacles

- **Chevalley–Warning is degree-blind about length.** The polynomial method yields a zero-sum subsequence of length $p$, $2p$ **or** $3p$. Nothing in the degree count distinguishes them. Rónyai's $4p-2$ was exactly the point at which the counting argument ran out of slack; Reiher had to add a genuinely new ingredient (a $p$-adic/Cauchy–Davenport analysis of how many subsequences of each admissible size can exist) rather than sharpen the degree bound.
- **No group-invariant extremal structure.** In dimension 1 the extremal sequences are $0^{n-1}1^{n-1}$ up to affine equivalence; in dimension 2 the extremal configurations are richer, so inductive "peel off a block" arguments lose control of the residual structure.
- **Fourier analysis is too lossy.** Character-sum estimates over $\mathbb{Z}_n^2$ give bounds of the form $Cn$ with $C$ not close to $4$; the extremal example is a perfect cube $\{0,1\}^2$ with equal multiplicities, i.e. highly structured and not detected as an obstruction by $L^2$ methods.
- **Dimension $\ge 3$: the lower bound itself is wrong.** Elsholtz's tensor-product constructions beat $(n-1)2^d+1$ by an exponential factor, so there is no plausible conjectural answer to aim at. This is why $c(d)$ is only pinned between $2^d$-type and $(d\log d)^d$-type growth.
- **Slice rank does not localize.** The cap-set technique bounds $s(\mathbb{Z}_p^d)$ for fixed $p$ and large $d$, but degrades badly when $p$ grows, which is the regime relevant to the linear-in-$n$ question.

## 6. The Gap

For $d=2$ there is no gap: Section 4 matches Section 1 exactly, and $4n-3$ is sharp. The residual gap is the *generalized* Kemnitz problem:

$$\text{Determine } c(d) = \lim_{n\to\infty} \frac{s(\mathbb{Z}_n^d)}{n}, \quad\text{known: } c(1)=2,\; c(2)=4,\; \text{unknown for } d \ge 3.$$

Current knowledge for $d=3$: $8n-7 \le s(\mathbb{Z}_n^3) \le c(3)\,n$ with $c(3)$ known only via Alon–Dubiner's general bound, and $s(\mathbb{Z}_3^3)=19$ already exceeding $8\cdot 3-7=17$. The precise step needed is a structure theorem for length-$\ell$ sequences over $\mathbb{Z}_n^3$ with no zero-sum $n$-subsequence — an analogue of the "$\{0,1\}^2$ with multiplicity $n-1$ is essentially the only extremum" statement that Savchev–Chen establish in the plane.

## 7. Current Research (as of June 2026)

- **Exact EGZ constants in dimension 3.** Groups around Geroldinger (Graz), Gao (Nankai) and Schmid continue to compute $s(\mathbb{Z}_n^3)$ for small $n$ and to test whether $s(\mathbb{Z}_n^3) = 9n-8$ holds for $n=3^k$ *(frontier — verify)*.
- **Slice-rank / polynomial-method bounds.** Following Croot–Lev–Pach and Ellenberg–Gijswijt, Fox–Sauermann and Naslund gave $s(\mathbb{Z}_p^d) \le (Cp)^d$; refinements aimed at making $C$ explicit and small are active.
- **Inverse problems.** Characterizing sequences of length $4n-4$ over $\mathbb{Z}_n^2$ with no zero-sum $n$-subsequence (the inverse Kemnitz problem) — Savchev–Chen's proof method is the natural entry point.
- **Non-homocyclic groups.** $s(\mathbb{Z}_{n_1}\oplus\mathbb{Z}_{n_2})$ for $n_1 \mid n_2$ is settled ($= 2n_1+2n_2-3$), but rank-3 analogues remain open.
- **Affine-cap connection.** The Edel et al. link between $\eta(\mathbb{Z}_3^d)$ and caps in $AG(d,3)$ ties higher-dimensional Kemnitz directly to cap-set progress.

## 8. Future Work

- Establish the true order of $c(d)$: is it $2^{d(1+o(1))}$, or genuinely superexponential in $d$? Alon and Dubiner explicitly posed whether $c(d)$ can be taken polynomial in $d$; Elsholtz's lower bound rules out $c(d) = 2^d$ exactly but leaves the exponential-rate question open.
- Prove or disprove $s(\mathbb{Z}_n^3) = 9n - 8$ for $n$ a power of 3, using multiplicativity plus a base case at $n=3$ ($=19$).
- Extract from Reiher's proof a general "Chevalley–Warning plus length-control" lemma applicable in rank 3.
- Push the inverse theorem in the plane to a full classification, then attempt a tensor-lifting argument to rank 3.
- Improve algorithmic search: exact computation of $s(\mathbb{Z}_5^3)$ would be the first genuinely new data point in the regime $n>3$, $d=3$.

## 9. Key References

- **[Foundational]** P. Erdős, A. Ginzburg, A. Ziv. *Theorem in the additive number theory.* Bull. Res. Council Israel 10F (1961), 41–43.
- **[Foundational]** H. Harborth. *Ein Extremalproblem für Gitterpunkte.* J. Reine Angew. Math. 262/263 (1973), 356–360.
- **[Foundational]** A. Kemnitz. *On a lattice point problem.* Ars Combinatoria 16B (1983), 151–160.
- **[Key bound]** N. Alon, M. Dubiner. *A lattice point problem and additive number theory.* Combinatorica 15 (1995), 301–309.
- **[Key bound]** L. Rónyai. *On a conjecture of Kemnitz.* Combinatorica 20 (2000), 569–573.
- **[SOTA / Resolution]** C. Reiher. *On Kemnitz' conjecture concerning lattice points in the plane.* The Ramanujan Journal 13 (2007), 333–337.
- **[SOTA / Resolution]** S. Savchev, F. Chen. *Kemnitz' conjecture revisited.* Discrete Mathematics 307 (2007), 2671–2679.
- **[Higher dimensions]** C. Elsholtz. *Lower bounds for multidimensional zero sums.* Combinatorica 24 (2004), 351–358.
- **[Higher dimensions]** Y. Edel, C. Elsholtz, A. Geroldinger, S. Kubertin, L. Rackham. *Zero-sum problems in finite abelian groups and affine caps.* Quarterly J. Math. 58 (2007), 159–186.
- **[Recent]** J. Fox, L. Sauermann. *Erdős–Ginzburg–Ziv constants by avoiding three-term arithmetic progressions.* Electronic J. Combinatorics 25 (2018), \#P2.14.
- **[Recent]** E. Naslund. *Exponential bounds for the Erdős–Ginzburg–Ziv constant.* J. Combinatorial Theory Ser. A 174 (2020), 105185.
- **[Survey]** W. Gao, A. Geroldinger. *Zero-sum problems in finite abelian groups: a survey.* Expositiones Mathematicae 24 (2006), 337–369.

## 10. Worked Example / Concrete Special Case

**(a) Sharpness: $4n-4$ points are not enough.** Take the four residues $(0,0),(0,1),(1,0),(1,1) \in \mathbb{Z}_n^2$, each with multiplicity $n-1$; total $4n-4$. Let a chosen $n$-subset use $a,b,c,d$ copies respectively, so $a+b+c+d=n$ and each of $a,b,c,d \le n-1$. The sum is $(c+d,\; b+d) \bmod n$. Since $0 \le c+d \le n$, zero-sum forces $c+d \in \{0,n\}$.
- If $c+d=n$: then $a=b=0$, and $b+d=d\equiv 0$ forces $d=0$, so $c=n$ — contradicts $c\le n-1$.
- If $c+d=0$: then $c=d=0$, and $b+d=b\equiv 0$ forces $b=0$, so $a=n$ — contradicts $a\le n-1$.

No zero-sum $n$-subset exists, so $s(\mathbb{Z}_n^2) \ge 4n-3$.

**(b) The case $n=3$ by hand.** Claim: any $9$ points of $\mathbb{Z}^2$ contain $3$ with lattice centroid, i.e. any 9-term sequence over $\mathbb{Z}_3^2$ has three elements summing to $0$. In $\mathbb{Z}_3^2 = AG(2,3)$, three elements sum to zero iff they are all equal or form an affine line. Suppose a sequence of length $\ell$ avoids this. Then every value occurs at most twice, and the support contains no line — the support is a *cap* in $AG(2,3)$. The maximum cap in $AG(2,3)$ has size $4$ (e.g. $\{(0,0),(0,1),(1,0),(1,1)\}$: no three of these are collinear mod 3). Hence $\ell \le 2\cdot 4 = 8$, and every sequence of length $9$ contains a zero-sum triple. Combined with (a), $s(\mathbb{Z}_3^2) = 9 = 4\cdot 3 - 3$. ∎

**(c) Why dimension 3 breaks.** Run the same argument in $AG(3,3)$: the maximum cap has size $9$ (the Hill/Pellegrino cap), so a sequence of length $2 \cdot 9 = 18$ over $\mathbb{Z}_3^3$ avoids all zero-sum triples, giving $s(\mathbb{Z}_3^3) \ge 19$. The Harborth-type guess predicts only $(3-1)2^3+1 = 17$. The naive pattern $s(\mathbb{Z}_n^d)=(n-1)2^d+1$ therefore fails at $(n,d)=(3,3)$ — the exact point where the plane proof stops generalizing.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*