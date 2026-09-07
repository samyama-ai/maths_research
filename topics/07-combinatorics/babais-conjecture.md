---
id: 07-combinatorics/babais-conjecture
title: "Babai's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Babai's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/babais-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Babai; Babai–Seress 1992).** There is an absolute constant $C$ such that for every finite simple non-abelian group $G$ and every generating set $S \subseteq G$,
$$\operatorname{diam}\big(\mathrm{Cay}(G,S)\big) \;\le\; \big(\log |G|\big)^{C}.$$

The bound must be **uniform**: $C$ may not depend on $G$, on the rank or characteristic of a group of Lie type, on the degree of an alternating group, or on $|S|$. A proof requires the bound for all generating sets, including the worst case
$$\operatorname{diam}(G) := \max_{\langle S\rangle = G} \operatorname{diam}(\mathrm{Cay}(G,S)).$$
A disproof requires a family $G_i$ of finite simple groups with generating sets $S_i$ such that $\operatorname{diam}(\mathrm{Cay}(G_i,S_i)) / (\log|G_i|)^{k} \to \infty$ for every fixed $k$.

Both hypotheses are necessary. Simplicity/non-abelianness cannot be dropped: $\mathrm{Cay}(\mathbb{Z}/n, \{\pm 1\})$ has diameter $\lfloor n/2 \rfloor = \Theta(|G|)$. The conjecture is the extremal-diameter counterpart to the known fact that *some* small generating set always works well (Babai–Kantor–Lubotzky).

## 2. Mathematical Foundations

Let $G$ be a finite group and $S \subseteq G$ with $\langle S \rangle = G$. Throughout, $S$ is taken symmetric, $S = S^{-1} \ni 1$ (this changes diameters by at most a factor $2$ in the general case). The **Cayley graph** $\mathrm{Cay}(G,S)$ has vertex set $G$ and edges $\{g, sg\}$ for $s \in S$. Word length is
$$\ell_S(g) = \min\{ k : g = s_1 s_2 \cdots s_k,\ s_i \in S \}, \qquad \operatorname{diam}(\mathrm{Cay}(G,S)) = \max_{g \in G} \ell_S(g).$$
Writing $S^k = \{s_1\cdots s_k\}$, the diameter is the least $k$ with $S^k = G$.

**Trivial lower bound.** $|S^k| \le |S|^k$, so
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \;\ge\; \frac{\log |G|}{\log |S|} \;\ge\; \log_{|G|}|G| \cdot \text{(const)},$$
and for bounded $|S|$ this is $\Omega(\log |G|)$. Babai's conjecture asserts the truth is polylogarithmic, i.e. matching this bound up to a power.

**Growth / product theorems.** The dominant tool. For $A \subseteq G$ finite, $A\cdot A = \{ab\}$, $A^3 = A\cdot A\cdot A$.

> **Product Theorem (Helfgott 2008 for $\mathrm{SL}_2(\mathbb{F}_p)$; Pyber–Szabó, Breuillard–Green–Tao in general).** For every $r$ there are $\varepsilon = \varepsilon(r) > 0$ and $K = K(r)$ such that if $G$ is a finite simple group of Lie type of rank $\le r$ and $A \subseteq G$ generates $G$, then either $|A^3| \ge |A|^{1+\varepsilon}$ or $A^3 = G$.

Equivalently, in the language of approximate groups: any $K$-approximate subgroup $A$ ($|A^2| \le K|A|$, $A$ symmetric) of a bounded-rank simple group of Lie type is either of size $\le K^{O(1)}$ or of index $\le K^{O(1)}$ in $G$.

**From growth to diameter.** If $|A^3| \ge |A|^{1+\varepsilon}$ whenever $A \ne G$, iterate from $A_0 = S$: $A_{i+1} = A_i^3 = S^{3^{i+1}}$, so $\log|A_i| \ge (1+\varepsilon)^i \log 2$. After
$$k = \left\lceil \log_{1+\varepsilon}\!\frac{\log|G|}{\log 2} \right\rceil \quad\text{steps},\qquad S^{3^k} = G,$$
giving
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \le 3^{k} = \big(\log|G|\big)^{\frac{\log 3}{\log(1+\varepsilon)} + o(1)}.$$
This is exactly Babai's bound with $C = C(\varepsilon)$ — hence the conjecture reduces, for each family, to a product theorem with $\varepsilon$ independent of the parameters.

