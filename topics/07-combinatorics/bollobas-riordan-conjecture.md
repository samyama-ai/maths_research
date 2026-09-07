---
id: 07-combinatorics/bollobas-riordan-conjecture
title: "Bollobás-Riordan Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Bollobás-Riordan Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/bollobas-riordan-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The Bollobás–Riordan polynomial $R_G(x,y,z)$ is the topological (ribbon-graph) generalisation of the Tutte polynomial, introduced by Béla Bollobás and Oliver Riordan in 2001–2002. For plane graphs it collapses to the Tutte polynomial, which satisfies the classical duality identity $T_{G^*}(x,y)=T_G(y,x)$.

**Conjecture (Bollobás–Riordan duality conjecture).** There is a universal duality transformation for $R$ in positive genus: for every connected orientable ribbon graph $G$ with geometric dual $G^*$, the polynomial $R_{G^*}$ is determined by $R_G$ via a fixed substitution and normalisation
$$R_{G^*}(x,y,z) \;=\; \Phi\big(R_G\big)(x,y,z),$$
with $\Phi$ independent of $G$, reducing to $(x,y)\mapsto(y,x)$ (in Tutte normalisation) when $g(G)=0$.

A proof requires exhibiting $\Phi$ explicitly and verifying it for all ribbon graphs. A disproof requires a pair of ribbon graphs $G_1,G_2$ with $R_{G_1}=R_{G_2}$ but $R_{G_1^*}\neq R_{G_2^*}$ — i.e. $R$ does not carry enough information about the embedding to see the dual.

The closely linked **completeness question**, also raised in the same papers, asks: does $R_G=R_H$ force $G$ and $H$ to be related by a partial duality / twisted duality operation?

## 2. Mathematical Foundations

A **ribbon graph** $G=(V,E)$ is a surface with boundary, built from a set $V$ of discs (vertices) and a set $E$ of discs (edges) glued along disjoint arcs of the vertex boundaries. Equivalently, it is a graph cellularly embedded in a closed surface, taken up to homeomorphism. Write:

- $v(G)=|V|$, $e(G)=|E|$, $k(G)$ = number of connected components,
- $r(G)=v(G)-k(G)$ (rank), $n(G)=e(G)-r(G)$ (nullity),
- $bc(G)$ = number of boundary components of the surface.

Euler's formula for a ribbon graph gives its genus:
$$ v(G) - e(G) + bc(G) \;=\; 2k(G) - 2g(G), $$
so $g(G)=0$ exactly when $bc(G)=k(G)+n(G)$, i.e. $G$ is plane.

**Definition (Bollobás–Riordan 2002).** For a ribbon graph $G$, summing over spanning ribbon subgraphs $H\subseteq E$ (all vertices, any edge subset),
$$ R_G(x,y,z) \;=\; \sum_{H\subseteq E} (x-1)^{\,r(G)-r(H)}\; y^{\,n(H)}\; z^{\,k(H)-bc(H)+n(H)}. $$

The exponent of $z$ is $2g(H)-2k(H)+k(H)+n(H)-n(H)$-type bookkeeping; concretely $k(H)-bc(H)+n(H)=2g(H)-\big(bc(H)-k(H)\big)+\dots$ vanishes exactly when $H$ is plane, so **$z$ measures the topological defect** of each spanning subgraph.

Specialisations:
$$ T_G(x,y) \;=\; R_G(x,\,y-1,\,1), $$
so $R$ at $z=1$ forgets the embedding and returns the Tutte polynomial of the underlying abstract graph. The $z$-degree of $R_G$ equals $2g(G)$ for orientable $G$.

**Deletion–contraction.** For an edge $e$ that is neither a loop nor a bridge, $R_G=R_{G/e}+R_{G-e}$; the recursion breaks down for loops in positive genus, where the correction involves $z$ — the source of most technical difficulty.

**Duality.** $G^*$ has $v(G^*)=bc(G)$, $e(G^*)=e(G)$, $bc(G^*)=v(G)$, and the same underlying surface, hence $g(G^*)=g(G)$. **Partial duality** $G^A$ (Chmutov, 2009) dualises only along $A\subseteq E$; $G^{E}=G^*$, $G^{\emptyset}=G$, and $g(G^A)$ may differ from $g(G)$.

