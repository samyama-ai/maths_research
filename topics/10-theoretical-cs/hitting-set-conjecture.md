---
id: 10-theoretical-cs/hitting-set-conjecture
title: "HITTING-SET Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# HITTING-SET Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/hitting-set-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The **Hitting Set (HS) problem** in the fine-grained sense is: given two families $A, B$ of $n$ subsets each of a universe $U$ with $|U| = d$, decide whether

$$\exists\, a \in A \;\; \forall\, b \in B: \; a \cap b \neq \emptyset .$$

A set $a$ with this property is said to *hit* $B$.

**HITTING-SET Conjecture (HSC).** For every $\varepsilon > 0$ there exists a constant $c = c(\varepsilon)$ such that HS on $n$ sets over a universe of size $d = c \log n$ cannot be decided in $O(n^{2-\varepsilon})$ time by a randomized algorithm (on a word-RAM with $O(\log n)$-bit words).

A **disproof** requires an algorithm running in $O(n^{2-\varepsilon})$ time for *some* fixed $\varepsilon>0$ and *every* $d = O(\log n)$. A **proof** would have to be conditional on some complexity hypothesis (an unconditional proof would imply $\mathsf{P} \neq \mathsf{NP}$-scale separations far beyond current technique), so "proving HSC" in practice means deriving it from a hypothesis such as SETH or a quantified variant.

## 2. Mathematical Foundations

Identify subsets of $U = [d]$ with vectors in $\{0,1\}^d$. For $a, b \in \{0,1\}^d$ write $\langle a,b\rangle = \sum_{i=1}^d a_i b_i$. Then $a \cap b = \emptyset \iff \langle a,b\rangle = 0$ ("orthogonal"). The two central problems are:

- **Orthogonal Vectors (OV):** decide $\exists a \in A\ \exists b \in B: \langle a,b\rangle = 0$.
- **Hitting Set (HS):** decide $\exists a \in A\ \forall b \in B: \langle a,b\rangle \neq 0$.

HS is the $\exists\forall$ ("$\Sigma_2$-shaped") analogue of the $\exists\exists$ problem OV. Equivalently, with the counting function

$$N(a) \;=\; \bigl|\{ b \in B : \langle a,b\rangle = 0 \}\bigr|,$$

HS is a **yes**-instance iff $\min_{a\in A} N(a) = 0$.

**Relevant hypotheses.**

- **SETH** (Impagliazzo–Paturi): for every $\varepsilon>0$ there is $k$ with no $O(2^{(1-\varepsilon)n})$-time algorithm for $k$-SAT.
- **OV Conjecture:** for every $\varepsilon>0$ there is $c$ with no $O(n^{2-\varepsilon})$ algorithm for OV with $d = c\log n$. R. Williams' split-and-list reduction gives $\text{SETH} \Rightarrow \text{OVC}$.
- **NSETH** (Carmosino et al.): for every $\varepsilon>0$ there is $k$ such that $k$-**UNSAT** (co-nondeterministic refutation of $k$-CNF) requires $2^{(1-\varepsilon)n}$ nondeterministic time.

**Structural fact.** HS lies in $\mathsf{NTIME}[\tilde O(n)] \cap \mathsf{coNTIME}[\tilde O(n)]$ for $d = O(\log n)$: a yes-instance is certified by exhibiting the hitting set $a$ (verification costs $O(nd)$); a no-instance is certified by exhibiting, for each $a \in A$, an index of a witness $b_a \in B$ with $\langle a, b_a\rangle = 0$ (total $O(nd)$ verification).

**Downstream consequences** (Abboud–Vassilevska Williams–Wang, SODA 2016). Under HSC, for sparse graphs with $m = \tilde O(n)$ edges and every $\varepsilon>0$, there is no $O(m^{2-\varepsilon})$ algorithm for
$$\text{Radius} = \min_{v} \max_{u} d(v,u), \qquad \text{Median} = \min_v \sum_u d(v,u),$$
nor for computing the vertex of minimum *betweenness centrality*, nor a $(3/2-\delta)$-approximation of Radius.

## 3. History & State of the Art (SOTA)

