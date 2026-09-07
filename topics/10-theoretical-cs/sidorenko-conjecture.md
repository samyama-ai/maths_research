---
id: 10-theoretical-cs/sidorenko-conjecture
title: "Sidorenko Conjecture"
topic: 10-theoretical-cs
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Sidorenko Conjecture

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/sidorenko-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $H$ be a bipartite graph with $v(H)$ vertices and $e(H)$ edges. Sidorenko's conjecture asserts that among all graphs (or graphons) of a fixed edge density, the quasirandom one asymptotically minimizes the density of copies of $H$.

**Conjecture (Erdős–Simonovits 1984; Sidorenko 1993).** For every bipartite graph $H$ and every symmetric measurable $W : [0,1]^2 \to [0,1]$,
$$t(H, W) \;\ge\; t(K_2, W)^{e(H)},$$
where $t(H,W)$ is the homomorphism density of $H$ in $W$ (Section 2).

Finite-graph form: for every $\varepsilon > 0$ there is $n_0$ such that every graph $G$ on $n \ge n_0$ vertices with edge density $p$ contains at least $(p^{e(H)} - \varepsilon) n^{v(H)}$ homomorphic copies of $H$.

A complete proof must establish the inequality for **all** bipartite $H$ and all graphons; a disproof needs one bipartite $H$ and one $W$ (equivalently, one finite weighted graph) with $t(H,W) < t(K_2,W)^{e(H)}$. Bipartiteness is necessary: if $H$ has an odd cycle and $W$ is the graphon of a complete bipartite graph with $t(K_2,W)=1/2$, then $t(H,W)=0 < 2^{-e(H)}$.

Relevance to theoretical computer science: the statement is a tight, dimension-free counting lemma. It is the extremal case of the property-testing/quasirandomness framework (subgraph counts as a distinguisher), it underlies transference of counting lemmas to sparse pseudorandom hosts, and Sidorenko graphs are exactly the ones whose homomorphism-counting oracle cannot be fooled below the random baseline.

## 2. Mathematical Foundations

**Homomorphism density.** For a finite simple graph $H=(V(H),E(H))$ and a graphon $W$,
$$t(H,W) \;=\; \int_{[0,1]^{V(H)}} \prod_{\{u,v\} \in E(H)} W(x_u, x_v) \prod_{u \in V(H)} dx_u .$$
For a finite graph $G$ on $n$ vertices, $t(H,G) = |\mathrm{Hom}(H,G)| / n^{v(H)}$, and $t(H,W_G) = t(H,G)$ for the associated step graphon $W_G$. Write $p = t(K_2,W) = \int\!\!\int W$.

**Equivalent formulations.**

1. *Normalized form.* Setting $U = W/p$ (so $\int\!\!\int U = 1$), the conjecture is $t(H,U) \ge 1$ for all nonnegative kernels $U$ of average $1$.
2. *Perturbative form.* Writing $W = p(1+U)$ with $\int\!\!\int U = 0$ and $U \ge -1$, the conjecture says
$$\sum_{\emptyset \ne F \subseteq E(H)} t_F(U) \;\ge\; 0, \qquad t_F(U)=\int \prod_{\{u,v\}\in F} U(x_u,x_v),$$
i.e. no cancellation among the "non-quasirandom" correction terms drives the total negative.
3. *Entropy form (Szegedy).* $t(H,W) \ge p^{e(H)}$ is equivalent to exhibiting a coupling — a probability distribution $\mu$ on $[0,1]^{V(H)}$ absolutely continuous with respect to the $H$-homomorphism measure — with
$$\mathbb{H}(\mu) + \mathbb{E}_\mu\!\left[\sum_{\{u,v\}\in E(H)} \log W(x_u,x_v)\right] \;\ge\; e(H)\log p,$$
by Jensen/Gibbs variational principle. This reduces Sidorenko to constructing $\mu$ with enough entropy, typically via Shearer-type subadditivity.