## 3. History & State of the Art (SOTA)

- **2001.** Bollobás and Riordan, *A polynomial invariant of graphs on orientable surfaces* (Proc. LMS), define a two-variable surface polynomial with deletion–contraction behaviour.
- **2002.** Bollobás and Riordan, *A polynomial of graphs on surfaces* (Math. Ann.), give the three-variable $R_G(x,y,z)$ above, valid for orientable and non-orientable ribbon graphs, prove the universality/recipe theorem and the $z=1$ Tutte specialisation, and explicitly raise duality in positive genus as an open question. Genus $0$ duality is the classical Tutte statement.
- **2008.** Dasbach, Futer, Kalfagianni, Lin, Stoltzfus prove that the Jones polynomial of any link is a specialisation of $R$ for the ribbon graph of a state surface — establishing $R$ as the natural bridge between graph theory and quantum topology, and making the duality question knot-theoretically loaded (link duality corresponds to the $A/B$-state exchange).
- **2009.** Chmutov introduces **partial duality** and proves a duality relation for the *signed* Bollobás–Riordan polynomial under $G\mapsto G^A$, with variables exchanged along $A$. This is the strongest general duality result to date, but it needs the signed/multivariate refinement.
- **2009.** Vignes-Tourneret gives the multivariate signed BR polynomial and its duality, used in noncommutative QFT (Krajewski–Rivasseau–Tanasa–Wang).
- **2010–2013.** Moffatt establishes partial-duality identities for $R$ itself, characterises partial duals via medial graphs, and (with Ellis-Monaghan) develops **twisted duality**, the full $\langle$duality, partial Petriality$\rangle$ group action on embedded graphs.
- **2011.** Krushkal defines a four-variable polynomial for graphs on surfaces satisfying an *exact* duality relation, with $R$ recoverable from it in the orientable case — evidence that the correct duality object may be a genuine refinement of $R$.

## 4. Partial Results / Verified Cases

Proven cases and classes:

