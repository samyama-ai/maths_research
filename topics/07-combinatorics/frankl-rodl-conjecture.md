---
id: 07-combinatorics/frankl-rodl-conjecture
title: "Frankl-Rödl Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Frankl–Rödl Conjecture (Forbidden Intersections and Forbidden Distances)

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/frankl-rodl-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Frankl and Rödl (*Forbidden intersections*, Trans. AMS 1987) proved that forbidding a **single** intersection size, or a **single** Hamming distance, forces exponential loss in the size of a family. They asked and conjectured that the same principle holds far beyond the range their method reached. Three statements form the "Frankl–Rödl conjecture" cluster:

**(C1) $q$-ary codes.** Fix an integer $q\ge 2$ and $0<\gamma<1$. There is $\epsilon=\epsilon(q,\gamma)>0$ such that any $\mathcal C\subseteq[q]^n$ with
$$d_H(x,y)\ne \gamma n \quad\text{for all } x\ne y\in\mathcal C$$
satisfies $|\mathcal C|\le (q-\epsilon)^n$ (for $n$ large, $\gamma n$ an integer, and $\gamma n$ even when $q=2$). Frankl–Rödl proved $q=2$; $q\ge 3$ was their question.

**(C2) Permutations.** Fix $0<\gamma<1$. Any $\mathcal A\subseteq S_n$ with no two permutations at Hamming distance exactly $\gamma n$ (i.e. differing in exactly $\gamma n$ points) satisfies $|\mathcal A|\le e^{-\epsilon n}\,n!$ — a conjecture of Frankl–Deza type restated by Frankl and Rödl.

**(C3) Uniform set families, full range.** For $\mathcal F\subseteq\binom{[n]}{k}$ with $|A\cap B|\ne\ell$ for all $A,B\in\mathcal F$, the exponential bound should persist when $\ell$ is *not* a positive proportion of $n$ — in particular the **Erdős–Sós** case $\ell=t-1$ with $k=\Theta(n)$, where the conjectured exact bound is $|\mathcal F|\le\binom{n-t}{k-t}$-type (attained by $\{A:\ |A\cap T|\ge t+1\}$-style constructions).

A complete resolution means: proofs valid for the whole parameter range, or a counterexample family exceeding the bound for some admissible $(q,\gamma)$ or $(k,\ell)$.

## 2. Mathematical Foundations

Work in the Hamming cube $\{0,1\}^n$ with $d_H(x,y)=|\{i:x_i\ne y_i\}|$, and in the Johnson scheme $\binom{[n]}{k}$, where for $A,B\in\binom{[n]}{k}$, $d_H(\mathbf 1_A,\mathbf 1_B)=2(k-|A\cap B|)$. So "forbidden intersection $\ell$" and "forbidden distance $2(k-\ell)$" are the same constraint.

**Frankl–Rödl theorem (1987).** For every $\eta>0$ there is $\delta>0$ such that if $\ell$, $k-\ell$ and $n-2k+\ell$ are all $\ge\eta n$, then every $\ell$-avoiding $\mathcal F\subseteq\binom{[n]}{k}$ obeys
$$|\mathcal F|\le (1-\delta)^n\binom{n}{k}.$$
Cube form: for fixed $0<\gamma<1$ with $\gamma n$ even, $\mathcal F\subseteq\{0,1\}^n$ avoiding distance $\gamma n$ has $|\mathcal F|\le(2-\delta)^n$.