- **2005.** R. Williams reduces CNF-SAT to OV, founding SETH-based hardness for quadratic-time problems.
- **2014–2015.** Roditty–Vassilevska Williams and Abboud–Vassilevska Williams–Wang establish SETH-hardness of Diameter in sparse graphs. Radius and Median resist: the natural OV reduction fails because those objectives are $\min\max$ / $\min\sum$, i.e. $\exists\forall$-quantified, while OV is purely existential.
- **2016 (SODA).** Abboud, Vassilevska Williams and Wang isolate exactly the missing hypothesis, name it the **Hitting Set Conjecture**, and prove it implies quadratic lower bounds for Radius, Median, betweenness minimization, and $3/2$-approximation of Radius. This is the origin of the conjecture as a named object.
- **2016 (ITCS).** Carmosino, Gao, Impagliazzo, Mihajlin, Paturi and Schneider introduce **NSETH** and show it as a *non-reducibility* barrier: since HS is in $\mathsf{NTIME}[\tilde O(n)] \cap \mathsf{coNTIME}[\tilde O(n)]$, a deterministic fine-grained reduction from CNF-SAT to HS would refute NSETH. They also show HSC does follow from a quantified ($\Sigma_2$-style) strengthening of SETH.
- **2018 (STOC).** Backurs, Roditty, Segal, Vassilevska Williams and Wein use HS to prove near-tight approximation lower bounds for eccentricities ($5/3$-type thresholds), broadening HSC's role beyond exact problems.
- **2018–present.** HSC is listed as one of the standard "hardness cores" of fine-grained complexity, alongside SETH, 3SUM, APSP and OV, in Vassilevska Williams' ICM 2018 survey. No subquadratic algorithm and no derivation from SETH is known.

## 4. Partial Results / Verified Cases

- **Constant $d$: solved.** For $d = O(1)$ the problem is linear-time. Compute $\beta[S] = |\{b \in B: b \subseteq S\}|$ for all $S \subseteq [d]$ by a subset-sum (zeta) transform in $O(2^d d)$ time; then $a$ hits $B$ iff $\beta[\,[d]\setminus a\,] = 0$. Total $O(nd + 2^d d)$. Subquadratic for all $d \le (2-\varepsilon)\log_2 n$.
- **$d = c\log n$, $c$ constant: subquadratic.** The polynomial method of Abboud–Williams–Yu (SODA 2015), derandomized by Chan–Williams (SODA 2016), computes the *counts* $N(a)$ for all $a \in A$ in time $n^{2 - 1/O(\log c)}$. Since HS is a yes-instance iff some $N(a)=0$, HS inherits this bound. So for every fixed $c$ the problem is subquadratic — the conjecture asserts only that the savings $1/O(\log c)$ must degrade as $c \to \infty$, exactly as for OV.
- **Bit-parallel baseline.** Brute force runs in $O(n^2 d / w)$ with word size $w = \Theta(\log n)$, i.e. $O(n^2)$ for $d = \Theta(\log n)$ — no better general bound is known.
- **Sparse/structured families.** If every $b \in B$ has $|b| \le k$ and $B$ contains all $k$-subsets of its support, or if $B$ is a laminar family, HS reduces to a covering test solvable in $\tilde O(n \cdot 2^{k})$ or $\tilde O(n)$ time.
- **Conditional derivation.** HSC holds under a $\Sigma_2$-quantified variant of SETH (Carmosino et al., ITCS 2016): hardness of $\exists\forall$-quantified CNF evaluation transfers by split-and-list.
- **Downstream verified transfers.** HSC $\Rightarrow$ Radius, Median, minimum betweenness, and $(5/3-\delta)$-approximate eccentricities all require $m^{2-o(1)}$ in sparse graphs — these implications are unconditionally proved.

## 5. Principal Obstacles

- **Quantifier alternation defeats split-and-list.** Williams' reduction encodes a CNF-SAT witness by splitting the variable set in half and listing $2^{n/2}$ partial assignments; satisfiability becomes an $\exists\exists$ statement over the two lists. HS's $\exists\forall$ pattern has no such symmetric decomposition: the universal quantifier ranges over the *whole* second list for each candidate, so the reduction target would be a $\Sigma_2$ formula, not a CNF.
- **NSETH barrier.** Because HS has both $\tilde O(n)$-time nondeterministic and co-nondeterministic certificates (Section 2), any deterministic fine-grained reduction from CNF-SAT to HS would yield a $2^{(1-\varepsilon)n}$ co-nondeterministic refutation algorithm for $k$-SAT, refuting NSETH. So the standard route to "proving" HSC is blocked unless one is willing to refute NSETH — which would itself be a major result.
- **Polynomial method saturates.** Razborov–Smolensky probabilistic polynomials for $\mathsf{AC}^0$-type predicates give degree $O(\log(1/\delta) \cdot \log^{?} d)$ and yield exactly the $n^{2-1/O(\log c)}$ savings; the exponential dependence on $c$ is intrinsic to the polynomial degree, and pushing to $n^{2-\varepsilon}$ uniformly in $c$ would refute OVC and hence SETH. The technique cannot separate HS from OV.
- **No known self-reduction.** OV is known to be equivalent (up to subpolynomial factors) to several problems and has a "moderate-dimension" self-improvement; HS lacks an analogous equivalence class, so lower-bound machinery cannot be imported.