**Alternating groups.** For $G = \mathrm{Alt}(n)$, $\log|G| = \Theta(n\log n)$, so the conjecture predicts $\operatorname{diam} = n^{O(1)}$ up to logs — a *polynomial in $n$* bound.

## 3. History & State of the Art (SOTA)

- **1988.** Babai and Seress prove $\operatorname{diam}(\mathrm{Cay}(\mathrm{Sym}(n),S)) \le \exp\big((1+o(1))\sqrt{n \ln n}\big)$ for all $S$, via a sifting/covering argument. This remained the general permutation-group bound for 26 years.
- **1989.** Babai, Kantor and Lubotzky: every finite simple group $G$ has *some* generating set $S$ with $|S| \le 7$ and $\operatorname{diam}(\mathrm{Cay}(G,S)) = O(\log|G|)$. So the conjectured order of magnitude is attained; the difficulty is uniformity over all $S$.
- **1992.** Babai–Seress state the conjecture in its standard form and prove $\exp(O(\log^3 n))$ for primitive permutation groups of degree $n$ not containing $\mathrm{Alt}(n)$.
- **2008.** Helfgott's breakthrough: growth in $\mathrm{SL}_2(\mathbb{Z}/p\mathbb{Z})$, giving $\operatorname{diam} \le (\log p)^{C}$ for all generating sets — the first infinite family confirming the conjecture. Extended to $\mathrm{SL}_3(\mathbb{Z}/p\mathbb{Z})$ in 2011.
- **2011–2016.** Breuillard–Green–Tao (model-theoretic/Larsen–Pink methods) and Pyber–Szabó independently prove the product theorem for **all** simple groups of Lie type of bounded rank, settling Babai's conjecture for that entire class.
- **2014.** Helfgott–Seress: $\operatorname{diam}(\mathrm{Cay}(\mathrm{Sym}(n),S)) = \exp\big(O((\log n)^{4}\log\log n)\big)$ — quasipolynomial in $n$, a vast improvement on $\exp(\sqrt{n\log n})$ but still short of $n^{O(1)}$.
- **2019.** Halasi–Maróti–Pyber–Qiao and, earlier, Biswas–Yang give the best unconditional bounds for high-rank classical groups: for $G$ classical of rank $r$ over $\mathbb{F}_q$, $\operatorname{diam}(G) \le q^{O(r(\log r + \log q))}$-type bounds, quasipolynomial in $|G|$ when $q$ is bounded.
- **2022.** Eberhard–Jezernik: Babai's conjecture holds for high-rank classical groups with **random** generating sets.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\mathrm{SL}_2(\mathbb{F}_p)$, $p$ prime | $\operatorname{diam} \le (\log p)^{C}$, all $S$ | Helfgott 2008 |
| $\mathrm{SL}_3(\mathbb{F}_p)$ | $(\log p)^{C}$, all $S$ | Helfgott 2011 |
| All simple groups of Lie type of rank $\le r$, any $q$ | $(\log|G|)^{C(r)}$, all $S$ | Pyber–Szabó 2016; Breuillard–Green–Tao 2011 |
| Classical groups, rank $r$, bounded $q$ | quasipolynomial: $\exp(O(\log^{c}|G|))$ | Biswas–Yang 2017; Halasi–Maróti–Pyber–Qiao 2019 |
| High-rank classical groups, random $S$ | $(\log|G|)^{O(1)}$ w.h.p. | Eberhard–Jezernik 2022 |
| $\mathrm{Alt}(n)$/$\mathrm{Sym}(n)$, random $S$ of size $\ge 2$ | $O(n^{2}\log^{c} n)$ w.h.p. | Helfgott–Seress–Zuk 2015 |
| $\mathrm{Alt}(n)$, $S$ containing a permutation of support $\le 0.63n$ | $n^{O(1)}$ | Babai–Beals–Seress; Helfgott–Seress 2014 |
| $\mathrm{Sym}(n)$, $S$ containing a transposition or a $3$-cycle | $O(n^{2}\log n)$-type polynomial bounds | classical sorting-network arguments |
| $\mathrm{Sym}(n)$, $n \le 16$ (all $S$) | verified computationally, diameters $\le O(n^{2})$ scale | Bamberg–Gill–Hayes–Helfgott–Seress–Spiga 2014 |
| General $\mathrm{Sym}(n)$, all $S$ | $\exp(O((\log n)^{4}\log\log n))$ | Helfgott–Seress 2014 |

