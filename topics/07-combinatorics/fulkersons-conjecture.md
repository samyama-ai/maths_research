---
id: 07-combinatorics/fulkersons-conjecture
title: "Fulkerson's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Fulkerson's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/fulkersons-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Fulkerson, 1971; also called the Berge–Fulkerson conjecture).** Every bridgeless cubic graph $G$ admits a list of six perfect matchings $M_1,\dots,M_6$ (repetitions allowed) such that every edge of $G$ lies in exactly two of them.

Formally, writing $\chi^{M}\in\{0,1\}^{E(G)}$ for the incidence vector of a matching $M$, the claim is
$$\sum_{i=1}^{6}\chi^{M_i} \;=\; 2\cdot\mathbf{1}_{E(G)} .$$
Such a list is a **Fulkerson cover**. "Bridgeless" (2-edge-connected) is necessary: a cubic graph with a bridge has no perfect matching cover at all, since Petersen's theorem fails there.

A complete resolution means either (a) a proof valid for every bridgeless cubic graph — equivalently, by Section 4, for every *snark* — or (b) an explicit bridgeless cubic graph, or an infinite family, shown to have no six-matching double cover. Because the property is checkable by finite search on any fixed graph, a disproof is in principle a finite certificate; the difficulty is that the smallest counterexample, if any exists, is expected to be large and cyclically highly connected.

## 2. Mathematical Foundations

Let $G=(V,E)$ be cubic ($3$-regular) and bridgeless. A **perfect matching** $M\subseteq E$ covers every vertex exactly once; $|M|=|V|/2$ and $|E| = 3|V|/2$. Its complement $E\setminus M$ is a **2-factor** (a disjoint union of circuits).

**Petersen's theorem (1891).** Every bridgeless cubic graph has a perfect matching. More strongly, every edge lies in some perfect matching (Schönberger; Plesník: $G$ minus any two edges still has one).

**Edmonds' perfect matching polytope theorem (1965).** For any graph $G$, the convex hull $\mathrm{PM}(G)$ of incidence vectors of perfect matchings is
$$\Big\{x\in\mathbb{R}^{E}_{\ge 0} \;:\; \textstyle\sum_{e\ni v} x_e = 1\ \forall v\in V,\quad \sum_{e\in\partial(S)} x_e \ge 1 \ \ \forall S\subseteq V,\ |S| \text{ odd}\Big\}.$$
For $G$ bridgeless cubic, the uniform vector $x \equiv \tfrac13$ satisfies all constraints: degree sums give $1$, and $|\partial(S)|\ge 3$ for odd $S$ by parity plus 2-edge-connectivity. Hence
$$\tfrac13\,\mathbf{1}_{E}\in \mathrm{PM}(G),$$
so $\mathbf{1}$ is a *rational* nonnegative combination of perfect matchings. Clearing denominators: **there exists $k\ge 1$ and $3k$ perfect matchings covering each edge exactly $k$ times**. Fulkerson's conjecture is the assertion that $k=2$ always works. ($k=1$ means $G$ is 3-edge-colourable.)

**Edge colouring.** By Vizing, $\chi'(G)\in\{3,4\}$; a **snark** is a bridgeless cubic graph with $\chi'(G)=4$, usually also required to be cyclically 4-edge-connected with girth $\ge 5$ to exclude trivial modifications. The **oddness** $\omega(G)$ is the minimum number of odd circuits in a 2-factor; $\omega(G)=0 \iff \chi'(G)=3$, and $\omega$ is even.

**Related statements.**
- *Berge's conjecture*: every bridgeless cubic graph has $5$ perfect matchings whose union is $E$. Mazzuoccolo (2011) proved Berge $\iff$ Fulkerson.
- *Fan–Raspaud conjecture*: there exist perfect matchings with $M_1\cap M_2\cap M_3=\varnothing$. Implied by Fulkerson (Fan–Raspaud, 1994).
- *Jaeger's Petersen colouring conjecture*: every bridgeless cubic $G$ has a map $\phi:E(G)\to E(P)$ ($P$ = Petersen graph) sending each 3-edge-star of $G$ to a 3-edge-star of $P$. This implies Fulkerson, by pulling back a Fulkerson cover of $P$.
- *Seymour's generalization*: every $r$-graph ($r$-regular, $|\partial(S)|\ge r$ for odd $S$) has $2r$ perfect matchings covering each edge twice.

