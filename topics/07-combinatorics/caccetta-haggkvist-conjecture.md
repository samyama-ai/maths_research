---
id: 07-combinatorics/caccetta-haggkvist-conjecture
title: "Caccetta-Häggkvist Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Caccetta-Häggkvist Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/caccetta-haggkvist-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $D$ be a digraph on $n$ vertices (no loops; at most one arc $u\to v$ for each ordered pair, so a $2$-cycle "digon" is allowed). Write $d^+(v)$ for the out-degree of $v$ and $g(D)$ for the *directed girth*, the length of a shortest directed cycle ($g(D)=\infty$ if $D$ is acyclic).

**Conjecture (Caccetta–Häggkvist, 1978).** If every vertex of $D$ has $d^+(v)\ge r$ with $r\ge 1$, then
$$g(D)\;\le\;\left\lceil \frac{n}{r}\right\rceil .$$

Equivalently: every digraph with minimum out-degree at least $n/k$ contains a directed cycle of length at most $k$.

The case $k=3$ is the celebrated open core:

**Triangle case.** Every digraph on $n$ vertices with $\delta^+(D)\ge n/3$ contains a directed triangle. Contrapositive: every digraph with no directed cycle of length $\le 3$ has a vertex of out-degree $< n/3$.

A complete proof must handle all $n$ and all $r$; a disproof requires one explicit family with $\delta^+\ge r$ and $g > \lceil n/r\rceil$. The bound is sharp (Section 10), so no constant-factor weakening is available: the target is the exact constant $1$ in front of $n/r$.

## 2. Mathematical Foundations

Let $D=(V,A)$, $|V|=n$. For $v\in V$ set
$$N^+(v)=\{u: (v,u)\in A\},\quad N^-(v)=\{u:(u,v)\in A\},\quad \delta^+(D)=\min_v |N^+(v)| .$$
Define $N^{++}(v)=\bigcup_{u\in N^+(v)}N^+(u)\setminus (N^+(v)\cup\{v\})$, the *second out-neighbourhood*.

**Girth-3-free characterisation.** $D$ has no directed triangle and no digon iff for all $v$, $N^+(v)$ is an independent set in $D$ (no arc inside $N^+(v)$), i.e. $A\cap (N^+(v)\times N^+(v))=\emptyset$.

**Extremal circulant.** For $n,r$ let $C_n(1,\dots,r)$ have $V=\mathbb Z_n$ and arcs $i\to i+j$, $1\le j\le r$. Then $\delta^+=r$ and
$$g\bigl(C_n(1,\dots,r)\bigr)=\left\lceil \frac{n}{r}\right\rceil,$$
since a closed walk of $\ell$ steps has step-sum in $[\ell,\ell r]$ and must equal a positive multiple of $n$; the least such $\ell$ is $\lceil n/r\rceil$. This shows the conjecture, if true, is best possible for every $n,r$.

**Density normalisation.** Put $\alpha=\delta^+(D)/n$. The triangle case asserts: $\alpha\ge 1/3 \Rightarrow$ triangle. Define
$$\alpha^\ast=\inf\{\alpha:\ \delta^+(D)\ge \alpha n \Rightarrow D \text{ has a directed triangle}\}.$$
Conjecture: $\alpha^\ast=1/3$. All known unconditional results give upper bounds $\alpha^\ast\le c$ with $c>1/3$.

**Related statements used as leverage.**
- *Behzad–Chartrand–Wall (1970):* for $r$-regular digraphs, $g\le\lceil n/r\rceil$ — the regular special case.
- *Seymour's Second Neighbourhood Conjecture:* every digraph without digons has a vertex $v$ with $|N^{++}(v)|\ge |N^+(v)|$. It implies the triangle case of Caccetta–Häggkvist for digon-free digraphs, since $|N^+|+|N^{++}|\le n$ forces a vertex with $|N^+(v)|\le n/3$ when triangle-free.
- *Chudnovsky–Seymour–Sullivan:* in a triangle-free digraph, $\beta(D)\le \gamma(D)/2$, where $\gamma$ is the number of digon-free "non-edges" completing a directed triangle-path and $\beta$ is the minimum number of arcs whose removal makes $D$ acyclic.

## 3. History & State of the Art (SOTA)