**Graph norms.** $H$ is *norming* if $\|W\|_H := t(H,W)^{1/e(H)}$ is a norm on symmetric kernels, and *weakly norming* if it is a norm on nonnegative kernels. Weakly norming $\Rightarrow$ Sidorenko, since $\|W\|_H \ge \|W\|_{K_2} = p$ by monotonicity of the norm under the $L^1$ comparison (Hatami 2010).

**Related conjectures.** *Forcing conjecture:* every bipartite $H$ with a cycle satisfies "$t(H,W)=p^{e(H)}$ forces $W \equiv p$" — a strengthening of Sidorenko. *Erdős–Simonovits common-graph* problems and Kruskal–Katona-type density inequalities sit in the same semialgebraic framework.

## 3. History & State of the Art (SOTA)

- **1984** — Erdős and Simonovits, in "Compactness results in extremal graph theory" (*Combinatorica*), state the conjecture in the supersaturation language of extremal graph theory.
- **1991–1993** — Sidorenko independently states and studies it analytically, proving it for trees, even cycles, complete bipartite graphs, and all bipartite graphs on at most $5$ vertices; the standing reference is "A correlation inequality for bipartite graphs" (*Graphs and Combinatorics*, 1993).
- **2010** — Conlon, Fox, Sudakov (*GAFA*) prove it for every bipartite $H$ containing a vertex adjacent to all vertices of the other part, and give an approximate version with $p^{e(H)}$ weakened by a $\log(1/p)$ factor in the exponent. Hatami (*Israel J. Math.*) proves it for weakly norming graphs, including hypercubes $Q_d$ and $K_{t,t}$.
- **2011** — Lovász proves the *local* Simonovits–Sidorenko conjecture: every bipartite $H$ satisfies the inequality for $W$ in an $L^\infty$-neighbourhood of the constant $p$.
- **2011–2015** — Li and Szegedy introduce the logarithmic/entropy calculus; Szegedy circulates an entropy-based argument claiming the full conjecture. It remains unverified and unpublished.
- **2016** — Kim, Lee, Lee (*Trans. AMS*) prove it for *tree-arrangeable* graphs and for graphs admitting suitable "$n$-fold" structures, via random-walk couplings and entropy.
- **2017–2018** — Conlon, Lee (*Adv. Math.*) characterize many weakly norming graphs via finite reflection groups; Conlon, Kim, Lee, Lee (*JLMS*) prove it for graphs with a "strongly tree-decomposable" structure, settling $K_{5,5}$ minus a perfect matching, which had been the smallest open case.
- **2021** — Conlon, Lee (*Discrete Analysis*): for every bipartite $H$ there is $k$ such that the $k$-fold vertex blow-up of $H$ is Sidorenko.
- **2020–2022** — Blekherman, Raymond, Singh, Thomas show natural graph density inequalities of this type admit no sums-of-squares certificates, ruling out the most direct semidefinite-programming route.

## 4. Partial Results / Verified Cases

Known Sidorenko classes:

- **Trees and forests**, all paths $P_k$ — immediate by Jensen/Cauchy–Schwarz.
- **Even cycles** $C_{2k}$ for all $k \ge 1$; **complete bipartite** $K_{s,t}$ for all $s,t$; **hypercubes** $Q_d$ for all $d$.
- **All bipartite graphs on at most $5$ vertices** (Sidorenko 1993); exhaustive verification extends to all bipartite graphs with small edge counts.
- **Graphs with a "dominating" vertex**: some $v$ in one part adjacent to every vertex of the other part (Conlon–Fox–Sudakov 2010). This covers all bipartite $H$ with a part of size $\le 4$ under mild conditions and every $H$ obtainable by adding such a vertex.
- **Weakly norming graphs**, including complete bipartite graphs, hypercubes, and the reflection-group families of Conlon–Lee (2017).
- **Tree-arrangeable graphs** (Kim–Lee–Lee 2016): includes every bipartite $H$ where one part has a vertex of degree $\le 2$ adjacent appropriately, and all bipartite $H$ with a part of maximum degree $2$.
- **Strongly tree-decomposable graphs** (Conlon–Kim–Lee–Lee 2018), including $K_{5,5}$ minus a perfect matching.
- **Blow-ups**: for each bipartite $H$, $H^{(k)}$ is Sidorenko for $k$ large (Conlon–Lee 2021).
- **Local regime**: all bipartite $H$, for $\|W - p\|_\infty$ small (Lovász 2011), and all $H$ in the "locally dense" setting where $W \ge p$ on a suitable structure.
- **Approximate regime**: all bipartite $H$ satisfy $t(H,W) \ge p^{c \cdot e(H)\log(1/p)}$-type bounds, i.e. correct up to a $\log(1/p)$ loss in the exponent.