## 3. History & State of the Art (SOTA)

D. R. Fulkerson stated the conjecture in *Blocking and anti-blocking pairs of polyhedra* (Mathematical Programming 1, 1971), as an integrality question about the anti-blocking/blocking structure of the matching polyhedron: the fractional point $\tfrac13\mathbf 1$ is always feasible, and the question is how small the integral "denominator" $k$ can be forced to be. Claude Berge circulated the weaker covering form (five matchings covering $E$) in the same period; the joint name reflects Mazzuoccolo's later proof that the two are equivalent.

Milestones:
- **1979.** Seymour, *On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte* (Proc. LMS): proves the conjecture for planar bridgeless cubic graphs (via the four-colour theorem, since planar such graphs are 3-edge-colourable), and establishes the polyhedral framework and the $r$-graph generalization; proves the "$k$ exists" statement quantitatively.
- **1994.** Fan and Raspaud derive circuit-cover consequences and isolate the weaker three-matching statement.
- **2005.** Máčajová–Škoviera reformulate Fulkerson via *Fano colourings*: $G$ has a Fulkerson cover iff its edges can be coloured by points of the Fano plane $PG(2,2)$ so that each vertex star receives a line — a finite-algebraic recasting.
- **2011.** Mazzuoccolo: Berge $\iff$ Fulkerson.
- **2011–2014.** Explicit Fulkerson covers constructed for large snark families (flower snarks, Goldberg snarks, generalized Blanuša snarks, superposition families) by Fouquet–Vanherpe, Hägglund–Steffen, and others.
- **2014.** Esperet–Mazzuoccolo: infinite families of bridgeless cubic graphs whose edges cannot be covered by four perfect matchings — so the "5" in Berge's form is best possible.

## 4. Partial Results / Verified Cases

