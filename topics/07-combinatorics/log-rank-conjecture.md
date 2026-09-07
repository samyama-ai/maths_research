---
id: 07-combinatorics/log-rank-conjecture
title: "Log-Rank Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Log-Rank Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/log-rank-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $f:\mathcal{X}\times\mathcal{Y}\to\{0,1\}$ be a Boolean function with communication matrix $M_f = \big(f(x,y)\big)_{x\in\mathcal{X},\,y\in\mathcal{Y}}$, and let $\mathrm{rank}(M_f)$ denote its rank **over the reals**. Let $D(f)$ be the deterministic two-party communication complexity of $f$: the minimum, over correct protocols in which Alice holds $x$ and Bob holds $y$, of the worst-case number of bits exchanged.

**Conjecture (Lovász–Saks, 1988).** There is an absolute constant $c$ such that for every Boolean $f$ with $\mathrm{rank}(M_f)=r\ge 2$,
$$D(f) \;\le\; \big(\log_2 r\big)^{c} + O(1).$$

The reverse inequality $\log_2 \mathrm{rank}(M_f) \le D(f)$ is a theorem (Mehlhorn–Schmidt, 1982), so the conjecture asserts that rank is a *polynomially tight* lower bound — the only known general lower-bound technique that could be. A proof must supply protocols of cost $\mathrm{polylog}(r)$ for all Boolean matrices of rank $r$; a disproof must exhibit a family with $D(f) = (\log r)^{\omega(1)}$.

## 2. Mathematical Foundations

**Rectangles and partitions.** A *combinatorial rectangle* is a set $R = A\times B$ with $A\subseteq\mathcal{X}$, $B\subseteq\mathcal{Y}$; it is *monochromatic* if $f$ is constant on $R$. Every deterministic protocol of cost $c$ induces a partition of $\mathcal{X}\times\mathcal{Y}$ into at most $2^c$ monochromatic rectangles. Writing $\chi(f)$ for the minimum number of monochromatic rectangles in a partition,
$$\log_2 \chi(f) \;\le\; D(f) \;\le\; O\big(\log^2 \chi(f)\big),$$
the upper bound by Aho–Ullman–Yannakakis (1983). So the conjecture is equivalent to $\chi(f) \le 2^{\mathrm{polylog}\,\mathrm{rank}(M_f)}$.

**Rank lower bound.** If a protocol partitions into rectangles $R_1,\dots,R_t$ with $1$-rectangles $R_{i_1},\dots,R_{i_s}$, then $M_f=\sum_j \mathbf{1}_{R_{i_j}}$ and each $\mathbf{1}_{R}$ has rank $1$, giving $\mathrm{rank}(M_f)\le 2^{D(f)}$.

**Trivial upper bound.** $D(f)\le r+1$: fix $r$ linearly independent columns; every row of a rank-$r$ Boolean matrix is determined by its restriction to them, so Alice names her row type.

**Equivalent "big rectangle" form (Nisan–Wigderson, 1995).** The conjecture is equivalent to: there is $c'$ with every rank-$r$ Boolean matrix containing a monochromatic rectangle of density at least $2^{-(\log r)^{c'}}$. (Iterating a large-rectangle lemma inside a rank-decreasing induction builds the protocol.)

**Graph form.** For a graph $G$ with adjacency matrix $A$ of rank $r$, the conjecture implies $\chi(G)\le 2^{\mathrm{polylog}\,r}$ for the chromatic number, since the clique-cover/colouring number is sandwiched by rectangle partitions of $A$.

**XOR functions.** For $F(x,y)=f(x\oplus y)$ on $\mathbb{F}_2^n$, $\mathrm{rank}(M_F)=\|\hat f\|_0$, the Fourier sparsity of $f$ (the number of nonzero coefficients in $f=\sum_S \hat f(S)\chi_S$). Log-rank restricted to this class asks for protocols of cost $\mathrm{polylog}\,\|\hat f\|_0$.

## 3. History & State of the Art (SOTA)

