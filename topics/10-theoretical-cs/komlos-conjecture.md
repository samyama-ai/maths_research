---
id: 10-theoretical-cs/komlos-conjecture
title: "Komlos Conjecture"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Komlós Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/komlos-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Komlós).** There is a universal constant $K < \infty$, independent of $n$ and $d$, such that for every $d \ge 1$ and every family of vectors $v_1,\dots,v_n \in \mathbb{R}^d$ with $\|v_i\|_2 \le 1$, there exist signs $\varepsilon_1,\dots,\varepsilon_n \in \{-1,+1\}$ with

$$\Big\| \sum_{i=1}^n \varepsilon_i v_i \Big\|_\infty \;\le\; K .$$

Equivalently, in matrix form: for every $A \in \mathbb{R}^{d \times n}$ whose columns have Euclidean norm at most $1$, $\min_{x \in \{-1,1\}^n} \|Ax\|_\infty \le K$.

A complete resolution requires either (i) a proof exhibiting an absolute constant $K$ (existence suffices; no algorithm is demanded), or (ii) a family of instances $\{A_n\}$ with unit-norm columns and $\min_{x\in\{\pm1\}^n}\|A_n x\|_\infty \to \infty$. The conjecture is *not* about the ordinary discrepancy of a set system directly, but implies the Beck–Fiala conjecture as a corollary (Section 2).

## 2. Mathematical Foundations

**Discrepancy.** For $A \in \mathbb{R}^{d\times n}$, the *discrepancy* is $\mathrm{disc}(A) = \min_{x\in\{-1,1\}^n}\|Ax\|_\infty$, and the *hereditary discrepancy* is $\mathrm{herdisc}(A) = \max_{S\subseteq[n]} \mathrm{disc}(A_{|S})$. For a set system $\mathcal{S} = \{S_1,\dots,S_d\}$ on $[n]$ with incidence matrix $A \in \{0,1\}^{d\times n}$, $\mathrm{disc}(\mathcal{S}) = \min_{\chi:[n]\to\{\pm1\}} \max_j |\sum_{i\in S_j}\chi(i)|$.

**Vector balancing constants.** Following Bárány–Grinberg, for convex bodies $U, V \subset \mathbb{R}^d$ with $V$ symmetric, define
$$\beta(U,V) = \sup_{v_1,\dots,v_n \in U}\;\min_{\varepsilon \in \{\pm1\}^n}\; \inf\{ t>0 : \textstyle\sum_i \varepsilon_i v_i \in tV \}.$$
The Komlós conjecture asserts $\beta(B_2^d, B_\infty^d) = O(1)$, uniformly in $d$, where $B_p^d$ is the unit $\ell_p$ ball. The Bárány–Grinberg theorem gives $\beta(V,V) \le 2d$ for any symmetric convex $V$ — dimension-dependent, hence too weak.

**Beck–Fiala reduction.** If every column of $A\in\{0,1\}^{d\times n}$ has at most $t$ ones (each element lies in $\le t$ sets), then $\|A_{\cdot i}\|_2 \le \sqrt{t}$. Applying Komlós to $A/\sqrt{t}$ gives $\mathrm{disc}(A) \le K\sqrt{t}$: the **Beck–Fiala conjecture** $\mathrm{disc} = O(\sqrt{t})$. The Beck–Fiala theorem (1981) proves only $\mathrm{disc}(A) \le 2t-1$ by an iterative linear-algebra ("floating variables") argument: at each stage the tight constraints number fewer than the fractional variables, so a nonzero vector in the kernel exists and can be walked until a variable rounds.

**Banaszczyk's theorem (1998).** If $\mathcal{K} \subseteq \mathbb{R}^d$ is convex with Gaussian measure $\gamma_d(\mathcal{K}) \ge 1/2$, and $v_1,\dots,v_n$ satisfy $\|v_i\|_2 \le 1/5$, then some signing satisfies $\sum_i \varepsilon_i v_i \in \mathcal{K}$. Since $\gamma_d(c\sqrt{\log d}\, B_\infty^d) \ge 1/2$ for a suitable $c$, and one may reduce to $d \le n$, this yields the current record
$$\mathrm{disc}(A) \;=\; O\!\big(\sqrt{\log \min(n,d)}\big) \quad\text{for unit-norm columns.}$$