- **1970.** Behzad, Chartrand and Wall conjecture the regular case.
- **1978.** L. Caccetta and R. Häggkvist state the general conjecture at the 9th Southeastern Conference and prove $g\le \lceil n/r\rceil$ for $r\le 3$, plus the bound $\alpha^\ast\le (3-\sqrt5)/2\approx 0.3820$ for triangles.
- **1983.** Chvátal and Szemerédi prove $g\le n/r+2500$ — the first result with the right leading constant, off by an additive absolute constant.
- **1987.** Hoàng–Reed settle $r=5$; Hamidoune settles $r=4$ and proves the conjecture for Cayley digraphs of abelian groups.
- **1997–2002.** Bondy's subgraph-counting method gives $\alpha^\ast\le (2\sqrt6-3)/5\approx 0.3797$; Shen improves to $0.3542$ (1998) and sharpens the additive constant to $g\le \lceil n/r\rceil+73$ (2002).
- **2007.** Hamburger, Haxell and Kostochka: $\alpha^\ast\le 0.35312$.
- **2009/2017.** Hladký, Král' and Norin apply Razborov's flag algebras: $\alpha^\ast\le 0.3465$ — still the record.
- **2013.** Razborov proves the triangle case under explicit forbidden-subgraph hypotheses.
- **2020.** Aharoni, DeVos, González Hermosillo de la Maza, Montejano and Šámal prove a rainbow Mantel theorem, the natural "colour-class" relaxation of the triangle case.

**Status summary:** open in general; open for $k=3$; the additive-constant version is essentially solved ($+73$), the multiplicative-constant version is not.

## 4. Partial Results / Verified Cases

| Case / class | Result | Source |
|---|---|---|
| $r\le 3$ | conjecture true | Caccetta–Häggkvist 1978 |
| $r=4$ | true | Hamidoune 1987 |
| $r=5$ | true | Hoàng–Reed 1987 |
| all $r$, additive slack | $g\le n/r+2500$ | Chvátal–Szemerédi 1983 |
| all $r$, additive slack | $g\le\lceil n/r\rceil+73$ | Shen 2002 |
| Cayley digraphs of abelian groups | true | Hamidoune 1987 |
| $k=3$, density form | $\delta^+\ge 0.3820n\Rightarrow$ triangle | Caccetta–Häggkvist 1978 |
| $k=3$ | $0.3797n$ | Bondy 1997 |
| $k=3$ | $0.3542n$ | Shen 1998 |
| $k=3$ | $0.35312n$ | Hamburger–Haxell–Kostochka 2007 |
| $k=3$ | $0.3465n$ (SOTA) | Hladký–Král'–Norin 2017 |
| $k=3$ with forbidden subgraphs | true under explicit local hypotheses | Razborov 2013 |
| second-neighbourhood proxy | some $v$ with $\vert N^{++}(v)\vert\ge 0.657\,\vert N^+(v)\vert$ | Chen–Shen–Yuster 2003 |
| Seymour SNC for tournaments | true | Fisher 1996; Havet–Thomassé 1999 |
| rainbow Mantel | colour classes $>\frac{26-2\sqrt7}{81}n^2\approx 0.2557n^2$ force a rainbow triangle | Aharoni et al. 2020 |

Note the additive results imply the conjecture asymptotically whenever $r=\Theta(n)$ *fails*: for $r \le c\sqrt n$ the $+73$ term is negligible relative to $n/r$, so the hard regime is exactly $r=\Theta(n)$, i.e. bounded $k$.

## 5. Principal Obstacles

- **No slack in the extremal example.** $C_n(1,\dots,r)$ meets the bound with equality for every $n,r$, and the near-extremal family $C_{3r+1}(1,\dots,r)$ is triangle-free with $\delta^+=(n-1)/3$. Any argument must be exactly tight; stability/robustness methods that lose $o(n)$ still leave the constant undetermined only if they are tight, and none are.
- **Counting methods saturate.** Bondy-style arguments count paths of length $2$ and compare with $\sum_v d^+(v)^2$; convexity gives $\sum_v |N^{++}(v)|$ lower bounds that stop short of $1/3$ because triangle-free digraphs can have highly irregular second neighbourhoods. The extremal configurations for the counting inequality are not the conjectured extremal digraph.
- **Flag algebras hit a numerical floor.** The Hladký–Král'–Norin semidefinite programme is a finite relaxation of the true limit object (digraph limits / "diloimons"). The $0.3465$ value appears to be a genuine optimum of the relaxation at that flag order, not a computational limit; certificates at higher order have not closed the $0.3465\to 1/3$ gap, suggesting the plain flag hierarchy lacks the needed global constraints.
- **Regularity is the wrong tool.** Szemerédi regularity for digraphs loses $\varepsilon n^2$ arcs, which can destroy a minimum out-degree condition at a single vertex; the conjecture is a *minimum-degree* statement, not an average-density statement, so removal-lemma machinery does not apply directly.
- **No algebraic/spectral certificate.** Unlike Mantel/Turán problems, there is no known eigenvalue or polynomial-method reformulation whose optimum is $1/3$; the failure is that directed triangle-freeness is not expressible as a positive-semidefiniteness condition on the adjacency matrix.
- **Equivalent problems are equally hard.** Seymour's SNC and the Chudnovsky–Seymour–Sullivan conjecture would each imply the triangle case, and each is itself open with best constants ($0.657$; $\beta\le 0.88\gamma$) well away from target.

