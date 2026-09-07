---
id: 07-combinatorics/babais-core-free-graph-problem
title: "Babai's Core-Free Graph Problem"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Babai's Core-Free Graph Problem

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/babais-core-free-graph-problem` · **Status:** open

## 1. Problem Statement / Conjecture

A graph $X$ is a **core** if every endomorphism of $X$ is an automorphism. A **core of** $X$ is a retract of $X$ that is a core. Every *finite* graph has a core, unique up to isomorphism (Hell–Nešetřil). A graph with no core at all is called **core-free**.

Core-free graphs exist among infinite graphs (Bauslaugh, 1995), but all known constructions are either disconnected, of unbounded degree, or of uncountable order. Babai's core-free graph problem asks whether the phenomenon survives strong local and symmetry constraints:

> **Problem.** Does there exist a connected, locally finite core-free graph? In particular, does there exist a **vertex-transitive** core-free graph?

Equivalently: is it true that every connected graph in which each vertex has finite degree admits a retract $Y \le X$ with $\operatorname{End}(Y) = \operatorname{Aut}(Y)$?

A complete solution is either (i) an explicit connected locally finite (resp. vertex-transitive) graph $X$ together with a proof that *every* retract of $X$ has a proper retract, or (ii) a proof that local finiteness plus connectivity forces the descending chain of retracts to terminate (or to have a retract as a limit). A weaker, also-open variant replaces "retract" by "homomorphically equivalent graph": does the hom-equivalence class of every connected locally finite graph contain a core?

## 2. Mathematical Foundations

All graphs are simple and undirected unless stated otherwise.

**Homomorphism.** $f : V(X) \to V(Y)$ is a homomorphism $X \to Y$ if
$$uv \in E(X) \implies f(u)f(v) \in E(Y).$$
Write $X \to Y$ if one exists. The relation $\to$ is a quasi-order on graphs; $X \leftrightarrow Y$ ("hom-equivalent") means $X \to Y$ and $Y \to X$. The quotient of $\to$ by $\leftrightarrow$ is a partial order, the **homomorphism order**, and it is a distributive lattice with meet $X \times Y$ (categorical product) and join $X \sqcup Y$.

**Retract.** An induced subgraph $Y \le X$ is a retract if there is $r : X \to Y$ with $r|_{V(Y)} = \mathrm{id}$. Then $X \leftrightarrow Y$. Retractions are exactly the idempotent endomorphisms of $X$ up to restriction of codomain.

**Core.** $X$ is a core iff $\operatorname{End}(X) = \operatorname{Aut}(X)$, iff $X$ has no proper retract, iff no proper induced subgraph $Y \subsetneq X$ satisfies $X \to Y$.

**Basic invariants.** $\chi(X) = \min\{n : X \to K_n\}$ and $\omega(X) = \max\{n : K_n \to X \text{ injectively}\}$; a homomorphism $X \to K_n$ is exactly a proper $n$-colouring. For finite $X$, $\operatorname{core}(X) \cong K_n$ iff $\chi(X) = \omega(X) = n$. Odd cycles satisfy
$$C_{2k+1} \to C_{2\ell+1} \iff k \ge \ell,$$
so $C_3 > C_5 > C_7 > \cdots$ strictly in the homomorphism order, with $K_2$ as infimum.

**Core-free.** $X$ is core-free if for every retract $Y$ of $X$ there is a retract $Z \subsetneq Y$. Equivalently, $X$ carries a strictly descending chain of retracts
$$X = Y_0 \supsetneq Y_1 \supsetneq Y_2 \supsetneq \cdots$$
that cannot be terminated, i.e. the poset of retracts of $X$ ordered by inclusion has no minimal element.

**Local finiteness.** $X$ is locally finite if $\deg(v) < \infty$ for all $v$. Connected + locally finite $\Rightarrow$ $|V(X)| \le \aleph_0$ and $\omega(X) < \infty$ on each vertex neighbourhood, though clique sizes may be unbounded globally.

**Compactness input.** De Bruijn–Erdős: for finite $k$, $\chi(X) \le k$ iff $\chi(F) \le k$ for every finite $F \subseteq X$. Equivalently $X \to K_k$ is a compact ("finitely determined") property. The core property is *not* finitely determined — this is the technical heart of the problem.

## 3. History & State of the Art (SOTA)

- **1970s–80s.** Retracts and fixed-point properties of graphs are developed by Hell, Nowakowski, Rival, Nešetřil. Welzl (1984) proves that the core of a finite vertex-transitive graph is vertex-transitive and that $|V(\operatorname{core}(X))|$ divides $|V(X)|$.
- **1990.** Hell and Nešetřil prove the $H$-colouring dichotomy: $H$-COL is polynomial if $H$ is bipartite or has a loop, NP-complete otherwise — making the core the canonical representative of a hom-equivalence class.
- **1992.** Hell and Nešetřil, *The core of a graph*, fixes terminology and proves existence/uniqueness for finite graphs by a minimal-image argument.
- **1991–95.** Babai's survey work on infinite vertex-transitive graphs and his Handbook of Combinatorics chapter foreground endomorphism monoids of infinite symmetric graphs, and the question of whether infinite transitive graphs behave like finite ones with respect to retraction. The core-free question is attributed to him in this circle; the earliest printed formulation we can verify is Bauslaugh's.
- **1995–96.** Bauslaugh, *Core-like properties of infinite graphs and structures*, isolates the notion of a core-free structure and shows core-free graphs exist; his companion paper shows compactness fails badly for cores of infinite digraphs.
- **1997.** Hahn and Tardif's survey *Graph homomorphisms: structure and symmetry* records the infinite-core problems as open and links them to transitivity.
- **2001–11.** Cameron–Kazanidis (2008) prove that for rank-3 graphs the core is either the graph itself or complete; Godsil–Royle study cores of geometric and vertex-transitive graphs. All of this is finite-side structure theory; the locally finite and transitive infinite cases remain untouched.

**SOTA summary.** Existence of core-free graphs: settled (yes, in general). Existence under connectivity + local finiteness, or under vertex-transitivity: open. No non-trivial lower-bound obstruction is known either.

## 4. Partial Results / Verified Cases

- **All finite graphs.** Every finite graph has a unique core; core-free finite graphs do not exist (Hell–Nešetřil 1992). Proof: take an endomorphism whose image is inclusion-minimal.
- **Finite vertex-transitive graphs.** The core is vertex-transitive and its order divides $|V(X)|$ (Welzl 1984). Hence any vertex-transitive counterexample must be infinite.
- **Graphs of finite chromatic number.** If $\chi(X) = k < \infty$ then $X \leftrightarrow \operatorname{core}$ of some finite graph is *not* automatic, but $X \to K_k$ and $K_{\omega} \to X$ with $\omega = \omega(X)$; if $\chi(X) = \omega(X) = k$ then $K_k$ is a retract of $X$ and $X$ has a core. This covers all perfect infinite graphs of finite clique number.
- **Graphs with a finite retract.** Any $X$ admitting a homomorphism onto a finite induced subgraph fixing it pointwise has a core (iterate finitely).
- **Countable homogeneous graphs.** The Rado graph $R$ satisfies $R \leftrightarrow K_{\aleph_0}$ and retracts onto an infinite clique, so $R$ has a core, namely $K_{\aleph_0}$, which is itself a core.
- **Disconnected / unbounded-degree case.** Core-free graphs exist: see Section 10 for a fully explicit one, $\bigsqcup_{n \ge 1} K_n$. This settles the unconstrained question and is why the problem is stated with connectivity and local finiteness.
- **Uncountable case.** Bauslaugh's constructions give core-free graphs and relational structures of arbitrary infinite cardinality, including connected ones of unbounded degree.

## 5. Principal Obstacles

- **The minimal-image argument dies.** The finite proof picks an endomorphism $f$ with $|f(V(X))|$ minimum. For infinite $X$ there is no well-founded measure: a strictly descending chain of retracts $Y_0 \supsetneq Y_1 \supsetneq \cdots$ can have all $Y_i$ of the same cardinality, and $\bigcap_i Y_i$ need be neither a retract nor even non-empty.
- **Retraction does not pass to limits.** Retractions $r_i : Y_i \to Y_{i+1}$ compose to $r_{i} \cdots r_0$, but the pointwise limit need not exist: a vertex can be moved infinitely often. Without local finiteness one cannot apply a König/compactness argument to stabilise the orbit of a vertex.
- **Compactness genuinely fails.** $X \to K_k$ is finitely determined (De Bruijn–Erdős), but "is a core" is not: every finite subgraph of a core-free graph is a core-having graph. Bauslaugh's work on infinite digraphs shows there is no compactness theorem for cores, so no finite-to-infinite transfer is available.
- **Local finiteness has no known homomorphism-order consequence.** Local finiteness bounds neighbourhood size but not clique number, odd girth, or chromatic number globally; there is no theorem saying that a connected locally finite graph is hom-equivalent to a finite graph. Indeed $\chi$ of a connected locally finite graph is at most $\aleph_0$ but can be any finite value, and no structure theory forces a stable retract.
- **Transitivity gives no descent.** Welzl's finite proof that the core of a vertex-transitive graph is vertex-transitive uses a counting/divisibility argument on $|V(X)|$, which is vacuous for infinite $X$. Nothing in the infinite case forbids a transitive graph from retracting onto a proper transitive subgraph forever.
- **No known invariant separates the classes.** To *prove* every connected locally finite graph has a core one would need a well-founded ordinal-valued invariant strictly decreasing along proper retractions; no candidate (odd girth, chromatic number, growth, ends, spectral radius) is known to be strictly monotone under retraction.

## 6. The Gap

Proven: (a) finite $\Rightarrow$ core exists; (b) general infinite $\Rightarrow$ core may fail, with explicit disconnected, unbounded-degree witnesses. The gap is the class

$$\mathcal{C} = \{\, X : X \text{ connected, } \deg_X(v) < \infty \ \forall v \,\} \quad \text{and its subclass of vertex-transitive } X.$$

Every known core-free graph exploits an infinite family of mutually non-retracting pieces (cliques of unbounded size, or components) that can be shifted "upward" forever. Connectivity forces these pieces to be joined; local finiteness forces the join to be sparse. The precise unresolved step: **must a connected locally finite graph admit a retraction whose image is fixed by all further retractions?** Bridging this requires either a new well-founded invariant on $\mathcal{C}$ that strictly drops under proper retraction, or a construction in which the infinite shifting is implemented through finite-degree connectors — i.e. simulating $\bigsqcup_n K_n$ inside a locally finite connected graph without creating a stabilising retract.

## 7. Current Research (as of June 2026)

- **Infinite homomorphism order.** Groups working on the structure of the homomorphism quasi-order (Nešetřil's school in Prague; Tardif in Kingston) study density, gaps, and dualities; the core-free question is the order-theoretic statement that the class of $X$ has no minimum representative realised as a retract.
- **Constraint-satisfaction transfer.** Infinite-domain CSP dichotomy work (Bodirsky and collaborators, Dresden/Vienna) develops model-theoretic cores for $\omega$-categorical structures, where a canonical "model-complete core" always exists. Whether an analogue can be forced by local finiteness rather than $\omega$-categoricity is an active question. *(frontier — verify)*
- **Cores of symmetric finite graphs.** Continuation of Cameron–Kazanidis and Godsil–Royle: which vertex-transitive graphs are cores, which have complete cores. Provides the finite intuition the infinite problem tests.
- **Retracts of locally finite graphs and ends.** Fixed-point and retract theory for infinite graphs via ends and metric structure (Polat's programme on retracts of infinite bridged/median graphs) yields classes where retractions stabilise; extending these stabilisation theorems beyond bridged/helly-type geometry is the nearest live line of attack. *(frontier — verify)*

## 8. Future Work

- Prove a stabilisation theorem: for connected locally finite $X$ and any chain of retractions, show that each vertex is moved only finitely often, hence the pointwise limit is a retraction onto a core. This would settle the problem affirmatively.
- Attempt the negative direction by encoding $\bigsqcup_{n\ge1} K_n$ into a connected locally finite host: replace $K_n$ by a graph of bounded degree with the same "no downward homomorphism" behaviour (e.g. Kneser graphs $K(3k-1,k)$, or high-odd-girth high-chromatic graphs à la Erdős), and link them by long paths of controlled odd length so that no retraction can collapse the linkage.
- Settle the weaker hom-equivalence version: does every connected locally finite graph have a core in its hom-equivalence class (not necessarily a retract)? A negative answer here implies a negative answer to the retract version.
- Determine whether vertex-transitivity alone (dropping local finiteness) forces a core; note that infinite transitive graphs of infinite degree already admit rich endomorphism monoids.
- Compute the complexity/descriptive-set-theoretic status: is "core-free" $\Pi^1_1$-complete for countable graphs? A completeness result would explain the absence of a structural characterisation.

## 9. Key References

- **[Foundational]** Pavol Hell, Jaroslav Nešetřil. *The core of a graph.* Discrete Mathematics, 109 (1992), 117–126.
- **[Foundational]** Pavol Hell, Jaroslav Nešetřil. *On the complexity of $H$-coloring.* Journal of Combinatorial Theory, Series B, 48 (1990), 92–110.
- **[Foundational]** Emo Welzl. *Symmetric graphs and interpretations.* Journal of Combinatorial Theory, Series B, 37 (1984), 235–244.
- **[Core-free / SOTA]** Bruce L. Bauslaugh. *Core-like properties of infinite graphs and structures.* Discrete Mathematics, 138 (1995), 101–111.
- **[Core-free / SOTA]** Bruce L. Bauslaugh. *Cores and compactness of infinite directed graphs.* Journal of Combinatorial Theory, Series B, 68 (1996), 255–276.
- **[Survey]** Geňa Hahn, Claude Tardif. *Graph homomorphisms: structure and symmetry.* In: Graph Symmetry (G. Hahn, G. Sabidussi, eds.), NATO ASI Series C 497, Kluwer, 1997, 107–166.
- **[Survey]** László Babai. *Automorphism groups, isomorphism, reconstruction.* In: Handbook of Combinatorics, Vol. 2 (R. L. Graham, M. Grötschel, L. Lovász, eds.), Elsevier / MIT Press, 1995, 1447–1540.
- **[Background]** László Babai. *Vertex-transitive graphs and vertex-transitive maps.* Journal of Graph Theory, 15 (1991), 587–627.
- **[Book]** Pavol Hell, Jaroslav Nešetřil. *Graphs and Homomorphisms.* Oxford University Press, 2004.
- **[Book]** Chris Godsil, Gordon Royle. *Algebraic Graph Theory.* Graduate Texts in Mathematics 207, Springer, 2001 (Chapter 6, Homomorphisms).
- **[Recent]** Peter J. Cameron, Priscila A. Kazanidis. *Cores of symmetric graphs.* Journal of the Australian Mathematical Society, 85 (2008), 145–154.
- **[Recent]** Chris Godsil, Gordon F. Royle. *Cores of geometric graphs.* Annals of Combinatorics, 15 (2011), 267–276.

## 10. Worked Example / Concrete Special Case

**(a) Finite warm-up: $C_5$ is a core.** Let $f \in \operatorname{End}(C_5)$. Since $\chi(C_5)=3 > 2$, $f$ cannot be non-injective: if $f$ identified two vertices, the image would be a proper subgraph of $C_5$ on $\le 4$ vertices, hence bipartite or a triangle-free graph with $\chi \le 2$, giving $C_5 \to K_2$ — impossible because $C_5$ is not bipartite. So $f$ is injective, hence bijective on a finite vertex set, hence an automorphism. Thus $\operatorname{End}(C_5) = \operatorname{Aut}(C_5) \cong D_5$ and $C_5$ is a core.

**(b) An explicit core-free graph.** Let
$$X = \bigsqcup_{n \ge 1} K_n,$$
the disjoint union of one complete graph of each finite order.

*Step 1: every retract of $X$ contains arbitrarily large cliques.* Let $r : X \to Y$ be a retraction. For each $n$, $r|_{K_n}$ is a homomorphism from a complete graph, hence injective, so $Y$ contains an induced $K_n$. Since $Y$ is an induced subgraph of $X$, $Y$ is itself a disjoint union of complete graphs, of unbounded orders $n_1 < n_2 < \cdots$ (with multiplicity).

*Step 2: every retract has a proper retract.* Fix such a $Y$ and pick any component $K_{n_1} \subseteq Y$ of minimum order. Because the orders are unbounded, there is another component $K_m \subseteq Y$ with $m > n_1$. Define $s : Y \to Y - V(K_{n_1})$ by mapping $V(K_{n_1})$ injectively onto any $n_1$ vertices of $K_m$, and fixing every other vertex. Adjacency is preserved (edges inside $K_{n_1}$ go to edges of $K_m$; there are no edges between components), and $s$ is the identity on $Y - V(K_{n_1})$, which is an induced subgraph. So $s$ is a retraction onto a *proper* retract.

*Conclusion.* No retract of $X$ is a core: $X$ is core-free. Concretely, the chain
$$\textstyle\bigsqcup_{n\ge1} K_n \;\supsetneq\; \bigsqcup_{n\ge2} K_n \;\supsetneq\; \bigsqcup_{n\ge3} K_n \;\supsetneq\; \cdots$$
consists of retracts, strictly decreasing, with empty intersection.

**(c) Why this does not answer Babai's problem.** $X$ is disconnected and has unbounded vertex degrees ($\Delta(X) = \infty$). Both features are used: the shifting map $s$ needs a *disjoint* larger clique to absorb $K_{n_1}$, and the absorbing cliques must grow without bound. Connect the components by a path and the construction breaks — a connecting path of even length lets one collapse structure, and one must check whether the linked graph now retracts onto a finite core. Making the pieces bounded-degree (say Kneser graphs $K(3k-1,k)$, which satisfy $\chi = 3$, $\omega = 2$, and admit no homomorphism from $K(3k'-1,k')$ for $k' < k$) while keeping the "shift upward forever" property inside a single connected locally finite graph is exactly the unresolved construction described in Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*