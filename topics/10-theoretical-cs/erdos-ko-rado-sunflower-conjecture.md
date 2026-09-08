---
id: 10-theoretical-cs/erdos-ko-rado-sunflower-conjecture
title: "Sunflower-Free Set Growth and the Sunflower Conjecture"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sunflower-Free Set Growth and the Sunflower Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/erdos-ko-rado-sunflower-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

A family $\mathcal{S} = \{S_1,\dots,S_r\}$ of distinct sets is an **$r$-sunflower** (or $\Delta$-system) with **core** $Y$ if
$$S_i \cap S_j = Y \quad \text{for all } i \neq j .$$
The sets $S_i \setminus Y$ are the **petals**; they are pairwise disjoint and (for $r \ge 3$) may be empty only if $r$ sets coincide, which distinctness forbids for more than one index. The core may be empty, in which case a sunflower is just a family of $r$ pairwise disjoint sets.

Let $f(k,r)$ be the maximum size of a **sunflower-free** family — a family of sets each of size exactly $k$ containing no $r$-sunflower.

**Erdős–Rado Sunflower Conjecture (1960).** For every $r \ge 3$ there is a constant $C(r)$ such that
$$f(k,r) \le C(r)^{\,k}.$$
The strong form asserts $C(r) = O(r)$, i.e. $f(k,r) \le (Cr)^k$ for an absolute constant $C$. Erdős offered \$1000 for the case $r = 3$.

A complete proof requires an upper bound $f(k,r) \le C(r)^k$ valid for all $k$; a disproof requires, for some fixed $r$, a family of $k$-sets of size $\omega(C^k)$ for every constant $C$, i.e. super-exponential growth in $k$.

## 2. Mathematical Foundations

Fix a ground set $X$ and write $\binom{X}{k}$ for its $k$-subsets. A family $\mathcal{F} \subseteq \binom{X}{k}$ is $k$-uniform.

**Erdős–Rado theorem (1960).** If $|\mathcal{F}| > k!\,(r-1)^k$ then $\mathcal{F}$ contains an $r$-sunflower. Equivalently
$$f(k,r) \le k!\,(r-1)^k .$$

*Proof sketch (greedy).* Induct on $k$. Take a maximal collection of pairwise disjoint members of $\mathcal{F}$. If it has $\ge r$ members we have a sunflower with empty core. Otherwise its union $Z$ has $|Z| \le (r-1)k$ and meets every $S \in \mathcal{F}$; some $x \in Z$ lies in $\ge |\mathcal{F}|/((r-1)k)$ sets. The link $\mathcal{F}_x = \{S \setminus \{x\} : x \in S \in \mathcal{F}\}$ is $(k-1)$-uniform, and an $r$-sunflower in $\mathcal{F}_x$ pulls back to one in $\mathcal{F}$ with core enlarged by $x$. $\square$

**Lower bound.** Let $B_1,\dots,B_k$ be pairwise disjoint sets of size $r-1$ and let
$$\mathcal{T} = \{ \{b_1,\dots,b_k\} : b_i \in B_i \}, \qquad |\mathcal{T}| = (r-1)^k .$$
Any $r$ members must repeat a coordinate value by pigeonhole in some block, so no $r$ of them are "pairwise-equal-intersection" with disjoint petals: $\mathcal{T}$ is sunflower-free. Hence
$$(r-1)^k \le f(k,r) \le k!\,(r-1)^k ,$$
and the conjecture asserts the truth is the lower end up to an exponential factor. The gap between the two bounds is the factor $k! = 2^{\Theta(k\log k)}$.

**Erdős–Szemerédi variant (1978).** Let $g(n)$ be the maximum size of a family $\mathcal{F} \subseteq 2^{[n]}$ (not uniform) with no $3$-sunflower. Conjecture: $g(n) \le c^n$ for some $c < 2$. The uniform conjecture implies this one by summing over $k$.

**Robust sunflowers (Rossman).** $\mathcal{F} \subseteq 2^{[n]}$ is $(p,\varepsilon)$-**spread**/robust with core $Y$ if for a $p$-random subset $W \subseteq [n]$,
$$\Pr_W\!\left[\exists S \in \mathcal{F} : S \setminus Y \subseteq W \right] \ge 1-\varepsilon .$$
Modern proofs bound the size forcing a robust sunflower, then convert; the conversion loses only $O(r)^k$.

## 3. History & State of the Art (SOTA)

