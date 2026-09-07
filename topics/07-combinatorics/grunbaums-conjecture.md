---
id: 07-combinatorics/grunbaums-conjecture
title: "Grünbaum's Conjecture"
topic: 07-combinatorics
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Grünbaum's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/grunbaums-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

Grünbaum's conjecture (1969) asserts:

> If $G$ is a simple cubic graph that has a **polyhedral embedding** in some closed **orientable** surface $\Sigma$, then $G$ is 3-edge-colorable, i.e. $\chi'(G) = 3$.

For the sphere this is exactly the Four Colour Theorem, restated through Tait's 1880 equivalence, so the conjecture was proposed as the natural genus-$g$ generalization of map colouring. Equivalently, in the contrapositive: **no snark** (a cyclically 4-edge-connected cubic graph of girth $\ge 5$ with $\chi'=4$) admits a polyhedral embedding in an orientable surface.

Orientability is not decorative. The Petersen graph embeds polyhedrally in the projective plane (Section 10), so the non-orientable analogue is false outright; the conjecture is precisely about whether orientability rescues the Tait mechanism.

**Current status.** The conjecture as stated is **false**: Kochol (2009) constructed snarks with polyhedral embeddings in orientable surfaces. What survives, and is the live problem, is the *small-genus* question: for which genera $g \ge 1$ is every cubic graph polyhedrally embedded in the orientable surface $S_g$ 3-edge-colorable? A full resolution means determining the least $g$ admitting a polyhedrally embedded snark, and proving 3-edge-colorability below it.

## 2. Mathematical Foundations

**Cubic graphs and edge colouring.** $G=(V,E)$ is cubic if every vertex has degree 3. By Vizing's theorem $\chi'(G) \in \{3,4\}$ for cubic $G$; graphs with $\chi'(G)=4$ are *class 2*. A proper 3-edge-colouring is equivalently a nowhere-zero $\mathbb{Z}_2\times\mathbb{Z}_2$-flow, or a partition of $E$ into three perfect matchings.

**Snark.** A cubic, bridgeless, cyclically 4-edge-connected graph with girth $\ge 5$ and $\chi'=4$. The smallest is the Petersen graph $P$ ($|V|=10$, $|E|=15$).

**Embeddings.** An embedding of $G$ in a closed surface $\Sigma$ is *cellular* if every face is homeomorphic to an open disc. Euler's formula gives
$$|V| - |E| + |F| = \chi(\Sigma) = 2 - 2g \quad (\text{orientable genus } g),\qquad \chi = 2 - k \ \ (\text{non-orientable genus } k).$$
For cubic $G$, $|E| = \tfrac32|V|$, hence
$$|F| = \chi(\Sigma) + \tfrac12 |V|.$$

**Face-width (representativity).**
$$\rho(G,\Sigma) \;=\; \min\{\, |C \cap G| \;:\; C \subset \Sigma \text{ a noncontractible simple closed curve}\,\}.$$

**Polyhedral embedding.** An embedding is polyhedral iff $G$ is simple and $\rho(G,\Sigma)\ge 3$; equivalently every face is bounded by an induced cycle and any two distinct faces meet in at most one vertex or one edge. This is the combinatorial abstraction of the face lattice of a convex polytope's boundary, which is why the sphere case reduces to 3-connected planar graphs (Steinitz).

**Tait's theorem (sphere only).** A bridgeless cubic plane graph has $\chi'=3$ iff its faces are properly 4-colorable; with the Four Colour Theorem this gives $\chi'(G)=3$ for every 3-connected cubic planar $G$. The proof uses the Klein four-group $\{1,a,b,c\}$: colour edges by the "difference" of the two incident face colours,
$$\varphi(uv) = f(F_1)\cdot f(F_2)^{-1},$$
which is well-defined and proper only because in the plane every edge lies on exactly two faces and face colourings are globally consistent. For $g\ge 1$ no such equivalence exists — face 4-colouring is neither necessary nor sufficient, and the Heawood bound $\big\lfloor (7+\sqrt{1+48g})/2 \big\rfloor$ exceeds 4 already for $g=1$.