## 6. The Gap

Proven: HS is subquadratic for each fixed $c$ ($n^{2-1/O(\log c)}$), and HSC follows from a $\Sigma_2$-quantified SETH. Conjectured: no single $\varepsilon>0$ works for all $c$.

The precise missing step is a **fine-grained reduction from a $\Sigma_2$-hard or $\Pi_1$-hard source problem to HS that does not require deterministic simulation of the universal quantifier**. Equivalently: either (i) derive HSC from SETH — which requires a *nondeterministic* or *randomized* reduction evading the NSETH barrier, or (ii) show HSC is strictly stronger than OVC by exhibiting an oracle/algebraic separation, or (iii) refute HSC by an algorithm computing $\min_{a} N(a)$ in $O(n^{2-\varepsilon})$ time for all $d = O(\log n)$ — which by the counting connection would also give faster OV counting and refute SETH.

## 7. Current Research (as of June 2026)

- **Fine-grained hardness of centrality measures.** Groups at MIT (Vassilevska Williams and students), Weizmann/Tel Aviv (Roditty), and Bar-Ilan continue mapping which graph parameters are HS-hard rather than OV-hard; the working slogan is "min-max parameters need HS, max-max parameters need OV."
- **Approximation thresholds.** Work following Backurs et al. (STOC 2018), Bonnet (STACS/ICALP 2021) and Dalirrooyfard–Wein (STOC 2021) pins exact approximation-ratio/time trade-offs for eccentricities and radius; several of the tight radius thresholds are known only under HSC. *(frontier — verify)*
- **Barrier refinement.** Continued study of NSETH, its randomized/Merlin–Arthur analogues (MA-SETH), and what they forbid; the question "which conjectures in the fine-grained zoo are provably not SETH-reducible" is active at UCSD, IAS and Copenhagen (BARC). *(frontier — verify)*
- **Algorithmic attacks.** Attempts to beat $n^{2-1/O(\log c)}$ for OV-counting via new low-degree representations or matrix-multiplication-based batching; no improvement past the Chan–Williams bound has been confirmed. *(frontier — verify)*

## 8. Future Work

- Determine whether HSC and OVC are equivalent, or construct a formal separation (e.g. in a restricted reduction model or via a natural oracle).
- Find a randomized or nondeterministic fine-grained reduction SETH $\to$ HS; this is the cleanest way to collapse HSC into the SETH world and is explicitly suggested by Carmosino et al. as the test case for whether NSETH is the "right" barrier.
- Identify further problems whose hardness is captured exactly by HSC (candidates: facility-location on sparse graphs, minimum-eccentricity shortest path, some dynamic-graph queries).
- Settle whether an $n^{2-\varepsilon}$ algorithm exists for HS with $d = \omega(\log n)$ but $d = O(\log n \log\log n)$, where the polynomial method just fails.
- Study *counting* and *approximate* variants: is estimating $\min_a N(a)$ within $1\pm\delta$ any easier than deciding $\min_a N(a) = 0$?

## 9. Key References

- **[Foundational]** Amir Abboud, Virginia Vassilevska Williams, Joshua R. Wang. *Approximation and Fixed Parameter Subquadratic Algorithms for Radius and Diameter in Sparse Graphs.* Proceedings of SODA 2016, pp. 377–391. (Introduces the Hitting Set Conjecture.)
- **[Foundational]** Ryan Williams. *A new algorithm for optimal 2-constraint satisfaction and its implications.* Theoretical Computer Science 348(2–3):357–365, 2005. (SETH $\Rightarrow$ OV hardness.)
- **[Foundational]** Russell Impagliazzo, Ramamohan Paturi. *On the Complexity of k-SAT.* Journal of Computer and System Sciences 62(2):367–375, 2001.
- **[SOTA / Recent]** Marco L. Carmosino, Jiawei Gao, Russell Impagliazzo, Ivan Mihajlin, Ramamohan Paturi, Stefan Schneider. *Nondeterministic Extensions of the Strong Exponential Time Hypothesis and Consequences for Non-reducibility.* Proceedings of ITCS 2016, pp. 261–270.
- **[SOTA / Recent]** Timothy M. Chan, Ryan Williams. *Deterministic APSP, Orthogonal Vectors, and More: Quickly Derandomizing Razborov–Smolensky.* Proceedings of SODA 2016, pp. 1246–1255.
- **[SOTA / Recent]** Amir Abboud, Ryan Williams, Huacheng Yu. *More Applications of the Polynomial Method to Algorithm Design.* Proceedings of SODA 2015, pp. 218–230.
- **[SOTA / Recent]** Arturs Backurs, Liam Roditty, Gilad Segal, Virginia Vassilevska Williams, Nicole Wein. *Towards Tight Approximation Bounds for Graph Diameter and Eccentricities.* Proceedings of STOC 2018, pp. 267–280.
- **[Related]** Marek Cygan, Holger Dell, Daniel Lokshtanov, Dániel Marx, Jesper Nederlof, Yoshio Okamoto, Ramamohan Paturi, Saket Saurabh, Magnus Wahlström. *On Problems as Hard as CNF-SAT.* ACM Transactions on Algorithms 12(3):41, 2016. (Set Cover Conjecture; contrasting covering hypothesis.)
- **[Survey]** Virginia Vassilevska Williams. *On Some Fine-Grained Questions in Algorithms and Complexity.* Proceedings of the International Congress of Mathematicians (ICM) 2018, Vol. IV, pp. 3447–3487.
- **[Survey]** Amir Abboud, Virginia Vassilevska Williams. *Popular Conjectures Imply Strong Lower Bounds for Dynamic Problems.* Proceedings of FOCS 2014, pp. 434–443.