- **1982.** Mehlhorn and Schmidt introduce the rank bound $D(f)\ge\log_2\mathrm{rank}(M_f)$.
- **1988.** Lovász and Saks (FOCS, *Lattices, Möbius functions and communication complexity*) pose the conjecture, motivated by lattice-theoretic and chromatic-number questions.
- **1994–95.** Nisan and Wigderson prove the equivalence with the large-monochromatic-rectangle statement, show that a rank-$r$ matrix has a rectangle of density $2^{-O(\sqrt{r}\log r)}$ that is nearly monochromatic, and record **Kushilevitz's example**: a function with $D(f)\ge (\log_2 r)^{\log_3 6}$, $\log_3 6 \approx 1.631$. This remains the largest known separation.
- **1996.** Kotlov and Lovász: a reduced graph of adjacency rank $r$ has at most $O(2^{r/2})$ vertices, giving $D \le r/2 + O(1)$ — an exponential improvement over $r+1$ only in the constant.
- **2014/2016.** Lovett proves $D(f) = O(\sqrt{r}\,\log r)$ (*Communication is bounded by root of rank*, STOC 2014, JACM 2016), the first sub-linear general bound, via discrepancy of low-rank matrices.
- **2019.** Chattopadhyay–Mande–Sherstov refute the *log-approximate-rank* conjecture (the randomized analogue), showing that rank-based intuition fails in the approximate regime.
- **2023–present.** Sudakov and Tomon (*Matrix discrepancy and the log-rank conjecture*, preprint) improve the general bound by removing the logarithmic factor, giving $D(f)=O(\sqrt{r})$ *(frontier — verify)*.

Current SOTA is therefore a gap between $\Omega\big((\log r)^{1.63}\big)$ and $O(\sqrt r) = O(2^{(\log r)/2})$ — polylogarithmic versus exponential in $\log r$.

## 4. Partial Results / Verified Cases

- **Bounded rank.** For any fixed $r$, $D(f)\le \min\{r+1,\ r/2+O(1)\}$; the conjecture is vacuous for $r=O(1)$ and verified exhaustively for small matrices. Rank-$1$, $2$ and $3$ Boolean matrices are classified, with $D\le 3$.
- **XOR functions of constant $\mathbb{F}_2$-degree.** Tsang, Wong, Xie and Zhang (FOCS 2013) prove the log-rank conjecture for $f\circ\oplus$ when $\deg_{\mathbb{F}_2}(f)=d$ is constant, with cost $\mathrm{polylog}(\|\hat f\|_0)$ for fixed $d$; they also prove it for functions of small spectral norm $\|\hat f\|_1$.
- **Symmetric XOR functions.** Zhang and Shi determine $D(f\circ\oplus)$ up to constants for symmetric $f$, confirming log-rank in that class.
- **Structure for XOR functions.** Hatami, Hosseini and Lovett (FOCS 2016 / SICOMP 2018) show that deterministic protocols and parity decision trees for XOR functions are polynomially equivalent, reducing the class to a purely Fourier-analytic question.
- **Additive-combinatorics route.** Ben-Sasson, Lovett and Ron-Zewi (FOCS 2012) show that the polynomial Freiman–Ruzsa (PFR) conjecture over $\mathbb{F}_2$ implies improved rank-to-communication bounds for low-degree XOR functions. PFR over $\mathbb{F}_2^n$ was proved by Gowers, Green, Manners and Tao (2023, *Annals* 2025), making those consequences unconditional *(frontier — verify the exact resulting exponents)*.
- **AND functions.** Knop, Lovett, McGuire and Yuan (STOC 2021) establish polylogarithmic bounds and a lifting theorem for $F(x,y)=f(x\wedge y)$, settling log-rank for this composed class.
- **Nonnegative rank.** If $M_f$ is a sum of $k$ nonnegative rank-one matrices, then $\chi(f)\le \mathrm{poly}(k)$ and $D(f)=O(\log^2 k)$ — log-rank holds when real and nonnegative rank are polynomially related.

## 5. Principal Obstacles

- **Rank is not robust.** Changing one entry of $M_f$ changes the rank by at most $1$, yet can change $D(f)$ structurally. Techniques that certify rank (spectral, algebraic) do not see the Boolean constraint, and Boolean-analytic techniques (Fourier expansion, hypercontractivity) do not see the rank.
- **Discrepancy plateaus at $\sqrt r$.** Lovett's argument finds a large *nearly* monochromatic rectangle, then recurses on a submatrix of rank $\le r/2$; each round costs $\Theta(\sqrt r)$ bits. The $\sqrt r$ arises from a Cauchy–Schwarz/Grothendieck-type bound on the discrepancy of a rank-$r$ sign matrix, and is tight for that bound. Any polylog result must find rectangles of density $2^{-\mathrm{polylog}\,r}$, exponentially larger than what discrepancy or spectral arguments deliver.
- **No candidate counterexample.** Random Boolean matrices have full rank and complexity $\Theta(\log r)$; algebraic constructions (inner product, disjointness) have rank exponential in their complexity. Tensor and recursive composition, the only known amplifiers, raise the exponent only from $1$ to $\log_3 6$ and appear to saturate.
- **The approximate analogue is false.** Chattopadhyay–Mande–Sherstov's refutation of log-approximate-rank shows the "low rank $\Rightarrow$ structured" heuristic fails in a closely neighbouring setting, so any proof must use exact rank in an essential, non-robust way.
- **Lifting barriers.** Query-to-communication lifting converts decision-tree lower bounds into communication ones but does not preserve rank; Göös–Pitassi–Watson's separation of $D(f)$ from $\log\chi(f)$ (SICOMP 2018) shows the partition-number route loses a quadratic factor that already sits inside the conjecture's slack.

