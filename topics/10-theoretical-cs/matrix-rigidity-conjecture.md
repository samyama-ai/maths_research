---
id: 10-theoretical-cs/matrix-rigidity-conjecture
title: "Matrix Rigidity Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Matrix Rigidity Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/matrix-rigidity-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Valiant's rigidity function measures how far a matrix is from having low rank, when distance is counted in *changed entries* rather than norm. For a field $\mathbb{F}$, a matrix $A \in \mathbb{F}^{n \times n}$ and a target rank $r$,

$$\mathcal{R}_A^{\mathbb{F}}(r) \;=\; \min\{\,\|S\|_0 \;:\; \operatorname{rank}_{\mathbb{F}}(A - S) \le r \,\},$$

where $\|S\|_0$ is the number of nonzero entries of $S$.

**The conjecture (Valiant, 1977).** There is an explicit family $\{A_n\}$ of $n \times n$ matrices — explicit meaning entries computable in time $\mathrm{poly}(n)$, i.e. the family lies in $\mathsf{P}$ (or at least in $\mathsf{E}^{\mathsf{NP}}$ for the weaker versions) — and constants $\varepsilon, \delta > 0$ with

$$\mathcal{R}_{A_n}(\varepsilon n) \;\ge\; n^{1+\delta} \qquad \text{for all large } n .$$

Such a family is called **Valiant-rigid**. A complete resolution means either exhibiting one explicit family with a proof of the bound, or proving that no family in the relevant explicitness class can satisfy it. The stake is not the bound itself but its corollary: a Valiant-rigid family cannot be computed by arithmetic circuits of size $O(n)$ and depth $O(\log n)$ over $\mathbb{F}$, which would be the first superlinear lower bound for log-depth linear circuits — a barrier open since 1977.

The open status is sharpened by the fact that *most* matrices are rigid (Section 4) while *every* natural candidate proposed in fifty years has been shown non-rigid (Section 3).

## 2. Mathematical Foundations

**Linear circuits.** A linear circuit over $\mathbb{F}$ is a DAG with $n$ input nodes, $n$ output nodes, and internal gates computing $\alpha u + \beta v$ for $\alpha,\beta\in\mathbb{F}$. Size is the edge count, depth the longest input–output path. Such a circuit computes $x \mapsto Ax$ for a unique $A$.

**Valiant's theorem.** If $A$ is computed by a linear circuit of size $O(n)$ and depth $O(\log n)$, then for every $\varepsilon > 0$,

$$\mathcal{R}_A\!\left(O\!\left(\tfrac{n}{\log\log n}\right)\right) \;\le\; n^{1+\varepsilon}.$$

The proof is graph-theoretic: in any $O(n)$-size $O(\log n)$-depth DAG one can delete $O(n/\log\log n)$ edges so that every remaining input–output path is short, hence each output depends on at most $n^{\varepsilon}$ inputs. The deleted edges contribute a rank-$O(n/\log\log n)$ term $L$; the truncated graph contributes a sparse term $S$ with $A = L + S$. The contrapositive is the conjecture's payoff.

**Razborov's connection.** Rigidity in a different parameter regime, $\mathcal{R}_A(2^{(\log\log n)^{\omega(1)}}) \ge n^2 / 2^{(\log\log n)^{\omega(1)}}$ over $\mathbb{F}_2$, separates the communication-complexity polynomial hierarchy $\mathsf{PH}^{cc}$ from $\mathsf{PSPACE}^{cc}$ (Razborov, 1989).

**Elementary facts.**
- Monotonicity: $\mathcal{R}_A(r)$ is nonincreasing in $r$; $\mathcal{R}_A(r) = 0$ iff $\operatorname{rank}(A)\le r$.
- Invariance: rigidity is preserved by row/column permutations and by multiplication by nonsingular *sparse-preserving* maps only — it is **not** invariant under general $A \mapsto UAV$, which is precisely why linear-algebraic machinery is weak here.
- Non-rigidity is a Zariski-closed-ish condition: the set of matrices with $\mathcal{R}_A(r) \le s$ is the image of the variety $\{L : \operatorname{rank} L \le r\}$ under adding sparse perturbations, a union of $\binom{n^2}{s}$ shifted determinantal varieties. Kumar and Volk (2021) showed this set is cut out by polynomials of degree $\mathrm{poly}(n)$ — far below what a naive elimination bound would give.

