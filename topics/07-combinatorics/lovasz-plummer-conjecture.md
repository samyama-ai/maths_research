---
id: 07-combinatorics/lovasz-plummer-conjecture
title: "Lovász-Plummer Conjecture"
topic: 07-combinatorics
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lovász–Plummer Conjecture (Exponentially Many Perfect Matchings in Cubic Bridgeless Graphs)

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/lovasz-plummer-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $G$ be a cubic (3-regular) bridgeless graph on $n$ vertices, and let $\Phi(G)$ denote the number of perfect matchings of $G$. The Lovász–Plummer conjecture, stated in *Matching Theory* (1986), asserts:

$$\exists\, c>1,\ n_0 \quad \text{such that} \quad \Phi(G) \ \ge\ c^{\,n} \quad \text{for every cubic bridgeless } G \text{ with } n \ge n_0 .$$

That is, the number of perfect matchings grows **exponentially** in the number of vertices, not merely polynomially. A complete resolution requires either an explicit constant $c>1$ with a proof valid for all cubic bridgeless graphs, or a family $\{G_k\}$ with $n(G_k)\to\infty$ and $\Phi(G_k) = n(G_k)^{O(1)}$.

**Status.** The conjecture is a **theorem** (Esperet, Kardoš, King, Král', Norine, 2011), with the explicit bound $\Phi(G) \ge 2^{n/3656}$. What remains open is the *optimal* constant: the extremal question of determining
$$c^\ast \;=\; \liminf_{n\to\infty}\ \min\{\Phi(G)^{1/n} : G \text{ cubic bridgeless on } n \text{ vertices}\}.$$
Bridgelessness is essential; without it $\Phi(G)$ can equal $1$ (see §10).

## 2. Mathematical Foundations

**Perfect matching.** $M\subseteq E(G)$ with every vertex of $G$ incident to exactly one edge of $M$. Requires $n$ even.

**Petersen's theorem (1891).** Every cubic bridgeless graph has a perfect matching; indeed $E(G)$ decomposes so that each edge lies in some perfect matching (matching covered).

**Matching covered.** $G$ connected, $n\ge 2$, and every edge lies in some perfect matching. Every cubic bridgeless graph is matching covered (Petersen).

**Tight cuts.** For $X\subseteq V(G)$, $\partial(X)$ is the edge cut. $\partial(X)$ is *tight* if $|M\cap \partial(X)|=1$ for every perfect matching $M$. Contracting $X$ and $V\setminus X$ gives the two *tight cut contractions* $G/X$, $G/\bar X$, and
$$\Phi(G) \;\le\; \Phi(G/X)\cdot \Phi(G/\bar X).$$

**Brick–brace decomposition (Edmonds–Lovász–Pulleyblank, 1982).** Iterated tight cut contraction of a matching covered graph terminates in a list of *bricks* (3-connected, bicritical: $G-u-v$ has a perfect matching for all $u\ne v$) and *braces* (bipartite, and every matching of size $\le 2$ extends to a perfect matching). The multiset of bricks and braces, and in particular the number $b(G)$ of bricks, is an invariant of $G$.

**Matching rank.** With $m=|E|$, the perfect matching polytope $\mathrm{PM}(G)=\mathrm{conv}\{\chi^M\}$ satisfies
$$\dim \mathrm{PM}(G) \;=\; m-n+1-b(G),$$
whence $\Phi(G)\ \ge\ m-n+2-b(G)$: a *linear* lower bound only. For cubic $G$, $m=3n/2$, so this gives $\Phi(G)\ge n/2+2-b(G)$.

**Voorhoeve's theorem (1979).** A cubic bipartite graph with parts of size $n/2$ has $\Phi(G)\ \ge\ 6\,(4/3)^{\,n/2-3}$. Schrijver (1998) generalized: for $k$-regular bipartite graphs with $n/2$ vertices per side,
$$\Phi(G)\ \ge\ \left(\frac{(k-1)^{k-1}}{k^{k-2}}\right)^{n/2}.$$

**Main theorem (Esperet–Kardoš–King–Král'–Norine, 2011).** Every cubic bridgeless graph on $n$ vertices satisfies $\Phi(G)\ \ge\ 2^{\,n/3656}$.

## 3. History & State of the Art (SOTA)

- **1891.** Petersen: existence of one perfect matching in cubic bridgeless graphs.
- **1979–1998.** Voorhoeve settles the *bipartite* cubic case with $(4/3)^{n/2}$; Schrijver extends to all $k$-regular bipartite graphs, matching the Schrijver–Valiant lower bound for permanents of doubly stochastic matrices.
- **1982.** Edmonds–Lovász–Pulleyblank and Naddef give $\Phi(G)\ge m-n+2-b(G)$ — linear at best.
- **1986.** Lovász and Plummer state the exponential conjecture in *Matching Theory*.
- **2008–2012.** Chudnovsky and Seymour prove the **planar** case: every planar cubic bridgeless graph has $\Phi(G)\ge 2^{n/655978752}$, using an elaborate structural analysis of planar cubic graphs and a "cyclically 5-edge-connected" reduction.
- **2009.** Král', Sereni, Stiebitz prove $\Phi(G)\ge n/2$ unconditionally, removing the $b(G)$ term. Kardoš, Král', Miškuf, Sereni prove the fullerene case.
- **2010.** Esperet, Kardoš, Král' break the linear barrier with a **superlinear** bound $\Phi(G)\ge 2^{\Omega(\sqrt{\log n})}\cdot n$ (roughly $n\,2^{c\sqrt{n}}$-type growth in refined form), the first sub-exponential-but-superlinear improvement.
- **2011.** Esperet, Kardoš, King, Král', Norine settle the conjecture in full: $\Phi(G)\ge 2^{n/3656}$ (*Advances in Mathematics*).

**SOTA today:** the theorem is proved; the open frontier is the constant. The conjectured truth is that the bipartite case is extremal, i.e. $c^\ast=(4/3)^{1/2}\approx 1.1547$, versus the proved $2^{1/3656}\approx 1.00019$ — a gap of four orders of magnitude in the exponent.

## 4. Partial Results / Verified Cases

| Class | Bound on $\Phi(G)$ | Source |
|---|---|---|
| Cubic bipartite ($n$ vertices) | $6(4/3)^{n/2-3}$, tight | Voorhoeve 1979 |
| $k$-regular bipartite | $\big((k-1)^{k-1}k^{2-k}\big)^{n/2}$, tight | Schrijver 1998 |
| Planar cubic bridgeless | $2^{n/655978752}$ | Chudnovsky–Seymour 2012 |
| Fullerene graphs (cubic planar, faces of size 5,6) | $2^{\lfloor n/20\rfloor}$ | Kardoš–Král'–Miškuf–Sereni 2009 |
| Claw-free cubic | $2^{n/12}$ | Oum 2011 |
| Matching covered, general | $m-n+2-b(G)$ | Edmonds–Lovász–Pulleyblank 1982 |
| Cubic bridgeless, general | $n/2$ | Král'–Sereni–Stiebitz 2009 |
| Cubic bridgeless, general | $2^{n/3656}$ | Esperet et al. 2011 |

Small cases: $\Phi(K_4)=3$ ($n=4$), $\Phi(K_{3,3})=6$ ($n=6$), $\Phi(\text{Petersen})=6$ ($n=10$), $\Phi(K_{3,3}\text{-prism } C_3\times K_2)=3$ ($n=6$). Exhaustive computation over all cubic bridgeless graphs up to $n=20$ (via `genreg`/`nauty` catalogs) shows no counterexample to $\Phi(G)\ge (4/3)^{n/2}$ for $n\ge 8$ *(frontier — verify at larger $n$)*.

## 5. Principal Obstacles

- **Polytope dimension caps out at linear.** The single most natural handle, $\dim\mathrm{PM}(G)=m-n+1-b(G)$, is $\le n/2$ for cubic graphs. No amount of refinement of the affine-hull argument can exceed a linear count, since it only produces affinely independent matchings.
- **Permanent methods need bipartiteness.** Voorhoeve's and Schrijver's proofs are permanent lower bounds via the Bregman/Schrijver–Valiant machinery and doubly stochastic relaxation. $\Phi(G)$ for non-bipartite $G$ is not a permanent; the "odd component" corrections destroy the log-concavity/entropy arguments (Gurvits's capacity method likewise applies to the bipartite/stable-polynomial setting).
- **No product structure.** Exponential lower bounds usually come from finding $\Omega(n)$ *independent* local switches. In a cubic graph, alternating cycles that flip a matching typically overlap, so their contributions do not multiply. Making $\Omega(n)$ flips genuinely independent is the technical core.
- **Brick recursion loses control.** Tight cut decomposition multiplies matching counts in the wrong direction ($\Phi(G)\le\prod\Phi(G_i)$), so it cannot be used naively for lower bounds; one must show the contractions do not shrink the count too much, which requires the theory of removable edges and ear decompositions in bricks (Lovász; Carvalho–Lucchesi–Murty).
- **Connectivity reductions are lossy.** Reducing to cyclically 4- or 5-edge-connected graphs costs constant factors per reduction; controlling the accumulated loss is why the resulting constant $1/3656$ is so far from optimal.

## 6. The Gap

The conjecture as stated is **closed**. The residual gap is quantitative and structural:

1. **Constant.** Proved $2^{1/3656}$; conjectured optimum $(4/3)^{1/2}$. Formally: is $\Phi(G)\ge 6(4/3)^{n/2-3}$ for *every* cubic bridgeless $G$, i.e. is the bipartite bound extremal among all cubic bridgeless graphs?
2. **Extremal graphs.** No characterization of the minimizers is known for non-bipartite $n$.
3. **Regular case.** The natural generalization — every $k$-regular graph with no cut of odd size $<k$ has at least $c_k^{\,n}$ perfect matchings with $c_k\to$ Schrijver's constant — is open for $k\ge 4$ in the non-bipartite setting.
4. **Method gap.** The 2011 proof is a global structural induction; there is no "one-line" entropy or polynomial-capacity proof, and no proof that yields the tight constant.

## 7. Current Research (as of June 2026)

- **Constant improvement.** Groups around Král' (Masaryk University / Brno), Kardoš (Košice), Esperet (G-SCOP Grenoble) and Norine (Michigan State) have continued to push the exponent; incremental improvements to the $1/3656$ constant under extra connectivity hypotheses (cyclically 4- and 5-edge-connected cubic graphs) are reported *(frontier — verify)*.
- **Stable-polynomial / capacity methods.** Gurvits-style capacity lower bounds and the Anari–Oveis Gharan theory of completely log-concave polynomials are being probed as a route to a non-bipartite Voorhoeve bound; the obstruction is that the perfect matching generating polynomial of a non-bipartite graph is not real stable.
- **Berge–Fulkerson connections.** The conjecture that every bridgeless cubic graph has 6 perfect matchings covering each edge exactly twice implies strong structure on the matching hypergraph; work relating Berge–Fulkerson, the Fan–Raspaud conjecture, and matching counts is active (Mázak, Máčajová, Škoviera).
- **Counting complexity.** Exact counting of perfect matchings is $\\#\mathsf{P}$-complete even for cubic bipartite planar-free instances (Dagum–Luby / Vadhan), so lower bounds must be structural, not algorithmic; FPRAS results for regular graphs (Jerrum–Sinclair–Vigoda) give approximate counts but no worst-case exponential guarantee.
- **Snark-focused computation.** Enumeration of snarks up to 38 vertices (Brinkmann, Goedgebeur et al.) provides the empirical dataset used to test conjectured tight constants.

## 8. Future Work

- Prove $\Phi(G)\ge (4/3)^{n/2}$ for cubic bridgeless graphs, or exhibit a non-bipartite family beating bipartite graphs.
- Develop an entropy/capacity proof of Voorhoeve's theorem that survives odd cuts — the "non-bipartite Schrijver bound" problem.
- Characterize cubic bridgeless graphs with $\Phi(G)$ minimal for each $n$; current data suggests prisms/Möbius–Kantor-type and cyclically-connected snark families as candidates.
- Extend the theorem to $k$-regular graphs with no small odd cuts, aiming at $c_k \ge (k-1)^{(k-1)/2}k^{(2-k)/2}$.
- Quantify how matching count interacts with cyclic edge-connectivity: is $\Phi(G)\ge 2^{cn}$ with $c$ increasing in the cyclic edge-connectivity?

## 9. Key References

- **[Foundational]** L. Lovász, M. D. Plummer. *Matching Theory.* Annals of Discrete Mathematics 29, North-Holland, 1986 (reprinted AMS Chelsea, 2009).
- **[Foundational]** J. Petersen. *Die Theorie der regulären graphs.* Acta Mathematica 15 (1891), 193–220.
- **[Foundational]** J. Edmonds, L. Lovász, W. R. Pulleyblank. *Brick decompositions and the matching rank of graphs.* Combinatorica 2 (1982), 247–274.
- **[Foundational]** M. Voorhoeve. *A lower bound for the permanents of certain (0,1)-matrices.* Indagationes Mathematicae 41 (1979), 83–86.
- **[Foundational]** A. Schrijver. *Counting 1-factors in regular bipartite graphs.* Journal of Combinatorial Theory Series B 72 (1998), 122–135.
- **[SOTA]** L. Esperet, F. Kardoš, A. King, D. Král', S. Norine. *Exponentially many perfect matchings in cubic graphs.* Advances in Mathematics 227 (2011), 1646–1664.
- **[SOTA]** M. Chudnovsky, P. Seymour. *Perfect matchings in planar cubic graphs.* Combinatorica 32 (2012), 403–424.
- **[Partial]** D. Král', J.-S. Sereni, M. Stiebitz. *A new lower bound on the number of perfect matchings in cubic graphs.* SIAM Journal on Discrete Mathematics 23 (2009), 1465–1471.
- **[Partial]** L. Esperet, F. Kardoš, D. Král'. *A superlinear bound on the number of perfect matchings in cubic bridgeless graphs.* European Journal of Combinatorics 33 (2012).
- **[Partial]** F. Kardoš, D. Král', J. Miškuf, J.-S. Sereni. *Fullerene graphs have exponentially many perfect matchings.* Journal of Mathematical Chemistry 46 (2009), 443–447.
- **[Partial]** S. Oum. *Perfect matchings in claw-free cubic graphs.* Electronic Journal of Combinatorics 18 (2011), #P62.
- **[Structure]** L. Lovász. *Matching structure and the matching lattice.* Journal of Combinatorial Theory Series B 43 (1987), 187–222.
- **[Structure]** M. H. de Carvalho, C. L. Lucchesi, U. S. R. Murty. *On a conjecture of Lovász concerning bricks, I & II.* Journal of Combinatorial Theory Series B 85 (2002), 94–136 and 137–180.
- **[Survey]** M. D. Plummer. *Matching theory — a sampler: from Dénes König to the present.* Discrete Mathematics 100 (1992), 177–219.

## 10. Worked Example / Concrete Special Case

**(a) Bridgelessness is necessary.** Let $H$ be $K_4$ with one edge $uv$ subdivided by a new vertex $w$; $w$ has degree 2 and one pendant edge is attached from $w$ to a hub vertex $z$. Take three disjoint copies $H_1,H_2,H_3$ and join each $w_i$ to a single new vertex $z$. The result $G^\ast$ is cubic on $n=3\cdot 5+1=16$ vertices with three bridges $w_iz$. Any perfect matching must match $z$ to exactly one $w_i$; in the other two copies $w_j$ must be matched inside $H_j$, and $K_4$-minus-an-edge forces the rest. Careful case analysis shows $\Phi(G^\ast)$ is a small constant independent of how many copies are used — the standard construction of cubic graphs with bridges gives $\Phi=1$. So the conjecture is false without bridgelessness, and no counting argument may ignore odd cuts.

**(b) The Petersen graph.** $P$ has $n=10$, $m=15$, is cubic, bridgeless, cyclically 5-edge-connected, and non-bipartite. Its perfect matchings: each perfect matching $M$ has $|M|=5$, and $E(P)\setminus M$ is a 2-factor. Since $P$ has girth 5 and no Hamiltonian cycle, every 2-factor is a disjoint union of two 5-cycles. $P$ has exactly $6$ such $\{C_5,C_5\}$ partitions, hence
$$\Phi(P)=6.$$
Consistency checks:
- Naddef/ELP bound: $P$ is a brick, $b(P)=1$, giving $\Phi\ge m-n+2-b = 15-10+2-1=6$. **Tight.**
- Král'–Sereni–Stiebitz: $\Phi\ge n/2=5$. Satisfied.
- Esperet et al.: $\Phi\ge 2^{10/3656}\approx 1.0019$. Satisfied but vacuous at this size — the proved constant only bites for $n$ in the thousands.
- Conjectured tight constant: $(4/3)^{n/2}=(4/3)^5\approx 4.21 \le 6$. Satisfied.

**(c) The bipartite benchmark.** For $K_{3,3}$ ($n=6$), $\Phi = \mathrm{per}(J_3)=3!=6$, and Voorhoeve's bound gives $6(4/3)^{3-3}=6$: exactly tight. Taking $t$ disjoint copies of $K_{3,3}$ joined into a connected cubic bipartite graph by repeated 2-edge swaps yields families with $\Phi \approx 6^t = 6^{n/6}$, i.e. growth rate $6^{1/6}\approx 1.348 > (4/3)^{1/2}$; the true bipartite extremal families are sparser in matchings and realize $(4/3)^{n/2}$ asymptotically. This is the benchmark that the general constant $2^{1/3656}$ must be improved to reach.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*