**Frankl–Rödl graph.** $G_{n,\gamma}$ has vertex set $\{0,1\}^n$ and $xy\in E$ iff $d_H(x,y)=\gamma n$. The theorem says $\alpha(G_{n,\gamma})\le(2-\delta)^n$, hence
$$\chi(G_{n,\gamma})\ \ge\ \frac{2^n}{\alpha(G_{n,\gamma})}\ \ge\ (1+\delta')^n .$$

**Spectral background.** $G_{n,\gamma}$ lies in the Hamming association scheme; its eigenvalues are Krawtchouk polynomials
$$K_d(i)=\sum_{j}(-1)^j\binom{i}{j}\binom{n-i}{d-j},\qquad d=\gamma n .$$
The Hoffman ratio bound gives $\alpha\le N\frac{-\lambda_{\min}}{\lambda_{\max}-\lambda_{\min}}$, but $K_{\gamma n}$ oscillates and the resulting bound is only exponentially weak in general — the reason purely spectral methods do not deliver (C1)–(C3).

**Comparison point.** The Frankl–Wilson theorem (1981) gives the analogous exponential bound when $\ell$ is a prime power constraint via linear algebra over $\mathbb F_p$; it is sharper but rigid in the allowed $(k,\ell)$.

## 3. History & State of the Art (SOTA)

- **1981.** Frankl–Wilson prove modular intersection theorems with geometric consequences (chromatic number of $\mathbb R^n$, Borsuk).
- **1985/87.** Frankl and Rödl develop a delicate iterated random-partition ("nibble"-flavoured) probabilistic argument and prove the binary cube and proportional-parameter set versions. They explicitly raise the $q$-ary and permutation analogues.
- **1993.** Kahn and Kalai use Frankl–Wilson-type bounds to disprove Borsuk's conjecture, cementing forbidden-intersection theorems as a central tool.
- **2000s.** Frankl–Rödl graphs become standard hard instances in approximation theory: integrality gaps for vertex cover / independent set and limits of SDP and sum-of-squares relaxations (Bansal–Khot; Kauers–O'Donnell–Tan–Zhou).
- **2017.** Keevash and Long, *Frankl–Rödl type theorems for codes and permutations* (Trans. AMS), give a new proof of the cube theorem and settle (C1) for all $q\ge2$, $0<\gamma<1$, and (C2) for permutations.
- **2019–2024.** The "junta method" and "spread approximation" machinery (Keller–Lifshitz; Ellis–Keller–Lifshitz; Kupavskii–Zakharov) push the uniform-family case (C3) into the sparse regime and prove exact extremal results, including the Erdős–Sós forbidden-one-intersection conjecture for $k<cn$.

**SOTA summary:** the qualitative conjectures (C1), (C2) are theorems; (C3) is proven in wide ranges with exact extremal families, and open only in residual regimes and for optimal constants.

## 4. Partial Results / Verified Cases

| Regime | Status | Source |
|---|---|---|
| $q=2$, fixed $0<\gamma<1$, $\gamma n$ even | Proved | Frankl–Rödl 1987 |
| $\binom{[n]}{k}$ with $\ell,\,k-\ell,\,n-2k+\ell\ge\eta n$ | Proved | Frankl–Rödl 1987 |
| $[q]^n$, all $q\ge3$, all fixed $0<\gamma<1$ | Proved | Keevash–Long 2017 |
| $S_n$, forbidden distance $\gamma n$ | Proved, $|\mathcal A|\le e^{-\epsilon n}n!$ | Keevash–Long 2017 |
| $\ell$ fixed, $n$ huge relative to $k$ | Exact bound $\binom{n-t}{k-t}$-type | Frankl–Füredi 1985 ($\Delta$-system method) |
| $\ell=t-1$, $k<cn$ for an absolute $c>0$, $n$ large | Exact bound + stability | Ellis–Keller–Lifshitz 2024 |
| $t$-intersecting analogues, $k=o(n)$ | Junta structure theorems | Keller–Lifshitz 2021 |
| Sparse/large-$\ell$ ranges via spread approximations | Near-optimal bounds | Kupavskii–Zakharov 2024 |
| Small cases ($n\le 6$, $\gamma n=2$) | Exact $\alpha(G_{n,\gamma})$ by eigenvalue/ILP computation | folklore; see §10 |

## 5. Principal Obstacles

- **Spectral methods saturate.** The Krawtchouk eigenvalue $K_{\gamma n}(i)$ oscillates in sign and has magnitude comparable to $\binom{n}{\gamma n}$ for many $i$, so the ratio bound loses an exponential factor. The Delsarte linear programming relaxation of the forbidden-distance problem has an integrality gap: LP-feasible profiles exist well above the truth.
- **Linear algebra needs arithmetic.** The Frankl–Wilson polynomial method requires $\ell$ (or $k-\ell$) to sit in a prescribed residue class mod a prime power. Generic $\gamma n$ has no such structure, and there is no known way to interpolate between primes without losing the exponential gain.
- **No product structure to iterate.** Forbidding one distance is not a "local" constraint: the family of admissible sets is not closed under coordinate restriction, so tensorization/hypercontractivity arguments (which handle $t$-intersecting *inequalities* well) do not apply directly to an *equality* constraint.
- **Degenerate ranges.** When $\ell=o(n)$ or $k-\ell=o(n)$ the extremal example changes character — from "pseudorandom, exponentially small" to "junta: determined by a bounded set of coordinates". Any single argument must handle both phases, and the transition point is where all classical machinery is weakest.
- **Constants.** Frankl–Rödl's $\delta(\gamma)$ is not explicit and is far from the conjectured truth; applications in hardness of approximation need the exact exponent, which the probabilistic proof cannot supply.

## 6. The Gap

What is proven is *qualitative*: for each fixed $(q,\gamma)$ or proportional $(k,\ell)$, some $\epsilon>0$ exists. What remains:

1. **Uniform and explicit dependence.** Determine the optimal $\epsilon(q,\gamma)$, in particular whether $\epsilon(\gamma)\to0$ polynomially or exponentially as $\gamma\to0$, and whether $\epsilon$ can be taken uniform for $\gamma$ ranging over an interval with $\gamma n$ integral.
2. **Sub-linear parameters.** Extend (C3) to $\ell$ and $k$ where $\ell=o(n)$ with $k=\Theta(n)$ — the range not covered either by $\Delta$-system arguments ($n\gg k$) or by the proportional Frankl–Rödl hypothesis.
3. **Exact extremal families.** Replace $(1-\delta)^n\binom nk$ with the conjectured exact optimum and its uniqueness/stability for the entire admissible range, currently known only for $k<cn$.
4. **Effective independence numbers.** Compute $\alpha(G_{n,\gamma})$ up to sub-exponential factors — the missing input for tight SOS/LP integrality-gap statements.

## 7. Current Research (as of June 2026)

- **Junta method school** (Keller, Lifshitz, Ellis, Long, and collaborators, Bar-Ilan / Oxford / HUJI): structure-vs-randomness dichotomies for hypergraph families; the goal is a single framework proving exact forbidden-intersection theorems across all $k=\Theta(n)$ regimes.
- **Spread approximations** (Kupavskii, Zakharov, and the Moscow/Lausanne circle): approximating an arbitrary family by a bounded list of spread families, then applying Frankl-type shifting. This has produced the cleanest known proofs of Frankl–Rödl bounds in sparse ranges. *(frontier — verify: claims of near-optimal constants for $\ell$ close to $k$.)*
- **Analytic/hypercontractive approaches** on the symmetric group and on $[q]^n$, aiming to recover Keevash–Long with explicit constants.
- **Theoretical CS side** (Weizmann, CMU, NYU): Frankl–Rödl graphs as candidate hard instances for sum-of-squares; sharper $\alpha(G_{n,\gamma})$ bounds translate immediately into stronger lower bounds against convex relaxations of Vertex Cover.
- **Computational**: exact independence numbers of $G_{n,\gamma}$ for $n\le 20$ via symmetry-reduced semidefinite (Terwilliger algebra) hierarchies. *(frontier — verify particular record values.)*

## 8. Future Work

- Prove a **single unified theorem** covering $\ell/n\to0$ and $\ell/n$ constant, with the extremal family switching from junta to pseudorandom at an identified threshold.
- Obtain **explicit $\delta(\gamma)$** in the cube theorem; even $\delta(\gamma)\ge\gamma^{C}$ for an absolute $C$ would be new and would sharpen known SOS gaps.
- Settle the **$q$-ary exact problem**: for which $(q,\gamma)$ is the optimum a product/junta code rather than an exponentially small pseudorandom code?
- Extend to **forbidding a bounded set of distances** $D$ with $|D|=O(1)$, and to non-abelian ambient spaces beyond $S_n$ (e.g. finite classical groups, $\mathrm{GL}_n(\mathbb F_q)$).
- Use forbidden-intersection bounds to attack the **chromatic number of $\mathbb R^n$**: improving $\delta$ improves the base in $\chi(\mathbb R^n)\ge(1+\delta)^n$.

## 9. Key References

- **[Foundational]** P. Frankl, V. Rödl. *Forbidden intersections.* Transactions of the American Mathematical Society, **300** (1987), 259–286.
- **[Foundational]** P. Frankl, R. M. Wilson. *Intersection theorems with geometric consequences.* Combinatorica, **1** (1981), 357–368.
- **[Foundational]** P. Frankl, V. Rödl. *Near perfect coverings in graphs and hypergraphs.* European Journal of Combinatorics, **6** (1985), 317–326.
- **[Foundational]** P. Frankl, Z. Füredi. *Forbidding just one intersection.* Journal of Combinatorial Theory, Series A, **39** (1985), 160–176.
- **[SOTA / Recent]** P. Keevash, E. Long. *Frankl–Rödl type theorems for codes and permutations.* Transactions of the American Mathematical Society, **369** (2017), 1147–1162.
- **[SOTA / Recent]** N. Keller, N. Lifshitz. *The junta method for hypergraphs and the Erdős–Chvátal simplex conjecture.* Advances in Mathematics, **392** (2021), 107991.
- **[SOTA / Recent]** D. Ellis, N. Keller, N. Lifshitz. *Stability for the Complete Intersection Theorem, and the forbidden intersection problem of Erdős and Sós.* Journal of the European Mathematical Society, 2024.
- **[SOTA / Recent]** A. Kupavskii, D. Zakharov. *Spread approximations for forbidden intersection problems.* Advances in Mathematics, 2024.
- **[Application]** J. Kahn, G. Kalai. *A counterexample to Borsuk's conjecture.* Bulletin of the AMS, **29** (1993), 60–62.
- **[Application]** M. Kauers, R. O'Donnell, L.-Y. Tan, Y. Zhou. *Hypercontractive inequalities via SOS, and the Frankl–Rödl graph.* Proc. SODA 2014.
- **[Survey]** P. Frankl, N. Tokushige. *Invitation to intersection problems for finite sets.* Journal of Combinatorial Theory, Series A, **144** (2016), 157–211.

## 10. Worked Example / Concrete Special Case

Take $n=4$, forbidden Hamming distance $d=2$ (so $\gamma=1/2$). The Frankl–Rödl graph $G_{4,1/2}$ has $16$ vertices and is $\binom42=6$-regular.

**Eigenvalues.** In the Hamming scheme the eigenvalues are $K_2(i)=\sum_j(-1)^j\binom{i}{j}\binom{4-i}{2-j}$:
$$K_2(0)=6,\quad K_2(1)=3-3=0,\quad K_2(2)=1-4+1=-2,\quad K_2(3)=0-3+3=0,\quad K_2(4)=6 .$$
Distance $2$ preserves weight parity, so $G_{4,1/2}$ splits into two components (even-weight and odd-weight), each on $8$ vertices, each $6$-regular with $\lambda_{\min}=-2$.

**Hoffman ratio bound per component:**
$$\alpha\le N\cdot\frac{-\lambda_{\min}}{\lambda_{\max}-\lambda_{\min}}=8\cdot\frac{2}{6+2}=2 .$$
Hence $\alpha(G_{4,1/2})\le 4$.

**Matching construction.** $\mathcal F=\{0000,\,1111,\,1000,\,0111\}$. Distances: $d(0000,1111)=4$, $d(1000,0111)=4$, $d(0000,1000)=1$, $d(0000,0111)=3$, $d(1111,1000)=3$, $d(1111,0111)=1$. No pair is at distance $2$, so $\alpha(G_{4,1/2})=4$ exactly.

**Reading off the exponential bound.** $|\mathcal F|=4=2^4/4$, i.e. $4=(2-\delta)^4$ with $2-\delta=\sqrt2$, giving $\delta\approx0.586$ at $n=4$. Correspondingly $\chi(G_{4,1/2})\ge 16/4=4$: the two components are each $K_{4,4}$-free but 6-regular on 8 vertices, and 4 colours suffice.

This is exactly the shape of the general claim: the graph is dense (degree $\binom{n}{\gamma n}$), yet every independent set is an exponentially small fraction of the cube. The conjecture asserts the same phenomenon over $[q]^n$ and $S_n$ — where no parity decomposition and no clean Krawtchouk sign pattern is available, which is why the elementary spectral computation above has no analogue and probabilistic or junta-based arguments are required.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*