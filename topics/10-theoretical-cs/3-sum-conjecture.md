---
id: 10-theoretical-cs/3-sum-conjecture
title: "3-SUM Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# 3-SUM Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/3-sum-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Given a set $A$ of $n$ numbers, decide whether there exist $a,b,c \in A$ with
$$a + b + c = 0.$$

The trivial algorithm is $O(n^2 \log n)$ by enumerating pairs; sorting first gives $O(n^2)$.

**3SUM Conjecture.** There is no algorithm solving 3SUM in time $O(n^{2-\delta})$ for any constant $\delta > 0$.

Two model-dependent variants are tracked separately, and the conjecture is asserted for both:

- **Real 3SUM.** $A \subset \mathbb{R}$, real-RAM model (unit-cost $+,-,\times,\div$ and comparisons; no bit tricks, no hashing).
- **Integer 3SUM.** $A \subset \{-U,\dots,U\}$ with $U = n^{O(1)}$, word-RAM with $w = \Theta(\log n)$-bit words.

A disproof is any algorithm — deterministic or randomized, in either model — running in $O(n^{2-\delta})$. A proof requires an unconditional $\Omega(n^{2-o(1)})$ lower bound in a general model, which would imply super-linear circuit-style separations far beyond current techniques; no one expects a proof soon. In practice the conjecture is used as a *hardness axiom*: it is the base of a large web of conditional lower bounds in fine-grained complexity.

The conjecture is now understood to tolerate polylogarithmic savings: current algorithms run in $n^2 / \operatorname{polylog}(n)$, so the statement must be read as "no polynomial improvement". A weaker, more robust form is used in reductions:

$$\text{3SUM requires } n^{2-o(1)} \text{ time.}$$

## 2. Mathematical Foundations

**Variants and their equivalences.** Let $A,B,C$ be sets of size $n$.

- *3-set version:* $\exists\, a\in A, b\in B, c\in C$ with $a+b=c$.
- *Distinctness:* require $a,b,c$ pairwise distinct indices ("non-degenerate 3SUM").

All variants are equivalent up to $O(n)$ additive overhead and constant blow-up: shift $A' = 3A + 1$, $B' = 3B + 2$, $C' = 3C$ to force one element from each set.

**Convolution-3SUM (Conv3SUM).** Given $A[1..n]$, decide whether $\exists\, i<j$ with
$$A[i] + A[j] = A[i+j].$$
Conv3SUM is trivially reducible to 3SUM; Pătraşcu (2010) proved the converse via hashing, so the two are subquadratic-equivalent. This direction is what makes 3SUM usable against *sequence* and *data-structure* problems.

**Linear degeneracy testing (LDT / $k$-LDT).** For fixed coefficients $\alpha_0,\dots,\alpha_k$, decide whether some $x_{i_1},\dots,x_{i_k}$ satisfy
$$\alpha_1 x_{i_1} + \cdots + \alpha_k x_{i_k} + \alpha_0 = 0 .$$
3SUM is the case $k=3$, $\alpha=(0,1,1,1)$. The general conjecture ($k$-SUM) asserts $n^{\lceil k/2\rceil - o(1)}$.

**Fredman's trick.** The identity
$$x_i + y_j \;\le\; x_k + y_\ell \iff x_i - x_k \;\le\; y_\ell - y_j$$
converts comparisons between *sums* into comparisons between *differences drawn from single arrays*. Sorting $X+Y$ therefore needs only $O(n^2)$ comparisons (Fredman 1976), even though $|X+Y| = n^2$ and the information-theoretic sorting bound is $\Theta(n^2\log n)$. All decision-tree progress on 3SUM descends from this identity.

**Decision-tree complexity.** In the $s$-linear decision tree model each query tests the sign of a linear form in at most $s$ inputs. Erickson (1999) proved that $k$-LDT needs $\Omega(n^{\lceil k/2\rceil})$ $k$-linear queries — for 3SUM, $\Omega(n^2)$ 3-linear queries. Ailon and Chazelle (2005) extended this to $s$-linear trees with $s>k$, giving $\Omega\!\left(n^{\,k/(s-k+1)}\,\right)$-type bounds that degrade rapidly in $s$.