**Probabilistic rank.** For $A$ over $\mathbb{F}$, the $\epsilon$-probabilistic rank is the least $r$ such that there is a distribution over rank-$r$ matrices $M$ with $\Pr[M_{ij} = A_{ij}] \ge 1-\epsilon$ for every entry $(i,j)$. Low probabilistic rank implies low rigidity by averaging, and is the engine of the modern non-rigidity results.

## 3. History & State of the Art (SOTA)

- **1977.** Valiant introduces rigidity in *Graph-theoretic arguments in low-level complexity* and proves the circuit consequence and the generic lower bound $(n-r)^2$.
- **1989.** Razborov links rigidity to communication complexity.
- **1993–1997.** Friedman, and independently Shokrollahi–Spielman–Stemann, prove $\mathcal{R}_A(r) = \Omega\!\big(\frac{n^2}{r}\log\frac{n}{r}\big)$ for generator matrices of good codes and for Cauchy matrices. This remains the best explicit bound over general fields.
- **1998–2006.** Kashin–Razborov, Lokam, and de Wolf (quantum argument) prove $\mathcal{R}_{H_N}(r) = \Omega(N^2/r)$ for the Walsh–Hadamard matrix. Lokam (2006) obtains $\Omega(n^2)$ rigidity at rank $\Omega(n)$ for an explicit real matrix with entries $\sqrt{p_{ij}}$ ($p_{ij}$ distinct primes) — Valiant-strength, but over $\mathbb{R}$ with irrational entries, and it does not transfer to finite fields or yield the intended Boolean-flavoured consequences.
- **2017 onward — the collapse of the candidates.** Alman and Williams show the Walsh–Hadamard matrix is **not** Valiant-rigid over any field: $\mathcal{R}_{H_N}(\varepsilon N) \le N^{2-\delta(\varepsilon)}$. Dvir–Liu (2019/2020) extend this to the DFT matrix over $\mathbb{C}$, all circulant and Toeplitz-like matrices arising from abelian-group convolution, and the Kronecker powers of small matrices. Alman (2021) generalises: for *every* fixed matrix $M$, the Kronecker powers $M^{\otimes k}$ are non-rigid.
- **2019–2020 — semi-explicit successes.** Alman–Chen construct rigid matrices in $\mathsf{P}^{\mathsf{NP}}$; Bhangale–Harsha–Paradise–Tal construct them in $\mathsf{FNP}$/$\mathsf{E}^{\mathsf{NP}}$ via rectangular PCPs, for rank up to $2^{(\log n)^{1-\varepsilon}}$ — still far below the linear rank Valiant needs.

## 4. Partial Results / Verified Cases

