---
id: 10-theoretical-cs/all-pairs-shortest-paths-conjecture
title: "All-Pairs Shortest Paths Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# All-Pairs Shortest Paths Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/all-pairs-shortest-paths-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The **APSP Conjecture** (a central hypothesis of fine-grained complexity) asserts:

> There is no $\varepsilon > 0$ and no algorithm that solves All-Pairs Shortest Paths on $n$-vertex directed graphs with integer edge weights in $\{-n^{c}, \dots, n^{c}\}$ (for some constant $c$, no negative cycles) in time $O(n^{3-\varepsilon})$ on a word-RAM with $O(\log n)$-bit words.

Algorithms may be randomized with two-sided error and constant success probability; the conjecture is stated to rule these out as well. "Truly subcubic" means $O(n^{3-\varepsilon})$ for a fixed $\varepsilon>0$; shaving polylogarithmic or even $2^{\sqrt{\log n}}$ factors does **not** refute it.

A **disproof** is a truly subcubic algorithm for APSP (or, equivalently by Section 4, for any problem in its subcubic equivalence class). A **proof** would be an unconditional cubic lower bound for a problem in $\mathsf{P}$ on a general model — far beyond current lower-bound technology; the realistic positive target is a proof *conditional* on a weaker or more believable hypothesis.

## 2. Mathematical Foundations

Let $G=(V,E,w)$ with $|V|=n$, $w:E\to\mathbb{Z}$, no negative cycles. Define $d(u,v)$ as the minimum weight of a $u\to v$ walk. APSP asks for the matrix $D=(d(u,v))_{u,v\in V}$.

**The tropical (min-plus) semiring.** Work over $\overline{\mathbb{Z}} = \mathbb{Z}\cup\{+\infty\}$ with
$$a\oplus b=\min(a,b),\qquad a\otimes b=a+b,$$
identities $\bar 0=+\infty$, $\bar 1 = 0$. This is a semiring: $\oplus$ is idempotent and has **no additive inverses**. The min-plus product of $A,B\in\overline{\mathbb{Z}}^{\,n\times n}$ is
$$(A\star B)[i,j]=\min_{1\le k\le n}\bigl(A[i,k]+B[k,j]\bigr).$$

If $W$ is the weighted adjacency matrix ($W[i,i]=0$, $W[i,j]=w(i,j)$ or $+\infty$), then
$$D = W^{\star (n-1)} = \underbrace{W\star W\star\cdots\star W}_{n-1},$$
and by idempotence $D=W^{\star m}$ for any $m\ge n-1$, so repeated squaring gives $O(n^3\log n)$. Floyd–Warshall's dynamic program
$$d_k(i,j)=\min\bigl(d_{k-1}(i,j),\,d_{k-1}(i,k)+d_{k-1}(k,j)\bigr)$$
gives $\Theta(n^3)$.

**Two auxiliary problems.**
- **Min-Plus Product (MPP):** compute $A\star B$ for $n\times n$ integer matrices.
- **Negative Triangle (NT):** given a complete tripartite graph on $I\cup J\cup K$ with weights $a_{ik},b_{kj},c_{ij}$, decide whether $\exists\,i,j,k$ with $a_{ik}+b_{kj}+c_{ij}<0$.

**Theorem (Vassilevska Williams–Williams, FOCS 2010; JACM 2018).** APSP, MPP, NT, Minimum Weight Cycle, Second Shortest Path, Replacement Paths, Metricity Verification, and Min-Plus Product Verification are **subcubic equivalent**: a truly subcubic algorithm for any one yields truly subcubic algorithms for all. Formally, if NT is solvable in $O(n^{3-\delta})$ then MPP and APSP are solvable in $O(n^{3-\delta/3})$ time.

Contrast with the ring $(\mathbb{Z},+,\times)$, where matrix multiplication takes $O(n^{\omega})$ time with $\omega < 2.3714$ (Alman–Duan–Vassilevska Williams–Xu–Xu–Zhou, SODA 2025). The conjecture says the loss of subtraction is fatal.