**FFT bound for bounded universe.** If $A \subseteq \{0,\dots,U\}$, let $f(x)=\sum_{a\in A} x^{a}$. Then $f(x)^2$ is computable in $O(U\log U)$ time, and $a+b=c$ is detectable by reading coefficient $c$. So integer 3SUM is solvable in $\tilde O(n + U)$.

## 3. History & State of the Art (SOTA)

- **1976.** Fredman's sorting-$X+Y$ trick establishes the comparison-model anomaly that later drives all upper-bound work.
- **1995.** Gajentaan and Overmars introduce 3SUM as a hardness benchmark, defining the class of *3SUM-hard* problems in computational geometry (published in *Computational Geometry: Theory and Applications*, 1995). This paper is the origin of the conjecture in its modern form.
- **1999.** Erickson: $\Omega(n^2)$ for 3-linear decision trees — the strongest unconditional bound, and it is model-bound.
- **2005.** Baran, Demaine, Pătraşcu: integer 3SUM in $O\!\left(n^2 / \left(\tfrac{\log n}{\log\log n}\right)^2\right)$ expected time via universe reduction by almost-linear hashing. First subquadratic-by-polylog result.
- **2010.** Pătraşcu: 3SUM $\le$ Conv3SUM, and the first wave of 3SUM-based lower bounds for dynamic data structures (e.g. dynamic reachability, subgraph connectivity).
- **2014/2018.** Grønlund and Pettie, *Threesomes, degenerates, and love triangles* (FOCS 2014; JACM 2018): a **$O(n^{3/2}\sqrt{\log n})$ decision tree** for 3SUM — a genuine polynomial break in the decision-tree model — plus a real-RAM algorithm in $O\!\left(n^2 (\log\log n)^{2/3} / (\log n)^{2/3}\right)$.
- **2016.** Kopelowitz, Pettie, Porat: sharpened reductions ("higher lower bounds from the 3SUM conjecture"), notably for set-disjointness/triangle-listing style problems.
- **2017–2018.** Freund, and independently Gold and Sharir, improve the real-RAM bound to $O(n^2 \log\log n / \log n)$.
- **2018/2020.** Chan: $O\!\left(n^2 (\log\log n)^{O(1)} / \log^2 n\right)$ for real 3SUM — the current SOTA, matching the integer bound of Baran–Demaine–Pătraşcu.
- **2019.** Kane, Lovett, Moran (STOC 2019): $O(n\log^2 n)$ **linear** decision trees (queries of unbounded sparsity, integer coefficients bounded by $\mathrm{poly}(n)$) for $k$-SUM. This kills any hope of proving the conjecture by linear-decision-tree arguments alone.
- **2023.** Abboud, Bringmann, Fischer (STOC 2023) and Jin, Xu (STOC 2023) use additive combinatorics (BSG-type theorems) to remove additive structure from 3SUM reductions, yielding *deterministic* and stronger lower bounds — e.g. for approximate distance oracles. Chan, Vassilevska Williams, Xu (STOC 2023) combine Fredman's trick with dominance products for 3SUM *counting* and unweighted APSP.

**Status:** the conjecture stands. No $n^{2-\delta}$ algorithm and no unconditional $\omega(n\log n)$ general-model lower bound.

## 4. Partial Results / Verified Cases

Cases where 3SUM *is* solved subquadratically or the conjecture is proved in a restricted model:

