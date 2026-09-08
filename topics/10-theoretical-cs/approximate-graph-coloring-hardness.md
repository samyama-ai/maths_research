---
id: 10-theoretical-cs/approximate-graph-coloring-hardness
title: "Hardness of Approximating Graph Coloring within Polynomial Factors"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hardness of Approximating Graph Coloring within Polynomial Factors

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/approximate-graph-coloring-hardness` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Two linked questions, one settled and one wide open.

**(A) Chromatic number approximation (settled).** For every $\varepsilon>0$ it is NP-hard to approximate $\chi(G)$ on $n$-vertex graphs within a factor $n^{1-\varepsilon}$ (Zuckerman 2007). This matches the algorithmic side up to $\mathrm{polylog}$ factors.

**(B) Approximate graph coloring / promise coloring (open).** Fix constants $3 \le k \le c$. The problem $\mathrm{PCSP}(K_k, K_c)$ takes a graph $G$ *promised* to satisfy $\chi(G) \le k$ and asks for a proper $c$-coloring.

> **Conjecture (Garey–Johnson; Khanna–Linial–Safra).** For every $3 \le k \le c$ with $c$ a constant, $\mathrm{PCSP}(K_k,K_c)$ is NP-hard. In particular, given a 3-colorable graph it is NP-hard to find a proper 100-coloring.

A complete resolution means either an NP-hardness reduction for all constant $c$, or a polynomial-time algorithm that $c$-colors every 3-colorable graph for some constant $c$ — which would be a spectacular algorithmic breakthrough. The **polynomial-factor** version asks for the strongest form: is it NP-hard to color a $k$-colorable graph with $n^{\delta}$ colors for some $\delta = \delta(k) > 0$, for fixed constant $k$? Currently no NP-hardness beyond a *constant* number of colors is known for constant $k$.

## 2. Mathematical Foundations

**Graph homomorphism.** For graphs $G,H$, a homomorphism $f: G \to H$ is a map $V(G)\to V(H)$ with $\{u,v\}\in E(G) \Rightarrow \{f(u),f(v)\}\in E(H)$. Write $G\to H$. A proper $c$-coloring is exactly a homomorphism $G \to K_c$, and
$$\chi(G) = \min\{\, c : G \to K_c \,\}.$$

**Promise CSP.** Let $\mathbf{A}, \mathbf{B}$ be relational structures with $\mathbf{A}\to\mathbf{B}$. $\mathrm{PCSP}(\mathbf{A},\mathbf{B})$ is: given $\mathbf{X}$, output YES if $\mathbf{X}\to\mathbf{A}$, NO if $\mathbf{X}\not\to\mathbf{B}$; behaviour on the gap is unconstrained. Approximate coloring is $\mathbf{A}=K_k$, $\mathbf{B}=K_c$.

**Polymorphisms.** A map $f:\{1,\dots,k\}^n \to \{1,\dots,c\}$ is a polymorphism of $(K_k,K_c)$ if for all $x,y \in \{1,\dots,k\}^n$ with $x_i \ne y_i$ for every $i$, one has $f(x)\ne f(y)$. The set $\mathrm{Pol}(K_k,K_c)$ is closed under *minors* $f(x_{\pi(1)},\dots,x_{\pi(n)})$, forming a minion. The central theorem of the algebraic theory (Barto–Bulín–Krokhin–Opršal 2021) is that the complexity of $\mathrm{PCSP}(\mathbf{A},\mathbf{B})$ depends only on $\mathrm{Pol}(\mathbf{A},\mathbf{B})$ up to minion homomorphism; hardness follows from the absence of certain "bounded essential arity" or symmetric operations.

**Topological invariant.** To a polymorphism minion one attaches homomorphisms to $\mathbb{Z}_2$-equivariant maps of spheres. Borsuk–Ulam gives the obstruction: any continuous $\mathbb{Z}_2$-equivariant $g:S^{m}\to S^{m'}$ forces $m'\ge m$. Combinatorially, this is the Lovász bound
$$\chi(G) \ge \mathrm{conn}(\mathcal{N}(G)) + 3,$$
for the neighbourhood complex $\mathcal{N}(G)$, the same machinery that proves $\chi(\mathrm{KG}_{n,r}) = n-2r+2$ for Kneser graphs.

**Relaxations.** The vector chromatic number $\vec\chi(G)$ is the SDP value: the smallest $c$ for which unit vectors $v_i$ exist with $\langle v_i,v_j\rangle \le -\tfrac{1}{c-1}$ for all $\{i,j\}\in E$. Always $\vec\chi(G)\le\chi(G)$, and $\vec\chi$ can be computed to arbitrary precision in polynomial time; all known algorithms for (B) round this SDP or its Lasserre/Sum-of-Squares lifts.

## 3. History & State of the Art (SOTA)

- **1976.** Garey and Johnson show approximating $\chi$ within a factor $<2$ is NP-hard, and pose the 3-colorable/$c$-colorable question.
- **1983.** Wigderson gives a combinatorial algorithm coloring $k$-colorable graphs with $O(n^{1-1/(k-1)})$ colors — $O(\sqrt n)$ for $k=3$.
- **1993–2000.** Khanna, Linial and Safra prove it is NP-hard to 4-color a 3-colorable graph (Combinatorica 2000); Guruswami and Khanna give a second, purely combinatorial proof (2004).
- **1994–2007.** The chromatic-number side is closed: Lund–Yannakakis ($n^{\varepsilon}$), Feige–Kilian and Håstad ($n^{1-\varepsilon}$ under $\mathrm{NP}\not\subseteq\mathrm{ZPP}$), then Zuckerman's derandomization gives full NP-hardness of $n^{1-\varepsilon}$.
- **1998–2017.** SDP algorithms for $k=3$: Karger–Motwani–Sudan $\tilde O(n^{1/4})$, Blum–Karger $\tilde O(n^{3/14})$, Arora–Chlamtac–Charikar $O(n^{0.2111})$, Chlamtac $O(n^{0.2072})$, Kawarabayashi–Thorup $\tilde O(n^{0.19747})$ — the current record.
- **2001–2013.** For *large* constant $k$, Khot proves NP-hardness of coloring with $k^{\Omega(\log k)}$ colors; Huang improves this to $2^{\Omega(k^{1/3})}$.
- **2019–2023.** The algebraic/topological PCSP program: Bulín–Krokhin–Opršal prove NP-hardness of 5-coloring 3-colorable graphs; Wrochna–Živný and Krokhin–Opršal–Wrochna–Živný push $k$-colorable graphs to $\binom{k}{\lfloor k/2\rfloor}-1$ colors.

**SOTA summary for constant $k=3$:** hard for $c\le 5$; solvable in polynomial time for $c = \tilde O(n^{0.19747})$. Everything between $6$ and $n^{0.197}$ is open.

## 4. Partial Results / Verified Cases

| Regime | Result |
|---|---|
| $\chi(G)$ general | NP-hard within $n^{1-\varepsilon}$, all $\varepsilon>0$ (Zuckerman 2007); tight against Halldórsson's $O\!\big(n(\log\log n)^2/\log^3 n\big)$ algorithm |
| $k=3$, $c=4$ | NP-hard (Khanna–Linial–Safra 2000) |
| $k=3$, $c=5$ | NP-hard (Bulín–Krokhin–Opršal, STOC 2019) |
| $k\ge 4$ | NP-hard for $c \le \binom{k}{\lfloor k/2\rfloor}-1$ (Wrochna–Živný 2020; framework of Krokhin–Opršal–Wrochna–Živný 2023). For $k=6$: $c\le 19$ |
| $k$ large | NP-hard for $c \le 2^{\Omega(k^{1/3})}$ (Huang 2013), improving Khot's $k^{\Omega(\log k)}$ (2001) |
| Under 2-to-1 / $d$-to-1 conjectures | 3-colorable graphs hard to color with *any* constant $c$ (Dinur–Mossel–Regev 2009; Guruswami–Sandeep 2020) |
| Hypergraphs | 2-colorable 3-uniform hypergraphs NP-hard to color with $2^{(\log n)^{\Omega(1)}}$ colors (Dinur–Regev–Smyth 2005; Guruswami–Håstad–Harsha–Srinivasan–Varma 2017) — polynomial-factor hardness *is* achievable there |
| Bounded degree | 3-colorable graphs of max degree $\Delta$ colorable with $O(\Delta^{1/3}\mathrm{polylog}\,\Delta)$ colors (Karger–Motwani–Sudan) |

Note that in every graph result the hardness is $c = O(1)$ or $c$ a function of $k$ only — never a growing function of $n$ for fixed $k$.

## 5. Principal Obstacles

- **Perfect completeness.** Hardness of $\mathrm{PCSP}(K_3,K_c)$ requires a PCP with *perfect* completeness and a strong soundness gap for a 2-prover projection-like game. The 2-to-1 Games Theorem (Khot–Minzer–Safra 2018) delivers only *imperfect* completeness ($1-\varepsilon$), which is useless here: a single unsatisfied constraint destroys the promise $\chi(G)\le 3$. There is no known route from imperfect to perfect completeness.
- **Long-code / Fourier failure.** Dictatorship tests for coloring must be *linear-invariance-free* and preserve 3-colorability of the encoding graph. Standard Fourier/invariance-principle arguments (Mossel–O'Donnell–Oleszkiewicz) yield noise-robust statements, i.e. imperfect completeness, by their very nature.
- **Topology caps out.** The Borsuk–Ulam obstruction used by Wrochna–Živný and KOWŽ measures the equivariant connectivity of the polymorphism complex. This gives at most $\binom{k}{\lfloor k/2\rfloor}\approx 2^k/\sqrt{k}$ colors — a bound *in $k$*, not in $n$. Once $c$ exceeds this, non-trivial equivariant maps exist, so the invariant vanishes and the method is silent, regardless of instance size.
- **Algebra alone is insufficient.** $\mathrm{Pol}(K_3,K_c)$ contains no symmetric operations of large arity, yet no minion homomorphism to a known NP-hard minion is available; the "bounded width" dichotomy tools of finite-domain CSP do not transfer because the promise structure breaks the Galois correspondence with relations.
- **No hard-instance candidates.** Random $G(n,p)$ near the 3-colorability threshold is not known to defeat SDP rounding, and Kneser-type instances are colorable by the same topological argument that proves the lower bound.

## 6. The Gap

Proven: hardness up to $c=5$ for $k=3$, and up to $2^{\Omega(k^{1/3})}$ for large $k$. Conjectured: hardness for *all* constants $c$, and plausibly for $c=n^{\delta(k)}$.

The exact step required is a reduction producing, from a 3-SAT instance $\varphi$, a graph $G$ with
$$\varphi \text{ satisfiable} \;\Rightarrow\; \chi(G)\le 3, \qquad \varphi \text{ unsatisfiable} \;\Rightarrow\; \chi(G) > c ,$$
for $c$ growing — with **no error allowed in the YES case**. Equivalently: prove the 2-to-1 Conjecture *with perfect completeness*, which is known to imply hardness for all constant $c$. Whether polynomial-factor hardness ($c=n^\delta$) even holds is unclear: it would require a gap of the type only achieved so far for hypergraph coloring, where the analogous $2^{(\log n)^{\Omega(1)}}$ bound is already known.

## 7. Current Research (as of June 2026)

- **PCSP algebra/topology school** (Krokhin, Opršal, Živný, Barto, Bulín; Oxford, Durham, Charles University, Prague). Focus: new minion invariants beyond $\mathbb{Z}_2$-equivariant homotopy — higher homotopy groups, equivariant obstruction theory for $\mathbb{Z}_p$ actions.
- **Perfect-completeness PCP** (Khot, Minzer, Safra, Braverman, Lifshitz; NYU, Weizmann, MIT, Hebrew University). Grassmann- and hypercube-expansion techniques post-2-to-1; the aim is a rich 2-to-1 game with completeness exactly 1. *(frontier — verify)* Several 2025–2026 preprints report perfect-completeness variants for restricted label-cover alphabets; none yet implies $\mathrm{PCSP}(K_3,K_6)$ hardness.
- **Sum-of-Squares lower bounds.** Attempts to show degree-$n^{\Omega(1)}$ SoS cannot $O(1)$-color 3-colorable graphs, which would rule out the natural algorithmic route (Kothari, Potechin, Raghavendra school).
- **Algorithmic side.** No improvement on $\tilde O(n^{0.19747})$ since 2017; effort has shifted to $k=4,5$ and to degree-bounded and semi-random models.
- **Conditional programme.** Guruswami–Sandeep-style reductions showing that increasingly weak forms of $d$-to-1 suffice.

## 8. Future Work

1. **Prove 2-to-1 with perfect completeness.** The single highest-value target; it settles the constant-$c$ conjecture outright.
2. **Find a new minion invariant.** Krokhin and Opršal explicitly ask for an obstruction that survives when $\mathbb{Z}_2$-equivariant maps exist — e.g. cohomological operations or equivariant cup-length rather than connectivity.
3. **Rule out or exploit "smooth" reductions.** Determine whether $\mathrm{PCSP}(K_3,K_c)$ can be NP-hard with $c=\omega(1)$ growing with $n$ without polynomial-factor hardness for $\chi$ collapsing.
4. **Transfer hypergraph techniques.** Understand structurally why 3-uniform 2-colorable hypergraphs admit quasi-polynomial-factor hardness while graphs resist, and isolate the property that graphs lack.
5. **Beat $n^{0.197}$ algorithmically**, or prove Lasserre degree lower bounds showing $n^{0.19}$ is a barrier for SDP hierarchies.

## 9. Key References

- **[Foundational]** M. R. Garey, D. S. Johnson. *The complexity of near-optimal graph coloring.* Journal of the ACM 23(1), 1976.
- **[Foundational]** A. Wigderson. *Improving the performance guarantee for approximate graph coloring.* Journal of the ACM 30(4), 1983.
- **[Foundational]** S. Khanna, N. Linial, S. Safra. *On the hardness of approximating the chromatic number.* Combinatorica 20(3), 2000.
- **[Foundational]** D. Karger, R. Motwani, M. Sudan. *Approximate graph coloring by semidefinite programming.* Journal of the ACM 45(2), 1998.
- **[Foundational]** U. Feige, J. Kilian. *Zero knowledge and the chromatic number.* Journal of Computer and System Sciences 57(2), 1998.
- **[SOTA]** D. Zuckerman. *Linear degree extractors and the inapproximability of max clique and chromatic number.* Theory of Computing 3, 2007.
- **[SOTA]** S. Khot. *Improved inapproximability results for MaxClique, chromatic number and approximate graph coloring.* FOCS 2001.
- **[SOTA]** S. Huang. *Improved hardness of approximating chromatic number.* APPROX-RANDOM 2013.
- **[SOTA]** J. Bulín, A. Krokhin, J. Opršal. *Algebraic approach to promise constraint satisfaction.* STOC 2019.
- **[SOTA]** L. Barto, J. Bulín, A. Krokhin, J. Opršal. *Algebraic approach to promise constraint satisfaction.* Journal of the ACM 68(4), 2021.
- **[SOTA]** M. Wrochna, S. Živný. *Improved hardness for H-colourings of G-colourable graphs.* SODA 2020.
- **[SOTA]** A. Krokhin, J. Opršal, M. Wrochna, S. Živný. *Topology and adjunction in promise constraint satisfaction.* SIAM Journal on Computing 52(1), 2023.
- **[SOTA]** K. Kawarabayashi, M. Thorup. *Coloring 3-colorable graphs with less than $n^{1/5}$ colors.* Journal of the ACM 64(1), 2017.
- **[Conditional]** I. Dinur, E. Mossel, O. Regev. *Conditional hardness for approximate coloring.* SIAM Journal on Computing 39(3), 2009.
- **[Conditional]** V. Guruswami, S. Sandeep. *$d$-to-1 hardness of coloring 3-colorable graphs with $O(1)$ colors.* ICALP 2020.
- **[Survey]** A. Krokhin, J. Opršal. *An invitation to the promise constraint satisfaction problem.* ACM SIGLOG News 9(3), 2022.
- **[Survey]** S. Khot, D. Minzer, M. Safra. *Pseudorandom sets in Grassmann graph have near-perfect expansion.* FOCS 2018.

## 10. Worked Example / Concrete Special Case

**Wigderson's algorithm on a 3-colorable graph, $n=10{,}000$.**

Set threshold $\Delta = \sqrt n = 100$. Repeat while $G$ is non-empty:

1. If some vertex $v$ has $\deg(v) \ge \Delta$: its neighbourhood $N(v)$ is 2-colorable, because in any proper 3-coloring $N(v)$ avoids the color of $v$. A 2-coloring of a graph is found by BFS in $O(|E|)$ time. Spend **2 fresh colors** on $N(v)$, delete $N(v)\cup\{v\}$ — removing at least $\Delta+1 = 101$ vertices.
2. If all degrees are $< \Delta$: greedily color the remainder with $\Delta = 100$ colors (each vertex has $<100$ colored neighbours).

Step 1 runs at most $n/\Delta = 100$ times, using $\le 200$ colors; step 2 adds $100$. Total $\le 300 = 3\sqrt{n}$ colors, matching $O(n^{1-1/(k-1)})=O(n^{1/2})$ for $k=3$.

**Contrast with the hardness frontier.** For this $n$, Kawarabayashi–Thorup gives roughly $n^{0.19747}\approx 10^{0.79}\approx 6.2$ — order tens of colors after log factors. The proven hardness says only that finding a **5-coloring** is NP-hard. So the concrete gap at $n=10{,}000$ is: nobody can 6-color, and nobody can prove 6-coloring is hard.

**Why 5 is where topology stops (sketch).** For $k=3$, $c=5$, a polymorphism $f:\{1,2,3\}^n\to\{1,\dots,5\}$ must send every pair of *totally different* inputs to different outputs. BKO show such $f$ must have a bounded set of "essential" coordinates, and the induced $\mathbb{Z}_2$-equivariant map $S^1 \to S^1$ has odd degree, forcing a dictator-like structure that supports a gadget reduction from 3-SAT. At $c=6$, $\binom{4}{2}=6$ admits the "halving" polymorphism $f(x)=\{i : x_i = 1\}$-type constructions, the degree obstruction vanishes, and the proof collapses.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*