## 3. History & State of the Art (SOTA)

- **1959–1962.** Floyd–Warshall/Roy: $\Theta(n^3)$. Dijkstra with Fibonacci heaps plus Johnson's potential reweighting gives $O(mn+n^2\log n)$ — better only for sparse graphs.
- **1976.** Fredman shows $O(n^3(\log\log n/\log n)^{1/3})$ and, crucially, that MPP has **non-uniform decision-tree complexity $O(n^{2.5})$** — the information-theoretic content of APSP is subcubic.
- **1990s.** Takaoka, Dobosiewicz, Han: successive $\log$-factor shavings.
- **2007–2012.** Chan: $O(n^3(\log\log n)^3/\log^2 n)$ (SICOMP 2010). Han–Takaoka: $O(n^3\log\log n/\log^2 n)$.
- **2014.** R. Williams, *Faster all-pairs shortest paths via circuit complexity* (STOC 2014; SICOMP 2018): $\frac{n^3}{2^{\Omega(\sqrt{\log n})}}$ via the polynomial method — probabilistic polynomials for $\mathsf{ACC}^0$-style circuits combined with fast rectangular multiplication. This remains the fastest known bound for real/large integer weights and is *super-polylogarithmically* but not polynomially subcubic.
- **2010–2018.** The equivalence class is mapped out (Section 2), then extended: radius and median are APSP-equivalent (Abboud–Grandoni–Vassilevska Williams, SODA 2015); tree edit distance is APSP-hard (Bringmann–Gawrychowski–Mozes–Weimann, SODA 2018).
- **2016.** Carmosino et al. (ITCS 2016) show under **NSETH** that SETH cannot be fine-grained-reduced to APSP — the two hypotheses are formally incomparable, which is why APSP is maintained as a *separate* axiom of fine-grained complexity.
- **2021–2023.** Chan–Vassilevska Williams–Xu: small-weight APSP variants (ICALP 2021) and *Fredman's trick meets dominance product* (STOC 2023), unifying $n^3/2^{\Omega(\sqrt{\log n})}$-type bounds and linking APSP- and 3SUM-hardness through Exact Triangle.

**Current SOTA:** $n^3/2^{\Theta(\sqrt{\log n})}$ general; $\tilde O(n^{\omega})$ for unweighted undirected; $\tilde O(n^{2.53})$ for bounded weights. No truly subcubic algorithm, and no unconditional $\omega(n^2)$ lower bound.

## 4. Partial Results / Verified Cases

Truly subcubic algorithms **do exist** in restricted regimes, so the conjecture's scope is exactly "large weights, general graphs":

| Class | Bound | Source |
|---|---|---|
| Unweighted, undirected | $\tilde O(n^{\omega})\le \tilde O(n^{2.372})$ | Seidel (JCSS 1995) |
| Unweighted, directed | $\tilde O(n^{(3+\omega)/2})\le \tilde O(n^{2.69})$ | Alon–Galil–Margalit (JCSS 1997) |
| Directed, weights in $\{-M,\dots,M\}$ | $\tilde O(M^{1/(4-\omega)}n^{2+1/(4-\omega)})\approx \tilde O(n^{2.53})$ for $M=O(1)$ | Zwick (JACM 2002) |
| Directed, nonneg. weights, $(1+\epsilon)$-approx. | $\tilde O(n^{\omega}/\epsilon\cdot\log(W))$ | Zwick (JACM 2002) |
| Undirected, additive $+2$ approx. | $\tilde O(n^{7/3})$ | Dor–Halperin–Zwick (SICOMP 2000) |
| Planar graphs | $O(n^2)$ (output-optimal) | Frederickson (SICOMP 1987) |
| Sparse, real weights, $m=o(n^2/\log n)$ | $O(mn+n^2\log\log n)$ | Pettie (TCS 2004) |
| Non-uniform decision trees | $O(n^{2.5})$ comparisons | Fredman (SICOMP 1976) |
| $(\min,+)$ straight-line programs | $\Omega(n^3)$ **lower bound** | Kerr (PhD thesis, Cornell, 1970) |