- **3-edge-colourable graphs (oddness $0$).** If $E=C_1\sqcup C_2\sqcup C_3$ is a proper 3-edge-colouring, take each colour class twice: $M_1=M_2=C_1$, etc. Every edge is in exactly two. So only snarks are at issue.
- **Planar bridgeless cubic graphs.** Immediate from the four-colour theorem (Tait's equivalence) plus the previous item.
- **Graphs with a Petersen colouring.** Any $G$ admitting Jaeger's map to $P$ inherits a Fulkerson cover from $P$'s six matchings.
- **Named snark families.** Flower snarks $J_{2k+1}$ ($k\ge2$), Goldberg snarks $G_{2k+1}$, generalized Blanuša snarks, and several superposition-generated families have explicit Fulkerson covers (Fouquet–Vanherpe 2011; Hägglund–Steffen 2014).
- **Small cases.** All snarks up to $36$ vertices have been generated (Brinkmann–Goedgebeur–Hägglund–Markström 2013); no counterexample to Fulkerson or Berge appears among them. Exhaustive Fulkerson-cover checks over the full $36$-vertex catalogue are reported in follow-up computations *(frontier — verify)*.
- **Fractional/approximate covers.** Kaiser–Král'–Norine (2006): every bridgeless cubic graph has two perfect matchings covering at least $3/5$ of the edges; a Fulkerson cover would give $4/5$ from two suitable matchings. Later work pushes the constant for three matchings above $27/35$ under extra connectivity hypotheses.
- **Weak consequences proven unconditionally.** The Fan–Raspaud statement is known for graphs of small oddness and for several structured families, though not in general.

## 5. Principal Obstacles

- **The polyhedral route stalls at the denominator.** Edmonds' theorem gives $\tfrac13\mathbf1\in\mathrm{PM}(G)$ and Carathéodory bounds the number of matchings in a rational representation by $|E|+1$, but nothing in linear programming forces the denominator down to $2$. Bounding $k$ is an integrality-gap question for which no rounding scheme is known.
- **No local structure to induct on.** Snarks are closed under no useful reduction that preserves Fulkerson covers: contracting a $4$-edge-cut or reducing a circuit typically destroys the cover or leaves a graph whose cover cannot be lifted. Attempts to prove the statement by minimal-counterexample arguments produce cyclically $5$-edge-connected, girth-$\ge6$ minimal objects about which almost nothing is known.
- **Algebraic reformulations are as hard as the original.** The Fano-colouring form replaces matchings by $PG(2,2)$-labellings; the flow/nowhere-zero form ties it to Tutte's $5$-flow and to the Petersen colouring conjecture. Each translation is an equivalence, not a simplification.
- **Counting fails.** The number of perfect matchings in a bridgeless cubic graph grows exponentially (Esperet–Kardoš–King–Král'–Norine, 2011), so matchings are plentiful — but abundance gives no control over *how they overlap*, which is the entire content of the conjecture.
- **Hardness signals.** Deciding fine-grained perfect-matching covering properties of cubic graphs is NP-hard in nearby regimes, suggesting no efficient certificate schema and blocking "search plus local repair" proofs.

## 6. The Gap

Proven: a cover with each edge covered exactly $k$ times by $3k$ matchings exists for *some* $k$ (Edmonds/Seymour), and $k=1$ exactly for 3-edge-colourable graphs. Conjectured: $k=2$ always. The gap is the absence of any uniform upper bound on $k$ over all bridgeless cubic graphs — no proof that $k \le 2$, $k\le 10$, or $k \le f(|V|)$ with $f$ bounded. Equivalently, no one can show that the smallest number of perfect matchings needed to *cover* $E$ is bounded by any constant; only the lower bound $5$ (Esperet–Mazzuoccolo) is known to be attained. Closing the gap needs a structural theorem for snarks strong enough to build six matchings simultaneously, rather than one at a time.

## 7. Current Research (as of June 2026)

- **Snark structure theory.** Groups around Máčajová and Škoviera (Comenius University, Bratislava) work on decompositions of snarks along small edge-cuts, resistance/oddness parameters, and colourings by the Fano plane and by $\mathbb{Z}_2^3$.
- **Perfect matching index.** Mazzuoccolo (Modena–Reggio Emilia), Steffen (Paderborn), and collaborators study $\tau(G)$, the minimum number of matchings covering $E$; the programme is to prove $\tau(G)\le 5$ for restricted classes (bounded oddness, cyclic connectivity $\ge 5$) and to classify the $\tau=5$ examples.
- **Computational search.** Goedgebeur and Brinkmann (Ghent) extend snark generation past $38$ vertices with Fulkerson/Berge filters attached; no counterexample has surfaced *(frontier — verify)*.
- **Petersen colouring.** Recent work of Hakobyan and Mkrtchyan on normal and strong Petersen colourings tightens the link between Jaeger's conjecture and Fulkerson.

## 8. Future Work

- Prove *any* absolute constant bound on $\tau(G)$; even $\tau\le 100$ would be a breakthrough, since it would bound the polyhedral denominator.
- Settle the Fan–Raspaud conjecture in general, as the natural weakest nontrivial consequence.
- Establish Fulkerson for all cubic graphs of oddness $\le 4$, extending the oddness-$2$ techniques based on 2-factor surgery.
- Develop a superposition calculus in which Fulkerson covers compose: if the operation used to build snarks from smaller snarks always lifts covers, the conjecture reduces to the (unknown) irreducible snarks.
- Attack Jaeger's Petersen colouring conjecture directly, which would settle Fulkerson, the cycle double cover conjecture, and the 5-flow conjecture at once.

## 9. Key References

- **[Foundational]** D. R. Fulkerson. *Blocking and anti-blocking pairs of polyhedra.* Mathematical Programming 1, 168–194, 1971.
- **[Foundational]** J. Edmonds. *Maximum matching and a polyhedron with 0,1-vertices.* Journal of Research of the National Bureau of Standards B 69, 125–130, 1965.
- **[Foundational]** P. D. Seymour. *On multi-colourings of cubic graphs, and conjectures of Fulkerson and Tutte.* Proceedings of the London Mathematical Society (3) 38, 423–460, 1979.
- **[SOTA]** G. Mazzuoccolo. *The equivalence of two conjectures of Berge and Fulkerson.* Journal of Graph Theory 68, 125–128, 2011.
- **[SOTA]** L. Esperet, G. Mazzuoccolo. *On cubic bridgeless graphs whose edge-set cannot be covered by four perfect matchings.* Journal of Graph Theory 77, 144–157, 2014.
- **[SOTA]** T. Kaiser, D. Král', S. Norine. *Unions of perfect matchings in cubic graphs.* In Topics in Discrete Mathematics, Algorithms and Combinatorics 26, Springer, 225–230, 2006.
- **[SOTA]** E. Máčajová, M. Škoviera. *Fano colourings of cubic graphs and the Fulkerson conjecture.* Theoretical Computer Science 349, 112–120, 2005.
- **[SOTA]** J.-L. Fouquet, J.-M. Vanherpe. *On Fulkerson conjecture.* Discussiones Mathematicae Graph Theory 31, 253–272, 2011.
- **[SOTA]** J. Hägglund, E. Steffen. *Petersen-colorings and some families of snarks.* Ars Mathematica Contemporanea 7, 161–173, 2014.
- **[Computational]** G. Brinkmann, J. Goedgebeur, J. Hägglund, K. Markström. *Generation and properties of snarks.* Journal of Combinatorial Theory Series B 103, 468–488, 2013.
- **[Survey]** G. Fan, A. Raspaud. *Fulkerson's conjecture and circuit covers.* Journal of Combinatorial Theory Series B 61, 133–138, 1994.
- **[Survey]** C.-Q. Zhang. *Circuit Double Cover of Graphs.* London Mathematical Society Lecture Note Series 399, Cambridge University Press, 2012.

## 10. Worked Example / Concrete Special Case

**The Petersen graph $P$.** Label outer vertices $v_1,\dots,v_5$ in a 5-cycle, inner vertices $u_1,\dots,u_5$ with $u_i \sim u_{i+2}$ (indices mod 5), and spokes $v_iu_i$. Then $|V|=10$, $|E|=15$, and $\chi'(P)=4$, so $P$ is the smallest snark and the first genuine test case.

*Counting argument.* $P$ has exactly six perfect matchings. Each has $5$ edges, so the six of them use $6\times 5=30$ edge-slots over $15$ edges. By the automorphism group $S_5$ acting edge-transitively on $P$, every edge lies in the same number of perfect matchings, namely $30/15 = 2$. Hence the full list of the six perfect matchings *is* a Fulkerson cover.

*Explicit list.* Take
$$M_0=\{v_1u_1,\;v_2u_2,\;v_3u_3,\;v_4u_4,\;v_5u_5\}\quad(\text{all spokes}),$$
and for $i=1,\dots,5$ (indices mod 5),
$$M_i=\{\,v_iv_{i+1},\;v_{i+2}v_{i+3},\;v_{i+4}u_{i+4},\;u_iu_{i+2},\;u_{i+1}u_{i+3}\,\}.$$
Check $M_1=\{v_1v_2,\;v_3v_4,\;v_5u_5,\;u_1u_3,\;u_2u_4\}$: outer vertices $v_1,v_2,v_3,v_4$ are covered by the two outer edges and $v_5$ by the spoke; inner vertices $u_1,u_3,u_2,u_4$ by the two inner edges and $u_5$ by the spoke. Five disjoint edges, all ten vertices — a perfect matching.

*Verification of the double cover.*
- Spoke $v_ju_j$: appears in $M_0$, and in exactly one $M_i$ (namely $i=j+1$, since $M_i$ contains $v_{i+4}u_{i+4}$). Count $=2$. ✔
- Outer edge $v_jv_{j+1}$: appears in $M_j$ (as its first edge) and in $M_{j-2}$ (as its second edge $v_{(j-2)+2}v_{(j-2)+3}$). No other $M_i$ contains it, and $M_0$ has no outer edge. Count $=2$. ✔
- Inner edge $u_ju_{j+2}$: appears in $M_j$ (as $u_iu_{i+2}$ with $i=j$) and in $M_{j-1}$ (as $u_{i+1}u_{i+3}$ with $i=j-1$). Count $=2$. ✔

Total: $5\cdot2 + 5\cdot2 + 5\cdot 2 = 30 = 6\cdot 5$ edge-slots, consistent. So $\sum_{i=0}^{5}\chi^{M_i}=2\cdot\mathbf 1$, and $P$ satisfies Fulkerson's conjecture — with zero slack, since $P$ has no seventh matching to choose from. This rigidity is why $P$ sits at the centre of the conjecture: any bridgeless cubic graph mapping onto $P$ in the sense of Jaeger inherits this exact cover, and the general conjecture is, in effect, the claim that every snark is "Petersen-like" enough for the same bookkeeping to close.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*