The $C$ in the bounded-rank case degrades as $r$ grows: $\varepsilon(r)$ from the product theorem decays (roughly exponentially or worse in $r$ in the known proofs), so these results do **not** combine into a uniform constant.

## 5. Principal Obstacles

1. **Rank-dependence of the product theorem.** The Larsen–Pink and escape-from-subvarieties arguments quantify over subvarieties of the algebraic group whose degrees grow with the rank $r$. The resulting $\varepsilon(r)$ tends to $0$, so $C(r) = \log 3/\log(1+\varepsilon(r)) \to \infty$. Making $\varepsilon$ rank-independent would require a fundamentally different, dimension-free argument.
2. **Alternating groups have no algebraic geometry.** $\mathrm{Alt}(n)$ is not a group of Lie type of bounded rank; there is no variety on which to run escape arguments, no Lie algebra, no Larsen–Pink classification of approximate subgroups. Helfgott–Seress instead use Babai–Seress-style combinatorial sifting plus Schreier structure trees, and the $(\log n)^4$ exponent comes from nested recursion depth.
3. **Product theorems are false verbatim for $\mathrm{Alt}(n)$.** Sets like $A = \mathrm{Alt}(n-k) \cdot F$ (a point stabilizer thickened by a small set) satisfy $|A^3| \approx |A|$ while $\langle A\rangle$ can still be large. Any growth statement must be relativized to subgroup structure, which weakens the iteration.
4. **No expansion input.** For $\mathrm{SL}_2(\mathbb{F}_p)$ with fixed generators one can get $O(\log p)$ from Selberg's $3/16$ theorem or Bourgain–Gamburd, but expansion is a *property of a particular $S$*, and there is no known mechanism forcing every generating set of a simple group to be an expander (indeed uniform expansion over all $S$ is false: $|S|$ may be huge and unstructured).
5. **Lower bounds are weak.** Nobody knows a generating set of $\mathrm{Alt}(n)$ with diameter $\gg n^{2}$ (up to logs), so there is no candidate counterexample family to guide the search either way; the conjecture cannot be tested against a sharp extremal example.

## 6. The Gap

Two separate gaps.

- **Lie type:** proven $\operatorname{diam} \le (\log|G|)^{C(r)}$; needed $C$ absolute. The missing step is a **rank-uniform product theorem**: an $\varepsilon>0$ independent of $r$ and $q$ with $|A^3| \ge |A|^{1+\varepsilon}$ for every generating $A \subsetneq G$ with $A^3 \neq G$. All current proofs consume the rank in the algebraic-geometric input.
- **Alternating:** proven $\exp(O((\log n)^{4}\log\log n))$; needed $\exp(O(\log n \log\log n)) = n^{O(1)}$ (since $\log|\mathrm{Alt}(n)| \asymp n \log n$). The gap is a factor of roughly $(\log n)^{3}$ in the exponent — i.e. removing three of the four nested recursion levels in the Helfgott–Seress construction, or replacing sifting by a genuine growth statement for $\mathrm{Alt}(n)$.

Closing either gap alone would not prove the conjecture; by the classification of finite simple groups, both families (plus high-rank Lie type over unbounded $q$) must be handled.

## 7. Current Research (as of June 2026)