- **Small universe.** $A \subseteq \{-U,\dots,U\}$ with $U = O(n^{2-\delta})$: FFT gives $\tilde O(n+U)$. So the conjecture only bites for $U = \tilde\Omega(n^2)$ — exactly the regime where the sumset can be sparse.
- **Clustered inputs.** Chan and Lewenstein (STOC 2015): if $A$ can be covered by $n/g$ intervals ("clusters") of length $g$, integer 3SUM is solvable in $\tilde O(n^{2 - 2/7})$ time, using the Balog–Szemerédi–Gowers theorem. This is a genuine polynomial speedup on a structured class.
- **Small doubling.** If $|A+A| = O(n)$, Freiman-type structure forces $A$ into a generalized arithmetic progression and 3SUM becomes near-linear.
- **Decision-tree model.** $O(n^{3/2}\sqrt{\log n})$ (Grønlund–Pettie 2014) and $O(n\log^2 n)$ linear queries (Kane–Lovett–Moran 2019): the conjecture is **false** in these models.
- **3-linear decision trees.** Erickson's $\Omega(n^2)$: the conjecture is **true** in this model, tightly.
- **Preprocessing model.** Golovnev, Guo, Horel, Park, Vaikuntanathan (STOC 2020): with $\tilde O(n^{2-\delta})$ space preprocessing, 3SUM queries answerable in $\tilde O(n^{2-\delta})$ time — nontrivial trade-offs exist, so the conjecture is sensitive to non-uniformity.
- **Polylog savings, unconditional.** $n^2/\log^2 n$ up to $(\log\log n)^{O(1)}$, in both real-RAM and word-RAM.

## 5. Principal Obstacles

- **No lower-bound technique reaches $n^{2-o(1)}$.** For a problem in $\mathsf{P}$ with $n$ inputs, the best unconditional time bounds in any general model (RAM, branching programs) are barely super-linear. Proving 3SUM needs $n^{1.001}$ time would already be a breakthrough in circuit/branching-program lower bounds. This is the fundamental barrier: the conjecture is *not* attackable by current complexity theory.
- **Decision trees are provably the wrong model.** Kane–Lovett–Moran show $O(n\log^2 n)$ linear queries suffice. So any lower-bound proof must charge for something other than comparisons — the difficulty is entirely in *finding* which queries to make, not in the queries themselves. No formal framework currently prices "search cost" separately from "query cost".
- **Fredman's trick keeps eating logs.** Every attempt to prove hardness by information-theoretic counting of sorted orders fails because sorting $X+Y$ takes only $O(n^2)$ comparisons. Upper-bound progress ($n^2/\log^2 n$) exploits exactly this, and there is no known reason the exponent of the log savings must be bounded.
- **Additive-combinatorial structure cuts both ways.** BSG-type theorems turn structured inputs into easy instances (Chan–Lewenstein), so any hard family must be pseudorandom; but pseudorandom integer sets with $U \gg n^2$ are precisely those for which no algebraic handle (FFT, convolution) applies. Neither side can be pushed: hardness proofs would need a construction of hard instances, and $\mathsf{P}$-level explicit hard instances are not constructible with today's tools.
- **Reduction losses.** Reductions from 3SUM to other problems generically lose $n^{o(1)}$ or introduce additive structure that the target problem can exploit; the 2023 additive-combinatorics work exists precisely to plug those leaks.

## 6. The Gap

Proved: $\Omega(n^2)$ in the 3-linear decision tree model; $O(n^{3/2}\sqrt{\log n})$ and $O(n\log^2 n)$ decision-tree upper bounds; $O(n^2 (\log\log n)^{O(1)}/\log^2 n)$ real-RAM/word-RAM algorithms; subquadratic algorithms for clustered or small-universe inputs.

Wanted: an $n^{2-\delta}$ algorithm for arbitrary inputs, or an $n^{2-o(1)}$ unconditional lower bound.

The precise gap has two faces:

1. **Algorithmic.** All known speedups are of the form "sort a structured $O(n^{3/2})$-size subset of $X+Y$ using Fredman's trick, then batch-process with table lookup". This yields savings of $\mathrm{polylog}$ only, because the decision-tree gain ($n^{1/2}$) cannot be converted to running time: the $O(n^{3/2})$ queries are not *computable* in $O(n^{3/2})$ time. **Closing the gap means making the Grønlund–Pettie decision tree constructive.** That single step would disprove the conjecture.
2. **Lower bound.** Between $\Omega(n\log n)$ (trivial, comparison-based) and $n^{2-o(1)}$ (conjectured) there is no intermediate technique. The gap is the entire distance between "sorting-style arguments" and "polynomial lower bounds for a problem in $\mathsf{P}$".