## 6. The Gap

Proven: $D(f)\le O(\sqrt{r})$, i.e. $D \le 2^{(\log_2 r)/2 + O(1)}$. Conjectured: $D\le(\log_2 r)^{O(1)}$. The gap is *exponential in $\log r$*.

Concretely, the single missing step is the **large monochromatic rectangle lemma**: prove that every rank-$r$ Boolean matrix contains a monochromatic rectangle of density $\ge 2^{-(\log r)^{c}}$. Currently the best guaranteed density is $2^{-\Theta(\sqrt r)}$. Nisan–Wigderson's equivalence means this one lemma is not merely sufficient but equivalent to the conjecture. On the lower-bound side, the gap is between exponent $1.631$ and any super-constant exponent: no construction is known giving $D \ge (\log r)^{\omega(1)}$, and no argument rules one out.

## 7. Current Research (as of June 2026)

- **Matrix discrepancy.** Sudakov and Tomon's transfer of Spencer-type discrepancy machinery to low-rank Boolean matrices is the most active technical line, and has already removed Lovett's log factor *(frontier — verify)*. Whether discrepancy methods can beat $r^{1/2-\varepsilon}$ is the immediate open question (ETH Zürich, UCSD).
- **Post-PFR additive combinatorics.** With Marton's conjecture proved, the Ben-Sasson–Lovett–Ron-Zewi programme is being re-run to push degree-$d$ XOR functions to unconditional polylog bounds with explicit dependence on $d$ *(frontier — verify)*.
- **Structured classes.** Extensions of the AND-function and lifting results (Knop–Lovett–McGuire–Yuan) to general gadget compositions; Fourier-sparsity questions for parity decision trees (Zhang, Tsang, and collaborators).
- **Refutation attempts.** Search for base matrices improving on Kushilevitz's exponent by exhaustive/SAT-based search over small rank matrices, and via pseudorandom algebraic constructions.
- **Quantum and approximate variants.** After the refutation of log-approximate-rank, attention has moved to which weakened rank measures (e.g. $\gamma_2$, approximate nonnegative rank) *do* characterize randomized complexity.

## 8. Future Work

- Prove the rectangle lemma in the *restricted* regime where $M_f$ has few distinct rows relative to $r$, then bootstrap by rank reduction.
- Develop a rank-sensitive regularity lemma: decompose a low-rank Boolean matrix into structured blocks plus a low-rank pseudorandom part, with block count $2^{\mathrm{polylog}\,r}$.
- Settle the XOR-function case in full; Hatami–Hosseini–Lovett reduce it to showing every $s$-sparse Boolean function has a parity decision tree of depth $\mathrm{polylog}\,s$.
- Determine whether $D(f)=O(r^{1/2-\varepsilon})$ is achievable at all; even a single improvement of the exponent would show discrepancy is not the true barrier.
- Improve the lower bound past $\log_3 6$, or prove that recursive composition cannot exceed a fixed exponent — which would be evidence for the conjecture.

## 9. Key References