So: the conjecture is *false* for every graph class where weights are polynomially bounded and rectangular matrix multiplication can be invoked, *true* (unconditionally) in the restricted semiring-circuit model, and open exactly for word-RAM algorithms on general large-weight graphs.

## 5. Principal Obstacles

- **No additive inverses.** Strassen-type identities require cancellation ($AC+BD$ recovered from sums and differences of products). The tropical semiring is idempotent — $a\oplus a=a$ — hence has no group structure under $\oplus$, and Kerr's $\Omega(n^3)$ bound shows *any* algorithm using only $\min$ and $+$ on the entries is stuck at cubic. A refutation must therefore operate outside the semiring, e.g. via bit tricks, table lookup, or embedding into a ring.
- **Embedding blow-up.** The standard embedding $\min(a,b)\mapsto$ ring operations costs $x\mapsto z^{-x}$ with numbers of magnitude $z^{M}$; the arithmetic-to-bit-complexity conversion multiplies running time by $\Omega(M)$, cancelling the gain unless $M$ is polylogarithmic. This is precisely why the bounded-weight cases in Section 4 fall.
- **Word-RAM shaving hits a wall.** All of Fredman's trick, four-Russians tabulation, and the polynomial method save factors of the form $2^{O(\sqrt{\log n})}$ or $\mathrm{polylog}(n)$. Structurally, these methods exploit $\Theta(\log n)$-bit word parallelism, which can buy at most $n^{o(1)}$ — never $n^{\varepsilon}$.
- **Lower bounds are out of reach.** Proving an unconditional $\Omega(n^{2+\varepsilon})$ bound for any explicit problem in $\mathsf{P}$ on a general RAM would be a breakthrough of circuit-lower-bound magnitude; current techniques (communication complexity, algebraic degree, Ramsey-type arguments) yield only $\Omega(n^2)$ from output size.
- **Fredman's decision-tree gap is real.** $O(n^{2.5})$ comparisons suffice non-uniformly, so no information-theoretic argument can prove the conjecture. Any proof must charge for *computing* which comparisons to make — nobody knows how to formalize that cost.
- **Hypothesis isolation.** By NSETH-based non-reducibility (Carmosino et al. 2016), one cannot import SETH-hardness; and 3SUM-hardness is likewise not known to imply APSP-hardness. APSP must be attacked on its own terms.

## 6. The Gap

Proven: $n^3/2^{\Theta(\sqrt{\log n})} = n^{3-o(1)}$. Conjectured: $n^{3-\Omega(1)}$ is impossible.

The gap is exactly the **$n^{o(1)}$ vs. $n^{\varepsilon}$ boundary**. Every known speedup is $2^{O(\sqrt{\log n})}$, i.e. sub-polynomial; the conjecture forbids any polynomial speedup. Symmetrically, on the hardness side the gap is between $\Omega(n^2)$ (trivial, output size) and $\Omega(n^{3-o(1)})$.

Concretely, crossing it in the algorithmic direction requires one of:
1. A negative-triangle detection algorithm in $O(n^{3-\delta})$ — by the JACM 2018 equivalence this immediately gives APSP in $O(n^{3-\delta/3})$.
2. A *uniform* implementation of Fredman-style sorting-network structure at $O(n^{3-\varepsilon})$ total cost, closing the decision-tree/uniform gap.
3. A weight-oblivious ring embedding of $(\min,+)$ whose bit-complexity overhead is $n^{o(1)}$.

## 7. Current Research (as of June 2026)

