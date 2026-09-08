---
id: 09-probability/benjamini-schramm-nonuniqueness-conjecture
title: "Benjamini–Schramm Conjecture on Percolation Below the Uniqueness Threshold"
topic: 09-probability
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Benjamini–Schramm Conjecture on Percolation Below the Uniqueness Threshold

> **Topic:** Probability & Stochastic Processes · **ID:** `09-probability/benjamini-schramm-nonuniqueness-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Let $G=(V,E)$ be an infinite, connected, locally finite, **quasi-transitive** graph (the automorphism group $\operatorname{Aut}(G)$ has finitely many orbits on $V$). Run Bernoulli($p$) bond percolation. Define

$$p_c(G)=\inf\{p:\ \mathbb{P}_p[\exists\ \text{infinite cluster}]=1\},\qquad p_u(G)=\inf\{p:\ \mathbb{P}_p[\exists!\ \text{infinite cluster}]=1\}.$$

**Conjecture (Benjamini–Schramm, 1996).** $p_c(G)<p_u(G)$ if and only if $G$ is **nonamenable**.

The "only if" direction is a theorem (Burton–Keane, 1989): amenable quasi-transitive graphs have $p_c=p_u$. The open direction is:

> For every nonamenable quasi-transitive graph $G$, $p_c(G)<p_u(G)$; equivalently, there is a nonempty **nonuniqueness phase** $(p_c,p_u)$ in which infinitely many infinite clusters coexist almost surely.

A complete proof must produce, for an arbitrary nonamenable quasi-transitive $G$, some $p>p_c(G)$ at which the number of infinite clusters is a.s. $\infty$ — or exhibit a nonamenable counterexample with $p_c=p_u$. The group-theoretic restatement: *every nonamenable finitely generated group has $p_c<p_u$ in every one of its Cayley graphs.*

## 2. Mathematical Foundations

**Amenability.** For $K\subset V$ finite, $\partial_E K$ is the edge boundary. The edge-Cheeger constant is

$$\iota_E(G)=\inf_{K\subset V,\ |K|<\infty}\frac{|\partial_E K|}{|K|}.$$

$G$ is nonamenable iff $\iota_E(G)>0$. **Kesten's criterion:** for a $d$-regular transitive $G$ with simple random walk spectral radius $\rho(G)=\limsup_n p_n(v,v)^{1/n}$, nonamenability $\iff \rho(G)<1$, and $\iota_E(G)>0$ implies $\rho\le\sqrt{1-(\iota_E/d)^2}$.

**Cluster count.** Let $N\in\{0,1,\dots,\infty\}$ be the number of infinite clusters. By ergodicity of $\mathbb{P}_p$ under a transitive subgroup, $N$ is a.s. constant; by Newman–Schulman (1981), $N\in\{0,1,\infty\}$; by Burton–Keane (1989), $N=\infty$ is impossible when $\operatorname{Aut}(G)$ is amenable and transitive (the trifurcation-counting argument needs a Følner sequence).

**Monotonicity.** Häggström–Peres (1999, unimodular case) and Schonmann (1999, general quasi-transitive): if $\mathbb{P}_p[N=1]=1$ and $p<p'$ then $\mathbb{P}_{p'}[N=1]=1$. Hence the phase diagram is a clean triple

$$[0,p_c):\ N=0,\qquad (p_c,p_u):\ N=\infty,\qquad (p_u,1]:\ N=1,$$

and the conjecture is exactly the statement that the middle interval is nonempty for nonamenable $G$.

**Unimodularity.** $\Gamma\le\operatorname{Aut}(G)$ is unimodular if $|\Gamma_x y|=|\Gamma_y x|$ for all $x,y$ ($\Gamma_x$ = stabiliser). Unimodularity licenses the **mass-transport principle**: for $F:V\times V\to[0,\infty]$ diagonally $\Gamma$-invariant,

$$\sum_{y\in V}F(x,y)=\sum_{y\in V}F(y,x).$$

This is the workhorse of the whole theory. Cayley graphs are unimodular; some transitive graphs (e.g. grandparent graphs, Diestel–Leader graphs) are not.

**Structural theorems in the nonuniqueness phase.** For unimodular transitive $G$ and $p\in(p_c,p_u)$: every infinite cluster has $2^{\aleph_0}$ ends and is itself nonamenable (Benjamini–Lyons–Peres–Schramm, GAFA 1999); all infinite clusters are indistinguishable by $\Gamma$-invariant properties (Lyons–Schramm, 1999). At criticality, $\theta(p_c)=0$ for nonamenable unimodular transitive graphs (BLPS, Ann. Probab. 1999).

**Useful bounds.** For $d$-regular transitive $G$: $p_c\ge 1/(d-1)$; and $p_u\ge \frac{1}{2}\big(1-\sqrt{1-\rho^{-2}}\big)$-type spectral lower bounds hold via Schonmann's connectivity estimates, giving $p_c<p_u$ whenever $\rho(G)$ is small enough relative to $d$.

## 3. History & State of the Art (SOTA)

- **1981–1989.** Newman–Schulman prove $N\in\{0,1,\infty\}$; Burton–Keane give the trifurcation proof of uniqueness on $\mathbb{Z}^d$ and amenable transitive graphs.
- **1990.** Grimmett–Newman, *Percolation in $\infty+1$ dimensions*: on $T_k\times\mathbb{Z}$ with $k$ large, there is an interval of $p$ with infinitely many infinite clusters. First nonuniqueness phase outside a tree.
- **1996.** Benjamini and Schramm, *Percolation beyond $\mathbb{Z}^d$*, pose the conjecture together with $p_c<1$ for transitive graphs of superlinear growth (later proved by Duminil-Copin–Goswami–Raoufi–Severo–Yadin, 2020).
- **1998–2001.** Lalley (Fuchsian groups) and Benjamini–Schramm (hyperbolic plane, JAMS 2001) settle the planar hyperbolic case; BLPS build the invariant-percolation toolkit; Häggström–Peres and Schonmann prove uniqueness monotonicity; Pak–Smirnova-Nagnibeda settle the conjecture "up to change of generating set"; Schonmann gives spectral criteria.
- **2020.** Hutchcroft proves the conjecture for **all nonunimodular** quasi-transitive graphs (JAMS) and for **nonelementary hyperbolic groups** (GAFA), the two largest new classes in two decades.
- **Status.** Open in general; the hard residual case is unimodular, one-ended, non-hyperbolic — above all Kazhdan groups and lattices in higher-rank simple Lie groups.

## 4. Partial Results / Verified Cases

| Class | Result |
|---|---|
| Trees $T_k$, $k\ge3$ | $p_c=1/(k-1)<p_u=1$. Elementary. |
| Transitive graphs with infinitely many ends | $p_u=1>p_c$ (nonamenable, $p_c<1$). |
| $T_k\times\mathbb{Z}$, $k$ large | Grimmett–Newman (1990); later all $k\ge3$ and $T_k\times\mathbb{Z}^d$. |
| Planar nonamenable transitive graphs; Fuchsian groups | Lalley (1998); Benjamini–Schramm, JAMS (2001) — here $p_c<p_u<1$ and duality gives $p_u=1-p_c^\dagger$. |
| High girth / small spectral radius | Schonmann (2001): $p_c<p_u$ when $\rho(G)$ is sufficiently small for the degree, and mean-field exponents hold throughout $(p_c,p_u)$. |
| Every nonamenable group, **some** generating set | Pak–Smirnova-Nagnibeda (2000): each nonamenable f.g. group admits a finite generating set whose Cayley graph has $p_c<p_u$ (spectral radius can be pushed low; cf. Thom, IMRN 2015). |
| Nonunimodular quasi-transitive graphs | Hutchcroft, JAMS 33 (2020): $p_c<p_u$ always, plus triangle condition and mean-field exponents at $p_c$. |
| Nonelementary Gromov-hyperbolic groups (all Cayley graphs) | Hutchcroft, GFA (2020). |
| Groups with a nonamenable free-ish subgroup structure, free products, direct products $\Gamma_1\ast\Gamma_2$ | Nonuniqueness by end/tree-decomposition arguments. |

## 5. Principal Obstacles

- **Nonamenability is a "soft" hypothesis.** $\iota_E>0$ gives no local geometry — no dual graph, no tree structure, no boundary at infinity. Every proved case exploits extra structure (planarity, hyperbolic boundary, product structure, a nonunimodular scaling homomorphism). No proof uses nonamenability alone.
- **The unimodular obstruction.** Hutchcroft's nonunimodular proof uses the modular function $\Delta$ as a genuine weight: a nonunimodular graph carries a nontrivial $\Gamma$-invariant multiplicative "height", which forces clusters to be tree-like at scale. Unimodular graphs have $\Delta\equiv1$, so this entire mechanism vanishes.
- **No lower bound on $p_u$ from soft data.** Bounding $p_u$ from below requires controlling two-point functions $\tau_p(x,y)$ at long range; the available tools (spectral bounds $\tau_p(x,y)\lesssim \rho^{|x-y|}$-style estimates) only bite when $\rho$ is small, i.e. when the graph is already "almost a tree". Groups with property (T) have $\rho$ bounded away from $0$ uniformly over generating sets in the relevant regime.
- **No upper bound on $p_c$ that is sharp enough.** For a fixed nonamenable graph one can bound $p_c\le$ something in terms of $\iota_E$, but the gap between the best $p_c$-upper and $p_u$-lower bounds closes only in extreme geometry.
- **Kazhdan groups resist invariant-percolation arguments.** Property (T) kills many invariant random subgraph constructions (no invariant percolation with expected degree close to $d$ and infinitely many ends), which is precisely what a naive proof would need.

## 6. The Gap

Proven: $p_c<p_u$ for nonunimodular quasi-transitive graphs, hyperbolic groups, planar nonamenable graphs, products with trees, small-spectral-radius graphs, and every nonamenable group in *some* Cayley graph. Conjectured: the same for *every* nonamenable quasi-transitive graph.

The gap is a single missing implication:

$$\iota_E(G)>0 \ \Longrightarrow\ \exists\, p>p_c(G)\ \text{with}\ \mathbb{P}_p[N=\infty]=1,$$

for **unimodular, one-ended, non-hyperbolic** $G$. Concretely: exhibit at some $p>p_c$ either (i) a $\Gamma$-invariant percolation with infinitely many infinite clusters dominated by $\mathbb{P}_p$, or (ii) a quantitative decay $\sum_x \tau_p(o,x)^2 < \infty$-type condition surviving past $p_c$. The Pak–Smirnova-Nagnibeda theorem shows the obstruction is not group-theoretic but **generating-set dependent**: one must transport nonuniqueness from a good generating set to an arbitrary one, and no such transport principle exists — $p_c$ and $p_u$ are not quasi-isometry invariants.

## 7. Current Research (as of June 2026)

- **Hutchcroft's programme (Caltech).** Extending the nonunimodular/hyperbolic techniques: relative isoperimetry, anchored expansion, and two-point-function differential inequalities. Recent work on locality of $p_c$ and on percolation for graphs with "enough" hyperbolic directions.
- **Measured group theory bridge.** Gaboriau–Lyons (Invent. Math. 2009) used the nonuniqueness phase (via Pak–Smirnova-Nagnibeda's good generating set) to solve von Neumann's problem measurably. Conversely, cost/$\ell^2$-Betti-number invariants are being probed as certificates for $p_c<p_u$ — a group with first $\ell^2$-Betti number $\beta_1^{(2)}>0$ has free uniform spanning forest with infinitely many trees, which is a nonuniqueness-type statement. Whether $\beta_1^{(2)}>0$ implies $p_c<p_u$ in every Cayley graph remains open *(frontier — verify)*.
- **Kazhdan groups.** Hutchcroft–Pete, *Kazhdan groups have cost one* (Invent. Math. 2020), used invariant percolation to settle Gaboriau's cost question; the analogous "cheap" invariant subgraphs are being reused to attack $p_u$ bounds for property (T) lattices *(frontier — verify)*.
- **Random-cluster and long-range analogues.** Nonuniqueness phases for FK-percolation and for long-range models on nonamenable groups, where continuity/discontinuity of the phase transition interacts with $p_u$.
- **Groups:** Caltech (Hutchcroft), Rényi Institute (Pete, Timár), Indiana (Lyons), Weizmann/Tel Aviv (Benjamini), Geneva (Smirnova-Nagnibeda).

## 8. Future Work

- Find an invariant-percolation criterion depending only on $\iota_E$ and degree that forces trifurcations to survive — a "reverse Burton–Keane".
- Prove $p_c<p_u$ for all unimodular transitive graphs with **anchored expansion** plus one-endedness, then remove the extra hypothesis.
- Settle the smallest hard test cases: cocompact lattices in $\mathrm{SL}_3(\mathbb{R})$, $\mathrm{Sp}(n,1)$-lattices with unusual generating sets, and $\Gamma_1\times\Gamma_2$ with $\Gamma_i$ nonamenable (where $p_u$ can be pushed close to $p_c$).
- Determine whether the conjecture is generating-set-robust: is $\{S: p_c(G,S)<p_u(G,S)\}$ all finite generating sets, given it is nonempty?
- Establish the triangle condition on $(p_c,p_u)$ for unimodular graphs, which would give mean-field behaviour and, combined with a $p_u$ lower bound, the strict inequality.

## 9. Key References

- **[Foundational]** I. Benjamini, O. Schramm. *Percolation beyond $\mathbb{Z}^d$, many questions and a few answers.* Electronic Communications in Probability 1 (1996), 71–82.
- **[Foundational]** R. M. Burton, M. Keane. *Density and uniqueness in percolation.* Communications in Mathematical Physics 121 (1989), 501–505.
- **[Foundational]** C. M. Newman, L. S. Schulman. *Infinite clusters in percolation models.* Journal of Statistical Physics 26 (1981), 613–628.
- **[Foundational]** G. Grimmett, C. M. Newman. *Percolation in $\infty+1$ dimensions.* In *Disorder in Physical Systems*, Oxford University Press, 1990, 167–190.
- **[Foundational]** I. Benjamini, R. Lyons, Y. Peres, O. Schramm. *Group-invariant percolation on graphs.* Geometric and Functional Analysis 9 (1999), 29–66.
- **[Foundational]** I. Benjamini, R. Lyons, Y. Peres, O. Schramm. *Critical percolation on any nonamenable group has no infinite clusters.* Annals of Probability 27 (1999), 1347–1356.
- **[Foundational]** O. Häggström, Y. Peres. *Monotonicity of uniqueness for percolation on Cayley graphs: all infinite clusters are born simultaneously.* Probability Theory and Related Fields 113 (1999), 273–285.
- **[Foundational]** R. H. Schonmann. *Stability of infinite clusters in supercritical percolation.* Probability Theory and Related Fields 113 (1999), 287–300.
- **[Foundational]** R. Lyons, O. Schramm. *Indistinguishability of percolation clusters.* Annals of Probability 27 (1999), 1809–1836.
- **[Partial results]** S. P. Lalley. *Percolation on Fuchsian groups.* Annales de l'Institut Henri Poincaré, Probabilités et Statistiques 34 (1998), 151–177.
- **[Partial results]** I. Pak, T. Smirnova-Nagnibeda. *On non-uniqueness of percolation on nonamenable Cayley graphs.* Comptes Rendus de l'Académie des Sciences Paris, Série I 330 (2000), 495–500.
- **[Partial results]** I. Benjamini, O. Schramm. *Percolation in the hyperbolic plane.* Journal of the American Mathematical Society 14 (2001), 487–507.
- **[Partial results]** R. H. Schonmann. *Multiplicity of phase transitions and mean-field criticality on highly non-amenable graphs.* Communications in Mathematical Physics 219 (2001), 271–322.
- **[SOTA / Recent]** T. Hutchcroft. *Nonuniqueness and mean-field criticality for percolation on nonunimodular transitive graphs.* Journal of the American Mathematical Society 33 (2020), 1101–1165.
- **[SOTA / Recent]** T. Hutchcroft. *Percolation on hyperbolic groups.* Geometric and Functional Analysis, 2020.
- **[SOTA / Recent]** T. Hutchcroft, G. Pete. *Kazhdan groups have cost one.* Inventiones Mathematicae 221 (2020), 873–891.
- **[SOTA / Recent]** H. Duminil-Copin, S. Goswami, A. Raoufi, F. Severo, A. Yadin. *Existence of phase transition for percolation using the Gaussian free field.* Duke Mathematical Journal 169 (2020), 3539–3563.
- **[Related]** D. Gaboriau, R. Lyons. *A measurable-group-theoretic solution to von Neumann's problem.* Inventiones Mathematicae 177 (2009), 533–540.
- **[Survey / Book]** R. Lyons, Y. Peres. *Probability on Trees and Networks.* Cambridge University Press, 2016 (Chapters 7–8).

## 10. Worked Example / Concrete Special Case

Take $G=T_3$, the $3$-regular tree ($\iota_E(T_3)=1>0$, $\rho=2\sqrt2/3\approx0.943$), and $p=3/4$.

**Step 1 — $p_c$.** Exploring from a root, each vertex has $2$ forward children, so the exploration is a Galton–Watson process with mean offspring $2p$. Survival iff $2p>1$, so $p_c(T_3)=1/2$.

**Step 2 — branch extinction at $p=3/4$.** Let $s$ be the probability that a given forward branch (edge plus everything beyond) is finite. Conditioning on the edge and the two children edges below it:

$$s=(1-p)+p\,s^2 \ \Longrightarrow\ p s^2-s+(1-p)=0 \ \Longrightarrow\ s\in\Big\{1,\ \tfrac{1-p}{p}\Big\}.$$

For $p>1/2$ the relevant root is $s=(1-p)/p$; at $p=3/4$, $s=1/3$. Percolation probability: $\theta(3/4)=1-s^3=1-\tfrac1{27}=\tfrac{26}{27}$.

**Step 3 — forced nonuniqueness.** Fix a vertex $v$. Let $A$ be the event that all three edges at $v$ are closed, and $B$ the event that each of the three neighbouring subtrees (each a rooted tree where the root has $2$ children) is infinite. Given $A$, the three subtrees are independent; each is infinite with probability $1-q$ where $q=s^2=1/9$, i.e. $8/9$. Hence

$$\mathbb{P}_{3/4}[A\cap B]=\Big(\tfrac14\Big)^3\Big(\tfrac89\Big)^3=\frac{1}{64}\cdot\frac{512}{729}=\frac{8}{729}\approx 1.10\times10^{-2}>0.$$

On $A\cap B$ the three infinite clusters are pairwise disjoint (any path between them would pass through $v$, which is isolated). So $\mathbb{P}[N\ge3]>0$, and by the Newman–Schulman $0$–$1$ law $N=\infty$ a.s. Since this works for every $p<1$, $p_u(T_3)=1$ and

$$p_c(T_3)=\tfrac12<1=p_u(T_3).$$

**Why this does not generalise.** The argument used that deleting one vertex disconnects $T_3$ into three infinite pieces — an infinitely-many-ends property. On a one-ended nonamenable graph such as a cocompact lattice in $\mathbb{H}^3$ or in $\mathrm{SL}_3(\mathbb{R})$, no finite set separates the graph into three infinite pieces, so isolating a vertex creates no clusters at all. For the hyperbolic case one recovers nonuniqueness from the boundary circle/sphere (Benjamini–Schramm 2001; Hutchcroft 2020); for higher-rank lattices, no substitute for either mechanism is known. That is exactly the gap of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*