- **1960.** Erdős and Rado prove the sunflower lemma $f(k,r) \le k!(r-1)^k$ in *Intersection theorems for systems of sets* and pose the conjecture.
- **1961.** Erdős–Ko–Rado's intersecting-family theorem ($|\mathcal F| \le \binom{n-1}{k-1}$ for intersecting $\mathcal F \subseteq \binom{[n]}{k}$, $n \ge 2k$) establishes the surrounding extremal framework; sunflower problems are its non-intersecting counterpart.
- **1972.** Abbott, Hanson and Sauer give improved lower bounds, notably $f(k,3) \ge 10^{k/2} \approx 3.162^k$, beating the trivial $2^k$, and settle small $k$ exactly.
- **1978.** Erdős and Szemerédi state the non-uniform $c^n$, $c<2$ version.
- **1985.** Razborov's monotone circuit lower bound for CLIQUE uses sunflower-style approximation, making the lemma a staple of complexity theory (also DNF sparsification, switching lemmas, matrix multiplication).
- **1997.** Kostochka gives the first asymptotic improvement of the Erdős–Rado factorial: $f(k,3) \le c\,k!\,\big(\tfrac{\log\log\log k}{\log\log k}\big)^{k}$ — a $k!/(\log\log k)^{\Theta(k)}$ saving, still far from $C^k$.
- **2013.** Alon, Shpilka and Umans link the Erdős–Szemerédi conjecture to cap sets and to barriers for fast matrix multiplication.
- **2017.** Naslund and Sawin, using the Croot–Lev–Pach / Ellenberg–Gijswijt polynomial (slice-rank) method, prove the **Erdős–Szemerédi conjecture**: any $3$-sunflower-free $\mathcal{F} \subseteq 2^{[n]}$ satisfies $|\mathcal{F}| \le 3n\sum_{k \le n/3}\binom{n}{k} = (3/2^{2/3})^{n(1+o(1))} \approx 1.89^{\,n}$.
- **2019–2021.** Alweiss, Lovett, Wu and Zhang prove $f(k,r) \le (\log k)^{k}\,(r\log\log k)^{O(k)}$ — the first quasi-polynomial-in-$k$ base. Rao's *Coding for sunflowers* and Tao's entropy reformulation simplify it; Bell, Chueluecha and Warnke sharpen it to the current record
$$f(k,r) \;\le\; \big(C\,r\log k\big)^{k}.$$

The state of the art is therefore a single $\log k$ factor per element away from the conjecture.

## 4. Partial Results / Verified Cases

- **$r=2$:** trivial — any two distinct sets form a $2$-sunflower, so $f(k,2)=1$.
- **$k=1$:** $f(1,r) = r-1$ exactly (singletons; $r$ of them are disjoint).
- **$k=2$:** $f(2,r) = \Theta(r^2)$, with exact values by Abbott–Hanson–Sauer; e.g. $f(2,3)=6$ (see §10). The conjecture holds here.
- **$k=3$:** exact and near-exact values known for small $r$ by Abbott–Hanson–Sauer and later computation; conjecture holds.
- **Non-uniform / Erdős–Szemerédi form:** **proved** (Naslund–Sawin 2017), with $|\mathcal F| \le 1.89^n$ for subsets of $[n]$ and, in the $[3]^n$ combinatorial-cube formulation, at most $(3/2^{2/3})^{n(1+o(1))}$ sunflower-free points.
- **General $k$, all $r \ge 3$:** $f(k,r) \le (Cr\log k)^k$ (Bell–Chueluecha–Warnke 2021), improving ALWZ 2021 and Kostochka 1997.
- **Bounded ground set:** if $\mathcal F \subseteq \binom{[n]}{k}$ with $n = O(k)$, the polynomial method gives $c^n = C^{O(k)}$ bounds, so the conjecture holds when the universe is linear in $k$.
- **Structured families:** for families closed under a transitive group action, or families of low VC dimension / bounded "spread", $C(r)^k$-type bounds are known.
- **Lower bounds:** $f(k,3) \ge 10^{k/2}$; no super-exponential construction is known for any fixed $r$, which is the main empirical support for the conjecture.

## 5. Principal Obstacles

- **The greedy argument is lossy by design.** Erdős–Rado loses a factor $k$ per induction step (picking the most popular element of a $(r-1)k$-element cover), giving $k!$. Any proof of the conjecture must lose only $O(r)$ per step, i.e. must find an element of density $\Omega(1/r)$ rather than $\Omega(1/rk)$ — but such an element need not exist in a single step; the gain must be amortised over many steps, and no clean potential function achieving this is known.
- **Spread-based methods hit a genuine $\log k$.** ALWZ/Rao show that a $p$-spread family with $p = O(r\log k / k)$ contains a robust sunflower. The $\log k$ arises from a union bound over $k$ coordinates in the random-restriction/encoding argument, and matching lower bounds exist for the *spread-to-sunflower* step itself: $\log k$ is tight for the intermediate statement, though not known to be tight for $f(k,r)$. The obstacle is that the intermediate object is strictly weaker than what is needed.
- **The polynomial method does not survive non-uniformity loss.** Slice rank bounds the number of solutions to $x+y+z=0$-type equations in $\mathbb{F}_3^n$ and transfers to sunflower-freeness only because a $3$-sunflower in $2^{[n]}$ encodes as a $[3]^n$ line. The encoding is intrinsically tied to $r=3$ and to the *whole cube* $2^{[n]}$; for $k$-uniform families with $n \gg k$ the resulting bound $1.89^{n}$ is vacuous, since $\binom{n}{k}$ is far smaller. There is no known slice-rank argument sensitive to uniformity.
- **No $r$-uniform algebraic identity for $r>3$.** The cap-set machinery uses three-term structure; general $r$-sunflowers correspond to combinatorial lines of length $r$ in $[r]^n$, i.e. multidimensional Szemerédi/density-Hales–Jewett territory, where bounds are far weaker (tower-type or Ackermann-type in the general case).
- **Entropy/coding proofs are already tight for their encoding.** Rao's compression argument encodes a set by its interaction with a random restriction; the code length is provably $\Theta(k\log(r\log k))$ bits, so no reorganisation of that same encoding can reach $k\log(Cr)$.