- **Generic and random matrices.** Over any infinite field, a generic $A$ satisfies $\mathcal{R}_A(r) = (n-r)^2$ exactly; over $\mathbb{F}_q$, a uniform random matrix satisfies $\mathcal{R}_A(r) = \Omega\big((n-r)^2/\log q\big)$ by counting. So Valiant-rigid matrices exist in abundance — only explicitness is missing.
- **Totally nonsingular matrices** (all minors nonzero, e.g. Cauchy $A_{ij}=1/(x_i+y_j)$, Vandermonde with distinct nodes): $\mathcal{R}_A(r) \ge \frac{n(n-r)}{r+1}$ by the elementary argument in Section 10; improved to $\Omega\!\big(\frac{n^2}{r}\log\frac{n}{r}\big)$ for MDS-code generator matrices (Friedman 1993; Shokrollahi–Spielman–Stemann 1997).
- **Hadamard matrices:** $\mathcal{R}_{H_N}(r) \ge N^2/(4r)$ (Kashin–Razborov 1998; de Wolf 2006), tight in spirit given Alman–Williams.
- **Random Toeplitz / Hankel matrices:** Goldreich and Tal (2018) prove rigidity $\tilde\Omega(n^3/r^2)$ for $r \ge \sqrt n$ — superlinear at rank $r = n^{1/2+\epsilon}$, but zero at $r = \varepsilon n$, and Toeplitz matrices carry only $2n-1$ bits of randomness, so this is "semi-explicit".
- **Restricted-rank regimes.** At rank $r = n^{o(1)}$, explicit families with rigidity $n^{2-o(1)}$ are known (any good code's generator matrix). Valiant's application needs $r = \Theta(n/\log\log n)$.
- **Restricted decompositions.** If the sparse part $S$ is required to have $O(1)$ nonzeros per row, or the low-rank part $L$ has bounded entry-complexity, Valiant-strength bounds are provable for explicit matrices.

## 5. Principal Obstacles

- **Untouched-minor arguments saturate at $n^2/r$.** Every classical lower bound proceeds by finding a submatrix that the sparse perturbation misses and lower-bounding its rank. A sparse pattern with $s$ nonzeros always leaves a clean submatrix of dimension roughly $n^2/s$, and such an argument can never certify more than $\tilde O(n^2/r)$ changes. At $r = \varepsilon n$ this gives $O(n)$ — below the $n^{1+\delta}$ target by a polynomial factor. This is a genuine method barrier, not a matter of effort.
- **Spectral and analytic methods measure the wrong distance.** Singular values, Fourier coefficients and matrix norms are continuous in the $\ell_2$ metric; the sparse perturbation $S$ can be entrywise huge while touching few entries, so any norm-based bound on $\|A - L\|$ is vacuous.
- **Non-invariance.** Rigidity respects only permutations of rows and columns, so representation-theoretic and orbit-closure techniques (which drive geometric complexity theory) have no natural handle on it.
- **The candidates keep dying.** Every structured matrix with fast algorithms — DFT, Hadamard, circulant, Kronecker powers — turns out to be non-rigid, and this is no accident: fast recursive structure yields low probabilistic rank via polynomial-approximation and Croot–Lev–Pach-style arguments (Dvir–Edelman 2019). But explicitness itself tends to come from exactly such structure, so the sources of explicit matrices and the sources of non-rigidity coincide.
- **Weak dimension counting.** The non-rigid locus is an $O(n^2)$-dimensional union of varieties inside $\mathbb{F}^{n\times n}$; producing a *specific* point outside it requires an invariant that current algebraic geometry does not supply — and Kumar–Volk's low-degree equations show the locus is "algebraically simple", which is bad news for degree-based separations.

## 6. The Gap

Proven, for explicit families over general fields: $\mathcal{R}_A(r) = \Omega\!\big(\frac{n^2}{r}\log\frac{n}{r}\big)$. Required: $\mathcal{R}_A(\varepsilon n) \ge n^{1+\delta}$.

At $r = \varepsilon n$ the proven bound reads $\Omega(n\log(1/\varepsilon))$ — linear. The gap is a **factor of $n^{\delta}$ at linear target rank**, equivalently the passage from "some clean submatrix has full rank" to "no sparse pattern of size $n^{1+\delta}$ can be completed to rank $\varepsilon n$". Two crossings are conceivable:

1. **Rank axis:** push semi-explicit constructions (Alman–Chen, BHPT) from rank $2^{(\log n)^{1-\varepsilon}}$ up to $n^{\Omega(1)}$ and then to $\varepsilon n$, while keeping the construction in $\mathsf{P}$ rather than $\mathsf{E}^{\mathsf{NP}}$.
2. **Sparsity axis:** find a lower-bound technique that is sensitive to *entry patterns* rather than to submatrices — the untouched-minor barrier must be circumvented, not optimised.

A third, increasingly credible possibility: prove a general non-rigidity theorem showing that no matrix computable by a $\mathrm{poly}(n)$-time algorithm can be Valiant-rigid, refuting the programme.

## 7. Current Research (as of June 2026)

- **Non-rigidity as a positive theory.** Alman, Dvir, Liu and collaborators continue mapping which structured families collapse. The working slogan is that "fast Fourier-type structure $\Rightarrow$ non-rigid", and there is active work on whether *all* matrices with $O(n\,\mathrm{polylog}\,n)$-size circuits are non-rigid — which would make the rigidity method self-defeating for its intended targets. *(frontier — verify)*
- **Semi-explicit constructions.** Following Alman–Chen and Bhangale–Harsha–Paradise–Tal, work continues on improving the rank parameter of $\mathsf{E}^{\mathsf{NP}}$-constructible rigid matrices and on derandomising the PCP machinery. Groups at Tel Aviv, TIFR, Princeton/IAS and MIT are central here.
- **Algebraic-geometry route.** Kumar–Volk-style equations for the non-rigid locus, and attempts to bound the degree or defining ideal of that locus from below, remain a live line at ITCS/CCC.
- **Alternative rigidity notions.** Rigidity for restricted perturbation patterns, $\ell_p$-rigidity, tensor rigidity, and rigidity over rings are studied as possibly more tractable proxies with retained circuit consequences.
- **Consensus shift.** A visible fraction of the community now expects the specific Valiant programme to fail for all natural explicit candidates, while the *existence* of $\mathsf{E}^{\mathsf{NP}}$-rigid matrices at growing rank is seen as the achievable frontier. *(frontier — verify)*

## 8. Future Work

- **Push semi-explicit rank.** Get rigid matrices in $\mathsf{P}^{\mathsf{NP}}$ at rank $n^{\Omega(1)}$; this would already yield new $\mathsf{E}^{\mathsf{NP}}$ circuit lower bounds.
- **Barrier formalisation.** State and prove a theorem that untouched-submatrix arguments cannot exceed $\tilde O(n^2/r)$, analogous to natural proofs — this would tell the field where not to look.
- **Find a non-Fourier candidate.** Matrices from expander/Ramanujan graph incidence structures, from number-theoretic sources (Paley-type constructions over large fields), or from pseudorandom generators, chosen specifically to lack recursive Kronecker structure.
- **Settle the collapse question.** Prove or refute: every matrix family with $\mathrm{poly}(n)$-time computable entries is non-Valiant-rigid.
- **Weaker sufficient conditions.** Identify circuit-lower-bound consequences that follow from rigidity bounds achievable at rank $n^{1-\epsilon}$, lowering the target.

## 9. Key References

- **[Foundational]** L. G. Valiant. *Graph-theoretic arguments in low-level complexity.* Mathematical Foundations of Computer Science (MFCS), Lecture Notes in Computer Science 53, Springer, 1977, pp. 162–176.
- **[Foundational]** A. A. Razborov. *On rigid matrices.* Technical report (in Russian), Steklov Mathematical Institute, 1989.
- **[Foundational]** J. Friedman. *A note on matrix rigidity.* Combinatorica 13(2), 1993, pp. 235–239.
- **[Foundational]** M. A. Shokrollahi, D. A. Spielman, V. Stemann. *A remark on matrix rigidity.* Information Processing Letters 64(6), 1997, pp. 283–285.
- **[Foundational]** B. S. Kashin, A. A. Razborov. *Improved lower bounds on the rigidity of Hadamard matrices.* Matematicheskie Zametki 63(4), 1998, pp. 535–540.
- **[Theory]** S. V. Lokam. *Spectral methods for matrix rigidity with applications to size–depth trade-offs and communication complexity.* Journal of Computer and System Sciences 63(3), 2001, pp. 449–473.
- **[Theory]** R. de Wolf. *Lower bounds on matrix rigidity via a quantum argument.* ICALP 2006, LNCS 4051, pp. 62–71.
- **[Theory]** S. V. Lokam. *Quadratic lower bounds on matrix rigidity.* Theory and Applications of Models of Computation (TAMC) 2006, LNCS 3959, pp. 295–307.
- **[SOTA / Recent]** J. Alman, R. Williams. *Probabilistic rank and matrix rigidity.* STOC 2017, pp. 641–652.
- **[SOTA / Recent]** Z. Dvir, A. Liu. *Fourier and circulant matrices are not rigid.* Theory of Computing 16(20), 2020 (conference version CCC 2019).
- **[SOTA / Recent]** Z. Dvir, B. Edelman. *Matrix rigidity and the Croot–Lev–Pach lemma.* Theory of Computing 15(8), 2019.
- **[SOTA / Recent]** O. Goldreich, A. Tal. *Matrix rigidity of random Toeplitz matrices.* Computational Complexity 27(2), 2018, pp. 305–350.
- **[SOTA / Recent]** J. Alman, L. Chen. *Efficient construction of rigid matrices using an NP oracle.* FOCS 2019, pp. 1034–1055.
- **[SOTA / Recent]** A. Bhangale, P. Harsha, O. Paradise, A. Tal. *Rigid matrices from rectangular PCPs.* FOCS 2020, pp. 1063–1073.
- **[SOTA / Recent]** J. Alman. *Kronecker products, low-depth circuits, and matrix rigidity.* STOC 2021, pp. 772–785.
- **[SOTA / Recent]** M. Kumar, B. L. Volk. *A polynomial degree bound on equations for non-rigid matrices and small linear circuits.* ITCS 2021.
- **[Survey]** S. V. Lokam. *Complexity lower bounds using linear algebra.* Foundations and Trends in Theoretical Computer Science 4(1–2), 2009, pp. 1–155.
- **[Survey]** P. Bürgisser, M. Clausen, M. A. Shokrollahi. *Algebraic Complexity Theory.* Springer, Grundlehren der mathematischen Wissenschaften 315, 1997 (Chapter 13 covers rigidity).

## 10. Worked Example / Concrete Special Case

**Claim.** Let $A \in \mathbb{F}^{n\times n}$ be *totally nonsingular*: every square submatrix of $A$ is invertible. Then

$$\mathcal{R}_A(r) \;\ge\; \frac{n\,(n-r)}{r+1}.$$

*Proof.* Write $A = L + S$ with $\operatorname{rank}(L) \le r$ and $\|S\|_0 = s$. Partition the rows into $m = \lfloor n/(r+1)\rfloor$ disjoint blocks $R_1,\dots,R_m$ of $r+1$ rows each. Fix a block $R_k$ and let $C_k$ be the set of columns in which $S$ restricted to the rows $R_k$ is entirely zero. If $|C_k| \ge r+1$, pick any $r+1$ columns of $C_k$; the corresponding $(r+1)\times(r+1)$ submatrix of $A$ equals the same submatrix of $L$, so it has rank $\le r$ — contradicting total nonsingularity. Hence $|C_k| \le r$, so at least $n - r$ columns contain a nonzero of $S$ inside the rows $R_k$. Summing over the $m$ disjoint blocks,

$$s \;\ge\; m\,(n-r) \;\ge\; \frac{n(n-r)}{r+1} - (n-r). \qquad \square$$

**A concrete matrix.** Over $\mathbb{Q}$ take the Cauchy matrix $A_{ij} = \frac{1}{x_i + y_j}$ with $x_i = i$, $y_j = j - 1/2$ for $1 \le i,j \le 64$. Cauchy matrices are totally nonsingular (every minor equals a nonzero product of differences over a product of sums). For $r = 4$ the claim gives

$$\mathcal{R}_A(4) \;\ge\; \frac{64 \cdot 60}{5} \;=\; 768 .$$

Compare: a generic $64\times 64$ matrix has $\mathcal{R}(4) = (64-4)^2 = 3600$. So even at small rank the explicit bound is a factor $\approx 4.7$ short of generic.

**Where it fails for Valiant.** Set $r = \varepsilon n$. The bound becomes

$$\mathcal{R}_A(\varepsilon n) \;\ge\; \frac{n(1-\varepsilon)n}{\varepsilon n + 1} \;\approx\; \frac{(1-\varepsilon)}{\varepsilon}\, n,$$

which is $\Theta(n)$ — linear in $n$, for any fixed $\varepsilon$. Valiant needs $n^{1+\delta}$. Refining the counting to the code-based bound $\Omega\big(\frac{n^2}{r}\log\frac{n}{r}\big)$ only inserts a $\log(1/\varepsilon)$ factor. For $n = 2^{20}$ and $\varepsilon = 1/10$ the proven bound is about $9.4 \times 10^6$ changed entries, while $n^{1.1} \approx 4.2 \times 10^6$ — comfortably met — but at $n^{1.5} \approx 1.1\times 10^{10}$ the proven bound is short by three orders of magnitude, and the shortfall grows with $n$. That is the gap of Section 6, in numbers.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*