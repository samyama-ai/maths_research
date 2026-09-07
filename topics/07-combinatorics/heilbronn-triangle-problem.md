---
id: 07-combinatorics/heilbronn-triangle-problem
title: "Heilbronn Triangle Problem"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Heilbronn Triangle Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/heilbronn-triangle-problem` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Place $n \ge 3$ points in the closed unit square $[0,1]^2$. Every choice of three of them spans a triangle; let the *value* of the configuration be the area of its smallest triangle. Define

$$\Delta(n) \;=\; \sup_{p_1,\dots,p_n \in [0,1]^2} \;\; \min_{1 \le i < j < k \le n} \operatorname{area}\bigl(\triangle p_i p_j p_k\bigr).$$

**Problem (Heilbronn, c. 1948).** Determine the asymptotic growth of $\Delta(n)$.

Heilbronn conjectured $\Delta(n) = O(n^{-2})$; Erdős conjectured the matching order $\Delta(n) = \Theta(n^{-2})$. The lower-bound half of that conjecture is **false**: $\Delta(n) = \Omega(n^{-2}\log n)$. The problem is therefore now: pin down the exponent $\gamma = \lim -\log \Delta(n)/\log n$, if it exists, and ideally the exact order.

A complete solution requires matching upper and lower bounds up to constants (or up to $n^{o(1)}$ for the weaker "exponent" version). Current knowledge:

$$c\,\frac{\log n}{n^{2}} \;\le\; \Delta(n) \;\le\; n^{-8/7 - 1/2000} \quad (n \text{ large}),$$

a gap of nearly a full power of $n$ in the exponent ($1.143$ vs. $2$).

## 2. Mathematical Foundations

**Area functional.** For $p_i=(x_i,y_i)$,

$$\operatorname{area}(\triangle p_1p_2p_3) = \tfrac12\bigl|\det M\bigr|, \qquad M=\begin{pmatrix} x_2-x_1 & y_2-y_1 \\ x_3-x_1 & y_3-y_1\end{pmatrix}.$$

Equivalently $\operatorname{area} = \tfrac12 \,\lVert p_2-p_3\rVert \cdot d(p_1, \ell_{23})$, where $\ell_{23}$ is the line through $p_2,p_3$. This second form is what drives every upper-bound proof: small area means *near-collinearity*, quantified by distance to a line.

**Affine invariance.** $\Delta(n)$ is unchanged, up to a constant factor, if $[0,1]^2$ is replaced by any convex body $K$ of area $1$: an affine map $T$ with $|\det T| = 1$ preserves areas, and John's theorem gives bounded distortion between $K$ and a square. So the problem is genuinely about affine plane geometry, not about the square.

**Strip / cylinder formulation.** Fix $\delta>0$. For a pair $(p_j,p_k)$ at distance $r$, the set of points $q$ with $\operatorname{area}(\triangle q p_j p_k) < \delta$ is the open strip
$$S_{jk}(\delta) = \{q : d(q,\ell_{jk}) < 2\delta/r\},$$
of width $4\delta/r$. A configuration certifies $\Delta(n)\ge\delta$ iff no point lies in the strip of any other pair. Counting the total measure of $\binom n2$ such strips gives the trivial bound $\Delta(n) = O(1/n)$, since $\sum_{j<k} 4\delta/r_{jk} \ge 1$ forces $\delta \gtrsim 1/n^2 \cdot \min r$ — and after discarding close pairs, $\delta = O(1/n)$.

**Roth's amplification.** Roth's method replaces this first-moment count with a second-moment estimate on the number of point pairs inside thin strips, plus a *pigeonhole on directions*: partition directions into $\approx n^{\alpha}$ angular sectors and study, for each sector, the induced one-dimensional projection $\pi_\theta(p_i)$. If $\Delta(n)\ge\delta$, then for each $\theta$ the projected points cannot be too clustered relative to their transverse spread — a Fourier/orthogonality argument on the projection measures $\mu_\theta = \sum_i \delta_{\pi_\theta(p_i)}$ then bounds $\delta$.

**Random-model heuristic.** For $n$ i.i.d. uniform points, the minimum triangle area is $\Theta(n^{-3})$ in probability (Jiang–Li–Vu, 2002): $\mathbb P[\min \text{area} \le t/n^3] \to 1-e^{-2t}$ roughly. Deleting one point from each "bad" triple in a random sample is exactly the deletion argument that yields the $\Omega(n^{-2})$ and $\Omega(n^{-2}\log n)$ lower bounds.

## 3. History & State of the Art (SOTA)

- **c. 1948** — Hans Heilbronn poses the question to Roth at Bristol; conjectures $\Delta(n)=O(n^{-2})$.
- **1951** — K. F. Roth proves the first nontrivial bound $\Delta(n) = O\!\left(n^{-1}(\log\log n)^{-1/2}\right)$, i.e. $\Delta(n)=o(1/n)$.
- **1972–1976** — Roth and W. M. Schmidt break the exponent $1$ barrier: Roth (1972) $O(n^{-1.105\ldots})$, Schmidt (1972) $O(n^{-1.1})$, Roth (1973, 1976) pushes the exponent to about $1.117$.
- **1981** — Komlós, Pintz and Szemerédi prove $\Delta(n) = O(n^{-8/7+\varepsilon})$ for every $\varepsilon>0$. This stood as the record for **42 years**.
- **1982** — The same three authors *disprove* Erdős's conjectured order from below: a random-plus-deletion argument on a carefully weighted independent-set problem in a $3$-uniform hypergraph gives $\Delta(n) = \Omega(n^{-2}\log n)$.
- **1997–2000** — Bertram-Kretzberg, Hofmeister and Lefmann derandomize: a deterministic polynomial-time algorithm outputs $n$ points with minimum triangle area $\Omega(n^{-2}\log n)$.
- **2023–2025** — Cohen, Pohoata and Zakharov obtain the first improvement on the Komlós–Pintz–Szemerédi exponent: $\Delta(n) \le n^{-8/7-1/2000}$ for large $n$.

**Computational strand.** Goldberg (1972) gave explicit optimal-looking configurations for $n \le 16$; later work by Comellas–Yebra (2002), Dress–Yang (2002) and Cantrell improved several of these, showing Goldberg's conjectured optima were not always correct. Exact optimality proofs (with algebraic-number values) exist only for very small $n$.

## 4. Partial Results / Verified Cases

**Exact small values.** Proven optimal values include
$$\Delta(3)=\tfrac12,\quad \Delta(4)=\tfrac13,\quad \Delta(5)=\tfrac{1}{3\sqrt3}=0.19245\ldots,\quad \Delta(6)=\tfrac18 .$$
For $n=7$ the optimum is the algebraic number $0.083859\ldots$, a root of an explicit polynomial, established by Yang, Zhang and Zeng with computer-assisted exact-arithmetic case analysis. For $8 \le n \le 16$ only rigorous *lower* bounds from explicit constructions plus numerically-supported optimality claims are available (Goldberg; Comellas–Yebra; Dress–Yang).

**Asymptotic lower bounds (constructive).**
- Erdős: taking $n=p$ prime and $p_i = (i/p, (i^2 \bmod p)/p)$ gives minimum area $\ge \tfrac{1}{2p^2}$, so $\Delta(n) = \Omega(n^{-2})$ for all $n$ (fill in between primes by Bertrand).
- Komlós–Pintz–Szemerédi (1982): $\Delta(n) \ge c\,n^{-2}\log n$, non-constructive; made constructive and polynomial-time by Bertram-Kretzberg–Hofmeister–Lefmann (2000).

**Asymptotic upper bounds.** $O(n^{-8/7+\varepsilon})$ (KPS 1981), improved to $n^{-8/7-1/2000}$ (Cohen–Pohoata–Zakharov). Both are unconditional for all sufficiently large $n$.

**Solved variants.**
- *Random points*: minimum triangle area of $n$ uniform i.i.d. points is $\Theta(n^{-3})$ with an explicit limit distribution (Jiang–Li–Vu, 2002). This settles the "typical" case completely.
- *Higher dimensions / larger simplices*: for the analogous problem with $k$-point simplices in $[0,1]^d$, Lefmann established lower bounds of the form $\Omega\!\left(n^{-(k-1)/(d-k+2)} (\log n)^{1/(d-k+2)}\right)$ in several ranges; the $d$-dimensional simplex analogue has lower bound $\Omega(n^{-d}\log n)$.
- *Convex position*: if the $n$ points are required to be in convex position, the answer degrades and is known to order $\Theta(1/n^{3})$-type behaviour for related "smallest triangle among consecutive points" formulations — a genuinely easier, structured sub-case.

## 5. Principal Obstacles

**Upper bound side.** Roth-type arguments are *local averaging* arguments: they bound the number of triples that are "almost collinear at a given scale and direction", then sum over dyadic scales. The loss is that a configuration could, in principle, concentrate its near-collinearity at *many different scales simultaneously*, and the union bound over $\log n$ scales plus the sector decomposition costs powers of $n$. Fourier analysis of the projections $\mu_\theta$ controls only the $L^2$ behaviour; the extremal configurations that the analysis cannot rule out are highly non-uniform and are not known to exist, so the argument is bounding an *empty* set inefficiently. There is no known "structure theorem" saying that a configuration with many small triangles must contain a large collinear or near-collinear subset — the natural analogue of Szemerédi–Trotter incidence theory fails because near-collinearity at scale $\delta$ is not a transitive or matroid-like relation.

**Lower bound side.** The only known method is *random construction plus deletion* on the $3$-uniform hypergraph $H_\delta$ whose edges are triples of small area. Independent-set bounds in hypergraphs with a bounded-degree-type condition (Ajtai–Komlós–Pintz–Spencer–Szemerédi) give exactly one logarithmic factor over the trivial bound; extracting more requires exploiting the *geometry* of $H_\delta$ (its edges are not arbitrary), and no one has found a usable geometric property beyond "few triples per pair". Algebraic constructions (Erdős's parabola, Sidon-set variants, projective planes) plateau at $\Theta(n^{-2})$ because they come from a $\bmod\ p$ nondegeneracy that gives determinant $\ge 1$ and no more.

**Meta-obstacle.** Nobody knows which side is closer to the truth. Expert opinion is split between $\Delta(n)=n^{-2+o(1)}$ and $\Delta(n)=n^{-\gamma}$ for some $\gamma$ strictly between $8/7$ and $2$, which means there is no agreed target for a construction.

## 6. The Gap

Proven: $n^{-2}\log n \lesssim \Delta(n) \le n^{-8/7-1/2000}$. The exponent gap is
$$2 - \left(\tfrac87 + \tfrac1{2000}\right) \approx 0.857 .$$

The precise barrier is a missing **inverse theorem**: given $n$ points in $[0,1]^2$ with all triangles of area $\ge \delta$, deduce a structural statement strong enough to iterate. KPS's argument extracts, from a hypothetical good configuration, a subconfiguration that is uniform at one scale; the loss of $n^{1/7}$ against the conjectural truth is exactly the cost of not being able to *recurse* — to say the uniform subconfiguration is again a Heilbronn configuration in a smaller square and apply the bound self-similarly. Cohen–Pohoata–Zakharov recovered a $1/2000$ sliver of this by a partial recursion; a full self-improving scheme would plausibly give $n^{-3/2}$ or better, and is the identified next milestone.

## 7. Current Research (as of June 2026)

- **The Cohen–Pohoata–Zakharov programme.** Their proof combines the KPS machinery with cell decompositions in the style of polynomial partitioning and a new estimate on triples with small area lying in thin tubes. Current work asks whether the argument can be made *self-improving* so that $\delta$ appearing in $n^{-8/7-\delta}$ can be bootstrapped, or whether $8/7$ is a genuine barrier for tube-based methods. *(frontier — verify)*
- **Additive-combinatorial reformulations.** Groups at Cambridge, IAS/Princeton and MIT have studied whether small-area triples can be encoded as solutions to a translation-invariant equation, opening the door to higher-order Fourier analysis. No exponent improvement has come from this route yet. *(frontier — verify)*
- **Lower-bound side.** Attempts to beat $n^{-2}\log n$ focus on hypergraph containers and on algebraic constructions over $\mathbb F_p$ with extra multiplicative structure (Sidon sets, higher-degree curves). Nothing beyond a $\log$ factor is currently claimed.
- **Computation.** Continued numerical optimization (simulated annealing, semidefinite relaxations) for $17 \le n \le 40$, aimed at guessing whether optimal configurations look "random-like" ($n^{-2}$) or "algebraic". Configurations up to $n \approx 20$ look grid- and lattice-flavoured, weak evidence for $n^{-2+o(1)}$.

## 8. Future Work

1. **Build the recursion.** Formalize "a Heilbronn configuration restricted to a subsquare, rescaled, is again a Heilbronn configuration" with controlled parameter loss; a clean version would immediately push the exponent well past $8/7$.
2. **Prove or refute $\Delta(n) = n^{-2+o(1)}$.** Erdős's problem list and Guy's *Unsolved Problems in Number Theory* single this out as the decisive question.
3. **Find an inverse theorem for small-area triples**: characterize point sets in which $\Omega(n^3)$ triples have area $\le \delta$. This is the geometric analogue of the Balog–Szemerédi–Gowers theorem and is the most-requested missing tool.
4. **Constructive lower bounds beyond $\log n$.** Even $\Omega(n^{-2}(\log n)^{1+\epsilon})$ would be the first improvement since 1982.
5. **Higher-dimensional transfer.** Determine whether the $d$-dimensional simplex problem is easier — its extra degrees of freedom may make an inverse theorem accessible, and a proof there could be pulled back to $d=2$.

## 9. Key References

- **[Foundational]** K. F. Roth. *On a problem of Heilbronn.* Journal of the London Mathematical Society, 26 (1951), 198–204.
- **[Foundational]** K. F. Roth. *On a problem of Heilbronn, II* and *III.* Proceedings of the London Mathematical Society, 25 (1972), 193–212 and 543–549.
- **[Foundational]** W. M. Schmidt. *On a problem of Heilbronn.* Journal of the London Mathematical Society, 4 (1972), 545–550.
- **[Foundational]** J. Komlós, J. Pintz, E. Szemerédi. *On Heilbronn's triangle problem.* Journal of the London Mathematical Society, 24 (1981), 385–396.
- **[Foundational]** J. Komlós, J. Pintz, E. Szemerédi. *A lower bound for Heilbronn's problem.* Journal of the London Mathematical Society, 25 (1982), 13–24.
- **[SOTA / Recent]** A. Cohen, C. Pohoata, D. Zakharov. *A new upper bound for the Heilbronn triangle problem.* arXiv:2305.18253 (2023); Journal of the American Mathematical Society (2025).
- **[SOTA / Recent]** C. Bertram-Kretzberg, T. Hofmeister, H. Lefmann. *An algorithm for Heilbronn's problem.* SIAM Journal on Computing, 30 (2000), 383–390.
- **[SOTA / Recent]** T. Jiang, M. Li, V. Vu. *The asymptotic probability distribution of the smallest triangle.* (On the smallest triangle determined by random points), Journal of Applied Probability / related venue, 2002.
- **[Computational]** M. Goldberg. *Maximizing the smallest triangle made by $N$ points in a square.* Mathematics Magazine, 45 (1972), 135–144.
- **[Computational]** F. Comellas, J. Yebra. *Optimal configurations for the Heilbronn triangle problem.* Journal of Combinatorial Theory / electronic journals of combinatorics-style venue, 2002.
- **[Survey]** R. K. Guy. *Unsolved Problems in Number Theory*, 3rd ed., Springer, 2004 (Problem F4).
- **[Survey]** P. Brass, W. Moser, J. Pach. *Research Problems in Discrete Geometry.* Springer, 2005 (Chapter on area problems).

## 10. Worked Example / Concrete Special Case

**Erdős's parabola construction with $p=5$.** Take the $p$ points
$$P_i = \left(\frac{i}{p}, \frac{i^2 \bmod p}{p}\right), \qquad i = 0,1,\dots,p-1 .$$
For $p=5$: $(0,0), (\tfrac15,\tfrac15), (\tfrac25,\tfrac45), (\tfrac35,\tfrac45), (\tfrac45,\tfrac15)$.

**Claim.** Every triangle has area $\ge \dfrac{1}{2p^2}$.

*Proof.* Let $Q_i = (i, i^2 \bmod p)$ be the unscaled integer points, so $P_i = Q_i/p$ and areas scale by $1/p^2$. For $i<j<k$,
$$2\operatorname{area}(\triangle Q_iQ_jQ_k) = \bigl| (j-i)(y_k-y_i) - (k-i)(y_j-y_i) \bigr| =: D,$$
an **integer**. Reducing mod $p$ and using $y_i \equiv i^2$,
$$D \equiv (j-i)(k^2-i^2) - (k-i)(j^2-i^2) = (j-i)(k-i)(k-j) \pmod p .$$
Since $0 \le i<j<k \le p-1$, each factor is a nonzero residue mod $p$, and $p$ is prime, so $D \not\equiv 0 \pmod p$. Hence $D \ne 0$, so $D \ge 1$ and $\operatorname{area}(\triangle Q_iQ_jQ_k)\ge \tfrac12$. Rescaling, $\operatorname{area}(\triangle P_iP_jP_k) \ge \tfrac{1}{2p^2}$. $\square$

**Numerical check ($p=5$).** For $Q_1=(1,1), Q_2=(2,4), Q_3=(3,4)$:
$$D = |(2-1)(4-1) - (3-1)(4-1)| = |3-6| = 3 \Rightarrow \text{area} = \frac{3}{2\cdot 25}=0.06 .$$
For $Q_0=(0,0), Q_1=(1,1), Q_4=(4,1)$: $D=|1\cdot 1 - 4\cdot 1|=3$, area $0.06$. The minimum over all $\binom53=10$ triples is attained with $D=1$, giving $\tfrac{1}{50}=0.02$.

**Comparison.** The true optimum is $\Delta(5)= \tfrac{1}{3\sqrt3}=0.1925$, achieved by a regular-pentagon-like configuration — about $10\times$ better than the algebraic construction at $n=5$. This is the point of the example: the parabola construction is asymptotically correct in *order* ($\Omega(n^{-2})$) but badly suboptimal in *constant*, and no algebraic family is known that improves the order. Meanwhile the Cohen–Pohoata–Zakharov upper bound at, say, $n=10^6$ permits areas up to $\approx 10^{-6.86}$, whereas this construction only guarantees $5\times10^{-13}$ — the seven-order-of-magnitude picture of the exponent gap described in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*