- **[Foundational]** L. Lovász, M. Saks. *Lattices, Möbius functions and communication complexity.* Proc. 29th IEEE FOCS, 81–90, 1988.
- **[Foundational]** K. Mehlhorn, E. M. Schmidt. *Las Vegas is better than determinism in VLSI and distributed computing.* Proc. 14th ACM STOC, 330–337, 1982.
- **[Foundational]** N. Nisan, A. Wigderson. *On rank vs. communication complexity.* Combinatorica 15(4):557–565, 1995.
- **[SOTA]** S. Lovett. *Communication is bounded by root of rank.* Journal of the ACM 63(1), Article 1, 2016 (STOC 2014).
- **[SOTA / Recent]** B. Sudakov, I. Tomon. *Matrix discrepancy and the log-rank conjecture.* Preprint, 2023.
- **[Recent]** A. Chattopadhyay, N. S. Mande, A. A. Sherstov. *The log-approximate-rank conjecture is false.* Journal of the ACM 67(4), 2020 (STOC 2019).
- **[Recent]** A. Knop, S. Lovett, S. McGuire, W. Yuan. *Log-rank and lifting for AND-functions.* Proc. 53rd ACM STOC, 2021.
- **[Recent]** H.-Y. Tsang, C. H. Wong, N. Xie, S. Zhang. *Fourier sparsity, spectral norm, and the log-rank conjecture.* Proc. 54th IEEE FOCS, 658–667, 2013.
- **[Recent]** H. Hatami, K. Hosseini, S. Lovett. *Structure of protocols for XOR functions.* SIAM Journal on Computing 47(1):208–217, 2018 (FOCS 2016).
- **[Recent]** E. Ben-Sasson, S. Lovett, N. Ron-Zewi. *An additive combinatorics approach relating rank to communication complexity.* Proc. 53rd IEEE FOCS, 177–186, 2012.
- **[Recent]** W. T. Gowers, B. Green, F. Manners, T. Tao. *On a conjecture of Marton.* Annals of Mathematics 201, 2025.
- **[Structural]** A. Kotlov, L. Lovász. *The rank and size of graphs.* Journal of Graph Theory 23(2):185–189, 1996.
- **[Survey]** S. Lovett. *Recent advances on the log-rank conjecture in communication complexity.* Bulletin of the EATCS 112, 2014.
- **[Survey / Book]** E. Kushilevitz, N. Nisan. *Communication Complexity.* Cambridge University Press, 1997.
- **[Survey]** M. Göös, T. Pitassi, T. Watson. *Deterministic communication vs. partition number.* SIAM Journal on Computing 47(6):2435–2450, 2018.

## 10. Worked Example / Concrete Special Case

**(a) A tight instance: equality.** Let $\mathcal{X}=\mathcal{Y}=\{0,1\}^n$ and $\mathrm{EQ}(x,y)=1$ iff $x=y$. Then $M_{\mathrm{EQ}} = I_{2^n}$, so $r=\mathrm{rank}=2^n$ and $\log_2 r = n$. Protocol: Alice sends $x$ ($n$ bits), Bob replies with one bit. So $D(\mathrm{EQ}) \le n+1 = \log_2 r + 1$. Here the conjecture holds with $c=1$ and the rank bound is essentially exact.

**(b) A small gap.** Take the $4\times 4$ upper-triangular matrix $M$ with $M_{xy}=1$ iff $x\le y$ (rows and columns indexed $1..4$):
$$M=\begin{pmatrix}1&1&1&1\\0&1&1&1\\0&0&1&1\\0&0&0&1\end{pmatrix},\qquad \mathrm{rank}(M)=4,\quad \log_2 r = 2.$$
Any monochromatic rectangle has at most $\lceil 4\cdot 4/2\rceil$-ish area, and the finest monochromatic rectangle partition needs $\chi(M)=5$ rectangles (e.g. $\{1\}\times\{1,2,3,4\}$, $\{2\}\times\{1\}$, $\{2,3,4\}\times\{2,3,4\}$-refinements), so $D(M)=3 > \log_2 r = 2$. Alice sends $\lceil\log_2 4\rceil = 2$ bits, Bob one. The gap $D - \log_2 r = 1$ is additive and harmless.

**(c) Why amplification matters.** Kushilevitz's separation takes a fixed base function $g$ on $\{0,1\}^3\times\{0,1\}^3$ and composes it recursively $k$ times. Under recursive composition, the rank of the level-$k$ matrix satisfies $\log \mathrm{rank}(M_k)=\Theta(3^k)$ — the rank exponent triples per level — while the rectangle-partition lower bound multiplies by $6$ per level, $D(f_k)=\Omega(6^k)$. Eliminating $k$:
$$D(f_k) \;=\; \Omega\!\left(\big(\log \mathrm{rank}(M_k)\big)^{\log_3 6}\right), \qquad \log_3 6 \approx 1.6309.$$
This is the entire known lower-bound landscape. Any Boolean matrix family with a per-level ratio $\log(\text{complexity factor})/\log(\text{rank factor})$ unbounded as the base grows would refute the conjecture; no such base is known, and exhaustive search over small bases has not improved on $6$ versus $3$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*