Smallest cases commonly cited as still open: sparse $3$-regular bipartite graphs, notably the **Möbius–Kantor graph** ($16$ vertices, $24$ edges) and related cubic bipartite graphs of large girth *(frontier — verify current status)*.

## 5. Principal Obstacles

- **Convexity/Cauchy–Schwarz saturates.** Every proof for trees, even cycles, and $K_{s,t}$ threads an iterated Hölder or Cauchy–Schwarz argument along a structure that "peels off" one vertex at a time. Cubic bipartite graphs of girth $\ge 6$ have no low-degree vertex to peel and no complete-bipartite skeleton; each Cauchy–Schwarz step loses a factor and the losses compound rather than telescope.
- **No sums-of-squares certificate.** Blekherman–Raymond–Singh–Thomas (2020/2022) exhibit simple graph density inequalities, of the same flavour as Sidorenko's, that are valid but have no representation as a sum of squares in the natural gluing algebra. So SDP-based flag-algebra search — the standard automated tool for extremal density inequalities — cannot in general certify these inequalities, and no finite-degree relaxation is guaranteed to close.
- **Entropy method needs a global coupling.** Szegedy's variational reformulation shifts the burden to constructing a high-entropy measure on $\mathrm{Hom}(H,W)$. Known constructions (random walks along a spanning tree, Shearer partitions) work when $H$ has a tree-like or reflection-symmetric backbone. For high-girth cubic $H$ the natural couplings are not consistent on overlapping cycles, and the entropy deficit is exactly $e(H)-v(H)+1$ independent cycles' worth of correlation that no local construction controls.
- **Local $\ne$ global.** Lovász's local theorem holds for all bipartite $H$, so any counterexample must be a large perturbation. Perturbative/Fourier expansions of $W = p(1+U)$ involve $2^{e(H)}$ terms $t_F(U)$ with signs; controlling them requires bounding the higher Gowers-type norms of $U$, and no known norm inequality dominates the negative terms uniformly.
- **Induction on subgraphs is not available.** Sidorenko-ness is not monotone under subgraphs or minors, so partial results do not compose; each new class needs a new decomposition.

## 6. The Gap

Proven: all bipartite $H$ that admit a *local peeling structure* — a spanning tree, a reflection symmetry, a dominating vertex, a strong tree decomposition, or a large blow-up — plus the full statement in the local ($\|W-p\|_\infty$ small) and approximate ($\log(1/p)$ exponent loss) regimes.

Missing: a proof for bipartite $H$ with **no such structure**, i.e. sparse, high-girth, degree-regular bipartite graphs where cycle space rank $e(H)-v(H)+1$ is large relative to any tree-like scaffold. Concretely, the gap is the step from

$$t(H,W) \ge p^{C \cdot e(H) \log(1/p)} \quad\text{(known)}\qquad\text{to}\qquad t(H,W) \ge p^{e(H)} \quad\text{(conjectured)},$$

removing the $\log(1/p)$ factor, and equivalently the step from *local* to *global* in Lovász's theorem. In entropy terms: exhibit, for arbitrary bipartite $H$, a coupling on $\mathrm{Hom}(H,W)$ whose entropy deficit relative to the product measure is at most $e(H)\log(1/p)$ exactly, with no slack.

