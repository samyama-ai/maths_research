---
id: 10-theoretical-cs/boolean-matrix-multiplication
title: "Boolean Matrix Multiplication"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Boolean Matrix Multiplication

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/boolean-matrix-multiplication` · **Status:** open

## 1. Problem Statement / Conjecture

Given $A, B \in \{0,1\}^{n \times n}$, compute the Boolean product $C = A \odot B$ with
$$C_{ij} \;=\; \bigvee_{k=1}^{n} \left( A_{ik} \wedge B_{kj} \right).$$

Two distinct open questions sit on top of this operation.

**(Q1) Exponent question.** Let $\omega$ be the exponent of matrix multiplication over a ring. Boolean matrix multiplication (BMM) is computable in $n^{\omega+o(1)}$ time by embedding into $\mathbb{Z}$ and thresholding. Is $\omega = 2$? Equivalently: is BMM solvable in $n^{2+o(1)}$ time? A complete resolution is a family of algorithms with running time $n^{2+o(1)}$, or a proof that $\omega > 2$.

**(Q2) Combinatorial BMM Conjecture.** Informally: *no combinatorial algorithm computes $A \odot B$ in time $O(n^{3-\varepsilon})$ for a constant $\varepsilon > 0$.* "Combinatorial" has no accepted formal definition; the working meaning is an algorithm that manipulates the matrices as set systems / graphs without algebraic cancellation, and in practice one demands a genuine $n^{3-\varepsilon}$ bound rather than polylogarithmic savings. This conjecture is the hardness hypothesis underpinning a large family of conditional lower bounds in fine-grained complexity. Refuting it means exhibiting such an algorithm; proving it requires a formal model plus an unconditional $n^{3-o(1)}$ lower bound in that model.

Both remain open. The catalogued status **open** refers to both.

## 2. Mathematical Foundations

Work in the Boolean semiring $\mathbb{B} = (\{0,1\}, \vee, \wedge, 0, 1)$. It is commutative, idempotent ($x \vee x = x$), and **has no additive inverses** — this is the structural fact that blocks Strassen-type cancellation.

**Ring embedding.** Let $\phi: \{0,1\} \to \mathbb{Z}$ be inclusion. Then
$$(A \odot B)_{ij} = \mathbf{1}\!\left[ \sum_{k} \phi(A_{ik})\phi(B_{kj}) > 0 \right],$$
so BMM reduces to integer matrix multiplication with entries in $[0,n]$, i.e. $O(n^\omega \log n)$ bit operations, and $n^{\omega+o(1)}$ arithmetic operations.

**Tensor formulation.** The matrix multiplication tensor is
$$\langle n,n,n\rangle \;=\; \sum_{i,j,k=1}^{n} x_{ij} \otimes y_{jk} \otimes z_{ki},$$
and $\omega = \inf\{ \tau : R(\langle n,n,n\rangle) = O(n^\tau) \}$ where $R(\cdot)$ is tensor rank. Bini's border rank $\underline{R}$ and Schönhage's $\tau$-theorem give $\omega = \inf\{\tau: \underline{R}(\langle n,n,n\rangle) = O(n^\tau)\}$. Strassen's laser method and the Coppersmith–Winograd family bound $\omega$ from powers of a fixed small tensor.

**Semiring lower bound.** Over $\mathbb{B}$, or in any monotone Boolean circuit model, the product genuinely requires $\Theta(n^3)$ gates: Paterson and, independently, Mehlhorn–Galil showed monotone Boolean circuits for $A \odot B$ need $n^3 - o(n^3)$ (indeed exactly $n^3$ AND gates and $n^3 - n^2$ OR gates in the tight versions). Hence any subcubic algorithm must leave the semiring — either by cancellation (ring embedding) or by word-level parallelism / preprocessing.

**Equivalent problems.** Let $T$ denote triangle detection in an $n$-vertex graph and $\mathrm{TC}$ transitive closure. Then, up to $O(n^{2})$ additive overhead and constant-factor blowup, BMM, $\mathrm{TC}$, triangle *detection/finding*, and verifying a Boolean product are subcubic-equivalent (Vassilevska Williams–Williams). Also relevant is the **OMv conjecture**: given $M \in \{0,1\}^{n\times n}$ to preprocess, then $n$ online vectors $v_1,\dots,v_n$, computing all $M \odot v_t$ before seeing $v_{t+1}$ requires $n^{3-o(1)}$ time.

**Witness version.** A *witness matrix* $W$ has $W_{ij} = k$ for some $k$ with $A_{ik}=B_{kj}=1$ (and $0$ if none). Computing all witnesses is solvable in $\tilde O(n^\omega)$ by random sampling (Alon–Naor; Seidel), a nontrivial step beyond the plain product.

## 3. History & State of the Art (SOTA)

- **1959–1962.** Warshall's and Floyd's $O(n^3)$ transitive-closure algorithms fix the naive baseline.
- **1969.** Strassen: $\omega \le \log_2 7 \approx 2.8074$. Fischer–Meyer (1971) and Furman show $\mathrm{TC}$ and BMM are equivalent up to constants, so $\mathrm{TC}$ inherits $O(n^\omega)$.
- **1970.** Arlazarov, Dinic, Kronrod, Faradzhev — the "Four Russians" method: preprocess $\log n$-wide column blocks into lookup tables, giving $O(n^3/\log n)$, and $O(n^3/\log^2 n)$ on a word-RAM with $w = \Theta(\log n)$.
- **1981.** Atkinson–Santoro, and later work on bit-parallel implementations, make the $n^3/w$ bound the practical baseline.
- **1987–1990.** Coppersmith–Winograd: $\omega < 2.376$.
- **2012–2014.** Stothers, Vassilevska Williams ($\omega < 2.3729$), Le Gall ($\omega < 2.3729$, refined) push the laser method.
- **2012.** Bansal–Williams give the first genuinely new combinatorial speedup since Four Russians, using the Szemerédi regularity lemma / graph triangle-removal structure: $\hat{O}(n^3/\log^{2.25} n)$.
- **2015.** Chan: $O(n^3/\log^3 n)$ (word-RAM), "speeding up Four Russians by about one more log factor". Yu: $\hat O(n^3/\log^4 n)$.
- **2021.** Alman–Vassilevska Williams: refined laser method, $\omega < 2.3729$ (2.37286).
- **2023–2024.** Duan–Wu–Zhou introduce an asymmetric hashing correction to the laser method: $\omega < 2.371866$; Vassilevska Williams–Xu–Xu–Zhou: $\omega < 2.371552$.
- **2024.** Abboud, Fischer, Kelley, Lovett, Meka (STOC 2024) break the polylogarithmic barrier for combinatorial BMM: a new graph decomposition, built on strong bounds for the corners/BLR-type problem, yields $n^3 / 2^{\Omega(\sqrt{\log n})}$ — superpolylogarithmic savings, but still $n^{3-o(1)}$.
- **2025.** Alman, Duan, Vassilevska Williams, Xu, Xu, Zhou (SODA 2025): $\omega < 2.371339$. *(frontier — verify current record)*

## 4. Partial Results / Verified Cases

- **Rectangular / unbalanced shapes.** $n \times n^\alpha$ by $n^\alpha \times n$ products run in $n^{2+o(1)}$ time for all $\alpha \le \alpha^* $, with $\alpha^* > 0.321$ (Le Gall–Urrutia; improved to $\ge 0.3213$, and to $\approx 0.3216$ in 2023–24 work). So for these aspect ratios the "$\omega=2$-like" behaviour is *proved*.
- **Sparse inputs.** If $A$ and $B$ have $m$ nonzeros total, the product is computable in $\tilde O(m^{2/3} n^{2/3} + n^2)$-type bounds (Yuster–Zwick, Amossen–Pagh); output-sensitive algorithms compute a product with $Z$ nonzeros in $\tilde O(n^2 Z^{(\omega-2)/(\omega-1)})$ (Lingas 2009).
- **Small $n$ / exact rank.** $R(\langle 2,2,2\rangle) = 7$ (Strassen upper, Winograd lower bound), so $2\times 2$ is fully settled. $R(\langle 3,3,3\rangle) \in [19, 23]$: the upper bound $23$ (Laderman 1976, and AlphaEvolve-era rediscoveries) and lower bound $19$ (Bläser) leave $3\times 3$ open. $\underline{R}(\langle n,n,n\rangle) \ge 2n^2 - \lceil \log n\rceil - 1$ (Landsberg–Michałek), still far below $n^{2+\varepsilon}$-forcing bounds.
- **Structured matrices.** If $A$ is the adjacency matrix of a graph of bounded treewidth, bounded VC-dimension, or a $K_{t,t}$-free bipartite graph, near-linear-in-input-size algorithms exist (Feder–Motwani compression; the Bansal–Williams regularity approach is a general-position analogue).
- **Quantum.** Output-sensitive quantum BMM in $\tilde O(n^{1.5})$ when the output has $O(1)$ nonzeros, and $\tilde O(n\sqrt{\ell} + \ell\sqrt{n})$ for output weight $\ell$ (Buhrman–Špalek; Le Gall 2012; Jeffery–Kothari–Magniez), beating $n^2$ input-reading in the query model.
- **Model-specific lower bounds.** $\Theta(n^3)$ in monotone Boolean circuits (Paterson 1975; Mehlhorn–Galil 1976); $\Omega(n^2)$ trivially for any model reading the input.

## 5. Principal Obstacles

**For $\omega = 2$.** All records since 1987 come from the laser method applied to powers of the Coppersmith–Winograd tensor $CW_q$. Two barrier results say this route cannot reach 2:

- *Group-theoretic / tensor barriers.* Ambainis, Filmus, Le Gall (2015) proved that the laser method applied to any fixed tensor of border rank $\le$ that of $CW_q$, taken to arbitrary powers, cannot prove $\omega < 2.3078$; in particular no amount of further optimisation of the current framework gets to 2.
- *Asymptotic-rank and slice-rank barriers.* Alman–Vassilevska Williams (2018) and Blasiak et al. showed the "universal method" — any bound derived only from the tensor's asymptotic degeneration behaviour — is limited for all tensors currently in hand; the Cohn–Umans group-algebra program hits the cap-set barrier (Ellenberg–Gijswijt bounds kill the abelian STPP constructions).
- On the lower-bound side, the best unconditional bound on tensor rank is $\approx 3n^2 - o(n^2)$; no technique is known that could give $n^{2+\varepsilon}$, and arithmetic-circuit lower bounds of that strength are far beyond current methods.

**For combinatorial BMM.** The semiring has no cancellation, so the $n^3$ monotone lower bound is real; every subcubic method must smuggle in either word-parallelism (which buys $\log$ factors, capped by $w = \Theta(\log n)$ per operation) or pseudorandomness/structure (regularity, corner-free sets). The Abboud–Fischer–Kelley–Lovett–Meka route trades savings against the density bounds for corner-free sets in $[n]^2$; the best such bounds are quasi-polynomial-type, and the resulting savings are $2^{\Theta(\sqrt{\log n})}$ — polynomial savings would require corner-free sets of density $n^{-\Omega(1)}$-scale bounds that are *false*, so this specific route is capped.

**For proving the conjecture.** There is no formal model of "combinatorial". Attempts to formalise (monotone circuits, restricted branching programs, bounded-fan-in set-cover models) either admit Four-Russians tricks or exclude them artificially. Proving $n^{3-o(1)}$ unconditionally in a general model would imply super-linear circuit lower bounds, which is out of reach.

## 6. The Gap

- **Exponent gap.** Proved: $2 \le \omega < 2.371339$. Conjectured: $\omega = 2$. The exact missing step is a tensor construction (or a non-tensor algorithmic paradigm) whose asymptotic rank certifies exponent $2+o(1)$, evading the Ambainis–Filmus–Le Gall bound of $2.3078$ and the universal-method barriers. No candidate object is known to be barrier-free.
- **Combinatorial gap.** Proved: $n^3/2^{\Theta(\sqrt{\log n})}$ upper bound; no unconditional lower bound above $\Omega(n^2)$. Conjectured: no $O(n^{3-\varepsilon})$ combinatorial algorithm. The gap is exactly the region between $2^{\sqrt{\log n}}$ savings and $n^{\varepsilon}$ savings — a savings function that is superpolylogarithmic but subpolynomial. Crossing it upward requires a decomposition with polynomial (not quasi-polynomial) density loss; crossing it downward requires a computational model in which the additive-combinatorial decompositions are provably unavailable.

## 7. Current Research (as of June 2026)

- **Laser-method refinements.** Duan (Tsinghua), Zhou, Wu; Vassilevska Williams, Xu, Xu (MIT/Berkeley/Simons). The asymmetric-hashing idea of Duan–Wu–Zhou (2023) is the current engine; successive papers squeeze $\sim 10^{-4}$ off $\omega$ per iteration. Consensus among these authors is that the method saturates near $2.37$.
- **Barrier-evading tensors.** Search for tensors with small asymptotic rank not covered by the universal-method barrier; Kaski, Karppa (Aalto) on probabilistic tensors and "opportunistic" BMM ($n^{2.778}$-type bounds for BMM specifically, exploiting that Boolean output tolerates one-sided error).
- **Additive-combinatorial BMM.** Abboud (Weizmann), Fischer, Kelley, Lovett, Meka: extending the STOC 2024 decomposition, and asking whether the $2^{\sqrt{\log n}}$ savings can be pushed to $2^{(\log n)^{1-o(1)}}$. *(frontier — verify)*
- **Fine-grained consequences.** OMv and BMM-hardness used for dynamic reachability, distance oracles, context-free parsing (Lee's $O(n^{3-\varepsilon})$-parsing $\Rightarrow$ subcubic BMM), and RNA folding.
- **Machine-discovered algorithms.** AlphaTensor (2022) and AlphaEvolve (2025) found new small-format schemes (e.g. $4\times4$ over $\mathbb{C}$ in 48 multiplications); none improve the asymptotic exponent. *(frontier — verify claims about asymptotic impact.)*

## 8. Future Work

1. Find a tensor family whose *asymptotic* rank is $n^{2+o(1)}$ and that is not blocked by the group-theoretic cap-set barrier — Cohn–Umans suggested non-abelian groups with suitable simultaneous triple product property.
2. Prove or refute $\omega > 2$ via a border-rank lower bound of the form $\underline{R}(\langle n,n,n\rangle) \ge n^{2+\varepsilon}$ using algebraic geometry (Landsberg's program: equations for secant varieties).
3. Formalise "combinatorial algorithm" so that the conjecture becomes a theorem or a refutable statement — e.g. a circuit class closed under table lookup but not under integer cancellation.
4. Determine whether corner-free-set bounds fundamentally cap combinatorial savings at $2^{o(\log n)}$; a matching conditional lower bound would be a major structural result.
5. Settle $R(\langle 3,3,3\rangle)$; the gap $[19,23]$ is embarrassingly open and any improvement informs the general lower-bound toolkit.

## 9. Key References

- **[Foundational]** V. Strassen. *Gaussian elimination is not optimal.* Numerische Mathematik 13(4):354–356, 1969.
- **[Foundational]** V. Arlazarov, E. Dinic, M. Kronrod, I. Faradzhev. *On economical construction of the transitive closure of a directed graph.* Doklady Akademii Nauk SSSR 194(3), 1970.
- **[Foundational]** M. J. Fischer, A. R. Meyer. *Boolean matrix multiplication and transitive closure.* IEEE 12th Annual Symposium on Switching and Automata Theory (SWAT/FOCS), 1971.
- **[Foundational]** M. S. Paterson. *Complexity of monotone networks for Boolean matrix multiplication.* Theoretical Computer Science 1(1):13–20, 1975.
- **[Foundational]** D. Coppersmith, S. Winograd. *Matrix multiplication via arithmetic progressions.* Journal of Symbolic Computation 9(3):251–280, 1990.
- **[SOTA / Recent]** J. Alman, V. Vassilevska Williams. *A refined laser method and faster matrix multiplication.* SODA 2021.
- **[SOTA / Recent]** R. Duan, H. Wu, R. Zhou. *Faster matrix multiplication via asymmetric hashing.* FOCS 2023.
- **[SOTA / Recent]** V. Vassilevska Williams, Y. Xu, Z. Xu, R. Zhou. *New bounds for matrix multiplication: from alpha to omega.* SODA 2024.
- **[SOTA / Recent]** A. Abboud, N. Fischer, Z. Kelley, S. Lovett, R. Meka. *New graph decompositions and combinatorial Boolean matrix multiplication algorithms.* STOC 2024.
- **[SOTA / Recent]** N. Bansal, R. Williams. *Regularity lemmas and combinatorial algorithms.* Theory of Computing 8:69–94, 2012 (conference version FOCS 2009).
- **[SOTA / Recent]** T. M. Chan. *Speeding up the Four Russians algorithm by about one more logarithmic factor.* SODA 2015.
- **[SOTA / Recent]** V. Vassilevska Williams, R. Williams. *Subcubic equivalences between path, matrix, and triangle problems.* Journal of the ACM 65(5), 2018 (FOCS 2010).
- **[SOTA / Recent]** A. Ambainis, Y. Filmus, F. Le Gall. *Fast matrix multiplication: limitations of the Coppersmith–Winograd method.* STOC 2015.
- **[SOTA / Recent]** J. Alman, V. Vassilevska Williams. *Limits on all known (and some unknown) approaches to matrix multiplication.* FOCS 2018.
- **[Survey]** P. Bürgisser, M. Clausen, M. A. Shokrollahi. *Algebraic Complexity Theory.* Springer, Grundlehren 315, 1997.
- **[Survey]** J. M. Landsberg. *Geometry and Complexity Theory.* Cambridge University Press, 2017.
- **[Survey]** V. Vassilevska Williams. *On some fine-grained questions in algorithms and complexity.* Proceedings of the ICM 2018, Vol. 4, pp. 3447–3487.

## 10. Worked Example / Concrete Special Case

**Direct product, $n=4$.** Let
$$A=\begin{pmatrix}1&0&1&0\\0&1&0&0\\0&0&1&1\\1&0&0&0\end{pmatrix},\qquad B=\begin{pmatrix}0&1&0&0\\1&0&0&1\\0&0&1&0\\0&1&0&0\end{pmatrix}.$$
Read $A \odot B$ row-wise: row $i$ of $C$ is the OR of those rows of $B$ selected by the 1s in row $i$ of $A$.

- Row 1 of $A$ picks rows $\{1,3\}$ of $B$: $(0,1,0,0)\vee(0,0,1,0)=(0,1,1,0)$.
- Row 2 picks row $\{2\}$: $(1,0,0,1)$.
- Row 3 picks rows $\{3,4\}$: $(0,0,1,0)\vee(0,1,0,0)=(0,1,1,0)$.
- Row 4 picks row $\{1\}$: $(0,1,0,0)$.

$$C = A\odot B=\begin{pmatrix}0&1&1&0\\1&0&0&1\\0&1&1&0\\0&1&0&0\end{pmatrix}.$$
Over $\mathbb{Z}$ the same product gives $C^{\mathbb{Z}}_{13}=1$, $C^{\mathbb{Z}}_{33}=1$, and no entry exceeds $1$ here; thresholding recovers $C$.

**Four Russians on this instance.** Split the $k$-index into blocks of size $t=2$: $k\in\{1,2\}$ and $k\in\{3,4\}$. For the first block, precompute the OR of every subset of rows $\{B_{1\cdot},B_{2\cdot}\}$:
$$\emptyset\mapsto(0,0,0,0),\ \{1\}\mapsto(0,1,0,0),\ \{2\}\mapsto(1,0,0,1),\ \{1,2\}\mapsto(1,1,0,1).$$
Now each row of $C$ needs one table lookup per block instead of $t$ row-ORs: row 1 of $A$ has pattern $10$ on block 1 (lookup $\to (0,1,0,0)$) and $10$ on block 2 (lookup $\to (0,0,1,0)$), OR $=(0,1,1,0)$. ✓ Cost is $2^t \cdot n$ preprocessing per block and $n$ lookups per block, total $O(2^t n^2/t + \cdot)$, minimised at $t=\log n$ to give $O(n^3/\log n)$. The example shows exactly where the savings come from — and why they are only logarithmic: the table has $2^t$ rows, so $t$ cannot exceed $\log n$.

**Reduction to triangle detection.** Let $G$ be tripartite with parts $I,K,J$ of size $n$, edges $i\!-\!k$ when $A_{ik}=1$ and $k\!-\!j$ when $B_{kj}=1$, plus edge $i\!-\!j$ for the single pair we test. Then $C_{ij}=1$ iff $G$ contains a triangle through $i\!-\!j$. With $i=1,j=3$: edges $1\!-\!1$, $1\!-\!3$ into $K$, and $1\!-\!3$, $3\!-\!3$ out of $K$; vertex $k=3$ closes the triangle $1\!-\!3_K\!-\!3_J$, confirming $C_{13}=1$. Batching all $n^2$ pairs is precisely the subcubic-equivalence of Vassilevska Williams–Williams: an $O(n^{3-\varepsilon})$ combinatorial triangle detector would refute the combinatorial BMM conjecture.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*