- **Explicit and effective growth.** Making $\varepsilon$ and $C$ explicit for $\mathrm{SL}_2$, $\mathrm{SL}_3$ and $\mathrm{SL}_n$ over $\mathbb{F}_q$ — work of Kowalski, Dona, Rudnev–Shkredov, and the Hungarian school (Pyber, Maróti, Halasi, Szabó). The aim is to see whether the explicit $\varepsilon(r)$ can be pushed to a constant. *(frontier — verify)*
- **Additive-combinatorial input.** Improved sum–product and incidence estimates over $\mathbb{F}_q$ (Rudnev, Shkredov, Murphy, Petridis) feed directly into growth constants; several groups are testing whether the new incidence bounds give rank-independent growth for $\mathrm{SL}_2$-type subvarieties inside high-rank groups. *(frontier — verify)*
- **Random generators.** Following Helfgott–Seress–Zuk and Eberhard–Jezernik, the goal is a polynomial diameter bound for $\mathrm{Alt}(n)$ with two random generators with an explicit small exponent, and a unified statement covering all simple groups with random $S$.
- **Alternating groups via structure trees.** Continuation of Helfgott–Seress: reduce the exponent $4$ using better splitting/orbit-refinement arguments, or prove a "growth in $\mathrm{Alt}(n)$" theorem relativized to Young-subgroup-like obstructions. Helfgott (Göttingen), Spiga (Milano-Bicocca), Pyber (Rényi Institute) are the visible centres.
- **Algorithmic motivation.** Babai's conjecture underpins the analysis of nearly-linear-time algorithms in computational group theory (Seress' book, GAP/Magma black-box algorithms); a proof would remove heuristics from permutation-group algorithms.

## 8. Future Work

- Prove a **dimension-free product theorem** for $\mathrm{SL}_n(\mathbb{F}_q)$, e.g. via a Freiman-type structure theorem for approximate subgroups that does not quantify over subvariety degrees.
- Establish Babai's conjecture for $\mathrm{Alt}(n)$ first for **primitive** generating sets containing a fixed-degree element, then bootstrap; the weakest link is generating sets consisting of permutations of full support and large order.
- Develop **lower-bound technology**: exhibit generating sets of $\mathrm{Alt}(n)$ with diameter $\Omega(n^{2+\delta})$, or prove $\operatorname{diam}(\mathrm{Alt}(n)) = O(n^{3})$; either would sharpen expectations.
- Extend growth theorems to **bounded-generation and mixing-time** statements, following the Bourgain–Gamburd machinery, to obtain $O(\log|G|)$ (not just polylog) for generic $S$.
- Weaker but useful targets: a $(\log|G|)^{C\log\log|G|}$ bound for *all* finite simple groups uniformly, which is currently open in full generality.

## 9. Key References

- **[Foundational]** L. Babai, Á. Seress. *On the diameter of Cayley graphs of the symmetric group.* Journal of Combinatorial Theory Series A, 49 (1988), 175–179.
- **[Foundational]** L. Babai, Á. Seress. *On the diameter of permutation groups.* European Journal of Combinatorics, 13 (1992), 231–243.
- **[Foundational]** L. Babai, W. M. Kantor, A. Lubotzky. *Small-diameter Cayley graphs for finite simple groups.* European Journal of Combinatorics, 10 (1989), 507–522.
- **[Breakthrough]** H. A. Helfgott. *Growth and generation in $SL_2(\mathbb{Z}/p\mathbb{Z})$.* Annals of Mathematics, 167 (2008), 601–623.
- **[Breakthrough]** H. A. Helfgott. *Growth in $SL_3(\mathbb{Z}/p\mathbb{Z})$.* Journal of the European Mathematical Society, 13 (2011), 761–851.
- **[SOTA]** E. Breuillard, B. Green, T. Tao. *Approximate subgroups of linear groups.* Geometric and Functional Analysis, 21 (2011), 774–819.
- **[SOTA]** L. Pyber, E. Szabó. *Growth in finite simple groups of Lie type.* Journal of the American Mathematical Society, 29 (2016), 95–146.
- **[SOTA]** H. A. Helfgott, Á. Seress. *On the diameter of permutation groups.* Annals of Mathematics, 179 (2014), 611–658.
- **[SOTA]** Z. Halasi, A. Maróti, L. Pyber, Y. Qiao. *An improved diameter bound for finite simple groups of Lie type.* Bulletin of the London Mathematical Society, 51 (2019), 645–657.
- **[SOTA]** A. Biswas, Y. Yang. *A diameter bound for finite simple groups of large rank.* Journal of the London Mathematical Society, 95 (2017), 455–474.
- **[Recent]** S. Eberhard, U. Jezernik. *Babai's conjecture for high-rank classical groups with random generators.* Inventiones Mathematicae, 227 (2022).
- **[Recent]** H. A. Helfgott, Á. Seress, A. Zuk. *Random generators of the symmetric group: diameter, mixing time and spectral gap.* Journal of Algebra, 421 (2015), 349–368.
- **[Computational]** J. Bamberg, N. Gill, T. P. Hayes, H. A. Helfgott, Á. Seress, P. Spiga. *Bounds on the diameter of Cayley graphs of the symmetric group.* Journal of Algebraic Combinatorics, 40 (2014), 1–22.
- **[Survey]** H. A. Helfgott. *Growth in groups: ideas and perspectives.* Bulletin of the American Mathematical Society, 52 (2015), 357–413.
- **[Book]** Á. Seress. *Permutation Group Algorithms.* Cambridge University Press, 2003.