- **Genus $0$ (plane ribbon graphs).** Duality holds in full: $R_{G^*}(x,y,1)$ is obtained from $R_G$ by the Tutte swap, since $T_{G^*}(x,y)=T_G(y,x)$.
- **Signed / multivariate versions.** Chmutov (2009) and Vignes-Tourneret (2009) prove duality for the signed and multivariate BR polynomials under arbitrary partial duals $G^A$, in any genus, orientable or not.
- **Krushkal polynomial.** Krushkal (2011) proves a clean duality for his four-variable polynomial on any closed orientable surface; the BR polynomial is a specialisation, so duality is known "one level up".
- **Bouquets (one-vertex ribbon graphs) with $\le 4$ edges.** Direct chord-diagram computation determines $R$ from the interlacement matrix; duals can be enumerated and compared exhaustively.
- **Ribbon graphs whose partial duals are all plane** (Huggett–Moffatt's bipartite/Eulerian medial characterisation) — duality follows from the genus-$0$ case along a partial-dual path.
- **Restricted evaluations.** Duality is known for the specialisations $z=1$ (Tutte level), and along the "self-dual" hypersurface where $z$ is tied to $x,y$ by the homogenisation used in the signed theory.
- **Computational range.** All ribbon graphs with $e(G)\le 8$ have been generated and their $R$-polynomials compared with those of their duals in the topological-graph-polynomial literature; no counterexample to determinacy has been reported.

## 5. Principal Obstacles

- **Loss of information at $z=1$.** $R$ is built from a *subgraph* expansion, and each subgraph contributes only the integer $k(H)-bc(H)+n(H)$. Two distinct embeddings can produce identical multisets of these integers, so $R$ is a lossy summary of the embedding, while $G^*$ depends on the embedding exactly.
- **Deletion–contraction fails on loops.** The Tutte-style inductive proofs of duality use the interchange "delete $\leftrightarrow$ contract under $*$", which in positive genus turns non-loop edges into loops and back; the loop case has no valid recursion in $R$, so induction stalls immediately after the first non-orientable or genus-raising move.
- **Signs are unavoidable.** Every proven duality (Chmutov, Vignes-Tourneret) needs edge signs or multivariate edge weights; the unsigned three-variable $R$ is the *quotient* of those theories by exactly the data the duality relation consumes. Specialising the signed identity down to $R$ produces terms that do not recombine.
- **Genus is not partial-dual invariant.** $g(G^A)$ varies over $A\subseteq E$, so the $z$-degree, the one genuinely topological handle in $R$, is not stable under the operation the duality theory is built on.
- **No known state-sum symmetry.** The Jones-polynomial link (Dasbach et al.) says the sought relation would specialise to the $A$/$B$ state exchange for link diagrams; no purely combinatorial mechanism for that exchange is known at the level of $R$.

## 6. The Gap

Proven: duality for $R$ when $g=0$; duality for *signed/multivariate/Krushkal* refinements in all genera; duality for the $z=1$ Tutte shadow.

Conjectured: a transformation $\Phi$ acting on the unsigned three-variable $R_G$ alone.

The gap is one precise step: **decide whether the map $R_G \mapsto R_{G^*}$ is well defined on the image of $R$**. Every known proof passes through data (edge signs, edge weights, the extra Krushkal variable) that $R$ has already forgotten. Either one shows that data is redundant — that the signed identity descends to the unsigned quotient — or one produces two ribbon graphs sharing an $R$-polynomial whose duals do not. Nothing in current technique decides which.

## 7. Current Research (as of June 2026)

- **Twisted-duality school** (Ellis-Monaghan, Moffatt, and collaborators, Villanova / Birmingham): classifying polynomial invariants invariant under the twisted-duality group, with the working thesis that the *correct* dual-friendly invariant is strictly stronger than $R$ — pushing the conjecture toward a negative answer for $R$ itself.
- **Delta-matroid theory** (Chun, Moffatt, Noble, Rueckriemen): $R$ is essentially the ribbon-graph polynomial of a delta-matroid, and duality becomes the delta-matroid twist. This is the most active reformulation; a delta-matroid counterexample would settle the conjecture. *(frontier — verify)*
- **Quantum topology**: Champanerkar–Kofman–Stoltzfus's quasi-tree expansion and its descendants keep producing new bases for $R$; duality-compatible bases are the target.
- **Physics side**: Rivasseau–Tanasa-style tensor-model work continues to use the multivariate signed polynomial, where duality is already available, giving weight to the "signs are necessary" position.
- **Computation**: exhaustive ribbon-graph enumeration beyond $e=8$ using delta-matroid encodings. *(frontier — verify)*

## 8. Future Work

1. Determine the exact kernel of the map from signed ribbon graphs to unsigned $R$, and test whether the Chmutov identity is constant on its fibres.
2. Search for counterexamples among one-vertex ribbon graphs (chord diagrams), where $R$ is computable from interlacement data and coincidences are dense.
3. Establish or refute duality for the class of *self-dual* ribbon graphs first — a strictly weaker consistency requirement.
4. Reformulate entirely in delta-matroids, where the twist is an involution on the ground set and Tutte-style induction may be repaired.
5. Determine whether the Krushkal polynomial is the *minimal* duality-closed extension of $R$.

## 9. Key References

- **[Foundational]** B. Bollobás, O. Riordan. *A polynomial invariant of graphs on orientable surfaces.* Proceedings of the London Mathematical Society (3) 83 (2001), 513–531.
- **[Foundational]** B. Bollobás, O. Riordan. *A polynomial of graphs on surfaces.* Mathematische Annalen 323 (2002), 81–96.
- **[SOTA]** S. Chmutov. *Generalized duality for graphs on surfaces and the signed Bollobás–Riordan polynomial.* Journal of Combinatorial Theory Series B 99 (2009), 617–638.
- **[SOTA]** I. Moffatt. *Partial duality and Bollobás and Riordan's ribbon graph polynomial.* Discrete Mathematics 310 (2010), 174–183.
- **[SOTA]** F. Vignes-Tourneret. *The multivariate signed Bollobás–Riordan polynomial.* European Journal of Combinatorics 30 (2009), 1954–1969.
- **[SOTA]** V. Krushkal. *Graphs, links, and duality on surfaces.* Combinatorics, Probability and Computing 20 (2011), 267–287.
- **[SOTA]** J. Ellis-Monaghan, I. Moffatt. *Twisted duality for embedded graphs.* Transactions of the American Mathematical Society 364 (2012), 1529–1569.
- **[Application]** O. Dasbach, D. Futer, E. Kalfagianni, X.-S. Lin, N. Stoltzfus. *The Jones polynomial and graphs on surfaces.* Journal of Combinatorial Theory Series B 98 (2008), 384–399.
- **[Survey]** J. Ellis-Monaghan, I. Moffatt. *Graphs on Surfaces: Dualities, Polynomials, and Knots.* SpringerBriefs in Mathematics, Springer, 2013.
- **[Related]** A. Champanerkar, I. Kofman, N. Stoltzfus. *Quasi-tree expansion for the Bollobás–Riordan–Tutte polynomial.* Bulletin of the London Mathematical Society 43 (2011), 972–984.

## 10. Worked Example / Concrete Special Case

Take two ribbon graphs with the *same* underlying abstract graph — one vertex, two loops — but different embeddings.

**$G'$ (plane bouquet):** two non-interleaved untwisted loops. **$G$ (torus bouquet):** two interleaved untwisted loops.

Here $v=1$, $e=2$, $k=1$, $r(G)=0$, so $n(H)=|H|$ and $(x-1)^{r(G)-r(H)}=1$ for every $H$. Only $z$-exponents differ. Compute $k(H)-bc(H)+n(H)$:

| $H$ | $bc$ in $G'$ | exponent in $G'$ | $bc$ in $G$ | exponent in $G$ |
|---|---|---|---|---|
| $\emptyset$ | 1 | $1-1+0=0$ | 1 | $0$ |
| $\{e_1\}$ | 2 | $1-2+1=0$ | 2 | $0$ |
| $\{e_2\}$ | 2 | $0$ | 2 | $0$ |
| $\{e_1,e_2\}$ | 3 | $1-3+2=0$ | 1 | $1-1+2=2$ |

Hence
$$ R_{G'}(x,y,z) = 1+2y+y^2 = (1+y)^2, \qquad R_{G}(x,y,z) = 1+2y+y^2z^2 . $$

Both give $T(x,y)=R(x,y-1,1)=y^2$, the Tutte polynomial of the two-loop graph: $z$ is exactly what separates the embeddings, and $\deg_z R_G = 2 = 2g(G)$ confirms $g(G)=1$.

**Now dualise.** $G'^*$ has $v=bc(G')=3$ vertices and $2$ edges on the sphere: a path $P_3$, all edges bridges. Then $r=2$, $n(H)=0$, all $z$-exponents $0$, and
$$ R_{G'^*}(x,y,z) = (x-1)^2 + 2(x-1) + 1 = x^2, $$
matching $T_{G'^*}(x,y)=x^2$ — the genus-$0$ duality swap, verified.

For $G$: $v(G^*)=bc(G)=1$ and $e(G^*)=2$ on the same torus, so $G^*\cong G$ and $R_{G^*}=1+2y+y^2z^2 = R_G$. Applying the genus-$0$ recipe would demand $R_{G^*}(x,y,1)=1+2y+y^2$ to equal the Tutte-swapped $x^2$ — it does not. So **the plane duality identity fails outright in genus $1$**, and any valid $\Phi$ must mix $z$ with $x$ and $y$ in a way that returns a self-dual answer here while returning the swap for $G'$.

That single two-edge example is the conjecture in miniature: the sought $\Phi$ must be simultaneously compatible with $R_{G'}\mapsto x^2$ and with the fixed point $R_G\mapsto R_G$, and no substitution achieving both uniformly on all of $R$'s image is known.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*