## 7. Current Research (as of June 2026)

- **Additive-combinatorial reductions.** Abboud–Bringmann–Fischer and Jin–Xu (both STOC 2023) established the technique of removing additive structure from 3SUM-hard instances; follow-up work extends it to approximate distance oracles, dynamic problems, and string problems. Groups: Weizmann (Abboud), MPI-INF / Saarland (Bringmann, Fischer), MIT (Xu, Jin). This is the most active line.
- **Log-shaving.** Chan (UIUC) and collaborators continue to push $n^2/\log^c n$; the open question of whether $c$ can be made arbitrarily large — or whether $n^2/2^{\Theta(\sqrt{\log n})}$ is reachable — is a live target. *(frontier — verify)*
- **3SUM counting and APSP links.** Chan–Vassilevska Williams–Xu (STOC 2023) unify Fredman's trick with dominance products; ongoing work asks whether 3SUM and APSP hardness can be tied together beyond the current one-way reductions. Groups: MIT (Vassilevska Williams), UIUC.
- **Quantum and preprocessing models.** Ambainis-style quantum walk gives $\tilde O(n)$ for 3SUM in the quantum query model, so the classical conjecture has no quantum analogue at exponent 2; interest has shifted to quantum fine-grained hypotheses for $k$-SUM. *(frontier — verify)*
- **Space-bounded and streaming 3SUM**, and 3SUM with preprocessing (following Golovnev et al. 2020), remain open on the trade-off frontier.

## 8. Future Work

- **Make the decision tree constructive.** Determine whether the $O(n^{3/2}\sqrt{\log n})$ query bound can be accompanied by an $O(n^{3/2+\epsilon})$-time *search* procedure, or prove a formal barrier showing it cannot (a "search vs. query" separation for linear degeneracy).
- **Extend BSG-based speedups.** Chan–Lewenstein handles clustered inputs at $n^{2-2/7}$; identify the largest natural class (bounded doubling, bounded additive energy) for which subquadratic algorithms exist, and characterize the pseudorandom residue.
- **Determinize reductions.** Several 3SUM-hardness results still rely on randomized hashing; the 2023 additive-combinatorics machinery should be pushed to give deterministic reductions throughout.
- **Unify hypotheses.** Establish or refute implications among 3SUM, APSP, and SETH. Currently all three are independent axioms; a reduction in any direction would restructure fine-grained complexity.
- **Sharpen $k$-SUM.** The conjectured $n^{\lceil k/2\rceil-o(1)}$ bound is unproven for every $k \ge 3$; even $k=4$ has no better-than-polylog understanding.

## 9. Key References

