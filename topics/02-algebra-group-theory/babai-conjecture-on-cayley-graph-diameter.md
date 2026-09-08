---
id: 02-algebra-group-theory/babai-conjecture-on-cayley-graph-diameter
title: "Babai's Conjecture on Diameters of Cayley Graphs"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Babai's Conjecture on Diameters of Cayley Graphs

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/babai-conjecture-on-cayley-graph-diameter` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Babai; Babai–Seress, 1988/1992).** There is an absolute constant $C$ such that for every non-abelian finite simple group $G$ and every generating set $S \subseteq G$,
$$\operatorname{diam}\big(\mathrm{Cay}(G,S)\big) \;\le\; \big(\log |G|\big)^{C}.$$

The quantifier order is what makes the problem hard: $C$ must be uniform over *all* simple groups and *all* generating sets, including adversarially chosen ones. A proof must produce such a $C$; a disproof must exhibit a family $(G_i, S_i)$ with $\operatorname{diam}(\mathrm{Cay}(G_i,S_i)) / (\log|G_i|)^{k} \to \infty$ for every fixed $k$.

Non-abelian simplicity is necessary: for $G = \mathbb{Z}/p\mathbb{Z}$ and $S=\{1\}$ the diameter is $p-1 = e^{(1+o(1))\log|G|}$, exponentially larger than any polylogarithm.

## 2. Mathematical Foundations

**Cayley graph.** For a finite group $G$ and generating set $S$, $\mathrm{Cay}(G,S)$ has vertex set $G$ and edges $\{g, gs\}$ for $s \in S$. Unless stated otherwise $S$ is taken symmetric ($S = S^{-1}$) and the graph undirected; the directed and undirected diameters differ by at most a factor of $|G|$ in general but by $O(1)$ powers in all bounds below.

**Word metric.** $|g|_S = \min\{k : g = s_1\cdots s_k,\ s_i \in S\cup S^{-1}\}$, and
$$\operatorname{diam}(\mathrm{Cay}(G,S)) = \max_{g \in G} |g|_S .$$
Writing $S^{(k)} = (S\cup S^{-1}\cup\{1\})^k$ for the ball of radius $k$, the diameter is the least $k$ with $S^{(k)} = G$.

**Trivial lower bound.** Since $|S^{(k)}| \le (2|S|+1)^k$,
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \;\ge\; \frac{\log|G|}{\log(2|S|+1)},$$
so the conjecture asserts that the trivial bound is tight up to a fixed power.

**Growth / product theorems.** The engine of all positive results. A *product theorem* for a family $\mathcal{G}$ asserts: there is $\varepsilon>0$ such that for all $G\in\mathcal{G}$ and all generating $A \subseteq G$ with $A = A^{-1}$,
$$|A\cdot A\cdot A| \;\ge\; |A|^{1+\varepsilon} \qquad\text{unless}\qquad A\cdot A\cdot A = G .$$
Iterating from $A = S$ gives $|S^{(3^m)}| \ge |S|^{(1+\varepsilon)^m}$, hence $G$ is filled after $m = O(\varepsilon^{-1}\log\log|G|)$ rounds and
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \;\le\; 3^{m} = (\log|G|)^{O(1/\varepsilon)} .$$
So a product theorem with $\varepsilon$ bounded below yields Babai's conjecture for that family, with $C = O(1/\varepsilon)$.

**Approximate groups.** $A$ is a *$K$-approximate group* if $A=A^{-1}$, $1\in A$, and $A\cdot A \subseteq X\cdot A$ for some $X$ with $|X|\le K$. Product theorems are equivalent to classification statements: every $K$-approximate subgroup of a bounded-rank finite simple group of Lie type is, up to $K^{O(1)}$-controlled error, a coset of a subgroup (Breuillard–Green–Tao; Pyber–Szabó).

**Reduction via CFSG.** The classification of finite simple groups splits the conjecture into: (i) alternating groups $A_n$, where $\log|A_n| = (1+o(1))\,n\log n$; (ii) groups of Lie type $G(q)$ of rank $r$, where $\log|G| \asymp r^2 \log q$; (iii) 26 sporadic groups, a finite list, hence trivial.

## 3. History & State of the Art (SOTA)

- **1988.** Babai and Seress, studying $\mathrm{Cay}(S_n,S)$, prove $\operatorname{diam} \le \exp\big((1+o(1))\sqrt{n\ln n}\big)$ and raise the polylogarithmic question. The general conjecture for all non-abelian finite simple groups is stated in Babai–Seress (1992).
- **1989.** Babai–Kantor–Lubotzky: every finite simple group $G$ admits *some* generating set of size $\le 7$ with $\operatorname{diam} = O(\log|G|)$. So the conjecture is about the worst generating set, not the existence of a good one.
- **2008.** Helfgott's breakthrough: $\operatorname{diam}(\mathrm{Cay}(\mathrm{SL}_2(\mathbb{F}_p),S)) = O((\log p)^{C})$ for all generating $S$, via the first product theorem $|A^3|\ge|A|^{1+\varepsilon}$. Bourgain–Gamburd independently derived uniform spectral-gap (expansion) results for $\mathrm{SL}_2(\mathbb{F}_p)$ under a Zariski-density hypothesis on lifts.
- **2011.** Helfgott extends to $\mathrm{SL}_3(\mathbb{Z}/p\mathbb{Z})$.
- **2011–2016.** Breuillard–Green–Tao and, independently, Pyber–Szabó prove product theorems for **all** finite simple groups of Lie type of bounded rank $r$, with $\varepsilon = \varepsilon(r)>0$. This settles Babai's conjecture for bounded rank.
- **2014.** Helfgott–Seress: for every transitive $G\le S_n$ (hence for $A_n$, $S_n$),
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \le \exp\!\big(O((\log n)^4 \log\log n)\big),$$
a quasipolynomial-in-$n$ bound; Helfgott later removed the $\log\log n$ factor. This is still superpolynomial in $n$, and Babai's conjecture wants $\mathrm{poly}(n\log n)$.
- **2017–2022.** Large-rank progress: Biswas–Yang give $\operatorname{diam} \le q^{O(r(\log r+\log q)^3)}$ for classical groups of rank $r$ over $\mathbb{F}_q$; Halasi–Maróti–Pyber–Qiao improve the rank-dependence of the exponent in the bounded-rank bound to an explicit polynomial in $r$; Eberhard–Jezernik prove the conjecture for high-rank classical groups with **random** generators.

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| $\mathrm{SL}_2(\mathbb{F}_p)$, all $S$ | $(\log p)^{O(1)}$ | Helfgott 2008 |
| $\mathrm{SL}_3(\mathbb{Z}/p\mathbb{Z})$, all $S$ | $(\log p)^{O(1)}$ | Helfgott 2011 |
| Simple Lie type, rank $r = O(1)$, all $q$, all $S$ | $(\log|G|)^{C(r)}$ — **conjecture proved** | BGT 2011; Pyber–Szabó 2016 |
| $\mathrm{SL}_2(\mathbb{F}_q)$, $q=p^k$, $k$ bounded | $(\log q)^{O(1)}$ | Dinai 2011 |
| $\mathrm{SL}_n(\mathbb{F}_p)$, $S$ containing a transvection | $\mathrm{poly}(n, \log p)$ | Babai–Beals–Seress 2004 |
| Classical rank $r$ over $\mathbb{F}_q$, all $S$ | $q^{O(r(\log r + \log q)^3)}$ | Biswas–Yang 2017 |
| High-rank classical, random $S$ (w.h.p.) | $(\log|G|)^{O(1)}$ | Eberhard–Jezernik 2022 |
| $A_n$, $S$ two random elements (w.h.p.) | $O(n^2 (\log n)^{c})$ | Helfgott–Seress–Żuk 2015 |
| $A_n$, $S_n$, all $S$ | $\exp\big(O((\log n)^4)\big)$ | Helfgott–Seress 2014 |
| Sporadic groups | finite list — trivially true | — |

**Lower bounds.** For $S_n$ with $S=\{(1\,2),(1\,2\,\cdots\,n)\}$ the diameter is $\Theta(n^2)$, while $\log|S_n| \sim n\log n$; this forces $C \ge 2-o(1)$ in any true version of the conjecture. No family is known needing $C > 2$.

## 5. Principal Obstacles

- **$\varepsilon$ degenerates with rank.** All Lie-type product theorems give $\varepsilon = \varepsilon(r)$ decaying polynomially (at best) in the rank $r$, so $C = O(1/\varepsilon(r)) \to \infty$. Since $\log|G| \asymp r^2\log q$, the bound $(\log|G|)^{C(r)}$ is vacuous when $r$ grows with $|G|$. Making $\varepsilon$ rank-uniform is the central open technical demand.
- **Escape from subvarieties is dimension-sensitive.** The Larsen–Pink / escape machinery bounds $|A \cap V(\mathbb{F}_q)|$ for subvarieties $V$ with constants depending on the degree and dimension of the ambient group — both grow with $r$. There is no known degree-free substitute.
- **$A_n$ has no algebraic geometry.** For alternating groups there is no variety, no torus, no regular semisimple element, so the entire growth toolkit is unavailable. Helfgott–Seress instead run a recursive descent through point stabilizers and Schreier graphs, using CFSG-based structure of primitive groups. The recursion costs a factor at each of $O(\log n)$ levels, and the accumulated loss is exactly what yields $\exp((\log n)^4)$ rather than $\mathrm{poly}(n)$.
- **No expansion in general.** For bounded-rank Lie type one can sometimes upgrade diameter to a spectral gap (Bourgain–Gamburd), but for $A_n$ with arbitrary generators no uniform expansion is known or expected to be provable by current means; diameter bounds cannot be imported from mixing-time arguments.
- **Adversarial generating sets.** Random-generator results (Eberhard–Jezernik, Helfgott–Seress–Żuk) rely on genericity: random elements have large support, regular characteristic polynomials, and no invariant structure. Worst-case sets can be highly structured (e.g. supported on a small-index subgroup plus one element), and no method converts average-case control to worst-case.

## 6. The Gap

Two disjoint gaps remain.

1. **Rank.** Proved: $(\log|G|)^{C(r)}$ with $C(r)\to\infty$. Wanted: $C$ independent of $r$. The precise missing step is a **rank-uniform product theorem**: an absolute $\varepsilon>0$ with $|A^3|\ge |A|^{1+\varepsilon}$ for every generating $A$ in every finite simple group of Lie type, regardless of rank. Equivalently, a classification of approximate subgroups with constants independent of the dimension of the ambient algebraic group.
2. **Alternating groups.** Proved: $\exp(O((\log n)^4))$. Wanted: $n^{O(1)}$. The gap is exponential — from quasipolynomial to polynomial in $n$. Crossing it requires replacing the $O(\log n)$-deep stabilizer recursion by a mechanism producing *multiplicative* growth of $|S^{(k)}|$ inside $A_n$ directly, for which no candidate structure theorem exists.

## 7. Current Research (as of June 2026)

- **Rank-uniform growth.** Groups around Pyber and Maróti (Rényi Institute, Budapest), Szabó, and Helfgott (Göttingen / IMJ-PRG) continue pushing the rank dependence in classical groups; the target is replacing $q^{O(r(\log r+\log q)^3)}$ by a genuinely polylogarithmic bound. Progress has been incremental since 2019. *(frontier — verify)*
- **Random and generic generators.** The Eberhard–Jezernik method (character bounds plus concentration for random elements) is being extended to sparser randomness models and to exceptional groups. *(frontier — verify)*
- **Character-theoretic routes.** Bounds of Larsen–Shalev–Tiep type on mixing for products of conjugacy classes give strong diameter results for *normal* (conjugation-invariant) generating sets, uniformly in rank; extending this leverage beyond normal sets is an active line.
- **Permutation-group algorithms.** The Babai–Beals–Seress line of work is pursued for its algorithmic payoff: polylogarithmic diameter would give near-optimal constructive membership testing in matrix and permutation groups.
- **Expansion.** Bourgain–Gamburd-style super-approximation for thin groups (Salehi Golsefidy, Varjú) remains adjacent; it produces expansion for congruence quotients of fixed thin groups, not for arbitrary generating sets.

## 8. Future Work

- Prove a product theorem for $\mathrm{SL}_n(\mathbb{F}_p)$ with $\varepsilon$ independent of $n$, even under an extra hypothesis (e.g. $A$ contains a regular semisimple element) — this is the cleanest identified milestone.
- Obtain $\mathrm{poly}(n)$ diameter for $A_n$ under restrictions on $S$, e.g. $S$ containing an element of small support or of bounded order; Babai–Beals–Seress already do this when $S$ contains a transvection in the linear analogue.
- Replace CFSG-dependent steps in Helfgott–Seress by intrinsic combinatorial arguments, which would make the recursion cheaper and possibly polynomial.
- Search computationally for generating sets of $A_n$ or $\mathrm{PSL}_2(\mathbb{F}_p)$ with diameter exceeding $(\log|G|)^{2}$; the absence of such examples for $n \le 20$ is the main empirical support for $C = 2$.
- Settle the directed vs. undirected diameter question for non-symmetric $S$, where even the bounded-rank case is less clean.

## 9. Key References

- **[Foundational]** L. Babai, Á. Seress. *On the diameter of Cayley graphs of the symmetric group.* Journal of Combinatorial Theory, Series A, 49(1):175–179, 1988.
- **[Foundational]** L. Babai, Á. Seress. *On the diameter of permutation groups.* European Journal of Combinatorics, 13(4):231–243, 1992.
- **[Foundational]** L. Babai, W. M. Kantor, A. Lubotzky. *Small-diameter Cayley graphs for finite simple groups.* European Journal of Combinatorics, 10(6):507–522, 1989.
- **[SOTA]** H. A. Helfgott. *Growth and generation in $\mathrm{SL}_2(\mathbb{Z}/p\mathbb{Z})$.* Annals of Mathematics, 167(2):601–623, 2008.
- **[SOTA]** H. A. Helfgott. *Growth in $\mathrm{SL}_3(\mathbb{Z}/p\mathbb{Z})$.* Journal of the European Mathematical Society, 13(3):761–851, 2011.
- **[SOTA]** E. Breuillard, B. Green, T. Tao. *Approximate subgroups of linear groups.* Geometric and Functional Analysis, 21(4):774–819, 2011.
- **[SOTA]** L. Pyber, E. Szabó. *Growth in finite simple groups of Lie type.* Journal of the American Mathematical Society, 29(1):95–146, 2016.
- **[SOTA]** H. A. Helfgott, Á. Seress. *On the diameter of permutation groups.* Annals of Mathematics, 179(2):611–658, 2014.
- **[Recent]** S. Eberhard, U. Jezernik. *Babai's conjecture for high-rank classical groups with random generators.* Inventiones Mathematicae, 227(1):149–210, 2022.
- **[Recent]** A. Biswas, Y. Yang. *A diameter bound for finite simple groups of large rank.* Journal of the London Mathematical Society, 95(2):455–474, 2017.
- **[Recent]** Z. Halasi, A. Maróti, L. Pyber, Y. Qiao. *An improved diameter bound for finite simple groups of Lie type.* Bulletin of the London Mathematical Society, 51(4):645–657, 2019.
- **[Recent]** H. A. Helfgott, Á. Seress, A. Żuk. *Random generators of the symmetric group: diameter, mixing time and spectral gap.* Journal of Algebra, 421:349–368, 2015.
- **[Related]** J. Bourgain, A. Gamburd. *Uniform expansion bounds for Cayley graphs of $\mathrm{SL}_2(\mathbb{F}_p)$.* Annals of Mathematics, 167(2):625–642, 2008.
- **[Survey]** H. A. Helfgott. *Growth in groups: ideas and perspectives.* Bulletin of the American Mathematical Society, 52(3):357–413, 2015.
- **[Survey]** E. Breuillard. *A brief introduction to approximate groups.* In *Thin Groups and Superstrong Approximation*, MSRI Publications 61, Cambridge University Press, 2014.

## 10. Worked Example / Concrete Special Case

**Growth of a maximal torus in $\mathrm{SL}_2(\mathbb{F}_p)$ — the mechanism behind Helfgott's theorem.**

Let $p$ be an odd prime, $G=\mathrm{SL}_2(\mathbb{F}_p)$, $|G| = p(p^2-1) \approx p^3$, so $\log|G| \approx 3\log p$. Let
$$T=\left\{ d_t=\begin{pmatrix} t & 0\\ 0 & t^{-1}\end{pmatrix} : t\in\mathbb{F}_p^{\times}\right\},\qquad |T| = p-1 \approx |G|^{1/3}.$$
$T$ is a subgroup: it does not grow at all, $|T\cdot T\cdot T| = |T|$. A product theorem must therefore *escape* it. Take
$$g=\begin{pmatrix}1&1\\0&1\end{pmatrix},\qquad g^{-1}d_t g=\begin{pmatrix}1&-1\\0&1\end{pmatrix}\begin{pmatrix} t& t\\ 0& t^{-1}\end{pmatrix}=\begin{pmatrix} t & t-t^{-1}\\ 0 & t^{-1}\end{pmatrix}.$$
Now multiply by another torus element:
$$d_s\,(g^{-1}d_t g)=\begin{pmatrix} st & s(t-t^{-1})\\ 0 & (st)^{-1}\end{pmatrix}.$$
Ask which upper-triangular matrices $\begin{pmatrix}\alpha&\beta\\0&\alpha^{-1}\end{pmatrix}$ arise. Set $\alpha=st$, $\beta=s(t-t^{-1})$. Then $t=\alpha/s$ and
$$\beta=s\left(\frac{\alpha}{s}-\frac{s}{\alpha}\right)=\alpha-\frac{s^2}{\alpha}\quad\Longrightarrow\quad s^{2}=\alpha(\alpha-\beta).$$
This is solvable for $s$ exactly when $\alpha(\alpha-\beta)$ is a nonzero square in $\mathbb{F}_p$, which happens for $\tfrac12(1+o(1))$ of the $(\alpha,\beta)$ pairs. Hence
$$\big|T\cdot (g^{-1}Tg)\big| \;\ge\; \tfrac{1}{2}(1-o(1))\,p(p-1) \;\approx\; \tfrac{p^2}{2},$$
so a set of size $\approx p$ has grown to size $\approx p^2/2$ — i.e. $|A|\mapsto |A|^{2-o(1)}$ — after only a bounded number of multiplications, provided $g \in S^{(k)}$ for small $k$.

**Reading off the diameter.** This is the local step; the product theorem packages it uniformly: for any generating symmetric $A\subseteq \mathrm{SL}_2(\mathbb{F}_p)$, either $A^3=G$ or $|A^3|\ge|A|^{1+\varepsilon}$ with $\varepsilon>0$ absolute. Starting from $A=S\cup S^{-1}\cup\{1\}$, after $m$ tripling rounds $|S^{(3^m)}| \ge 2^{(1+\varepsilon)^m}$, so $S^{(3^m)}=G$ once $(1+\varepsilon)^m \ge \log_2|G| \approx 3\log_2 p$, i.e. $m = O(\log\log p)$, giving
$$\operatorname{diam}(\mathrm{Cay}(G,S)) \le 3^{m} = (\log p)^{O(1/\varepsilon)} = (\log|G|)^{O(1)} .$$

**Where it stops.** Repeat the computation in $\mathrm{SL}_n(\mathbb{F}_p)$: the diagonal torus has size $(p-1)^{n-1}\approx |G|^{1/n}$, and the varieties one must escape have degree growing with $n$. Every known quantitative escape lemma loses a factor depending on $n$, so the resulting $\varepsilon$ shrinks and $C = O(1/\varepsilon)$ blows up. That failure, in this exact computation, is the whole of the unbounded-rank gap in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*