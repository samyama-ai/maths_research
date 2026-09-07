---
id: 07-combinatorics/kellers-conjecture
title: "Keller's Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Keller's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/kellers-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Keller's conjecture (1930): in any tiling of $\mathbb{R}^n$ by translates of the unit cube $[0,1]^n$, some two cubes share a complete $(n-1)$-dimensional face.

Formally, let $T \subseteq \mathbb{R}^n$ satisfy
$$\mathbb{R}^n = \bigcup_{t \in T} \left( [0,1]^n + t \right), \qquad \operatorname{int}\big([0,1]^n+t\big) \cap \operatorname{int}\big([0,1]^n+t'\big) = \emptyset \ \ (t \neq t').$$
The conjecture asserts there exist $t \neq t'$ in $T$ with $t - t' \in \{\pm 1\}$ in exactly one coordinate and $0$ in all others — a *face-sharing* (or *twin*) pair.

**Resolution.** The statement is now decided in every dimension:

- **True** for $n \le 7$ (Perron 1940 for $n\le 6$; Brakensiek–Heule–Mackey–Narváez 2020 for $n = 7$).
- **False** for $n \ge 8$ (Mackey 2002 for $n=8$, extending Lagarias–Shor 1992 for $n \ge 10$).

So $n = 7$ is the exact threshold. A complete disproof requires exhibiting a face-share-free tiling; a complete proof for a fixed $n$ requires showing no such tiling exists, which by the reductions of Section 2 is a finite (but astronomically large) combinatorial statement.

## 2. Mathematical Foundations

**Minkowski's precursor.** Minkowski (1907) conjectured the lattice case: if $T$ is a *lattice*, a face-sharing pair exists. Proved by Hajós (1942) using a factorization theorem for finite abelian groups: if a finite abelian group $G$ is a direct product $G = A_1 A_2 \cdots A_n$ of *cyclic-generated* subsets $A_i = \{e, a_i, a_i^2, \dots, a_i^{k_i-1}\}$, then some $A_i$ is a subgroup. Keller's conjecture drops the lattice hypothesis.

**Szabó's periodic reduction.** Szabó (1986) showed that if a counterexample exists in dimension $n$, then one exists that is $2s\mathbb{Z}^n$-periodic with all translation vectors in $\frac{1}{s}\mathbb{Z}^n$ for some integer $s \ge 1$. This converts the geometric problem into a finite search.

**The Keller graph.** For integers $n \ge 1$, $s \ge 2$, define $G_{n,s}$ on vertex set $\{0,1,\dots,2s-1\}^n$ with $u \sim v$ iff

$$\exists\, i:\ u_i - v_i \equiv s \pmod{2s} \qquad \text{and} \qquad \exists\, j \neq i:\ u_j \neq v_j .$$

The first condition says two cubes are *separated* in coordinate $i$; the second says they are not face-sharing twins. Corrádi and Szabó (1990) proved the equivalence:

$$\text{Keller's conjecture fails in dimension } n \iff \exists s \ \ \omega(G_{n,s}) = s^n,$$

where $\omega$ is the clique number. One always has $\omega(G_{n,s}) \le s^n$. The classical Keller graph is $G_n := G_{n,2}$ on $\{0,1,2,3\}^n$, with $4^n$ vertices; a clique of size $2^n$ encodes a face-share-free tiling with half-integer offsets.

**Why cliques.** A clique of size $s^n$ forces every residue class of the periodic lattice to be covered exactly once, so the vertex set of the clique is precisely a full set of coset representatives — a tiling — and the "differ in $\ge 2$ coordinates" edge condition forbids twins.

## 3. History & State of the Art (SOTA)

- **1907** — Minkowski poses the lattice-tiling conjecture in *Diophantische Approximationen*.
- **1930** — Ott-Heinrich Keller, *Crelle's Journal* 163, conjectures the statement for arbitrary (non-lattice) cube tilings.
- **1940** — Oskar Perron proves it for $n \le 6$ by an exhaustive but hand-executed case analysis on the associated combinatorial structures.
- **1942** — György Hajós proves Minkowski's lattice case via group factorization.
- **1986–1990** — Szabó's periodicity reduction, then the Corrádi–Szabó graph reformulation, make the problem finite and machine-attackable.
- **1992** — Lagarias and Shor construct a clique of size $2^{10}$ in $G_{10}$, disproving the conjecture for all $n \ge 10$. Their construction starts from a clique of size $2^{5}\cdot ?$ in a $6$-dimensional auxiliary structure over a $4$-symbol alphabet and lifts it.
- **2002** — John Mackey finds a clique of size $2^8 = 256$ in $G_8$, closing the disproof range to $n \ge 8$ and leaving only $n = 7$.
- **2011** — Debroni, Eblen, Langston, Myrvold, Shor and Weerapurage compute $\omega(G_7) = 124 < 128$ exactly, using roughly $10^5$ CPU-hours of distributed branch-and-bound. This kills $s = 2$ in dimension 7 but not larger $s$.
- **2020** — Brakensiek, Heule, Mackey and Narváez reduce dimension 7 to the single graph $G_{7,3}$ and prove $\omega(G_{7,3}) < 3^7 = 2187$ by SAT solving with aggressive symmetry breaking. Keller's conjecture is true for $n = 7$; the problem is closed.

## 4. Partial Results / Verified Cases

| Dimension | Status | Source |
|---|---|---|
| $n \le 6$ | True | Perron (1940) |
| $n = 7$ | True | Brakensiek–Heule–Mackey–Narváez (2020/2022) |
| $n = 8, 9$ | False | Mackey (2002) |
| $n \ge 10$ | False | Lagarias–Shor (1992) |
| Lattice tilings, all $n$ | True | Hajós (1942) |

Exact clique numbers of the classical Keller graphs $G_n = G_{n,2}$:

$$\omega(G_1)=1,\ \omega(G_2)=2,\ \omega(G_3)=5,\ \omega(G_4)=12,\ \omega(G_5)=28,\ \omega(G_6)=60,\ \omega(G_7)=124,$$

and $\omega(G_n) = 2^n$ for $n \ge 8$. The values for $n \le 6$ satisfy $\omega(G_n) < 2^n$ with growing slack; $\omega(G_7)=124$ is only $4$ short of $128$, which is why dimension 7 sat open for eighteen years after $n=8$ fell.

Additional verified classes: tilings whose translation set has all coordinates in $\frac{1}{2}\mathbb{Z}$ in dimension 7 (the $s=2$ case, Debroni et al.); "rigid" and low-complexity polybox structures analysed by Kisielewicz and Łysakowska.

## 5. Principal Obstacles

The obstacles were computational and structural rather than analytic, and they are worth recording because they recur in adjacent tiling problems.

- **No analytic handle.** Cube tilings have no smoothing or perturbation structure: the tiling condition is a rigid measure identity $\sum_{t\in T}\mathbf{1}_{[0,1]^n+t} \equiv 1$, and Fourier methods only yield the necessary condition that the translation set be spectral-like — they cannot see the *combinatorial* twin condition, which is not expressible as a vanishing-of-transform statement.
- **Non-lattice tilings destroy the group structure.** Hajós's factorization theorem needs $T$ to be a group. For general $T$, the only group left is the ambient $\mathbb{Z}_{2s}^n$ acting on the Keller graph, and cliques are not subgroups.
- **The $s$-parameter is unbounded a priori.** Corrádi–Szabó gives an equivalence over *all* $s$; there is no general bound on the $s$ needed, so a negative answer for $s=2$ (Debroni et al.) proved nothing. Ruling out $s = 3$ multiplies the vertex count from $4^7 = 16384$ to $6^7 = 279936$ and the target clique from $128$ to $2187$.
- **Clique search is exponential and the graphs are dense.** $G_7$ was already a standard benchmark for maximum-clique solvers; direct branch-and-bound on $G_{7,3}$ is far out of reach without symmetry reduction. The automorphism group of $G_{n,s}$ (coordinate permutations $\times$ per-coordinate symbol symmetries) is huge, and exploiting it soundly inside a proof-producing search was the technical crux.
- **Human case analysis saturates around $n=6$.** Perron's method is a hand-run tree search; the $n=7$ tree is many orders of magnitude larger.

## 6. The Gap

Historically, the gap was exactly the interval $\{7\}$: everything $\le 6$ was hand-provable, everything $\ge 8$ had an explicit counterexample, and the decisive missing step was a finite verification that no $s$ admits a clique of size $s^7$ in $G_{7,s}$.

That gap closed in two moves. First, a reduction bounding the relevant $s$: it suffices to rule out $s \le 3$ for $n=7$ (Brakensiek et al., building on Kisielewicz and Łysakowska's analysis of which multipliers can arise). Second, the SAT refutation of "$G_{7,3}$ has a clique of size $2187$". The clausal (DRAT/LRAT) refutation is roughly 200 GB and was checked by a formally verified proof checker, so the result does not rest on trusting the solver. *(Verify the exact proof size and checker before quoting.)*

The residual gap is now interpretive, not logical: no human-surveyable proof of the $n=7$ case exists, and no structural reason is known for why $7$ is the threshold.

## 7. Current Research (as of June 2026)

- **Human-comprehensible $n=7$ proof.** The main open challenge. Compressing the $200$ GB certificate to an argument a mathematician can read would likely reveal the structural reason for the threshold at $7$. No such proof has appeared. *(frontier — verify)*
- **Clique numbers of generalized Keller graphs.** $\omega(G_{n,s})$ is unknown for most $(n,s)$ with $n \le 7$, $s \ge 4$, and for $n \ge 9$ beyond the trivial $2^n$ lower bound in the $s=2$ case. These remain live combinatorial-optimization targets.
- **Trusted large-scale automated reasoning.** The Keller proof, alongside Boolean Pythagorean triples and Schur number five, anchors ongoing work by Heule's group at CMU on verified SAT pipelines (cube-and-conquer, LRAT, verified checkers such as `cake_lpr`).
- **Adjacent tiling conjectures.** Fuglede's spectral set conjecture and cube-tiling questions for non-unit or mixed boxes (Kisielewicz, Łysakowska, Kolountzakis, Łaba) are the natural successors; Keller's graph technology transfers only partially.

## 8. Future Work

- Extract a compact combinatorial invariant separating $n=7$ from $n=8$ — e.g., an obstruction to embedding the Lagarias–Shor $8$-dimensional clique pattern into $7$ coordinates.
- Determine whether the Corrádi–Szabó equivalence admits an *effective* bound $s \le f(n)$ in general, not just for $n = 7$. This is the obstacle to attacking any further Keller-type problem by finite search.
- Push exact clique numbers for $G_{n,s}$ with $s \ge 4$; even $\omega(G_{4,4})$ would test whether larger alphabets behave qualitatively differently.
- Study "almost-counterexamples": the $124$-cliques in $G_7$ are near-tilings missing four cubes; classifying them may explain the tightness.
- Transfer the verified-SAT methodology to Fuglede-type and Minkowski-type questions where the finite reduction is known but the search was previously infeasible.

## 9. Key References

- **[Foundational]** O.-H. Keller. *Über die lückenlose Erfüllung des Raumes mit Würfeln.* Journal für die reine und angewandte Mathematik **163** (1930), 231–248.
- **[Foundational]** G. Hajós. *Über einfache und mehrfache Bedeckung des n-dimensionalen Raumes mit einem Würfelgitter.* Mathematische Zeitschrift **47** (1942), 427–467.
- **[Foundational]** O. Perron. *Über lückenlose Ausfüllung des n-dimensionalen Raumes durch kongruente Würfel.* Mathematische Zeitschrift **46** (1940), 1–26 and 161–180.
- **[Foundational]** S. Szabó. *A reduction of Keller's conjecture.* Periodica Mathematica Hungarica **17** (1986), 265–277.
- **[Foundational]** K. Corrádi and S. Szabó. *A combinatorial approach for Keller's conjecture.* Periodica Mathematica Hungarica **21** (1990), 95–100.
- **[Milestone]** J. C. Lagarias and P. W. Shor. *Keller's cube-tiling conjecture is false in high dimensions.* Bulletin of the American Mathematical Society **27** (1992), 279–283.
- **[Milestone]** J. Mackey. *A cube tiling of dimension eight with no facesharing.* Discrete & Computational Geometry **28** (2002), 275–279.
- **[Computational]** J. Debroni, J. D. Eblen, M. A. Langston, W. Myrvold, P. W. Shor, D. Weerapurage. *A complete resolution of the Keller maximum clique problem.* Proceedings of SODA 2011, 129–135.
- **[SOTA / Recent]** J. Brakensiek, M. Heule, J. Mackey, D. Narváez. *The Resolution of Keller's Conjecture.* IJCAR 2020, LNCS 12166, Springer, 48–65; extended version in Journal of Automated Reasoning **66** (2022), 277–300.
- **[Survey]** C. Zong. *What is known about unit cubes.* Bulletin of the American Mathematical Society **42** (2005), 181–211.
- **[Survey / Book]** C. Zong. *The Cube: A Window to Convex and Discrete Geometry.* Cambridge University Press, 2006.

## 10. Worked Example / Concrete Special Case

**Claim.** $\omega(G_2) = 2 < 4 = 2^2$, hence Keller's conjecture holds in the plane for half-integer tilings.

$G_2 = G_{2,2}$ has vertex set $\{0,1,2,3\}^2$ ($16$ vertices). Since $n=2$, the condition "differ in at least two coordinates" means *both* coordinates differ. So $u=(u_1,u_2) \sim v=(v_1,v_2)$ iff

$$u_1 \neq v_1,\quad u_2 \neq v_2, \quad \text{and} \quad \big(u_1 - v_1 \equiv 2 \ \text{ or } \ u_2 - v_2 \equiv 2\big) \pmod 4 .$$

*Check:* $(0,0)$ and $(2,1)$ — both coordinates differ, and $0-2 \equiv 2$. Adjacent. $(1,2)$ and $(2,3)$ — both differ, but $1-2\equiv 3$ and $2-3\equiv 3$. Not adjacent.

**No triangle.** Suppose $\{v^{(1)},v^{(2)},v^{(3)}\}$ is a clique. All three first coordinates $a_1,a_2,a_3$ are distinct, and so are the second coordinates $b_1,b_2,b_3$. Any three distinct elements of $\mathbb{Z}_4$ contain **exactly one** antipodal pair (difference $2$): for $\{0,1,2\}$ it is $(0,2)$; for $\{0,1,3\}$ it is $(1,3)$; and similarly in every case, since $\mathbb{Z}_4$ has only two antipodal pairs $\{0,2\},\{1,3\}$ and a $3$-set meets each in at least one element but can contain only one pair.

So among $a_1,a_2,a_3$ exactly one pair — say $(a_1,a_2)$ — has difference $2$. The other two pairs, $(a_1,a_3)$ and $(a_2,a_3)$, do not, so adjacency forces
$$b_1 - b_3 \equiv 2 \pmod 4, \qquad b_2 - b_3 \equiv 2 \pmod 4 .$$
Subtracting gives $b_1 \equiv b_2$, contradicting distinctness. Hence no triangle, and $\omega(G_2)=2$ (edges clearly exist).

**Interpretation.** A face-share-free tiling of the plane would need a clique of size $2^2 = 4$. We get at most $2$. The same argument extended one step shows why the problem is hard: for $n=4$, $\omega(G_4)=12$ against a target of $16$ — the slack is already only $4$, and it stays at $4$ all the way to $\omega(G_7)=124$ versus $128$, before collapsing to zero at $n=8$ where Mackey's $256$-clique exists.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*