- **MIT (Vassilevska Williams, Xu) and UIUC/Illinois (Chan).** The dominant program: refined "Fredman's trick + dominance product" machinery for small-weight and structured APSP, and mapping the boundary between APSP-hardness and 3SUM-hardness via **Exact Triangle**, which is hard under both hypotheses.
- **Stanford / Weizmann (Abboud and coauthors).** Conditional hardness for approximation and for dynamic problems; the "hardness of approximation in P" line, aiming to show even $(2-\epsilon)$-approximations of diameter/eccentricities need near-cubic (or near-quadratic in $m$) time. Diameter's exact relationship to APSP remains open. *(frontier — verify)*
- **Karlsruhe/Copenhagen (Bringmann, Künnemann, Węgrzycki).** MinConv (min-plus convolution) as a lower-dimensional cousin; the MinConv hypothesis implies APSP-style hardness for knapsack-like problems. Whether MinConv is truly subquadratic is open and would be strong evidence about APSP.
- **Algebraic side.** Repeated $\omega$ improvements (SODA 2025, $\omega<2.3714$) mechanically improve *bounded-weight* APSP exponents but provably cannot touch the general case; several groups are probing whether laser-method techniques can be adapted to idempotent semirings. *(frontier — verify)*
- **Quantum.** No truly subcubic quantum APSP is known for dense graphs beyond $\tilde O(n^{2.5})$-type bounds for special cases; a quantum refutation would not disprove the classical conjecture but would reshape its use.

## 8. Future Work

- Settle **Negative Triangle** — the smallest, cleanest member of the class, a pure decision problem with a one-bit answer.
- Close the **Fredman decision-tree gap**: either improve the non-uniform bound toward $\tilde O(n^2)$, or prove a uniform simulation obstruction.
- Determine whether **Diameter** and **Betweenness Centrality** are APSP-equivalent or strictly easier; radius and median already are (SODA 2015).
- Prove or refute a **common generalization** of APSP and 3SUM hardness (Exact Triangle), which would collapse two of the three fine-grained axioms into one.
- Develop **fine-grained hardness of approximation**: for which $\alpha$ does $\alpha$-approximate APSP remain cubic?
- Explore whether the polynomial method can yield $n^{3}/2^{\Omega(\log^{c} n)}$ for $c>1/2$ — a barrier to that would sharply localize the difficulty.

## 9. Key References

- **[Foundational]** M. L. Fredman. *New bounds on the complexity of the shortest path problem.* SIAM Journal on Computing, 5(1):83–89, 1976.
- **[Foundational]** L. R. Kerr. *The effect of algebraic structure on the computational complexity of matrix multiplication.* Ph.D. thesis, Cornell University, 1970.
- **[Foundational]** R. Seidel. *On the all-pairs-shortest-path problem in unweighted undirected graphs.* Journal of Computer and System Sciences, 51(3):400–403, 1995.
- **[Foundational]** N. Alon, Z. Galil, O. Margalit. *On the exponent of the all pairs shortest path problem.* Journal of Computer and System Sciences, 54(2):255–262, 1997.
- **[Foundational]** U. Zwick. *All pairs shortest paths using bridging sets and rectangular matrix multiplication.* Journal of the ACM, 49(3):289–317, 2002.
- **[Key equivalence]** V. Vassilevska Williams, R. Williams. *Subcubic equivalences between path, matrix, and triangle problems.* Journal of the ACM, 65(5):27, 2018 (FOCS 2010).
- **[SOTA]** R. Williams. *Faster all-pairs shortest paths via circuit complexity.* SIAM Journal on Computing, 47(5):1965–1985, 2018 (STOC 2014).
- **[SOTA]** T. M. Chan. *More algorithms for all-pairs shortest paths in weighted graphs.* SIAM Journal on Computing, 39(5):2075–2089, 2010.
- **[SOTA]** Y. Han, T. Takaoka. *An $O(n^3\log\log n/\log^2 n)$ time algorithm for all pairs shortest paths.* Journal of Discrete Algorithms, 2016 (SWAT 2012).
- **[Recent]** T. M. Chan, V. Vassilevska Williams, Y. Xu. *Algorithms, reductions and equivalences for small weight variants of all-pairs shortest paths.* ICALP 2021.
- **[Recent]** T. M. Chan, V. Vassilevska Williams, Y. Xu. *Fredman's trick meets dominance product: fine-grained complexity of unweighted APSP, 3SUM counting, and more.* STOC 2023.
- **[Recent]** A. Abboud, F. Grandoni, V. Vassilevska Williams. *Subcubic equivalences between graph centrality problems, APSP and diameter.* SODA 2015.
- **[Recent]** K. Bringmann, P. Gawrychowski, S. Mozes, O. Weimann. *Tree edit distance cannot be computed in strongly subcubic time (unless APSP can).* ACM Transactions on Algorithms, 16(4), 2020 (SODA 2018).
- **[Recent]** M. Carmosino, J. Gao, R. Impagliazzo, I. Mihajlin, R. Paturi, S. Schneider. *Nondeterministic extensions of the Strong Exponential Time Hypothesis and consequences for non-reducibility.* ITCS 2016.
- **[Recent]** J. Alman, R. Duan, V. Vassilevska Williams, Y. Xu, Z. Xu, R. Zhou. *More asymmetry yields faster matrix multiplication.* SODA 2025.
- **[Survey]** V. Vassilevska Williams. *On some fine-grained questions in algorithms and complexity.* Proceedings of the International Congress of Mathematicians (ICM 2018), Vol. 3, pp. 3447–3487.
- **[Survey]** S. Pettie. *A new approach to all-pairs shortest paths on real-weighted graphs.* Theoretical Computer Science, 312(1):47–74, 2004.