## 7. Current Research (as of June 2026)

- **Entropy/coupling school** (Szegedy; Kim, Lee, Lee; Conlon and collaborators): extending tree decompositions to "higher" decompositions with bounded overlap; the status of Szegedy's full claimed proof is still unresolved and not accepted *(frontier — verify)*.
- **Graph-norm program** (Conlon, Lee, Sidorenko, Hatami): classifying weakly norming graphs; the reflection-group characterization is believed to be essentially complete for edge-transitive cases, leaving Sidorenko-but-not-norming graphs as the target.
- **Real algebraic geometry / SDP** (Blekherman, Raymond, Singh, Thomas, Sinn): mapping which density inequalities are SOS-certifiable and searching for higher-degree or non-SOS (e.g. Positivstellensatz with denominators) certificates for specific small $H$.
- **Sparse and relative versions** (Conlon, Fox, Zhao): relative Sidorenko inequalities in pseudorandom hosts, with applications to counting in sparse graphs and to transference results in additive combinatorics.
- **Computational search**: exhaustive verification for all bipartite graphs up to a fixed number of edges via rational-arithmetic optimization over weighted blow-ups; no counterexample has been found in any published search *(frontier — verify scope of latest searches)*.

Active groups: Oxford and IAS/Princeton (Conlon and coauthors), KAIST (J. Lee, J. H. Kim), Rényi Institute (Szegedy), Georgia Tech (Blekherman), MIT (Fox, Zhao).

## 8. Future Work

- Prove or refute the conjecture for a single explicit cubic bipartite graph of girth $\ge 6$ (Möbius–Kantor, Pappus, Heawood-type incidence graphs); a decision either way would break the current method boundary.
- Remove the $\log(1/p)$ loss in the Conlon–Fox–Sudakov approximate bound for a nontrivial class not covered by tree decompositions.
- Determine whether *every* Sidorenko graph is Sidorenko "with a certificate" of bounded complexity — i.e. settle whether a complete, effectively searchable proof system exists, given the SOS obstruction.
- Settle the forcing conjecture for the classes already known to be Sidorenko; forcing is strictly stronger and would sharpen quasirandomness testers.
- Push the blow-up theorem toward an explicit $k = k(H)$, ideally $k$ polynomial in $v(H)$, and understand whether $k=1$ can be reached by de-blow-up arguments.
- Formalize a verified proof of the known cases (trees, even cycles, $K_{s,t}$, hypercubes) in a proof assistant as a base for machine-assisted search.

## 9. Key References

- **[Foundational]** P. Erdős, M. Simonovits. *Compactness results in extremal graph theory.* Combinatorica **4** (1984), 71–80.
- **[Foundational]** A. F. Sidorenko. *A correlation inequality for bipartite graphs.* Graphs and Combinatorics **9** (1993), 201–204.
- **[Foundational]** A. F. Sidorenko. *Inequalities for functionals generated by bipartite graphs.* Diskretnaya Matematika **3** (1991), 50–65 (Discrete Math. Appl. translation).
- **[SOTA]** D. Conlon, J. Fox, B. Sudakov. *An approximate version of Sidorenko's conjecture.* Geometric and Functional Analysis **20** (2010), 1354–1366.
- **[SOTA]** H. Hatami. *Graph norms and Sidorenko's conjecture.* Israel Journal of Mathematics **175** (2010), 125–150.
- **[SOTA]** L. Lovász. *Subgraph densities in signed graphons and the local Simonovits–Sidorenko conjecture.* Electronic Journal of Combinatorics **18** (2011), \#P127.
- **[SOTA]** J. H. Kim, C. Lee, J. Lee. *Two approaches to Sidorenko's conjecture.* Transactions of the American Mathematical Society **368** (2016), 5057–5074.
- **[SOTA]** D. Conlon, J. Lee. *Finite reflection groups and graph norms.* Advances in Mathematics **315** (2017), 130–165.
- **[SOTA]** D. Conlon, J. H. Kim, C. Lee, J. Lee. *Some advances on Sidorenko's conjecture.* Journal of the London Mathematical Society **98** (2018), 593–608.
- **[SOTA]** D. Conlon, J. Lee. *Sidorenko's conjecture for blow-ups.* Discrete Analysis **2021**:2.
- **[SOTA]** G. Blekherman, A. Raymond, M. Singh, R. Thomas. *Simple graph density inequalities with no sum of squares proofs.* Combinatorica **42** (2022), 417–454.
- **[Frontier]** B. Szegedy. *An information theoretic approach to Sidorenko's conjecture.* arXiv preprint, 2014 (unpublished; claim not independently verified).
- **[Survey / Book]** L. Lovász. *Large Networks and Graph Limits.* AMS Colloquium Publications **60**, 2012.
- **[Survey / Book]** Y. Zhao. *Graph Theory and Additive Combinatorics: Exploring Structure and Randomness.* Cambridge University Press, 2023.