## 10. Worked Example / Concrete Special Case

**Setting.** $G = \mathrm{SL}_2(\mathbb{F}_p)$, $|G| = p(p^2-1)$, so $\log|G| = 3\log p + O(1/p)$. Take $p = 101$: $|G| = 101 \cdot 10200 = 1{,}030{,}200$.

**Step 1 — lower bound.** With any $S$ of size $4$ (two generators and inverses), $|S^k| \le 4^k$, so
$$\operatorname{diam} \ \ge\ \log_4(1{,}030{,}200) \approx 9.98 \ \Rightarrow\ \operatorname{diam} \ge 10 .$$
Diameter is therefore at least $\asymp \log|G|$ — the conjecture cannot be improved below exponent $C=1$.

**Step 2 — growth (Helfgott).** Helfgott's theorem: there is $\varepsilon>0$ (absolute for $\mathrm{SL}_2$) such that for $A \subseteq \mathrm{SL}_2(\mathbb{F}_p)$ generating and $|A| \le |G|^{1-\delta}$,
$$|A\cdot A\cdot A| \ \ge\ |A|^{1+\varepsilon}.$$

**Step 3 — iteration.** Set $A_0 = S$, $|A_0| \ge 2$, and $A_{i+1} = A_i^3$, so $A_i \subseteq S^{3^i}$ and
$$\log|A_i| \ \ge\ (1+\varepsilon)^{i}\log 2 .$$
The process saturates ($A_i = G$) once $(1+\varepsilon)^i \log 2 \ge \log|G| = 3\log p$, i.e. after
$$k \;=\; \left\lceil \frac{\log\big(3\log p/\log 2\big)}{\log(1+\varepsilon)} \right\rceil \text{ steps}.$$
Hence
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \ \le\ 3^{k} \ =\ \exp\!\Big( \tfrac{\log 3}{\log(1+\varepsilon)} \cdot \log\log|G| \cdot (1+o(1)) \Big) \ =\ (\log|G|)^{\,C}, \quad C = \frac{\log 3}{\log(1+\varepsilon)} .$$
For a modest $\varepsilon = 1/10$: $C = \log 3/\log 1.1 \approx 11.5$. With $p=101$, $3\log p / \log 2 \approx 20$, so $k = \lceil \log 20/\log 1.1\rceil = \lceil 31.4 \rceil = 32$ — a formally huge bound $3^{32}$, but a *constant power of $\log|G|$* as $p \to \infty$, which is exactly what the conjecture asserts.

**Step 4 — why this does not finish the problem.** Repeat for $G = \mathrm{SL}_r(\mathbb{F}_p)$. The known product theorems give $\varepsilon = \varepsilon(r)$ decaying in $r$, so $C(r) = \log 3/\log(1+\varepsilon(r)) \to \infty$: the same computation yields $(\log|G|)^{C(r)}$, not a uniform power. And for $G = \mathrm{Alt}(n)$ the very first step fails — no product theorem of this form is available, because $A = \mathrm{Alt}(n-1)\cup\{g\}$ has $|A^3| = O(|A|)$ while $\langle A\rangle = \mathrm{Alt}(n)$.

**Contrast with the abelian case.** For $G = \mathbb{Z}/p$, $S = \{\pm 1\}$: $|S^k| = 2k+1$ grows only linearly, $\operatorname{diam} = (p-1)/2 \approx |G|/2$, exponentially larger than $(\log|G|)^C$. This is the precise reason the conjecture is restricted to simple non-abelian groups: growth of the form $|A^3| \ge |A|^{1+\varepsilon}$ is impossible when large approximate subgroups (arithmetic progressions) exist.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*