## 6. The Gap

Proved: $f(k,r) \le (Cr\log k)^{k}$. Conjectured: $f(k,r) \le (Cr)^{k}$. The gap is the multiplicative factor
$$\left(\log k\right)^{k} = 2^{\,k \log\log k},$$
which is sub-factorial but still super-exponential — enough to break every complexity-theoretic application (DNF sparsification, monotone circuit approximators) that needs a clean $C^k$.

Concretely, the missing step is: **show that a $k$-uniform family which is $p$-spread for $p = C r/k$ (no $\log k$) contains a robust $r$-sunflower**, or find a different route that avoids spreadness. The known counterexamples to the naive spread statement at $p = Cr/k$ are not sunflower-free families — they are spread families with no robust sunflower — so the barrier is at the level of the proof technique, not the conjecture.

## 7. Current Research (as of June 2026)

- **Sharpening the spread threshold.** Groups around Lovett (UC San Diego), Rao (U. Washington), and Warnke (UCSD) study whether the $\log k$ in the spread-to-sunflower lemma can be removed under extra hypotheses (e.g. families of bounded "local" spread, or $k$-uniform families on a ground set of size $\mathrm{poly}(k)$). *(frontier — verify)* Preprints claiming $O(r\log\log k)^k$ for restricted universes circulate but are not consensus.
- **Thresholds connection.** The ALWZ machinery underlies the Park–Pham proof of the Kahn–Kalai conjecture (2022–2023); reverse transfer — using fractional-expectation-threshold technology to attack sunflowers — is an active line (Park, Pham, Frankston).
- **Robust/approximate sunflowers in complexity.** Rossman's robust sunflowers and the Lovett–Solomon–Zhang regularity framework are being pushed toward improved monotone circuit and DNF-compression bounds, where $(\log k)^k$ already suffices for some applications.
- **Algebraic approaches beyond slice rank.** Attempts to build an $r$-fold tensor analogue of the Croot–Lev–Pach lemma for $[r]^n$ lines; so far these recover density-Hales–Jewett-strength bounds only.
- **Computation.** SAT/ILP searches for $f(k,3)$ at $k = 4,5$ continue to refine lower bounds; no construction has beaten $10^{k/2}$ asymptotically since 1972.

## 8. Future Work

- **Amortised greedy.** Design a potential function $\Phi(\mathcal F)$ decreasing by $\log(Cr)$ bits per induction step on average, replacing the worst-case $\log(rk)$ loss.
- **Uniformity-aware polynomial method.** Find a slice-rank-style bound for $k$-uniform families on ground sets of size $n = k^{\omega(1)}$; this is the single most-cited desideratum.
- **Improve the lower bound.** Determine whether $f(k,3)$ is $\Theta(c^k)$ at all: even establishing $f(k,3) \ge 4^k$ would sharpen the target and rule out naive proof strategies.
- **Resolve the strong form for $r=3$ first**, as Erdős suggested; the $r$-dependence appears easier than the $k$-dependence.
- **Applications-first.** Isolate the weakest sunflower-type statement sufficient for DNF sparsification and monotone lower bounds, and prove that instead.

## 9. Key References