## 6. The Gap

For $k=3$ the entire gap is the interval
$$\alpha\in[\,1/3,\;0.3465\,],\qquad 0.3465-1/3\approx 0.0132 .$$
Concretely: no known theorem excludes a triangle-free digraph with $\delta^+ = 0.34n$. For general $k$ the gap is the difference between $\lceil n/r\rceil + 73$ (proved) and $\lceil n/r\rceil$ (conjectured), which is vacuous when $n/r$ is large but is the whole content when $k=n/r$ is a fixed small integer — i.e. for $r\ge 6$ and $k\in\{3,4,\dots\}$ nothing exact is known. The single step to be crossed: a tight-by-construction argument showing that in a triangle-free digraph, the local independence of every $N^+(v)$ propagates to a global out-degree deficit, with no loss beyond the $C_{3r+1}$ configuration.

## 7. Current Research (as of June 2026)

- **Higher-order flag algebras and directed limits.** Extensions of the Hladký–Král'–Norin SDP with additional structural flags and symmetry reductions; the bottleneck is SDP size growth and rounding to exact rational certificates. *(frontier — verify)* No published improvement on $0.3465$ has been confirmed.
- **Rainbow/colourful reformulations.** Following Aharoni et al. (2020), work continues on rainbow versions of Mantel and Turán-type theorems as a route to the $k=3$ case; groups associated with Aharoni (Technion), Šámal (Charles University) and DeVos (SFU) are active here.
- **Second-neighbourhood programme.** Improvements to the Chen–Shen–Yuster constant $\gamma\approx 0.657$ and proofs of SNC for further classes (digraphs with small independence number, oriented graphs of bounded degree). *(frontier — verify)*
- **Chudnovsky–Seymour–Sullivan line.** Successive improvements of $\beta\le c\,\gamma$ for triangle-free digraphs below $c=0.88$.
- **Computer-assisted exhaustive search.** Verification of the conjecture for all digraphs up to modest $n$ and structured families (circulants, Cayley digraphs of small groups) via SAT/ILP encodings.

## 8. Future Work

- Prove the triangle case for $r$-regular digraphs first ($n=3r$), where the Behzad–Chartrand–Wall form removes degree irregularity, then transfer by a degree-balancing reduction.
- Develop a stability theorem: show that a triangle-free digraph with $\delta^+\ge (1/3-\varepsilon)n$ must be close to a blow-up of a circulant $C_{3r+1}(1,\dots,r)$, then rule out the near-extremal window by exact local analysis.
- Extract from Razborov's forbidden-subgraph theorems a complete list of obstructions and close the case analysis.
- Find an entropy or spectral certificate matching $1/3$; the absence of any method whose natural optimum is $1/3$ is the strongest evidence that a new technique, not a refinement, is required.
- Settle Seymour's SNC for digon-free digraphs, which yields the $k=3$ case immediately.

## 9. Key References