## 3. History & State of the Art (SOTA)

- **1880.** Tait reduces the Four Colour Problem to 3-edge-colouring cubic planar maps.
- **1969.** Branko Grünbaum poses the conjecture as "Conjecture 6" in *Recent Progress in Combinatorics* (Tutte, ed.), explicitly as a genus-$g$ strengthening of the then-unproved Four Colour Conjecture.
- **1976–77.** Appel and Haken prove the Four Colour Theorem, settling the case $g=0$; Robertson–Sanders–Seymour–Thomas (1997) give a second, verified proof.
- **1990s–2000s.** Mohar and Thomassen's *Graphs on Surfaces* (2001) systematizes face-width; large face-width becomes the standard route to "planar-like" behaviour on higher surfaces, and the conjecture is repeatedly listed as a central open problem in topological graph theory.
- **2006.** Mohar and Vodopivec, *On polyhedral embeddings of cubic graphs*, analyze which snarks embed polyhedrally, settle the non-orientable side, and produce the small-genus tools.
- **2008.** Vodopivec rules out polyhedral embeddings of snarks in the torus.
- **2009.** **Kochol disproves the conjecture** (*Polyhedral embeddings of snarks in orientable surfaces*, Proc. AMS): snarks with polyhedral embeddings in orientable surfaces exist, and the construction yields infinitely many of unbounded genus.

SOTA is therefore a *refuted* global conjecture with an open quantitative core: the exact orientable genus threshold, and the behaviour under stronger connectivity or larger face-width.

## 4. Partial Results / Verified Cases