## 10. Worked Example / Concrete Special Case

Take $d = 4$, $U = \{1,2,3,4\}$, and

$$A = \{\, a_1 = \{1,2\},\; a_2 = \{2,3\},\; a_3 = \{1,4\} \,\}, \qquad
B = \{\, b_1 = \{2,4\},\; b_2 = \{1,3\},\; b_3 = \{3,4\} \,\}.$$

**Direct check.**

| | $b_1=\{2,4\}$ | $b_2=\{1,3\}$ | $b_3=\{3,4\}$ | hits all? |
|---|---|---|---|---|
| $a_1=\{1,2\}$ | $\{2\}$ ✓ | $\{1\}$ ✓ | $\emptyset$ ✗ | no |
| $a_2=\{2,3\}$ | $\{2\}$ ✓ | $\{3\}$ ✓ | $\{3\}$ ✓ | **yes** |
| $a_3=\{1,4\}$ | $\{4\}$ ✓ | $\{1\}$ ✓ | $\{4\}$ ✓ | **yes** |

So this is a yes-instance, witnessed by $a_2$ (and $a_3$).

**Via the subset-sum algorithm of Section 4.** Encode $S \subseteq [4]$ as a bitmask $\sum_{i \in S} 2^{i-1}$. Then $b_1 = 1010_2 = 10$, $b_2 = 0101_2 = 5$, $b_3 = 1100_2 = 12$. Set $f[m] = |\{ j : b_j = m\}|$, so $f[10]=f[5]=f[12]=1$ and $f=0$ elsewhere. Compute the zeta transform $\beta[S] = \sum_{T \subseteq S} f[T]$ by four in-place passes (one per element $i$): for all $S$ with $i \in S$, $\beta[S] \mathrel{+}= \beta[S \setminus \{i\}]$. Now $a$ hits $B$ iff $\beta[\overline{a}] = 0$, where $\overline{a} = [4]\setminus a$.

- $\overline{a_1} = \{3,4\} = 1100_2$. Subsets of $\{3,4\}$ include $b_3 = \{3,4\}$, so $\beta = 1 \neq 0$: $a_1$ fails, with explicit witness $b_3$ (indeed $a_1 \cap b_3 = \emptyset$).
- $\overline{a_2} = \{1,4\} = 1001_2$. Subsets: $\emptyset,\{1\},\{4\},\{1,4\}$ — none equals $b_1,b_2,b_3$. So $\beta = 0$: $a_2$ hits $B$. ✓
- $\overline{a_3} = \{2,3\} = 0110_2$. Subsets: $\emptyset,\{2\},\{3\},\{2,3\}$ — none in $B$, so $\beta = 0$: $a_3$ hits $B$. ✓

Cost: $O(2^4 \cdot 4 + 3\cdot 4) = O(76)$ operations instead of $3 \times 3 \times 4$ pairwise intersections. The method scales to $O(nd + 2^d d)$, which is subquadratic whenever $d \le (2-\varepsilon)\log_2 n$ — and this is precisely why HSC must be stated with $d = c\log n$ for *large* $c$: the conjecture lives exactly in the regime $2^d \gg n^2$, where enumerating the universe's subsets is no longer affordable and only the polynomial method's $n^{2-1/O(\log c)}$ savings survive.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*