## 10. Worked Example / Concrete Special Case

**(a) A $3\times 3$ min-plus product.** Let
$$A=\begin{pmatrix}0&4&7\\ \infty&0&2\\ 5&\infty&0\end{pmatrix},\qquad B=\begin{pmatrix}0&1&\infty\\ 3&0&6\\ \infty&2&0\end{pmatrix}.$$
Then $(A\star B)[1,3]=\min(0+\infty,\;4+6,\;7+0)=7$ and $(A\star B)[1,2]=\min(0+1,\,4+0,\,7+2)=1$. Full result:
$$A\star B=\begin{pmatrix}0&1&10\\ 5&0&2\\ 5&2&0\end{pmatrix}.$$
Each entry needed $n=3$ additions and $2$ comparisons; the whole product costs $\Theta(n^3)$ semiring operations, and Kerr's theorem says no min-plus straight-line program does better.

**(b) Why negative triangle is the crux.** Take $I=J=K=\{1,2\}$ with
$$a=\begin{pmatrix}3&-1\\ 0&2\end{pmatrix},\quad b=\begin{pmatrix}1&4\\ 2&-2\end{pmatrix},\quad c=\begin{pmatrix}-5&1\\ 0&-1\end{pmatrix}.$$
Check $(i,j,k)=(1,1,2)$: $a_{12}+b_{21}+c_{11}=-1+2-5=-4<0$. A negative triangle exists.

**(c) The reduction, in miniature.** Suppose NT ran in $O(n^{3-\delta})$. To compute $C=A\star B$: partition $[n]$ into $n/t$ blocks of size $t$. For each pair of blocks, binary-search the value of $C[i,j]$ using NT as an oracle — set $c_{ij}=-v$ and ask whether $\min_k(a_{ik}+b_{kj}) < v$. Each of the $O(\log(nM))$ search rounds costs $O((n/t)^2\cdot t^{3-\delta})$; balancing $t$ yields MPP in $\tilde O(n^{3-\delta/3})$, hence APSP in $\tilde O(n^{3-\delta/3})$ by repeated squaring with $O(\log n)$ products. So the entire conjecture rests on one Boolean question about $2n^2$ numbers: *is there a triple summing below zero?* — for which no algorithm beating $n^3/2^{\Theta(\sqrt{\log n})}$ is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*