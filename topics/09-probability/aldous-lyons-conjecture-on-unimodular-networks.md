---
id: 09-probability/aldous-lyons-conjecture-on-unimodular-networks
title: "Aldous-Lyons Conjecture on Unimodular Networks"
topic: 09-probability
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Aldous-Lyons Conjecture on Unimodular Networks

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/aldous-lyons-conjecture-on-unimodular-networks` · **Status:** open

## 1. Problem Statement / Conjecture

Aldous and Lyons (2007) asked whether **every unimodular random rooted network is a Benjamini–Schramm limit of finite networks** — i.e. whether every unimodular measure is *sofic*.

**Conjecture (Aldous–Lyons, 2007).** Let $\mu$ be a probability measure on the space $\mathcal{G}_*$ of isomorphism classes of rooted, connected, locally finite networks satisfying the Mass Transport Principle. Then there is a sequence of finite networks $G_n$ with
$$U_{G_n} \xrightarrow{\ \text{weak-}*\ } \mu ,$$
where $U_{G_n}$ is the law of $G_n$ rooted at a uniformly random vertex.

Status as of 2026:

- **Refuted for networks.** Bowen, Chapman, Lubotzky and Vidick (arXiv:2408.00110, 2024; STOC 2025, best paper) constructed a unimodular random network that is not a limit of finite networks.
- **Open in the forms that carry the main consequences**: (i) does a **non-sofic group** exist (the Gromov–Weiss question)? (ii) is every unimodular random rooted **graph without marks** sofic? The page is tracked as `open` for these.

A complete resolution of (i) means exhibiting a countable group whose Cayley diagram is not a limit of finite partial Cayley diagrams, or proving all groups sofic.

## 2. Mathematical Foundations

**Rooted networks.** Fix a complete separable metric mark space $\Xi$. A *network* is a connected, locally finite graph $G=(V,E)$ with marks $m: V \cup E \to \Xi$. Let $\mathcal{G}_*$ be the set of isomorphism classes $(G,o,m)$ of networks with a distinguished root $o$, topologised by *local convergence*: $(G_n,o_n) \to (G,o)$ iff for every $r$ the balls $B_r(o_n)$ converge to $B_r(o)$ as marked rooted graphs. $\mathcal{G}_*$ is Polish. Write $\mathcal{G}_{**}$ for the space of doubly rooted networks $(G,x,y)$.

**Mass Transport Principle (MTP).** A probability measure $\mu$ on $\mathcal{G}_*$ is *unimodular* if for every Borel $f:\mathcal{G}_{**}\to[0,\infty]$,
$$\mathbb{E}_\mu\Big[\sum_{x\in V} f(G,o,x)\Big] \;=\; \mathbb{E}_\mu\Big[\sum_{x\in V} f(G,x,o)\Big].$$
"Expected mass out = expected mass in." Taking $f$ supported on adjacent pairs gives the degree-bias identities used in Section 10.

**Soficity.** For a finite network $G$, $U_G := \frac{1}{|V(G)|}\sum_{v} \delta_{(G,v)}$ is unimodular (MTP is a double-counting identity). $\mu$ is *sofic* if $\mu \in \overline{\{U_G : G \text{ finite}\}}$ in the weak-$*$ topology. Soficity is equivalent to: for every $r,\varepsilon$ there is a finite network $G$ with
$$\big\| \text{law of } B_r(o) \text{ under } U_G \;-\; \text{law of } B_r(o) \text{ under } \mu \big\|_{TV} < \varepsilon .$$
So the conjecture is a *statistical local-to-global* statement: local ball statistics consistent with the MTP should be realisable, approximately, by a finite object.

**Groups and equivalence relations.** A group $\Gamma$ with finite generating set $S$ is *sofic* iff the Dirac measure on its Cayley diagram $\mathrm{Cay}(\Gamma,S)$ (edges marked by generators) is sofic; equivalently there are maps $\phi_n:\Gamma \to \mathrm{Sym}(V_n)$ that are asymptotically homomorphic and asymptotically free in normalised Hamming distance:
$$d_H(\phi_n(g)\phi_n(h),\phi_n(gh)) \to 0,\qquad d_H(\phi_n(g),\mathrm{id}) \to 1 \ (g\neq e).$$
Hence Aldous–Lyons $\Rightarrow$ all groups sofic $\Rightarrow$ Kaplansky's direct finiteness (Elek–Szabó 2004), Gottschalk surjunctivity (Gromov 1999), the determinant conjecture and Lück approximation, and Connes embedding for $L(\Gamma)$.

## 3. History & State of the Art (SOTA)

- **1999–2000.** Gromov introduces *initially subamenable* groups; Weiss names them *sofic* and asks whether every group is sofic.
- **2001.** Benjamini and Schramm formalise local (distributional) limits of finite graphs and prove recurrence of limits of finite planar graphs with bounded degree.
- **2007.** Aldous and Lyons, *Processes on unimodular random networks* (EJP 12, paper 54), give the MTP-based axiomatisation and pose the conjecture as Question 10.1, noting it implies the sofic-groups conjecture.
- **2010–2014.** Structural theory develops: Elek–Lippner on sofic equivalence relations; Bowen's sofic entropy (JAMS 2010) makes soficity a working hypothesis in ergodic theory; Hatami–Lovász–Szegedy relate local-global convergence to the conjecture.
- **2020.** $\mathrm{MIP}^*=\mathrm{RE}$ (Ji–Natarajan–Vidick–Wright–Yuen) refutes Connes' embedding problem by an undecidability route, supplying the template.
- **2024–2025.** **Bowen–Chapman–Lubotzky–Vidick**, *Subgroup tests and the Aldous–Lyons conjecture*: a computable reduction from the Halting problem to approximation of unimodular networks yields a non-sofic unimodular network. The construction uses *subgroup tests* — property tests for membership in a subgroup of a free group — plus an undecidability argument; the counterexample is a network with marks, not a group.

## 4. Partial Results / Verified Cases

Soficity is known (unconditionally) for:

- **Amenable unimodular networks.** If the graph is a.s. amenable (more precisely, the associated equivalence relation is hyperfinite), Ornstein–Weiss quasi-tiling gives finite approximants. Covers all $\mathbb{Z}^d$-type, polynomial-growth and subexponential-growth cases.
- **Trees and treeable relations.** Every unimodular random tree is sofic; Elek–Lippner (*Sofic equivalence relations*, J. Funct. Anal. 258, 2010) prove treeable p.m.p. equivalence relations are sofic, and that soficity is closed under amenable extensions.
- **Unimodular Galton–Watson trees** with offspring law of finite mean: realised as configuration-model limits with $n$ vertices and degree distribution the size-biased law; girth $\to\infty$ gives local convergence.
- **Networks from p.m.p. actions of sofic groups** (Elek–Lippner, Păunescu): includes all residually finite groups, all finitely generated linear groups (Malcev), amenable groups, free groups, surface groups, and any group in the closure of sofic groups under direct/free/amenable extensions, direct limits and LERF constructions.
- **Random regular and biregular graphs, random planar maps.** The $d$-regular tree, the UIPT (Angel–Schramm 2003), unimodular hyperbolic triangulations of bounded degree that arise as limits.
- **Bounded degree $D\le 2$, or any $\mu$ supported on finitely many rooted isomorphism types**: trivially sofic.

No counterexample is known within any of these classes; the BCLV counterexample lives outside all of them.

## 5. Principal Obstacles

- **Probabilistic tools give no global object.** MTP is a *local* first-moment identity. It constrains the law of $B_r(o)$ but says nothing about gluing balls into a finite graph with consistent statistics — the standard failure mode of local-to-global arguments.
- **Amenability is the only known engine.** Every positive result routes through Følner/quasi-tiling or a treeing. Beyond hyperfiniteness there is no substitute: expanders inside the network make tiling arguments useless.
- **No invariants that detect non-soficity.** $\ell^2$-invariants, entropy, cost and spectral measures are all *continuous* under local convergence, so they cannot distinguish sofic from non-sofic; they were engineered to be limit-stable.
- **Computability obstruction.** BCLV's proof shows the difficulty is not analytic but logical: deciding whether a described unimodular network is sofic is at least as hard as the Halting problem. Any purely "constructive/finitary approximation" scheme must therefore fail on some inputs.
- **The group case resists the same trick.** Undecidability arguments produce *networks/relations*, and turning a non-sofic network into a non-sofic **group** requires a group-theoretic encoding (an embedding theorem in the style of Higman) compatible with the test structure — not currently available.

## 6. The Gap

Proven: soficity for amenable/treeable/sofic-group-derived networks (Section 4). Refuted: the general network statement (BCLV 2024). The remaining gap has two precise components.

1. **Marks vs. no marks.** BCLV's counterexample carries edge/vertex marks encoding a subgroup test. Whether marks can be simulated by gadget subgraphs in an *unmarked bounded-degree graph* while preserving unimodularity and non-soficity is the open technical step; the encoding is expected to work but has not been fully verified in print *(frontier — verify)*.
2. **Networks vs. groups.** Non-soficity of a unimodular network does not imply the existence of a non-sofic group. The missing step is a mechanism converting a non-sofic invariant random subgroup / test into a finitely generated group whose Cayley diagram inherits the obstruction. This is the entire content of the Gromov–Weiss question and remains untouched.

## 7. Current Research (as of June 2026)

- **BCLV programme (UT Austin, Hebrew University, Weizmann, Caltech/Weizmann).** Extending subgroup tests to *stability* questions: which subgroup tests are robustly testable, and can the reduction be pushed to group presentations *(frontier — verify)*.
- **Stability and property testing school** (Becker, Lubotzky, Thom, Chapman): permutation stability of groups and its dual relation to soficity; a non-stable-but-testable presentation would be a route to non-sofic groups.
- **Quantum-information transfer.** Adaptation of $\mathrm{MIP}^*=\mathrm{RE}$ compression to the classical/permutation setting; open whether the analogous "gap-preserving compression" exists for permutation strategies.
- **Ergodic theory response.** Re-examination of theorems assuming soficity (sofic entropy, Lück approximation): which now need hypotheses, which survive for the still-open group case.
- **Structure theory of unimodular random graphs** (Angel, Hutchcroft, Nachmias, Ray, Timár): identifying the largest natural class — e.g. unimodular planar or hyperbolic graphs — for which soficity provably holds.

## 8. Future Work

- Determine whether the BCLV counterexample can be made **mark-free and bounded-degree**.
- Decide **soficity of every unimodular random planar graph** of bounded degree — a natural class where recurrence/circle-packing tools apply.
- Develop a **non-continuous invariant** — necessarily not a local-limit-stable quantity — certifying non-soficity, perhaps of computability-theoretic type.
- Attack the **Gromov–Weiss question** via presentations: construct a group whose word problem encodes the same undecidable test.
- Classify the **complexity of soficity**: locate "is this computably described unimodular network sofic?" in the arithmetical/analytic hierarchy.

## 9. Key References

- **[Foundational]** D. Aldous, R. Lyons. *Processes on Unimodular Random Networks.* Electronic Journal of Probability **12** (2007), paper 54, 1454–1508.
- **[Foundational]** I. Benjamini, O. Schramm. *Recurrence of Distributional Limits of Finite Planar Graphs.* Electronic Journal of Probability **6** (2001), paper 23.
- **[Foundational]** M. Gromov. *Endomorphisms of symbolic algebraic varieties.* Journal of the European Mathematical Society **1** (1999), 109–197.
- **[Foundational]** B. Weiss. *Sofic groups and dynamical systems.* Sankhyā Ser. A **62** (2000), 350–359.
- **[SOTA / Recent]** L. Bowen, M. Chapman, A. Lubotzky, T. Vidick. *Subgroup tests and the Aldous–Lyons conjecture.* arXiv:2408.00110 (2024); STOC 2025.
- **[SOTA / Recent]** Z. Ji, A. Natarajan, T. Vidick, J. Wright, H. Yuen. *MIP\*=RE.* Communications of the ACM **64** (11), 2021; arXiv:2001.04383.
- **[Related]** G. Elek, G. Lippner. *Sofic equivalence relations.* Journal of Functional Analysis **258** (2010), 1692–1708.
- **[Related]** G. Elek, E. Szabó. *Sofic groups and direct finiteness.* Journal of Algebra **280** (2004), 426–434.
- **[Related]** L. Bowen. *Measure conjugacy invariants for actions of countable sofic groups.* Journal of the AMS **23** (2010), 217–245.
- **[Related]** O. Becker, A. Lubotzky, A. Thom. *Stability and invariant random subgroups.* Duke Mathematical Journal **168** (2019), 2207–2234.
- **[Related]** H. Hatami, L. Lovász, B. Szegedy. *Limits of locally–globally convergent graph sequences.* GAFA **24** (2014), 269–296.
- **[Survey]** R. Lyons, Y. Peres. *Probability on Trees and Networks.* Cambridge University Press, 2016 (Chapter 8).
- **[Survey]** V. Pestov. *Hyperlinear and sofic groups: a brief guide.* Bulletin of Symbolic Logic **14** (2008), 449–480.
- **[Survey]** N. Ozawa. *Hyperlinearity, sofic groups and applications to group theory.* Lecture notes, 2009.

## 10. Worked Example / Concrete Special Case

**The $(2,3)$-biregular tree.** Let $T$ be the infinite tree in which every vertex has degree $2$ or $3$ and neighbours always have the other degree. Root it with
$$\mathbb{P}[\deg(o)=2]=\tfrac{3}{5},\qquad \mathbb{P}[\deg(o)=3]=\tfrac{2}{5}.$$

*Check the MTP.* Take $f(T,x,y)=\mathbf{1}\{y\sim x,\ \deg x=2,\ \deg y = 3\}$:
$$\mathbb{E}\Big[\sum_y f(T,o,y)\Big] = \tfrac{3}{5}\cdot 2 = \tfrac{6}{5},\qquad
\mathbb{E}\Big[\sum_x f(T,x,o)\Big] = \tfrac{2}{5}\cdot 3 = \tfrac{6}{5}.$$
Equal, so this $f$ is balanced; since every edge of $T$ joins a degree-2 to a degree-3 vertex, all transports reduce to this identity and $\mu$ is unimodular.

*The weights are forced.* With $\mathbb{P}[\deg(o)=2]=p$ the two sides read $2p$ and $3(1-p)$, so $p=3/5$ is the only unimodular choice. Taking $p=1/2$ gives $1 \neq 3/2$: the MTP fails, and indeed no sequence of finite graphs can converge to it — in a finite bipartite biregular graph with $a$ vertices of degree $2$ and $b$ of degree $3$, edge-counting forces $2a=3b$, i.e. $a/(a+b)=3/5$.

*Soficity.* Fix $n$ and take a uniform random bipartite graph with $3n$ vertices of degree $2$ and $2n$ of degree $3$ (configuration model). The number of cycles of length $2k$ is asymptotically Poisson with bounded mean, so for any $r$ the probability that $B_r(o)$ contains a cycle is $O(1/n)$; conditionally the ball is the biregular tree ball, and the root has degree $2$ with probability exactly $3/5$. Hence $U_{G_n}\to\mu$ and $\mu$ is sofic.

*What the counterexample changes.* Here the only local constraint is a degree-balance equation, and it is exactly the MTP — local statistics determine a realisable global object. BCLV's network instead carries marks whose consistency constraints encode a subgroup test; matching the local statistics to within $\varepsilon$ by a finite network would decide whether a Turing machine halts. Unimodularity holds, finite approximation does not.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*