---
id: 07-combinatorics/erdos-intersection-pattern-problem
title: "Erdős Intersection Pattern Problem"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Erdős Intersection Pattern Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/erdos-intersection-pattern-problem` · **Status:** open

## 1. Problem Statement / Conjecture

Fix integers $n \ge k \ge 0$ and a set $L \subseteq \{0,1,\dots,k-1\}$ of allowed intersection sizes. Call a family $\mathcal{F} \subseteq \binom{[n]}{k}$ **$L$-intersecting** if $|A \cap B| \in L$ for all distinct $A,B \in \mathcal{F}$, and **$L$-avoiding** if $|A \cap B| \notin L$ for all distinct $A,B \in \mathcal{F}$. Write
$$m(n,k,L) \;=\; \max\{|\mathcal{F}| : \mathcal{F} \subseteq \tbinom{[n]}{k},\ \mathcal{F} \text{ is } L\text{-avoiding}\}.$$

**The problem.** Determine $m(n,k,L)$ — or its asymptotics — for every intersection pattern $L$, and describe the extremal families.

The central open instance, posed by Erdős and Sós around 1971, is the **forbidden intersection** case $L=\{\ell\}$:

> **Conjecture (Erdős–Sós).** For every fixed $\ell \ge 0$ and every $k$ with $\ell < k$, if $\mathcal{F}\subseteq\binom{[n]}{k}$ contains no two sets $A,B$ with $|A\cap B|=\ell$, then $|\mathcal{F}| = o\!\left(\binom{n}{k}\right)$ as $n\to\infty$, and in fact $|\mathcal{F}| \le c(k,\ell)\, n^{k-\ell-1}$.

A complete solution means: for each $(k,\ell)$ an exact or asymptotically tight value of $m(n,k,\{\ell\})$ for all large $n$, together with a characterisation of the extremal configurations; and for general $L$, a determination of the exponent $\lim_{n\to\infty} \log m(n,k,L)/\log n$ when $k$ is fixed, and of the exponential rate when $k = \Theta(n)$. A disproof means exhibiting $(k,\ell)$ and families of size $\Omega(\binom{n}{k})$, or families beating the conjectured constructions.

## 2. Mathematical Foundations

Work in the **Johnson scheme** $J(n,k)$: vertices $\binom{[n]}{k}$, with $A \sim_i B$ iff $|A\cap B| = k-i$. An $L$-avoiding family is an independent set in the union of the relation graphs $\{|A\cap B| = \ell : \ell \in L\}$; an $L$-intersecting family is a clique in their union.

**Ray-Chaudhuri–Wilson (1975).** If $|L| = s$ and $\mathcal{F} \subseteq \binom{[n]}{k}$ is $L$-intersecting with $k > \max L$, then
$$|\mathcal{F}| \;\le\; \binom{n}{s}.$$

**Frankl–Wilson (1981), modular form.** If $p$ is prime, $L \subseteq \{0,\dots,p-1\}$ with $|L|=s$, $k \not\equiv \ell \pmod p$ for all $\ell \in L$, and $|A\cap B| \bmod p \in L$ for all distinct $A,B\in\mathcal F$, then $|\mathcal F| \le \binom{n}{s}$.

Both are proved by the **linear-algebra (polynomial) method**: associate to each $A \in \mathcal{F}$ the characteristic vector $x_A \in \{0,1\}^n$ and the multilinear polynomial
$$f_A(x) \;=\; \prod_{\ell \in L} \big(\langle x, x_A\rangle - \ell\big),$$
so $f_A(x_A) = \prod_{\ell\in L}(k-\ell) \ne 0$ while $f_A(x_B)=0$ for $B \ne A$. Diagonal dominance forces linear independence of $\{f_A\}$ in the space of multilinear polynomials of degree $\le s$, whose dimension is $\sum_{i\le s}\binom{n}{i}$; the refinement of Alon–Babai–Suzuki (1991) sharpens the count to $\binom{n}{s}$ in the uniform case.

**Deza–Frankl sunflower theorem (1981).** If $\mathcal{F}$ is $k$-uniform and $\{\ell\}$-intersecting (a *near-pencil* / $\Delta$-system condition) with $|\mathcal F| > k^2 - k + 1$, then $\mathcal{F}$ is a **sunflower**: there is a core $C$, $|C|=\ell$, with $A \cap B = C$ for all distinct $A,B$.

**Frankl–Rödl theorem (1987).** For every $\eta > 0$ there is $\epsilon = \epsilon(\eta) > 0$ such that if $\eta n < k < (1/2-\eta)n$ and $\ell$ satisfies
$$\min\{\ell,\; k-\ell,\; n-2k+\ell\} \;>\; \eta n,$$
then every $\{\ell\}$-avoiding $\mathcal F\subseteq\binom{[n]}{k}$ has $|\mathcal F| \le (1-\epsilon)^n \binom{n}{k}$.

The side conditions are not artefacts. For $n = 2k$, $\ell = 0$, picking one set from each complementary pair $\{A,[n]\setminus A\}$ gives an intersection-free family of size $\frac12\binom{n}{k}$, so $n-2k+\ell > \eta n$ cannot be dropped.

## 3. History & State of the Art (SOTA)

- **1961.** Erdős, Ko and Rado prove the $L = \{0\}$ case: for $n \ge 2k$, an intersecting family has $|\mathcal F| \le \binom{n-1}{k-1}$, with equality only for stars when $n>2k$.
- **1971–75.** Erdős and Sós raise the forbidden-intersection question for a single $\ell$; Erdős repeatedly offered prizes for the case $\ell=1$, $k=3$ and its generalisations.
- **1975/1981.** Ray-Chaudhuri–Wilson and Frankl–Wilson establish the $\binom{n}{s}$ bounds for $L$-intersecting families, launching the linear-algebra method.
- **1981–83.** Deza–Frankl prove the sunflower dichotomy and survey the field in "*The Erdős–Ko–Rado theorem — 22 years later*".
- **1985.** Frankl and Füredi, "*Forbidding just one intersection*", settle the fixed-$k$ regime for $k \ge 2\ell+2$: for $n \ge n_0(k,\ell)$,
  $$m(n,k,\{\ell\}) = \binom{n-\ell-1}{k-\ell-1},$$
  attained by all $k$-sets containing a fixed $(\ell+1)$-set.
- **1987.** Frankl–Rödl prove exponential savings in the linear regime $k = \Theta(n)$.
- **1993.** Kahn and Kalai use Frankl–Wilson to disprove Borsuk's conjecture, showing intersection patterns control geometric problems.
- **2009–2021.** The **junta method** (Dinur–Friedgut; Keller–Lifshitz; Ellis–Keller–Lifshitz) recasts extremal families as approximately determined by $O(1)$ coordinates, extending exact results to $n \ge Ck$ rather than $n \ge n_0(k,\ell)$ with tower-type $n_0$.
- **2017–2024.** Keevash–Long extend Frankl–Rödl to codes and permutations; Keevash–Lifshitz–Long–Minzer develop **global hypercontractivity**, giving forbidden-intersection theorems in sparse and non-product regimes with quantitatively better $\epsilon(\eta)$.

## 4. Partial Results / Verified Cases

| Regime | Result | Source |
|---|---|---|
| $L=\{0\}$, $n\ge 2k$ | $\binom{n-1}{k-1}$, exact | Erdős–Ko–Rado 1961 |
| $L=\{0,\dots,t-1\}$, $n \ge (t+1)(k-t+1)$ | $\binom{n-t}{k-t}$, exact ($t$-intersecting) | Ahlswede–Khachatrian 1997 (complete intersection theorem) |
| $L$-intersecting, $|L|=s$ | $\le \binom{n}{s}$ | Ray-Chaudhuri–Wilson 1975 |
| $\{\ell\}$-avoiding, $k \ge 2\ell+2$, $n \ge n_0(k,\ell)$ | $\binom{n-\ell-1}{k-\ell-1}$, exact | Frankl–Füredi 1985 |
| $k=3,\ \ell=1$, $4 \mid n$, $n$ large | $n$, extremal $=$ disjoint copies of $K_4^{(3)}$ | Frankl–Füredi 1985 |
| $k=\Theta(n)$, $\min\{\ell,k-\ell,n-2k+\ell\} > \eta n$ | $\le (1-\epsilon(\eta))^n\binom{n}{k}$ | Frankl–Rödl 1987 |
| $p$-modular patterns, $L\subseteq\{0,\dots,p-1\}$ | $\le \binom{n}{|L|}$ | Frankl–Wilson 1981 |
| Permutations, $q$-analogues, codes over $[m]^n$ | Frankl–Rödl analogues | Keevash–Long 2017; KLLM 2023 |
| $\mathcal F$ with all pairwise intersections in $L$, $0\notin L$, non-uniform | $\le \binom{n}{\lvert L\rvert}$ | Snevily 2003 |

Computationally, $m(n,k,L)$ has been determined by exact clique/independent-set search for all $n \le 20$ with $k \le 5$, and for $k=3,\ell=1$ up to $n \approx 30$, confirming the $n$-vs-$(n-2)$ crossover.

## 5. Principal Obstacles

- **The polynomial method saturates.** Rank arguments bound $L$-*intersecting* families by $\binom{n}{|L|}$ but say almost nothing about $L$-*avoiding* families, whose forbidden condition is a non-vanishing rather than a vanishing constraint. There is no known dual polynomial certificate.
- **No sharp isoperimetry in the middle range.** Frankl–Rödl's proof uses a Kruskal–Katona-style shifting plus a measure-concentration step whose $\epsilon(\eta)$ is exponentially small in $1/\eta$. Getting a polynomial dependence — required for $\ell$ within $o(n)$ of $k$ or of $2k-n$ — needs concentration for functions that are *not* small on every sub-cube, exactly where classical hypercontractivity fails.
- **Junta methods need $n \ge Ck$.** The Dinur–Friedgut/Keller–Lifshitz machinery approximates $\mathcal F$ by a junta on $O(1)$ coordinates; the approximation error is $\Theta((k/n)^{c})$, so it collapses when $k$ is linear in $n$, precisely the Frankl–Rödl regime.
- **Small-$k$ exceptions destroy uniformity.** For $k \le 2\ell+1$ the extremal families are not stars but algebraic designs (Steiner systems, partitions into cliques), and their existence depends on divisibility. Any general formula must encode design-existence conditions, which are themselves only known via Keevash-type probabilistic nibble constructions.
- **Spectral bounds are lossy.** The Hoffman/ratio bound in the Johnson scheme is tight for $L=\{0\}$ but off by a factor $n^{\Theta(1)}$ for $\ell \ge 1$, because the relevant eigenvalue is not attained by a rank-one perturbation.

## 6. The Gap

Two boundaries separate Section 4 from Section 1.

1. **The fixed-$k$ gap.** Frankl–Füredi gives the exact value only for $k\ge 2\ell+2$ and $n \ge n_0(k,\ell)$, where $n_0$ is not explicit and is at least exponential in $k$. For $\ell+1 \le k \le 2\ell+1$ no conjectured extremal family is even agreed on beyond sporadic cases; the truth is believed to be $\Theta(n^{\lfloor k/(\ell+1)\rfloor \cdot 0})$-type design constructions rather than juntas.
2. **The linear-$k$ gap.** Frankl–Rödl requires all three of $\ell$, $k-\ell$, $n-2k+\ell$ to exceed $\eta n$. The case $k-\ell = o(n)$ (e.g. $\ell = k - \sqrt{k}$) is open, and the boundary case $n-2k+\ell = \Theta(1)$ is genuinely different — a complement-pair construction gives $\frac12\binom{n}{k}$, so the transition from "$(1-\epsilon)^n$ small" to "constant fraction" happens somewhere in $n-2k+\ell \in [\,O(1), \eta n\,]$ and nobody knows where.

Crossing (2) requires a concentration inequality on $\binom{[n]}{k}$ with sharp dependence on the intersection parameter; crossing (1) requires a stability theory valid when the extremal object is a design rather than a junta.

## 7. Current Research (as of June 2026)

- **Global hypercontractivity school** (Keevash, Lifshitz, Long, Minzer; Oxford / HUJI / Bristol / Technion). Their JAMS-published framework replaces the requirement "$f$ has small influences" with "$f$ is global", yielding forbidden-intersection theorems for sparse families and for $[m]^n$. Work continues on pushing $\epsilon(\eta)$ to $\mathrm{poly}(\eta)$. *(frontier — verify)*
- **Junta / stability programme** (Ellis, Keller, Lifshitz). Recent efforts aim to replace $n_0(k,\ell)$ in Frankl–Füredi by an explicit linear bound $n \ge C(\ell)\,k$. *(frontier — verify)*
- **Spectral and Terwilliger-algebra approaches** to $L$-avoiding sets in $J(n,k)$, seeking semidefinite-programming bounds that beat the ratio bound for $\ell \ge 1$.
- **Design-theoretic constructions** post-Keevash's existence theorem, used to build large $\{\ell\}$-avoiding families in the range $k \le 2\ell+1$.
- **Applications feedback loop:** sharper Frankl–Rödl bounds directly improve chromatic numbers of Borsuk-type graphs and lower bounds in communication complexity, keeping the problem active outside pure extremal set theory.

## 8. Future Work

- Prove a **quantitative Frankl–Rödl theorem** with $\epsilon(\eta) = \eta^{O(1)}$; this is the stated goal of the global-hypercontractivity programme and would settle $k-\ell = n^{1-o(1)}$.
- Determine the **phase transition** in $n-2k+\ell$ between exponentially small and constant-fraction families.
- Settle $k = 2\ell+1$ exactly for all large $n$ — the first case outside Frankl–Füredi's range.
- Develop a **dual/LP-certificate** method that proves upper bounds for $L$-avoiding families the way the polynomial method does for $L$-intersecting ones.
- Extend to **general patterns** $L$ with $|L|\ge 2$: even the asymptotic exponent of $m(n,k,\{0,1\})$ for fixed $k \ge 5$ is not established.

## 9. Key References

- **[Foundational]** P. Erdős, C. Ko, R. Rado. *Intersection theorems for systems of finite sets.* Quarterly Journal of Mathematics (Oxford), Ser. 2, 12 (1961), 313–320.
- **[Foundational]** D. K. Ray-Chaudhuri, R. M. Wilson. *On $t$-designs.* Osaka Journal of Mathematics 12 (1975), 737–744.
- **[Foundational]** P. Frankl, R. M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica 1 (1981), 357–368.
- **[Foundational]** M. Deza, P. Frankl. *Every large set of equidistant $(0,+1,-1)$-vectors forms a sunflower.* Combinatorica 1 (1981), 225–231.
- **[Foundational]** P. Frankl, Z. Füredi. *Forbidding just one intersection.* Journal of Combinatorial Theory, Series A 39 (1985), 160–176.
- **[Foundational]** P. Frankl, V. Rödl. *Forbidden intersections.* Transactions of the American Mathematical Society 300 (1987), 259–286.
- **[Method]** N. Alon, L. Babai, H. Suzuki. *Multilinear polynomials and Frankl–Ray-Chaudhuri–Wilson type intersection theorems.* Journal of Combinatorial Theory, Series A 58 (1991), 165–180.
- **[Application]** J. Kahn, G. Kalai. *A counterexample to Borsuk's conjecture.* Bulletin of the American Mathematical Society 29 (1993), 60–62.
- **[Exact theory]** R. Ahlswede, L. H. Khachatrian. *The complete intersection theorem for systems of finite sets.* European Journal of Combinatorics 18 (1997), 125–136.
- **[Method]** I. Dinur, E. Friedgut. *Intersecting families are essentially contained in juntas.* Combinatorics, Probability and Computing 18 (2009), 107–122.
- **[SOTA]** P. Keevash, E. Long. *Frankl–Rödl type theorems for codes and permutations.* Transactions of the American Mathematical Society 369 (2017), 1147–1162.
- **[SOTA]** D. Ellis, N. Keller, N. Lifshitz. *Stability versions of Erdős–Ko–Rado type theorems via isoperimetry.* Journal of the European Mathematical Society 21 (2019), 3857–3902.
- **[SOTA]** N. Keller, N. Lifshitz. *The junta method for hypergraphs and the Erdős–Chvátal simplex conjecture.* Advances in Mathematics 392 (2021), 107991.
- **[SOTA]** P. Keevash, N. Lifshitz, E. Long, D. Minzer. *Hypercontractivity for global functions and sharp thresholds.* Journal of the American Mathematical Society 37 (2024), 245–279.
- **[Survey/Book]** P. Frankl, N. Tokushige. *Extremal Problems for Finite Sets.* Student Mathematical Library 86, American Mathematical Society, 2018.
- **[Survey]** M. Deza, P. Frankl. *The Erdős–Ko–Rado theorem — 22 years later.* SIAM Journal on Algebraic and Discrete Methods 4 (1983), 419–431.

## 10. Worked Example / Concrete Special Case

Take $k=3$, $\ell=1$: families of triples in which **no two triples meet in exactly one point**.

*Junta construction.* Fix the pair $P=\{1,2\}$ and let $\mathcal{S} = \{P \cup \{x\} : x \in [n]\setminus P\}$. Any two members meet in exactly $2$ points, so $\mathcal S$ is $\{1\}$-avoiding and $|\mathcal S| = n-2 = \binom{n-\ell-1}{k-\ell-1}$ with $\ell=1,k=3$. This is the family Frankl–Füredi prove optimal when $k \ge 2\ell+2$.

*Design construction beats it.* Here $k=3 < 2\ell+2 = 4$, so the theorem does not apply. Partition $[n]$ (with $4 \mid n$) into blocks $B_1,\dots,B_{n/4}$ of size $4$ and let
$$\mathcal{D} \;=\; \bigcup_{i} \binom{B_i}{3}.$$
Two triples inside the same $B_i$ share exactly $2$ elements; two triples in different blocks are disjoint, sharing $0$. Neither value is $1$, so $\mathcal D$ is $\{1\}$-avoiding, and
$$|\mathcal{D}| \;=\; \frac{n}{4}\binom{4}{3} \;=\; n \;>\; n-2 \;=\; |\mathcal{S}|.$$

*Why the gain is only additive.* Attempting blocks of size $5$ fails: $\binom{5}{3}=10$ triples per block gives $2n$ triples, but two triples inside a $5$-set can meet in exactly one point (e.g. $\{1,2,3\}$ and $\{1,4,5\}$), so the block must be thinned back to a partial Steiner system. Frankl and Füredi show that for large $n$ no construction beats $n$, so $m(n,3,\{1\}) = n$ for $4 \mid n$, $n$ large.

*The lesson.* The extremal object switches from a **junta** (all sets through a fixed $(\ell+1)$-set) to a **design** (a clique-partition) exactly at the threshold $k = 2\ell+2$. Every currently known proof technique is adapted to one side or the other, which is why the range $\ell+1 \le k \le 2\ell+1$ remains open in general.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*