- **[Foundational]** A. Gajentaan and M. H. Overmars. *On a class of $O(n^2)$ problems in computational geometry.* Computational Geometry: Theory and Applications, 5(3):165–185, 1995.
- **[Foundational]** M. L. Fredman. *How good is the information theory bound in sorting?* Theoretical Computer Science, 1(4):355–361, 1976.
- **[Foundational]** J. Erickson. *Lower bounds for linear satisfiability problems.* Chicago Journal of Theoretical Computer Science, 1999 (preliminary version SODA 1995).
- **[Foundational]** N. Ailon and B. Chazelle. *Lower bounds for linear degeneracy testing.* Journal of the ACM, 52(2):157–171, 2005.
- **[SOTA / Recent]** A. Grønlund and S. Pettie. *Threesomes, degenerates, and love triangles.* Journal of the ACM, 65(4):22, 2018 (FOCS 2014).
- **[SOTA / Recent]** T. M. Chan. *More logarithmic-factor speedups for 3SUM, (median,+)-convolution, and some geometric 3SUM-hard problems.* ACM Transactions on Algorithms, 16(1):7, 2020 (SODA 2018).
- **[SOTA / Recent]** D. M. Kane, S. Lovett, S. Moran. *Near-optimal linear decision trees for k-SUM and related problems.* Journal of the ACM, 66(3):16, 2019 (STOC 2018).
- **[SOTA / Recent]** T. M. Chan and M. Lewenstein. *Clustered integer 3SUM via additive combinatorics.* STOC 2015, pp. 31–40.
- **[SOTA / Recent]** A. Abboud, K. Bringmann, N. Fischer. *Stronger 3-SUM lower bounds for approximate distance oracles via additive combinatorics.* STOC 2023.
- **[SOTA / Recent]** C. Jin and Y. Xu. *Removing additive structure in 3SUM-based reductions.* STOC 2023.
- **[SOTA / Recent]** I. Baran, E. D. Demaine, M. Pătraşcu. *Subquadratic algorithms for 3SUM.* Algorithmica, 50(4):584–596, 2008 (WADS 2005).
- **[SOTA / Recent]** M. Pătraşcu. *Towards polynomial lower bounds for dynamic problems.* STOC 2010, pp. 603–610.
- **[SOTA / Recent]** T. Kopelowitz, S. Pettie, E. Porat. *Higher lower bounds from the 3SUM conjecture.* SODA 2016, pp. 1272–1287.
- **[Survey]** V. Vassilevska Williams. *On some fine-grained questions in algorithms and complexity.* Proceedings of the International Congress of Mathematicians (ICM 2018), Vol. IV, pp. 3447–3487, World Scientific, 2019.

## 10. Worked Example / Concrete Special Case

**Instance.** $A = \{-8,\, -3,\, -1,\, 2,\, 4,\, 9\}$, $n=6$. Does some triple sum to $0$?

**Quadratic algorithm.** Sort $A$ (already sorted). For each $a \in A$, run two pointers $i,j$ over $A$ seeking $A[i]+A[j] = -a$.

- $a=-8$: need pair summing to $8$. Pairs: $(-1,9)=8$. **Found:** $-8 + (-1) + 9 = 0$.

So the answer is YES. Cost: outer loop $n$, inner two-pointer scan $O(n)$, total $O(n^2) = 36$ steps.

**Why the trivial speedups fail.** Suppose we try to beat $O(n^2)$ by sorting the sumset $A+A$ and binary-searching each $-a$. Here
$$A+A \supseteq \{-16,-11,-9,-6,-4,-2,1,3,4,6,8,11,13,18\},$$
of size $\Theta(n^2)$. Building it explicitly already costs $n^2$. Fredman's trick says we can *sort* it with only $O(n^2)$ comparisons rather than $\Theta(n^2\log n)$ — but not with fewer than $n^2$ writes.

**Fredman's trick in miniature.** Take $X=\{-8,-3,-1\}$, $Y=\{2,4,9\}$. To decide $-3+9 \le -1+4$, i.e. $6 \le 3$, we instead compare
$$(-3) - (-1) \;\le\; 4 - 9 \quad\Longleftrightarrow\quad -2 \le -5,$$
which is false — consistent. The point: the left side draws only from $X$, the right only from $Y$. So one pre-sorted list of the $9$ differences $\{x_i - x_k\}$ and one of the $9$ differences $\{y_\ell - y_j\}$ answers *all* $81$ cross-comparisons by rank lookup. Generalizing, splitting $A$ into $n/g$ blocks of size $g$ and pre-sorting the $O(g^2)$ within-block differences lets a single sorted order be reused across blocks; Grønlund–Pettie tune $g \approx \sqrt{n}$ to reach $O(n^{3/2}\sqrt{\log n})$ **comparisons**.

**The gap, made concrete.** In the example, knowing the sorted order of the differences tells us *which* comparisons to make, but computing the block-difference orders and routing each of the $n$ target values $-a$ through them still costs one table-lookup per (element, block) pair — $\Theta(n \cdot n/g \cdot g) = \Theta(n^2)$ word operations. Word packing shrinks this by $\log^2 n$ (Chan 2020), never by $n^{\delta}$. Converting the $n^{3/2}$ comparison count into $n^{3/2}$ *time* is exactly the unresolved step in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*