**Partial coloring.** The dominant alternative machinery is Beck's entropy method / the Gluskin–Giannopoulos convex-geometric argument: if the entropy of a rounding is small, there is $x \in [-1,1]^n$ with $\ge n/2$ coordinates in $\{\pm1\}$ and $\|Ax\|$ small; iterating over $O(\log n)$ scales gives full colorings. This is how Spencer's $\mathrm{disc} \le 6\sqrt{n}$ for $n$ sets on $n$ points is obtained, and it loses a $\sqrt{\log n}$ factor in the Komlós setting.

## 3. History & State of the Art (SOTA)

- **Origin.** The question is attributed to János Komlós (1980s, unpublished; circulated via Beck and Spencer). It appears in print in Spencer's *Ten Lectures on the Probabilistic Method* (1987) and in Beck–Sós's *Handbook of Combinatorics* chapter (1995).
- **1981.** Beck–Fiala prove $\mathrm{disc} \le 2t-1$ for $t$-sparse systems; conjecture $O(\sqrt t)$.
- **1985.** Spencer's "Six standard deviations suffice" gives $6\sqrt n$ for $n\times n$ systems — nonconstructive, via the entropy/partial-coloring method.
- **1981/1994.** Bárány–Grinberg: $\beta(V,V)\le 2d$; Beck–Spencer and Bárány give early $O(\sqrt{\log n \cdot \log d})$-type Komlós bounds via partial coloring.
- **1998.** Banaszczyk, *Balancing vectors and Gaussian measures of $n$-dimensional convex bodies* — the $O(\sqrt{\log n})$ bound, still the best known, proved by a nonconstructive induction on a Gaussian-measure potential.
- **2010–2015.** Algorithmic revolution: Bansal (FOCS 2010) via SDP + random walk; Lovett–Meka (FOCS 2012) "random walks in Edge-Weighted..." giving constructive Spencer; Rothvoss (FOCS 2014) via random projection onto convex bodies.
- **2016–2019.** Bansal–Dadush–Garg give an algorithm matching Banaszczyk's $O(\sqrt{\log n})$ for Komlós (FOCS 2016 / SICOMP 2019); Bansal–Dadush–Garg–Lovett's **Gram–Schmidt walk** (STOC 2018) gives a simple $O(\sqrt{\log n})$ algorithm and subgaussian coloring guarantees.
- **2020–2024.** Random and smoothed instances resolved (Section 4); online/prefix variants developed; matrix analogues (matrix Spencer) resolved up to polylogarithmic rank.

**SOTA summary.** Best upper bound $O(\sqrt{\log \min(n,d)})$; best lower bound on $K$ is $\sqrt 2$ (Section 10). The gap is a single $\sqrt{\log}$ factor that has resisted attack since 1998.

## 4. Partial Results / Verified Cases

- **Sparse/Beck–Fiala regime.** $\mathrm{disc} \le 2t-1$ (Beck–Fiala 1981); improved to $2t - \log^{*} t$ by Bukh (2016). Banaszczyk gives $O(\sqrt{t \log n})$, better whenever $t \gg \log n$.
- **$t \le 2$.** Trivially $\mathrm{disc} \le 1$ for $t=1$; for $t=2$ the incidence structure is a graph and an Eulerian-orientation argument gives $\mathrm{disc}\le 2$ (constant, consistent with $K$).
- **SDP relaxation.** Nikolov (2013) proved the Komlós conjecture *for vector colorings*: the natural semidefinite relaxation has value $O(1)$ (in fact $\le \sqrt{2}$-type constants), so no SDP-integrality obstruction exists.
- **Random rectangular matrices.** Altschuler–Niles-Weed (RSA 2022) proved that for i.i.d. subgaussian columns with $n \ge C d\log d$, discrepancy is $O(1)$ — indeed exponentially small — establishing a sharp threshold. Franks–Saks (RSA 2020) earlier handled $n = \Omega(d^3\log^2 d)$.
- **Random sparse systems.** Ezra–Lovett (2016) obtained $O(\sqrt{t\log t})$ for random $t$-sparse systems; Bansal–Meka (SODA 2020) proved $O(\sqrt t)$ for random low-degree set systems in a wide parameter range; Potukuchi gave spectral bounds for random $t$-regular hypergraphs.
- **Smoothed analysis.** Bansal, Jiang, Meka, Singla, Sinha (ICALP 2022) showed that perturbing each vector by an independent Gaussian of magnitude $\sigma$ yields discrepancy $O(\mathrm{polylog}(1/\sigma))$ — arbitrary worst-case instances are "one perturbation away" from Komlós-type bounds.
- **Structured instances.** Unit vectors that are $\ell_\infty$-bounded by $O(1/\sqrt{\log d})$ per coordinate, orthonormal families ($\mathrm{disc}\le 1$ for $v_i = e_i$), and Hadamard-type systems all satisfy the conjecture with small explicit constants.
- **Algorithmic.** All the $O(\sqrt{\log n})$ bounds are now constructive in randomized polynomial time (Bansal–Dadush–Garg 2019; Gram–Schmidt walk 2018).