- **[Foundational]** P. Erdős, R. Rado. *Intersection theorems for systems of sets.* Journal of the London Mathematical Society, 35:85–90, 1960.
- **[Foundational]** P. Erdős, C. Ko, R. Rado. *Intersection theorems for systems of finite sets.* Quarterly Journal of Mathematics (Oxford), 12:313–320, 1961.
- **[Foundational]** H. L. Abbott, D. Hanson, N. Sauer. *Intersection theorems for systems of sets.* Journal of Combinatorial Theory, Series A, 12:381–389, 1972.
- **[Foundational]** P. Erdős, E. Szemerédi. *Combinatorial properties of systems of sets.* Journal of Combinatorial Theory, Series A, 24:308–313, 1978.
- **[Milestone]** A. V. Kostochka. *A bound of the cardinality of families not containing $\Delta$-systems.* In *The Mathematics of Paul Erdős II*, Springer, 1997.
- **[Milestone]** A. A. Razborov. *Lower bounds on the monotone complexity of some Boolean functions.* Doklady Akademii Nauk SSSR, 281:798–801, 1985.
- **[Milestone]** N. Alon, A. Shpilka, C. Umans. *On sunflowers and matrix multiplication.* Computational Complexity, 22(2):219–243, 2013.
- **[Milestone]** E. Naslund, W. Sawin. *Upper bounds for sunflower-free sets.* Forum of Mathematics, Sigma, 5:e15, 2017.
- **[SOTA]** R. Alweiss, S. Lovett, K. Wu, J. Zhang. *Improved bounds for the sunflower lemma.* Annals of Mathematics, 194(3):795–815, 2021 (also STOC 2020).
- **[SOTA]** A. Rao. *Coding for sunflowers.* Discrete Analysis, 2020:2, 2020.
- **[SOTA]** T. Bell, S. Chueluecha, L. Warnke. *Note on sunflowers.* Discrete Mathematics, 344(7):112367, 2021.
- **[Related]** J. S. Ellenberg, D. Gijswijt. *On large subsets of $\mathbb{F}_q^n$ with no three-term arithmetic progression.* Annals of Mathematics, 185(1):339–343, 2017.
- **[Survey]** M. Deza, P. Frankl. *Erdős–Ko–Rado theorem — 22 years later.* SIAM Journal on Algebraic and Discrete Methods, 4(4):419–431, 1983.
- **[Survey]** S. Jukna. *Extremal Combinatorics: With Applications in Computer Science.* 2nd ed., Springer, 2011 (Chapter on sunflowers and their circuit applications).

## 10. Worked Example / Concrete Special Case

**Claim: $f(2,3) = 6$.** That is, any $7$ distinct $2$-element sets contain a $3$-sunflower, and $6$ do not suffice.

View the family as a graph $G$ whose edges are the $2$-sets. A $3$-sunflower among $2$-sets is one of exactly two configurations:

- **Empty core:** three pairwise disjoint edges — a matching of size $3$.
- **Core $\{v\}$:** three edges sharing exactly $v$ and otherwise disjoint — a vertex of degree $3$ (the three other endpoints are automatically distinct).
- (A core of size $2$ is impossible: it would force three equal edges.)

So *sunflower-free* $\equiv$ $\Delta(G) \le 2$ **and** $\nu(G) \le 2$, where $\Delta$ is the maximum degree and $\nu$ the matching number.

*Upper bound.* $\Delta(G)\le 2$ forces $G$ to be a disjoint union of paths and cycles. For a path $P$ with $e$ edges, $\nu(P) = \lceil e/2 \rceil$; for a cycle $C_m$, $\nu = \lfloor m/2 \rfloor$ and $e = m$. Matching numbers add over components, so $\nu(G) \le 2$ means:
- one component with $\nu = 2$ plus one with $\nu \le 0$ (no edges), or two components with $\nu = 1$ each.

A single component with $\nu = 2$ has at most $5$ edges ($C_5$: $\nu = \lfloor 5/2\rfloor = 2$; $C_6$ has $\nu=3$; a path with $5$ edges has $\nu = 3$). Two components with $\nu = 1$ each are triangles or single edges/paths of length $\le 2$; a triangle has $3$ edges and $\nu = 1$, and it is the maximum such. So the best is two disjoint triangles: $6$ edges. Hence $|\mathcal F| \le 6$.

*Lower bound (extremal family).* Take
$$\mathcal{F} = \{12,\,23,\,13,\;45,\,56,\,46\}$$
— two vertex-disjoint triangles on $\{1,2,3\}$ and $\{4,5,6\}$. Every vertex has degree $2$, so no star-sunflower. The maximum matching picks one edge per triangle, so $\nu = 2$ and there is no $3$-matching. $\mathcal F$ is sunflower-free with $|\mathcal F| = 6$. $\blacksquare$

**Comparison of bounds at $k=2$, $r=3$.** The block construction of §2 gives $(r-1)^k = 2^2 = 4$; the truth is $6$; Erdős–Rado gives $k!(r-1)^k = 2\cdot 4 = 8$. The conjecture $C(3)^k$ is comfortably satisfied with $C(3) = \sqrt{6} \approx 2.449$. The whole difficulty is that as $k$ grows, the Erdős–Rado ratio $\text{upper}/\text{lower} = k!$ explodes while every known construction stays at $c^k$ with $c \le \sqrt{10}$ — exactly the tension the conjecture asserts should be resolved in favour of the constructions.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*