- **[Foundational]** L. Caccetta and R. Häggkvist. *On minimal digraphs with given girth.* Congressus Numerantium XXI (Proc. 9th S.E. Conf. on Combinatorics, Graph Theory and Computing), 181–187, 1978.
- **[Foundational]** V. Chvátal and E. Szemerédi. *Short cycles in directed graphs.* Journal of Combinatorial Theory, Series B 35(3):323–327, 1983.
- **[Partial case]** C. T. Hoàng and B. Reed. *A note on short cycles in digraphs.* Discrete Mathematics 66(1–2):103–107, 1987.
- **[Partial case]** Y. O. Hamidoune. *A note on minimal directed graphs with given girth.* Journal of Combinatorial Theory, Series B 43(3):343–348, 1987.
- **[Method]** J. A. Bondy. *Counting subgraphs: a new approach to the Caccetta–Häggkvist conjecture.* Discrete Mathematics 165/166:71–80, 1997.
- **[Bound]** J. Shen. *Directed triangles in digraphs.* Journal of Combinatorial Theory, Series B 74(2):405–407, 1998.
- **[Bound]** J. Shen. *On the girth of digraphs.* Discrete Mathematics 211(1–3):167–181, 2000.
- **[Bound]** J. Shen. *On the Caccetta–Häggkvist conjecture.* Graphs and Combinatorics 18(3):645–654, 2002.
- **[Bound]** P. Hamburger, P. Haxell and A. Kostochka. *On directed triangles in digraphs.* Electronic Journal of Combinatorics 14(1), Note 19, 2007.
- **[SOTA]** J. Hladký, D. Král' and S. Norin. *Counting flags in triangle-free digraphs.* Combinatorica 37(1):49–76, 2017.
- **[SOTA]** A. Razborov. *On the Caccetta–Häggkvist conjecture with forbidden subgraphs.* Journal of Graph Theory 74(2):236–248, 2013.
- **[Related]** M. Chudnovsky, P. Seymour and B. Sullivan. *Cycles in dense digraphs.* Combinatorica 28(1):1–18, 2008.
- **[Related]** G. Chen, J. Shen and R. Yuster. *Second neighborhood via first neighborhood in digraphs.* Annals of Combinatorics 7(1):15–20, 2003.
- **[Related]** D. C. Fisher. *Squaring a tournament: a proof of Dean's conjecture.* Journal of Graph Theory 23(1):43–48, 1996.
- **[Related]** R. Aharoni, M. DeVos, S. González Hermosillo de la Maza, A. Montejano and R. Šámal. *A rainbow version of Mantel's theorem.* Advances in Combinatorics, 2020:2.
- **[Survey]** B. D. Sullivan. *A summary of problems and results related to the Caccetta–Häggkvist conjecture.* arXiv:math/0605646, 2006.
- **[Book]** J. Bang-Jensen and G. Gutin. *Digraphs: Theory, Algorithms and Applications.* Springer, 2nd edition, 2009.

## 10. Worked Example / Concrete Special Case

**The tightness example for the triangle case: $n=7$, $r=2$.**

Take $D = C_7(1,2)$: $V=\mathbb Z_7$, arcs $i\to i+1$ and $i\to i+2$ (mod 7). Then $d^+(v)=2$ for all $v$, so $\delta^+ = 2 = (n-1)/3$.

*Girth computation.* A directed cycle of length $\ell$ uses steps $s_1,\dots,s_\ell\in\{1,2\}$ with
$$\sum_{i=1}^{\ell}s_i \equiv 0 \pmod 7,\qquad \ell \le \sum s_i \le 2\ell .$$
- $\ell=1$: sum $\in\{1,2\}$ — no loop.
- $\ell=2$: sum $\in[2,4]$, no multiple of 7.
- $\ell=3$: sum $\in[3,6]$, no multiple of 7. **No directed triangle.**
- $\ell=4$: sum $\in[4,8]$, and $7$ is attained, e.g. $(2,2,2,1)$: $0\to2\to4\to6\to0$. So $g(D)=4$.

Check against the conjecture: $\lceil n/r\rceil=\lceil 7/2\rceil=4=g(D)$. Equality — the bound is attained.

*Why this is the barrier.* Here $\delta^+/n = 2/7 \approx 0.2857 < 1/3$, consistent with the conjecture. The general family $C_{3r+1}(1,\dots,r)$ repeats this: $\ell=3$ gives step-sums in $[3,3r]$, which misses $3r+1$, so it is triangle-free, while
$$\frac{\delta^+}{n}=\frac{r}{3r+1}\;\xrightarrow[r\to\infty]{}\;\frac13^{-}.$$
So triangle-free digraphs with out-degree ratio arbitrarily close to $1/3$ exist, and the conjecture asserts $1/3$ is exactly unattainable. The proved SOTA only forbids ratios $\ge 0.3465$; the family above reaches $0.3333\ldots$, and nothing rules out a hypothetical construction in between.

*Contrast, $n=6$, $r=2$.* Now $\lceil 6/2\rceil=3$, so every digraph on 6 vertices with $\delta^+\ge2$ must contain a directed cycle of length $\le3$ — this is covered by the proven case $r\le3$. Indeed $C_6(1,2)$ has the triangle $0\to2\to4\to0$ (step-sum $6\equiv0$). The jump from $n=6$ to $n=7$ at fixed $r=2$ is exactly where triangle-freeness becomes possible, which is what the $\lceil\cdot\rceil$ in the conjecture encodes.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*