## 10. Worked Example / Concrete Special Case

**Claim.** $H = C_4$ satisfies Sidorenko: $t(C_4,W) \ge p^4$ where $p = \int_0^1\!\!\int_0^1 W$.

Define the *codegree kernel* $d(x,y) = \int_0^1 W(x,z)W(y,z)\,dz$ and the *degree function* $d(z) = \int_0^1 W(x,z)\,dx$. Then
$$t(C_4,W) = \int\!\!\int\!\!\int\!\!\int W(x_1,x_2)W(x_2,x_3)W(x_3,x_4)W(x_4,x_1) = \int\!\!\int d(x_1,x_3)^2\,dx_1dx_3 .$$

Apply Cauchy–Schwarz over the probability space $[0,1]^2$:
$$\int\!\!\int d(x_1,x_3)^2 \;\ge\; \left(\int\!\!\int d(x_1,x_3)\,dx_1dx_3\right)^{2}.$$

Now compute the inner integral by exchanging order:
$$\int\!\!\int d(x_1,x_3)\,dx_1dx_3 = \int_0^1 \left(\int_0^1 W(x,z)\,dx\right)^{2} dz = \int_0^1 d(z)^2\,dz .$$

Apply Cauchy–Schwarz again on $[0,1]$:
$$\int_0^1 d(z)^2\,dz \;\ge\; \left(\int_0^1 d(z)\,dz\right)^2 = p^2 .$$

Chaining: $t(C_4,W) \ge \left(p^2\right)^2 = p^4 = p^{e(C_4)}$. Equality holds iff $d(x,y)$ is a.e. constant and $d(z)$ is a.e. constant, which forces $W \equiv p$ a.e. — this is exactly the forcing property of $C_4$, i.e. the Chung–Graham–Wilson quasirandomness criterion.

**Numerical instance.** Take $G$ = complete bipartite $K_{n/2,n/2}$, so $p = 1/2$. Homomorphism count: $|\mathrm{Hom}(C_4,G)| = 2\,(n/2)^4 + \dots$; asymptotically $t(C_4,G) = 2\cdot(1/2)^4 = 1/8 \ge (1/2)^4 = 1/16$. The bound holds with a factor-$2$ slack, confirming $K_{n/2,n/2}$ is far from quasirandom.

**Contrast (why bipartiteness is needed).** For $H = K_3$ with the same $G$: $t(K_3,G) = 0$, whereas $p^{e(K_3)} = (1/2)^3 = 1/8 > 0$. So the inequality fails immediately for any $H$ containing an odd cycle.

**Where the method stops.** For the Möbius–Kantor graph the same peeling fails: every vertex has degree $3$, girth is $6$, and no iterated Cauchy–Schwarz over a single coordinate reduces the graph to a smaller Sidorenko instance without losing a factor $p^{\delta}$ with $\delta>0$ accumulating over $\Theta(e(H))$ steps — the concrete form of the gap in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*