---
id: 04-topology/colored-jones-polynomial-stability
title: "Colored Jones Polynomial Stability"
topic: 04-topology
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Colored Jones Polynomial Stability

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/colored-jones-polynomial-stability` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $K \subset S^3$ be a knot (or link) and let $J_{K,n}(q) \in \mathbb{Z}[q^{\pm 1}]$ denote its colored Jones polynomial, normalized so that $J_{\text{unknot},n} = 1$ and $J_{K,2} = V_K$ is the Jones polynomial. Write $\hat{J}_{K,n}(q) \in \mathbb{Z}[[q]]$ for the polynomial rescaled by a monomial so that its lowest-order term is $+1$.

**Stability Conjecture (Garoufalidis).** For every knot $K$ the sequence $(\hat J_{K,n})_{n\ge 2}$ is *stable to all orders*: there exist series $\Phi_{K,j}(q) \in \mathbb{Z}[[q]]$, $j \ge 0$, with

$$\hat J_{K,n}(q) \;-\; \sum_{j=0}^{k} \Phi_{K,j}(q)\, q^{jn} \;=\; O\!\left(q^{(k+1)n}\right) \qquad \text{for every } k \ge 0 .$$

Equivalently, the two-variable generating series
$$F_K(x,q) \;=\; \sum_{j \ge 0} \Phi_{K,j}(q)\, x^{j} \;\in\; \mathbb{Z}[[q]][[x]]$$
exists. The $j=0$ case ($\Phi_{K,0} = \lim_n \hat J_{K,n}$ coefficientwise) is the **tail** of $K$; applying the same statement to the mirror image gives the **head**.

A complete resolution requires either (i) a proof of stability for all knots, together with a structural description of the $\Phi_{K,j}$ (conjecturally Nahm-type $q$-series with quantum-modular behaviour), or (ii) an explicit knot whose coefficient sequence provably fails to converge at some order $k$.

## 2. Mathematical Foundations

**Colored Jones.** For $U_q(\mathfrak{sl}_2)$ let $V_n$ be the irreducible module of dimension $n$. The invariant $J_{K,n}(q)$ is the Reshetikhin–Turaev invariant of $K$ colored by $V_n$, normalized by the quantum dimension $[n] = (q^{n/2}-q^{-n/2})/(q^{1/2}-q^{-1/2})$.

**$q$-series notation.** $(x;q)_k = \prod_{j=0}^{k-1}(1 - xq^{j})$, $(q)_k = (q;q)_k$, and $(q)_\infty = \prod_{j\ge1}(1-q^j) = \sum_{n\in\mathbb{Z}}(-1)^n q^{n(3n-1)/2}$ (Euler pentagonal number theorem).

**Habiro cyclotomic expansion** (Habiro 2008; Masbaum 2003). With
$$\sigma_k(n) \;=\; \prod_{j=1}^{k}\left(q^{n}+q^{-n}-q^{j}-q^{-j}\right),$$
every knot admits $J_{K,n}(q) = \sum_{k \ge 0} c_{K,k}(q)\,\sigma_k(n)$ with $c_{K,k} \in \mathbb{Z}[q^{\pm1}]$ independent of $n$. Since $\sigma_k(n) = 0$ for $k \ge n$, the sum is finite; the $q$-adic growth of $\sigma_k(n)$ is what makes stability plausible but does not prove it, because $c_{K,k}$ may carry unbounded negative powers of $q$.

**Degrees.** For a link with a reduced alternating diagram $D$ with $c$ crossings and $c_\pm$ positive/negative crossings, Kauffman-bracket state sums give
$$\deg_{\min} \hat J_{K,n} = 0, \qquad \operatorname{span} J_{K,n} \;=\; \tfrac{1}{2}(n-1)\big((n-1)c + 2\big)\ \ \text{(up to convention)},$$
so the polynomial's degree grows quadratically in $n$ while its low-order coefficients are conjecturally eventually constant.

**Stability, formally.** $K$ is *$0$-stable* if for each $m$ the coefficient $[q^m]\hat J_{K,n}$ is independent of $n$ for $n \gg m$. It is *$k$-stable* if the displayed identity of §1 holds. The natural target ring for $\Phi_{K,j}$ is the ring of **Nahm sums**
$$\sum_{v \in \mathbb{N}^{r}} \frac{(-1)^{\ell\cdot v}\, q^{\frac12 v^{T}Av + b\cdot v}}{(q)_{v_1}\cdots(q)_{v_r}}, \qquad A \in \mathbb{Q}^{r\times r} \text{ symmetric, positive semidefinite,}$$
which converge $q$-adically and specialize to Rogers–Ramanujan/Andrews–Gordon products.

**Adequacy.** A diagram is $A$-adequate (resp. $B$-adequate) if the all-$A$ (resp. all-$B$) Kauffman state has no self-touching loops; a link is *adequate* if some diagram is both. Reduced alternating diagrams are adequate. Adequacy is the combinatorial hypothesis under which the tail is currently controlled.

## 3. History & State of the Art (SOTA)

- **2006 — Dasbach–Lin.** *Compositio Math.* 142: for an alternating link the first three coefficients (and by mirror symmetry the last three) of $\hat J_{K,n}$ are independent of $n$ for $n\ge 3$, and $|\beta_2| = $ the twist number of the diagram. This is the birth of the "head and tail" question.
- **2011–2013 — Armond.** Proved existence of the tail ($0$-stability) for all $B$-adequate links, hence for all alternating links, using skein-theoretic manipulation of Jones–Wenzl projectors. *Algebr. Geom. Topol.* 13 (2013).
- **2011 — Armond–Dasbach.** The tail of an alternating link depends only on the reduced checkerboard (Tait) graph of the diagram; for $(2,p)$ torus knots and related families the tail reproduces Rogers–Ramanujan and Andrews–Gordon type identities.
- **2014 — Rozansky.** Categorified the tail: the Khovanov homology of the $n$-colored $B$-adequate link stabilizes as $n\to\infty$, giving a homological tail whose graded Euler characteristic is $\Phi_{K,0}$. *Quantum Topology* 5.
- **2015 — Garoufalidis–Le.** The decisive theorem: **every alternating link is stable to all orders**, with each $\Phi_{K,j}$ expressed as an explicit Nahm sum determined by the reduced Tait graph. *Res. Math. Sci.* 2, Art. 1.
- **2015–2017 — Garoufalidis–Vuong, Keilthy–Osburn, Beirne–Osburn.** Tables of tails for alternating knots to 10–12 crossings and new $q$-series identities extracted from them.
- **2021–2023 — Garoufalidis–Zagier.** Stability at $q\to 0$ is placed alongside the $q \to$ root-of-unity asymptotics (Volume Conjecture) inside a single conjectural quantum-modularity package for the "knot's $q$-series".

## 4. Partial Results / Verified Cases

| Class | Result | Source |
|---|---|---|
| Alternating links | Stable to **all orders** $k$; $\Phi_{K,j}$ are Nahm sums in $r \le$ (number of Tait-graph edges) variables | Garoufalidis–Le 2015 |
| $B$-adequate links (incl. non-alternating, e.g. many pretzel and Montesinos links) | $0$-stability (tail exists); higher orders open | Armond 2013; Rozansky 2014 |
| Alternating links, first 3 coefficients | Explicitly computed; $\beta_1 = 1$, $|\beta_2| = $ twist number | Dasbach–Lin 2006 |
| $(2,p)$ torus knots, $p$ odd | Tail $=(q)_\infty$; head/tail of $(2,p)$ families yield Andrews–Gordon identities of modulus $p$ | Armond–Dasbach 2011; Andrews 1974 |
| Alternating knots up to 10 crossings (and much of 11–12) | Tails identified with explicit modular/false-theta $q$-series | Garoufalidis–Vuong 2015; Keilthy–Osburn 2016 |
| Torus knots $T(2,p)$, twist knots | Habiro cyclotomic coefficients known in closed form, permitting direct verification of $k$-stability for small $k$ | Habiro 2008; Masbaum 2003 |
| Categorified level | Colored Khovanov homology of $B$-adequate links stabilizes | Rozansky 2014 |

No knot is known to violate $0$-stability. Stability to all orders is **unverified for any non-alternating knot family in full generality**, though it holds numerically in every computed case.

## 5. Principal Obstacles

- **Cancellation in state sums.** The Kauffman-bracket state sum for $\hat J_{K,n}$ has $2^{c(n-1)}$ terms; for alternating diagrams all contributions to the lowest coefficients carry the same sign, so counting arguments succeed. For a non-alternating diagram the all-$A$ state is no longer of extremal degree and terms of opposite sign compete: low-order coefficients are differences of exponentially large quantities, and no combinatorial model isolates the survivors.
- **Loss of positivity in the quadratic form.** Garoufalidis–Le's proof turns the state sum into a $q$-series $\sum_v (-1)^{\ell\cdot v}q^{Q(v)}/\prod(q)_{v_i}$ with $Q$ positive definite, which forces $q$-adic convergence. Non-adequate diagrams produce indefinite $Q$, for which the sum need not converge $q$-adically at all — the method does not merely weaken, it becomes inapplicable.
- **Habiro coefficients are not $q$-adically controlled.** Although $\sigma_k(n) = O(q^{?})$ in a useful range, $\min\deg\, c_{K,k}(q)$ can decrease with $k$ at an unknown rate. Bounding it is equivalent to bounding the "cyclotomic degree", an open problem in itself.
- **No intrinsic (diagram-free) definition of $\Phi_{K,j}$.** Every existing construction is diagrammatic; invariance under Reidemeister moves is proved only *a posteriori*. Without an intrinsic model (e.g. from the $3$D-index, Floer-type homology, or a categorified Jones–Wenzl projector for general links) there is nothing to induct on.
- **Higher orders are not a formal consequence of the tail.** $0$-stability gives no leverage on $\Phi_{K,1}$: the correction term $q^{n}$ makes the relevant window of coefficients drift with $n$, so any argument must be uniform in $n$, not term-by-term.

## 6. The Gap

Proven: (a) all-orders stability for **alternating** links, where the Tait graph supplies a positive-definite Nahm datum; (b) $0$-stability for **$B$-adequate** links, where the all-$B$ state is degree-extremal and sign-coherent.

Conjectured: stability for **all** knots, with no adequacy hypothesis.

The precise missing step is a $q$-adic convergence criterion for the colored Kauffman state sum of an arbitrary diagram — a replacement for positive-definiteness of the Nahm matrix that survives the sign cancellations of non-adequate crossings. Concretely: prove that $\min\deg_q c_{K,k}(q) \ge -\alpha k$ for some $\alpha < 2$ depending only on $K$ (which would deliver stability of every order from Habiro's expansion), or exhibit an intrinsic invariant whose $q$-expansion is $F_K(x,q)$ and whose existence is manifest. Even for $B$-adequate but non-$A$-adequate links, passing from $k=0$ to $k=1$ is unresolved.

## 7. Current Research (as of June 2026)

- **Nahm-sum / quantum-modularity school (Garoufalidis, Zagier, Gu, Mariño, Wheeler).** The series $\Phi_{K,j}$ are conjectured to be entries of a matrix of $q$-series $\widehat{\Phi}(q)$ attached to a knot, with a matching matrix at $q\to e^{2\pi i/\hbar}$ governed by state integrals of the Andersen–Kashaev/Teichmüller TQFT. Stability then becomes a corollary of the existence of that matrix. *(frontier — verify)*
- **Categorification (Rozansky, Hogancamp, Beliakova–Putyra–Wehrli).** Stable colored Khovanov and Khovanov–Rozansky homology, and categorified Jones–Wenzl projectors, aim at a homological proof of stability whose input is a limit of chain complexes rather than a coefficient count; extension beyond $B$-adequacy is the active target. *(frontier — verify)*
- **Skein-theoretic combinatorics (Hajij, Dasbach, Armond, and collaborators).** Bubble-skein and adequate-graph techniques to compute $\Phi_{K,1}$ for adequate links; partial results announced for the "second tail" of alternating links. *(frontier — verify)*
- **$q$-series identities (Osburn, Keilthy, Beirne, Hikami).** Extracting new Rogers–Ramanujan-type identities from tails of specific alternating families, and testing conjectural tails of non-alternating knots against $q$-hypergeometric candidates.
- **Computation.** Garoufalidis–Koutschan-style $q$-holonomic recursions (the "$\hat{A}$-polynomial") are used to generate $\hat J_{K,n}$ for $n$ up to ~30 on 12–14 crossing knots, giving strong numerical evidence for stability of non-alternating knots. *(frontier — verify)*

## 8. Future Work

- Prove $1$-stability for all $B$-adequate links; this is the smallest genuinely new case and would test whether skein methods scale in $k$.
- Formulate stability for the whole $q$-holonomic sequence: show that any solution of a $q$-difference equation with suitable Newton-polygon data is automatically stable, converting a topological statement into one about $q$-difference modules.
- Identify $F_K(x,q)$ with a generating function of the $3$D-index of an ideal triangulation of $S^3 \setminus K$ (Dimofte–Gaiotto–Gukov / Garoufalidis–Hodgson–Rubinstein–Tillmann); this would give an intrinsic, diagram-free construction.
- Extend to $\mathfrak{sl}_N$ and to HOMFLY-PT colored by arbitrary Young diagrams, where stability should interact with refined topological-vertex formulas.
- Determine which $q$-series arise as tails: is the map $K \mapsto \Phi_{K,0}$ surjective onto some identifiable class of false-theta/modular objects, and what is its fiber?

## 9. Key References

- **[Foundational]** O. Dasbach, X.-S. Lin. *On the head and the tail of the colored Jones polynomial.* Compositio Mathematica 142 (2006), 1332–1342.
- **[Foundational]** K. Habiro. *A unified Witten–Reshetikhin–Turaev invariant for integral homology spheres.* Inventiones Mathematicae 171 (2008), 1–81.
- **[Foundational]** G. Masbaum. *Skein-theoretical derivation of some formulas of Habiro.* Algebraic & Geometric Topology 3 (2003), 537–556.
- **[SOTA]** S. Garoufalidis, T. T. Q. Le. *Nahm sums, stability and the colored Jones polynomial.* Research in the Mathematical Sciences 2 (2015), Article 1.
- **[SOTA]** C. Armond. *The head and tail conjecture for alternating knots.* Algebraic & Geometric Topology 13 (2013), 2809–2826.
- **[SOTA]** L. Rozansky. *Khovanov homology of a unicolored B-adequate link has a tail.* Quantum Topology 5 (2014), 541–579.
- **[SOTA]** C. Armond, O. Dasbach. *Rogers–Ramanujan type identities and the head and tail of the colored Jones polynomial.* arXiv:1106.3948 (2011).
- **[Recent]** S. Garoufalidis, T. Vuong. *Alternating knots, planar graphs, and q-series.* The Ramanujan Journal 36 (2015), 501–527.
- **[Recent]** M. Hajij. *The tail of a quantum spin network.* The Ramanujan Journal 40 (2016), 135–176.
- **[Recent]** A. Keilthy, R. Osburn. *Rogers–Ramanujan type identities for alternating knots.* Journal of Number Theory 161 (2016), 255–280.
- **[Recent]** P. Beirne, R. Osburn. *q-series and tails of colored Jones polynomials.* Indagationes Mathematicae 28 (2017), 647–660.
- **[Context]** D. Zagier. *Vassiliev invariants and a strange identity related to the Dedekind eta-function.* Topology 40 (2001), 945–960.
- **[Context]** G. E. Andrews. *An analytic generalization of the Rogers–Ramanujan identities for odd moduli.* PNAS 71 (1974), 4082–4085.
- **[Survey]** W. B. R. Lickorish. *An Introduction to Knot Theory.* Graduate Texts in Mathematics 175, Springer, 1997.
- **[Survey]** S. Garoufalidis, D. Zagier. *Knots and their related $q$-series.* SIGMA 19 (2023), 082.

## 10. Worked Example / Concrete Special Case

**The trefoil $3_1 = T(2,3)$.** Habiro's expansion has $c_{3_1,k}(q) = (-1)^k q^{-k(k+3)/2}$, so
$$J_{3_1,n}(q) \;=\; \sum_{k\ge 0} (-1)^k q^{-k(k+3)/2} \prod_{j=1}^{k}\left(q^{n}+q^{-n}-q^{j}-q^{-j}\right).$$

**$n=2$.** Here $\sigma_1(2) = q^2+q^{-2}-q-q^{-1}$ and $\sigma_2(2)=0$, so
$$J_{3_1,2} = 1 - q^{-2}\sigma_1(2) = -q^{-4}+q^{-3}+q^{-1},$$
the Jones polynomial of the left-handed trefoil. (Check: setting $q=1$ gives $1$.)

**$n=3$.** Now $\sigma_1(3)=q^3+q^{-3}-q-q^{-1}$, $\sigma_2(3)=\sigma_1(3)\,(q^3+q^{-3}-q^2-q^{-2})$, $\sigma_3(3)=0$. Expanding,
$$\sigma_2(3) = q^{6}-q^{5}-q^{4}+q^{3}-q^{2}+2-q^{-2}+q^{-3}-q^{-4}-q^{-5}+q^{-6},$$
$$J_{3_1,3} = 1 - q^{-2}\sigma_1(3) + q^{-5}\sigma_2(3) \;=\; q^{-2}+q^{-5}-q^{-7}+q^{-8}-q^{-9}-q^{-10}+q^{-11}.$$
Again the coefficients sum to $1$ at $q=1$.

**Reading off the stable end.** Mirror to the right-handed trefoil ($q\mapsto q^{-1}$) and normalize the *top* coefficient to $+1$, then reverse the variable so the stable end sits at $q^0$:

| $n$ | normalized series | coefficients $(q^0,q^1,q^2,q^3,\dots)$ |
|---|---|---|
| $2$ | $1-q-q^{3}$ | $1,\,-1,\,0,\,-1$ |
| $3$ | $1-q-q^{2}+q^{3}-q^{4}+q^{6}$ | $1,\,-1,\,-1,\,+1,\,-1,\,0,\,+1$ |

The two agree through order $q^{1}$; the $n=3$ series agrees through order $q^{2}$ with
$$\Phi_{3_1,0}(q) \;=\; (q;q)_\infty \;=\; 1-q-q^{2}+q^{5}+q^{7}-q^{12}-q^{15}+\cdots,$$
which is the head of the trefoil predicted by Armond–Dasbach. The pattern — the $n$-th normalized polynomial matching $\Phi_0$ through degree $n-1$ — is exactly $0$-stability. Higher-order stability asserts that the *discrepancy* starting at degree $\sim n$, after dividing by $q^{n}$, itself converges to a second series $\Phi_{3_1,1}(q)$, and so on; for the trefoil (alternating) all of these exist and are Nahm sums by Garoufalidis–Le, while for a non-adequate knot such as $8_{19}=T(3,4)$ or the Kinoshita–Terasaka knot the same statement is only observed numerically.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*