- **Genus 0 (sphere).** True. Equivalent to the Four Colour Theorem (Appel–Haken 1977; Robertson–Sanders–Seymour–Thomas 1997). Polyhedral $=$ 3-connected planar here.
- **Genus 1 (torus).** True: no snark has a polyhedral embedding in the torus (Vodopivec 2008). Equivalently every simple cubic graph with $\rho \ge 3$ in $S_1$ is 3-edge-colorable.
- **Small genus generally.** Counterexamples are known only at comparatively large genus; the smallest few positive genera above the torus remain unresolved — the residual open range. *(frontier — verify the exact minimum genus attained by Kochol-type constructions.)*
- **Non-orientable surfaces.** False, minimally: the Petersen graph embeds polyhedrally in the projective plane $N_1$ (Section 10). Mohar–Vodopivec (2006) extend this to families of snarks in non-orientable surfaces.
- **Minor-closed classes.** Every cubic graph with no Petersen minor is 3-edge-colorable (Tutte's conjecture; Robertson–Seymour–Thomas, completed with Edwards–Sanders–Seymour–Thomas 2016). Any polyhedrally embedded cubic graph avoiding a Petersen minor therefore satisfies the conclusion regardless of genus.
- **Structural restrictions.** Cubic graphs embedded with large face-width inherit many planar-type properties (Mohar–Thomassen), but 3-edge-colourability is *not* among the properties known to follow.
- **Counting constraint.** By Euler's formula, a snark on $n$ vertices polyhedrally embedded in $S_g$ needs girth $\ge5$, so $2|E| \ge 5|F|$ gives $g \ge 1 + \tfrac{n}{20}\cdot\big(\tfrac{?}{}\big)$-type bounds; concretely $|F| \le \tfrac{2|E|}{5} = \tfrac{3n}{5}$, hence $2-2g \le \tfrac{3n}{5} - \tfrac{n}{2}$, i.e. $g \ge 1 - \tfrac{n}{20}$ — vacuous, which is exactly why no easy Euler obstruction exists.

## 5. Principal Obstacles

- **No Tait duality beyond the sphere.** The group-difference argument converting face colourings into edge colourings needs the plane's global 2-colourability of the face adjacency structure. On $S_g$ with $g\ge1$, a face 4-colouring gives no edge colouring, and the Heawood bound permits 7 colours on the torus. Every classical map-colouring technique (discharging, reducible configurations, unavoidable sets) is thereby cut off from the edge-colouring conclusion.
- **Discharging does not close.** Discharging proofs need an Euler-formula "charge deficit"; on $S_g$ the total charge is $\propto \chi(\Sigma) = 2-2g \le 0$, so there is no surplus to distribute and no forced small configuration.
- **Face-width is the wrong invariant.** Large face-width forces local planarity — locally the graph looks planar — but 3-edge-colourability is a *global* parity/flow property. Kochol's construction exploits exactly this: snark obstructions are assembled from locally planar, high-face-width pieces glued around handles.
- **Class-2-ness is not local.** Deciding $\chi'(G)=3$ for cubic graphs is NP-complete (Holyer 1981), so no local structural certificate can exist in general; any proof must use the topology as a genuine global hypothesis, not as a supply of local reductions.
- **Orientability enters only through the cycle space.** The only known way orientability helps is via nowhere-zero flows and $\mathbb{Z}_2$-homology of the embedding, and current flow theory (Tutte's 5-flow, cycle double covers) is itself open in the relevant range.

## 6. The Gap

Proven: genus $0$ (Four Colour Theorem) and genus $1$ (Vodopivec). Refuted: genus large enough for Kochol's snark constructions, plus every non-orientable surface. The gap is the *finite unresolved window* of orientable genera between the torus and the smallest genus at which a polyhedrally embedded snark is known, together with two qualitative questions:

1. Is there a threshold $g_0$ such that the conjecture holds for all $g < g_0$ and fails for all $g \ge g_0$? Monotonicity in $g$ is not known — adding a handle neither obviously preserves nor destroys polyhedrality.
2. Does a strengthened hypothesis restore the conclusion? Candidates: face-width $\ge f(g)$ growing with genus, cyclic 5-edge-connectivity, or every face bounded by a cycle of length $\le 5$.

Crossing the gap means either a genus-2/3/4 analogue of the Four Colour Theorem's discharging machinery adapted to surfaces with $\chi \le -2$, or an explicit polyhedrally embedded snark of minimal genus.

## 7. Current Research (as of June 2026)

- **Minimum-genus search.** Computational work enumerates snarks (the Brinkmann–Goedgebeur snark catalogues, complete to 36 vertices) and computes their orientable genus and face-width, aiming to certify or exclude polyhedral embeddings at genus 2–4. Genus computation is NP-hard, so searches use SAT/ILP encodings of rotation systems. *(frontier — verify)*
- **Flow-theoretic reformulations.** Groups in Slovenia (Ljubljana), Slovakia (Bratislava, Kochol's school) and Ghent (Goedgebeur) relate polyhedral embeddings of snarks to cycle double covers: a polyhedral embedding of $G$ in an orientable surface is a *circular* double cover by induced cycles, tightening the Cycle Double Cover Conjecture into the same territory.
- **Local planarity programmes.** Continuations of Mohar–Thomassen ask which planar theorems survive at face-width $\ge k$; 3-edge-colourability is a benchmark negative instance and helps calibrate the general theory.
- **Non-orientable classification.** Determining exactly which snarks embed polyhedrally in $N_k$ for each $k$, following Mohar–Vodopivec.

## 8. Future Work

- Settle genus 2 outright — the smallest surface where both a proof and a counterexample are conceivable with current tools.
- Prove or refute monotonicity: if a snark embeds polyhedrally in $S_g$, does one embed in $S_{g+1}$?
- Formulate the "right" repaired conjecture: e.g. every cyclically 5-edge-connected cubic graph with $\rho \ge 4$ in an orientable surface is 3-edge-colorable, and test it against Kochol's family.
- Extract from Kochol's counterexamples a *quantitative* lower bound on the genus of any polyhedrally embedded snark, closing the window from below.
- Machine-checked discharging over surfaces: adapt the RSST formalization to $\chi(\Sigma)<0$, where charge is negative and the discharging calculus must be replaced by a deficiency argument.

## 9. Key References

- **[Foundational]** B. Grünbaum. *Conjecture 6.* In W. T. Tutte (ed.), *Recent Progress in Combinatorics*, Academic Press, 1969, p. 343.
- **[Foundational]** P. G. Tait. *Remarks on the colouring of maps.* Proceedings of the Royal Society of Edinburgh 10 (1880), 729.
- **[Foundational]** K. Appel and W. Haken. *Every planar map is four colorable, Part I: Discharging;* with J. Koch, *Part II: Reducibility.* Illinois Journal of Mathematics 21 (1977), 429–490, 491–567.
- **[SOTA / Recent]** M. Kochol. *Polyhedral embeddings of snarks in orientable surfaces.* Proceedings of the American Mathematical Society 137 (2009), 1613–1619.
- **[SOTA / Recent]** B. Mohar and A. Vodopivec. *On polyhedral embeddings of cubic graphs.* Combinatorics, Probability and Computing 15 (2006), 877–893.
- **[SOTA / Recent]** A. Vodopivec. *On embeddings of snarks in the torus.* Discrete Mathematics 308 (2008), 1847–1849.
- **[SOTA / Recent]** N. Robertson, D. Sanders, P. Seymour, R. Thomas. *The four-colour theorem.* Journal of Combinatorial Theory Series B 70 (1997), 2–44.
- **[SOTA / Recent]** K. Edwards, D. P. Sanders, P. Seymour, R. Thomas. *Three-edge-colouring doublecross cubic graphs.* Journal of Combinatorial Theory Series B 119 (2016), 66–95.
- **[Survey]** B. Mohar and C. Thomassen. *Graphs on Surfaces.* Johns Hopkins University Press, 2001.
- **[Survey]** G. Brinkmann, J. Goedgebeur, J. Hägglund, K. Markström. *Generation and properties of snarks.* Journal of Combinatorial Theory Series B 103 (2013), 468–488.
- **[Background]** I. Holyer. *The NP-completeness of edge-coloring.* SIAM Journal on Computing 10 (1981), 718–720.

## 10. Worked Example / Concrete Special Case

**The Petersen graph in the projective plane — why orientability is essential.**

Take the dodecahedron $D$: 20 vertices, 30 edges, 12 pentagonal faces, embedded in $S^2$. Quotient by the antipodal map $x \mapsto -x$, a fixed-point-free involution. The quotient surface is the projective plane $N_1$, and the quotient graph is the *hemi-dodecahedron*:
$$|V| = 20/2 = 10, \qquad |E| = 30/2 = 15, \qquad |F| = 12/2 = 6.$$
Euler check:
$$10 - 15 + 6 = 1 = \chi(N_1). \checkmark$$
This quotient graph is the **Petersen graph** $P$: it is cubic, has girth 5, and every face is a pentagon (an induced 5-cycle). Two distinct pentagonal faces share at most one edge, and no noncontractible curve meets the graph in fewer than 3 points, so $\rho(P,N_1)=3$ and the embedding is **polyhedral**.

Now check the colouring. Suppose $\chi'(P)=3$. A 3-edge-colouring partitions $E(P)$ into three perfect matchings, each of size $15/3 = 5$. Removing a perfect matching from $P$ leaves a 2-factor, i.e. a disjoint union of cycles covering all 10 vertices. Since $P$ has girth 5 and no two disjoint 5-cycles that together span $V(P)$ — every 5-cycle in $P$ has the property that the five vertices outside it induce a 5-cycle *plus* the removed matching is not perfect — the only candidate 2-factors would be $5+5$ or a single 10-cycle. A $5+5$ 2-factor is impossible (the complement of any 5-cycle in $P$ induces a 5-star, not a 5-cycle), and a Hamiltonian 2-factor is impossible because $P$ is non-Hamiltonian. Hence no perfect matching has a cycle-complement, $\chi'(P)=4$, and $P$ is a snark.

**Conclusion drawn from the example.** $P$ is a snark with a polyhedral embedding in a closed surface, so the hypothesis "polyhedral embedding" alone cannot force $\chi'=3$; Grünbaum's restriction to orientable surfaces is forced by this single 10-vertex example. Kochol's 2009 theorem shows the restriction is still not enough: replacing $N_1$ by a suitable orientable $S_g$, snarks with polyhedral embeddings exist there too. What the example leaves open — and what Section 6 isolates — is how many handles are actually needed.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*