## 5. Principal Obstacles

- **Partial coloring is $\log$-lossy by design.** The entropy method colors half the variables per round and must be iterated $\Theta(\log n)$ times; if each round contributes discrepancy $\delta_k$ at scale $k$, the total is $\sum_k \delta_k$. For Spencer's setting the $\delta_k$ form a geometric series; in the Komlós setting the per-round guarantee degrades exactly so that the sum is $\Theta(\sqrt{\log n})$. No known reweighting makes the series converge.
- **Banaszczyk's potential is tight for its own hypothesis.** The proof controls $\gamma_d$ of the shifted body, and $\gamma_d(t B_\infty^d)\ge 1/2$ genuinely requires $t = \Theta(\sqrt{\log d})$. The method certifies membership in *some* body of Gaussian measure $1/2$; the $\ell_\infty$ ball of constant radius has Gaussian measure $e^{-\Theta(d)}$, so the technique cannot even be stated for the target.
- **Gaussian/subgaussian colorings hit a hard wall.** Gram–Schmidt-walk colorings are $O(1)$-subgaussian, which by a union bound over $d$ coordinates yields $O(\sqrt{\log d})$ and no better. Any coloring distribution with subgaussian marginals must lose $\sqrt{\log d}$; Komlós requires a distribution whose $\ell_\infty$ norm concentrates *without* independent-like tails across coordinates — an object nobody has constructed.
- **No lower-bound technique for the hard direction either.** Standard discrepancy lower bounds (eigenvalue/determinant bound of Lovász–Spencer–Vesztergombi, the $\gamma_2$ characterization of hereditary discrepancy) are all $O(1)$ on unit-norm-column matrices, so they cannot refute the conjecture. This symmetric failure — neither technique can prove nor disprove — is why the problem is considered structurally hard.
- **Convex-geometry route is blocked.** Reducing Komlós to a statement about $\beta(B_2^d, B_\infty^d)$ makes it a question about how well the cube approximates sums of unit vectors; known transference results (Banaszczyk's $\gamma_2$-based bounds, Dadush–Nikolov–Talwar–Tomczak-Jaegermann) characterize vector balancing only up to $\sqrt{\log d}$ factors, precisely the gap in question.

## 6. The Gap

Proven: $\mathrm{disc}(A) \le C\sqrt{\log \min(n,d)}$ for unit-norm columns, plus $O(1)$ for random, smoothed, SDP-relaxed, and $t\le 2$ instances. Conjectured: $\mathrm{disc}(A) \le K$, absolute.

The precise missing step: produce, for arbitrary unit vectors $v_1,\dots,v_n$, a signed sum lying in the constant-radius cube $K B_\infty^d$ — a convex body of Gaussian measure $e^{-\Theta(d)}$ — whereas every existing method (Gaussian potentials, partial coloring, subgaussian random walks) can only reach bodies of Gaussian measure $\Omega(1)$. Equivalently: eliminate the union bound over the $d$ coordinates. A single new idea suffices in either direction: a coloring distribution with $O(1)$ $\ell_\infty$-norm in expectation, or an instance family forcing $\omega(1)$ discrepancy. Even improving $O(\sqrt{\log n})$ to $O((\log n)^{1/2-\delta})$ for any $\delta > 0$ would be a major breakthrough; no such improvement is known.

## 7. Current Research (as of June 2026)

- **Online and prefix variants.** Alweiss–Liu–Sawhney's self-balancing walk (2021) gives $O(\log(nd))$ online against oblivious adversaries; Kulkarni–Reis–Rothvoss (STOC 2024) obtained near-optimal online discrepancy bounds in the Komlós setting. These serve as testbeds for potentials that avoid coordinate union bounds. *(frontier — verify the exact polylog exponents in the latest versions.)*
- **Matrix discrepancy.** Bansal–Jiang–Meka (STOC 2023) resolved matrix Spencer up to polylogarithmic rank; Dadush–Jiang–Reis (SODA 2022) and Hopkins–Raghavendra–Shetty (STOC 2022, quantum-communication method) supply new non-partial-coloring tools. A matrix Komlós statement (symmetric matrices $A_i$ with $\|A_i\|_{\mathrm{op}}\le 1$, $\|\sum A_i^2\|\le 1$) is actively pursued.
- **Reis–Rothvoss school (CWI/Amsterdam, U. Washington).** Vector balancing in $\ell_p$ spaces and convex-geometric strengthenings of Banaszczyk; Rothvoss's programme of replacing partial coloring with direct convex-body arguments.
- **Beyond-worst-case.** Extensions of smoothed and random-instance analysis toward semi-random and planted models (Bansal, Singla, Sinha, and collaborators at Michigan/CMU/Georgia Tech).
- **Algorithmic derandomization and applications.** Gram–Schmidt walk is now standard in randomized experimental design (Harshaw–Sävje–Spielman–Zhang) and in bin-packing integrality gaps (Hoberg–Rothvoss), which keeps quantitative interest in the constant $K$ high.

## 8. Future Work

- Construct a coloring distribution whose $\ell_\infty$ norm is $O(1)$ in expectation — necessarily *not* subgaussian in the coordinates — perhaps by a negatively-correlated or determinantal walk.
- Prove the conjecture in the square case $n = d$, or for matrices with orthogonal-like row structure, as an intermediate target.
- Settle the Beck–Fiala conjecture $O(\sqrt t)$ for fixed small $t$ (e.g. $t = 3$, where even $\mathrm{disc}\le 3$ vs. the trivial $5$ is open in general) — a strictly weaker but still unresolved consequence.
- Seek lower bounds: identify any family beating $\sqrt 2$; even a bound of $3$ would be the first improvement in decades and would constrain the constant.
- Develop a "flatness"/covering-radius reformulation: relate $\beta(B_2^d,B_\infty^d)$ to lattice covering radii, where recent progress on the Kannan and subspace-flatness conjectures (Reis–Rothvoss 2023) supplies new machinery.

## 9. Key References

- **[Foundational]** J. Beck and T. Fiala. *"Integer-making" theorems.* Discrete Applied Mathematics, 3(1):1–8, 1981.
- **[Foundational]** J. Spencer. *Six standard deviations suffice.* Transactions of the American Mathematical Society, 289(2):679–706, 1985.
- **[Foundational]** I. Bárány and V. S. Grinberg. *On some combinatorial questions in finite-dimensional spaces.* Linear Algebra and its Applications, 41:1–9, 1981.
- **[Foundational]** W. Banaszczyk. *Balancing vectors and Gaussian measures of n-dimensional convex bodies.* Random Structures & Algorithms, 12(4):351–360, 1998.
- **[SOTA]** N. Bansal, D. Dadush, S. Garg. *An algorithm for Komlós conjecture matching Banaszczyk's bound.* SIAM Journal on Computing, 48(2):534–553, 2019 (FOCS 2016).
- **[SOTA]** N. Bansal, D. Dadush, S. Garg, S. Lovett. *The Gram–Schmidt walk: a cure for the Banaszczyk blues.* STOC 2018, pp. 587–597.
- **[SOTA]** A. Nikolov. *The Komlós conjecture holds for vector colorings.* arXiv:1301.4039, 2013.
- **[SOTA]** D. Altschuler and J. Niles-Weed. *The discrepancy of random rectangular matrices.* Random Structures & Algorithms, 60(4):551–593, 2022.
- **[SOTA]** N. Bansal, H. Jiang, R. Meka, S. Singla, M. Sinha. *Smoothed analysis of the Komlós conjecture.* ICALP 2022.
- **[SOTA]** N. Bansal, H. Jiang, R. Meka. *Resolving matrix Spencer conjecture up to poly-logarithmic rank.* STOC 2023.
- **[Recent]** B. Bukh. *An improvement of the Beck–Fiala theorem.* Combinatorics, Probability and Computing, 25(3):380–398, 2016.
- **[Survey]** J. Matoušek. *Geometric Discrepancy: An Illustrated Guide.* Springer, 1999 (Chapter 4).
- **[Survey]** B. Chazelle. *The Discrepancy Method: Randomness and Complexity.* Cambridge University Press, 2000.
- **[Survey]** J. Matoušek and A. Nikolov. *Combinatorial discrepancy for boxes via the $\gamma_2$ norm.* SoCG 2015; and W. Chen, A. Srivastava, G. Travaglini (eds.), *A Panorama of Discrepancy Theory*, Springer Lecture Notes in Mathematics 2107, 2014.

## 10. Worked Example / Concrete Special Case

**A lower bound of $\sqrt 2$ on the Komlós constant.** Take $d = n = 2$ and the normalized Hadamard columns
$$v_1 = \tfrac{1}{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix},\qquad v_2 = \tfrac{1}{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix},\qquad \|v_1\|_2=\|v_2\|_2=1 .$$
The four signings give $\pm(v_1+v_2) = \pm(\sqrt2, 0)^{\!\top}$ and $\pm(v_1-v_2) = \pm(0,\sqrt2)^{\!\top}$. Every outcome has $\ell_\infty$ norm exactly $\sqrt2$, so $\mathrm{disc} = \sqrt2$ and hence $K \ge \sqrt 2$. This is the best lower bound known; the general normalized Hadamard matrix $H_d/\sqrt d$ only reproduces $\mathrm{disc} \ge 1$, since $\|H_d\varepsilon\|_2/\sqrt d = \sqrt d$ forces just $\|\cdot\|_\infty \ge 1$.

**Why the trivial bound fails, and what Banaszczyk buys.** Take $d = n$ and $v_i = $ the $i$-th column of a matrix with entries $\pm 1/\sqrt{d}$ chosen i.i.d. uniformly. A *uniformly random* signing $\varepsilon$ gives each coordinate $(A\varepsilon)_j = \frac{1}{\sqrt d}\sum_i \pm 1$, a sum of $d$ independent signs scaled by $d^{-1/2}$: mean $0$, variance $1$. Hence
$$\Pr\big[|(A\varepsilon)_j| > \lambda\big] \le 2e^{-\lambda^2/2},\qquad \Pr\big[\|A\varepsilon\|_\infty > \lambda\big] \le 2d\,e^{-\lambda^2/2},$$
which is nontrivial only for $\lambda \gtrsim \sqrt{2\log d}$. This union bound *is* the $\sqrt{\log n}$ barrier: random colorings, and every known subgaussian coloring, stop exactly here. Banaszczyk's theorem recovers the same $O(\sqrt{\log d})$ by a different route (a Gaussian-measure induction), and Altschuler–Niles-Weed show that for this particular random instance the truth is $O(1)$ once $n \ge Cd\log d$ — but for $n=d$, and for worst-case $A$, closing the gap from $\sqrt{2\log d}$ to an absolute constant remains open.

**Beck–Fiala instance, $t=3$.** Let $\mathcal{S}$ be a $3$-regular set system on $[n]$: each element lies in exactly $3$ sets, so each column of the incidence matrix has $\|\cdot\|_2 = \sqrt3$. Beck–Fiala gives $\mathrm{disc}(\mathcal S) \le 2\cdot3-1 = 5$; Bukh's refinement gives $5 - \log^* 3$-type savings; Komlós would give $\mathrm{disc}(\mathcal S) \le K\sqrt3 \approx 1.73K$, and the conjectured truth for $3$-regular systems is $O(1)$ with a small constant. No proof of $\mathrm{disc}(\mathcal S)\le 4$ for all $3$-regular systems is known — the conjecture is open already at this smallest nontrivial parameter.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*