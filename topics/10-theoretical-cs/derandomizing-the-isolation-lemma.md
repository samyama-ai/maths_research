---
id: 10-theoretical-cs/derandomizing-the-isolation-lemma
title: "Derandomizing the Isolation Lemma"
topic: 10-theoretical-cs
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Derandomizing the Isolation Lemma

> **Topic:** Theoretical Computer Science · **ID:** `10-theoretical-cs/derandomizing-the-isolation-lemma` · **Status:** open

## 1. Problem Statement / Conjecture

The Isolation Lemma of Mulmuley, Vazirani and Vazirani (1987) says that a *random* small-integer weighting of a ground set makes the minimum-weight member of any nonempty set family unique, with high probability. It is the engine behind the RNC algorithm for perfect matching, the $\mathrm{NL} \subseteq \mathrm{UL}/\mathrm{poly}$ collapse, and many polynomial identity testing (PIT) hitting-set constructions.

**The problem.** Construct such weightings *deterministically*.

> **Conjecture (deterministic isolation for matching).** There is a logspace-uniform circuit family of depth $\mathrm{polylog}(n)$ and size $\mathrm{poly}(n)$ that, given a graph $G$ on $n$ vertices with $m$ edges, outputs a list $w_1,\dots,w_k$ of edge weight functions $w_j : E \to \{1,\dots,\mathrm{poly}(n)\}$, with $k = \mathrm{poly}(n)$, such that if $G$ has a perfect matching then some $w_j$ assigns a *unique* minimum weight to a perfect matching.

Such a construction would place perfect matching in $\mathrm{NC}$, resolving a question open since Karp, Upfal and Wigderson (1986). A complete solution is either an explicit construction with a proof of the isolation guarantee, or a proof that no such family exists in the stated resource bounds (a conditional impossibility, since the object is known to exist non-uniformly by counting).

## 2. Mathematical Foundations

**Set systems and weights.** Let $[m]=\{1,\dots,m\}$ and let $\mathcal{F} \subseteq 2^{[m]}$ be a nonempty family. For $w:[m]\to\mathbb{Z}$ put $w(S)=\sum_{i\in S} w(i)$. Say $w$ **isolates** $\mathcal{F}$ if
$$\big|\;\arg\min_{S\in\mathcal{F}} w(S)\;\big| = 1 .$$

**Isolation Lemma (MVV 1987).** If $w(1),\dots,w(m)$ are drawn independently and uniformly from $\{1,\dots,N\}$, then for every nonempty $\mathcal{F}\subseteq 2^{[m]}$,
$$\Pr_w\big[\,w \text{ does not isolate } \mathcal{F}\,\big] \;\le\; \frac{m}{N}.$$
*Proof sketch (threshold/"union of ambiguous elements"):* element $i$ is *ambiguous* if some minimum-weight set contains it and some does not; fixing all $w(j)$, $j\ne i$, there is exactly one value of $w(i)$ making $i$ ambiguous, so $\Pr[i \text{ ambiguous}] \le 1/N$; union bound over $i$. Non-uniqueness implies some element is ambiguous.

The lemma is **oblivious**: $\mathcal{F}$ may be arbitrary and is never inspected. Note $|\mathcal{F}|$ can be $2^{\Omega(m)}$.

**Derandomized form.** A family $W=\{w_1,\dots,w_k\}$ of weight functions with $\|w_j\|_\infty \le W_{\max}$ is **isolating for a class $\mathcal{C}$ of set systems** if for every $\mathcal{F}\in\mathcal{C}$ some $w_j$ isolates $\mathcal{F}$. The three cost parameters are $k$ (list length), $W_{\max}$ (weight magnitude), and the parallel complexity of producing $W$.

**Why matching.** For a bipartite graph $G=(U\cup V,E)$, $|U|=|V|=n$, with edge weights $w$, form the Tutte/Edmonds matrix
$$A_w[i,j] \;=\; \begin{cases} 2^{\,w(u_iv_j)} & u_iv_j \in E,\\ 0 & \text{otherwise,}\end{cases} \qquad \det(A_w)=\sum_{\sigma} \mathrm{sgn}(\sigma)\prod_i 2^{\,w(u_iv_{\sigma(i)})}.$$
If $w$ isolates the set of perfect matchings $\mathcal{M}(G)$, the minimum-weight matching contributes a term $\pm 2^{W_{\min}}$ that no other term cancels, so $\det(A_w)\ne 0$ and the matching is read off from the largest power of $2$ dividing $\det(A_w)$ — all in $\mathrm{NC}^2$ by Berkowitz/Csanky determinant evaluation. Randomness is the *only* obstacle.

**Geometric reformulation.** $\mathcal{M}(G)$ is the vertex set of the perfect matching polytope $P(G)\subseteq \mathbb{R}^E$. Isolation $=$ finding an objective $w$ whose optimal face of $P$ is a single vertex. For bipartite $G$, $P(G)$ is the Birkhoff-type polytope $\{x\ge 0: \sum_{j} x_{ij}=1, \sum_i x_{ij}=1\}$, and the relevant certificate is the **circulation**: for a cycle $C=(e_1,\dots,e_{2\ell})$ with alternating orientation,
$$\mathrm{circ}_w(C) \;=\; \sum_{t=1}^{2\ell} (-1)^t\, w(e_t).$$
Two perfect matchings $M_1\ne M_2$ satisfy $w(M_1)=w(M_2)$ iff the alternating cycles of $M_1\triangle M_2$ have circulations summing to zero. Hence: **$w$ isolates $\mathcal{M}(G)$ if $\mathrm{circ}_w(C)\ne 0$ for every cycle $C$ in the union of minimum-weight matchings.**

## 3. History & State of the Art (SOTA)

- **1979–1986.** Lovász's randomized matching test via the Tutte matrix; Karp–Upfal–Wigderson give RNC search algorithms and pose $\mathrm{NC}$ matching.
- **1987.** Mulmuley, Vazirani and Vazirani prove the Isolation Lemma and give the clean RNC$^2$ matching algorithm above (*Combinatorica* 7).
- **1995.** Chari, Rohatgi and Srinivasan give randomness-optimal isolation, cutting $O(m\log m)$ random bits to $O(m)$ using limited independence and hashing, and show that schemes valid for *arbitrary* set systems cannot do essentially better.
- **1999–2000.** Allender, Reinhardt and Zhou; Reinhardt and Allender: min-weight isolation for $s$–$t$ paths yields $\mathrm{NL} \subseteq \mathrm{UL}/\mathrm{poly}$, and full derandomization would give $\mathrm{NL}=\mathrm{UL}$.
- **2007–2010.** Agrawal, Hoang and Thierauf put polynomially bounded matching in $\mathrm{NC}^2$; Datta, Kulkarni and Roy isolate matchings deterministically in bipartite planar graphs.
- **2008.** Arvind and Mukhopadhyay show black-box derandomization of the lemma for circuit-described families implies circuit lower bounds — the first evidence that the *general* statement is hard.
- **2016–2017.** The breakthrough: Fenner, Gurjar and Thierauf put bipartite perfect matching in **quasi-$\mathrm{NC}^2$** ($n^{O(\log n)}$ processors, $O(\log^2 n)$ depth) with quasi-polynomial weights; Svensson and Tarnawski extend to general graphs; Gurjar and Thierauf to linear matroid intersection.
- **2018–2021.** Gurjar, Thierauf and Vishnoi generalize to polytopes with totally unimodular faces via lattice arguments; Anari and Vazirani obtain genuine $\mathrm{NC}$ for **planar** perfect matching.

**SOTA summary.** Bipartite and general matching: quasi-$\mathrm{NC}$, not $\mathrm{NC}$. Planar: $\mathrm{NC}$. General set systems: no nontrivial deterministic isolation, and provably none without circuit lower bounds.

## 4. Partial Results / Verified Cases

| Class | Result | Reference |
|---|---|---|
| Bipartite $G$, $\mathcal{M}(G)$ | isolating family of size $n^{O(\log n)}$, weights $n^{O(\log n)}$; quasi-$\mathrm{NC}^2$ | Fenner–Gurjar–Thierauf 2016 |
| General $G$, $\mathcal{M}(G)$ | quasi-$\mathrm{NC}$ | Svensson–Tarnawski 2017 |
| Planar $G$ (bipartite and general) | $\mathrm{NC}$, $\mathrm{poly}(n)$ weights | Anari–Vazirani 2020; Datta–Kulkarni–Roy 2010 (bipartite planar, $\mathrm{SPL}$) |
| Constant genus, small clique-width, $K_{3,3}$-free | $\mathrm{NC}$ / $\mathrm{poly}$-size isolating families | Datta et al.; Eppstein–Vazirani |
| Graphs with $\mathrm{poly}(n)$-many perfect matchings | $\mathrm{NC}^2$ (weights $2^i$ on $O(\log n)$ "hashed" buckets) | Agrawal–Hoang–Thierauf 2007 |
| Linear matroid intersection | quasi-$\mathrm{NC}^2$ | Gurjar–Thierauf 2017 |
| Polytopes whose faces have totally unimodular descriptions | quasi-$\mathrm{NC}$ vertex isolation | Gurjar–Thierauf–Vishnoi 2021 |
| ROABPs (read-once oblivious ABPs) | isolation of a monomial $\Rightarrow$ $n^{O(\log n)}$ hitting sets | Agrawal–Gurjar–Korwar–Saxena 2015 |
| $s$–$t$ paths, directed reachability | isolation in $\mathrm{UL}/\mathrm{poly}$; planar reachability in $\mathrm{UL}$ | Reinhardt–Allender 2000; Bourke–Tewari–Vinodchandran 2009 |

Also known: **pseudo-deterministic** $\mathrm{NC}$ for bipartite matching (Goldwasser–Grossman 2017) — a randomized algorithm returning the *same* canonical matching on almost all random strings, which is weaker than derandomization.

## 5. Principal Obstacles

- **Obliviousness is provably too strong.** A single family isolating *every* $\mathcal{F}\subseteq 2^{[m]}$ must be exponentially large: there are $2^{2^m}$ set systems, and each fixed $w$ with weights $\le W_{\max}$ isolates only a vanishing fraction. Any derandomization must therefore exploit the *structure* of $\mathcal{F}$ (matchings, bases, monomials), and structure re-enters through combinatorial arguments that do not transfer between classes.
- **Circuit-lower-bound barrier.** Arvind and Mukhopadhyay show that a black-box isolating family for set systems presented by small circuits implies a separation — informally, either $\mathrm{NEXP}\not\subseteq \mathrm{P}/\mathrm{poly}$ or the permanent has no polynomial-size arithmetic circuits. Full derandomization is thus at least as hard as a major lower bound, mirroring the Kabanets–Impagliazzo phenomenon for PIT.
- **The quasi-polynomial wall.** The FGT scheme is a $\log n$-round induction: round $i$ kills all cycles of length $\le 2^i$ in the current tight subgraph using $\mathrm{poly}(n)$ candidate weights, then scales. Each round multiplies both the list length and the weight magnitude by $\mathrm{poly}(n)$, giving $n^{\Theta(\log n)}$. Collapsing to $\mathrm{poly}(n)$ needs the rounds to be *reused* or handled in parallel; no known argument bounds the interaction between the surviving long cycles and the weights already committed.
- **Counting arguments give no construction.** A union bound shows $O(m)$ weight functions with weights $\le 2m$ suffice for any *fixed* $\mathcal{F}$, but the choice depends on $\mathcal{F}$; making it uniform is exactly the open part.
- **Algebraic tools do not localize.** Determinant identities certify *existence* of a matching but say nothing about uniqueness; Fourier/entropy methods measure global bias, whereas isolation is a statement about a single optimal face, a measure-zero event.

## 6. The Gap

Proven (Section 4): quasi-polynomial-size isolating families for matching, matroid intersection, and TU-face polytopes; polynomial-size families for planar and bounded-genus graphs.

Wanted (Section 1): $\mathrm{poly}(n)$-size families with $\mathrm{poly}(n)$ weights for general bipartite graphs.

The gap is one quantifier of depth: the FGT induction spends a fresh independent block of randomness on each of the $\log n$ scales of cycle length, so the total entropy is $\Theta(\log^2 n)$ bits, while $\mathrm{NC}$ demands $O(\log n)$. The precise open step is:

> **Find a single $\mathrm{poly}(n)$-size family $W$ of weight functions such that for every bipartite $G$ some $w\in W$ gives nonzero circulation to *every* cycle of $G$ simultaneously** — not merely to short cycles, and without re-randomizing per scale.

Equivalently: exhibit a $\mathrm{poly}(n)$-size hitting set for the (exponentially many) linear forms $\mathrm{circ}_{\cdot}(C)$ indexed by cycles $C$, exploiting that these forms are the $\pm 1$ vectors of the cycle space of $G$, a lattice of dimension $m-n+1$.

## 7. Current Research (as of June 2026)

- **Lattice and TU methods.** The Gurjar–Thierauf–Vishnoi program recasts isolation as finding a vector not orthogonal to any short lattice vector of the face lattice; active groups at IIT Bombay (Gurjar), Aalen/Ulm (Thierauf), and EPFL (Svensson) push toward polytopes beyond total unimodularity — in particular the matroid *union* and $b$-matching polytopes. *(frontier — verify)*
- **Isolation and PIT.** The Saxena school (IIT Kanpur) continues to trade isolation for hitting sets: isolating a monomial in a sparse/ROABP setting yields quasi-polynomial blackbox PIT, and any polynomial-size improvement in one direction transfers to the other.
- **Planar to bounded genus to general.** Following Anari–Vazirani, work on extending the matching-polytope-based $\mathrm{NC}$ algorithm to one-crossing-minor-free and bounded-genus classes continues; the obstacle is that planarity supplies a $\mathrm{poly}$-size cycle basis with a canonical orientation, absent in general.
- **Barrier refinement.** Whether *non-black-box* derandomization (algorithms allowed to read $G$) escapes the Arvind–Mukhopadhyay lower-bound implication is an open meta-question actively discussed; the matching case is non-black-box, which is why quasi-$\mathrm{NC}$ was achievable at all.
- **Pseudo-determinism.** Extending Goldwasser–Grossman to general graphs and to $\mathrm{NC}$ search problems more broadly. *(frontier — verify)*

## 8. Future Work

1. **Amortize the FGT rounds.** Design weights whose round-$i$ component is a deterministic *function* of the round-$(i-1)$ tight subgraph rather than fresh randomness; a $\mathrm{poly}$-size list would follow if the dependence were $O(\log n)$-bit.
2. **Cycle-space hitting sets.** Prove or refute: there is an explicit $\mathrm{poly}(n)$-size set $W \subseteq \{1,\dots,\mathrm{poly}(n)\}^E$ hitting all nonzero vectors of the cycle space of every graph on $n$ vertices under the pairing $\langle w, \cdot\rangle$.
3. **Structural shrinkage lemmas.** Sharpen the FGT lemma bounding the size of the tight subgraph after killing short cycles; a bound of $n + O(1)$ edges after $O(1)$ rounds would give $\mathrm{NC}$.
4. **Unconditional lower bounds on isolating families** for matching, to show quasi-polynomial is optimal for the circulation approach.
5. **Transfer to $\mathrm{NL}$ vs $\mathrm{UL}$**: derandomize min-weight path isolation for planar/bounded-treewidth digraphs, then general.

## 9. Key References

- **[Foundational]** K. Mulmuley, U. V. Vazirani, V. V. Vazirani. *Matching is as easy as matrix inversion.* Combinatorica 7(1):105–113, 1987.
- **[Foundational]** R. M. Karp, E. Upfal, A. Wigderson. *Constructing a perfect matching is in random NC.* Combinatorica 6(1):35–48, 1986.
- **[Foundational]** S. Chari, P. Rohatgi, A. Srinivasan. *Randomness-optimal unique element isolation with applications to perfect matching and related problems.* SIAM Journal on Computing 24(5):1036–1050, 1995.
- **[SOTA]** S. Fenner, R. Gurjar, T. Thierauf. *Bipartite perfect matching is in quasi-NC.* STOC 2016, pp. 754–763; SIAM Journal on Computing (STOC 2016 special issue), 2019.
- **[SOTA]** O. Svensson, J. Tarnawski. *The matching problem in general graphs is in quasi-NC.* FOCS 2017, pp. 696–707.
- **[SOTA]** R. Gurjar, T. Thierauf. *Linear matroid intersection is in quasi-NC.* STOC 2017, pp. 821–830.
- **[SOTA]** R. Gurjar, T. Thierauf, N. K. Vishnoi. *Isolating a vertex via lattices: polytopes with totally unimodular faces.* SIAM Journal on Computing 50(2):636–661, 2021 (conf. version ICALP 2018).
- **[SOTA]** N. Anari, V. V. Vazirani. *Planar graph perfect matching is in NC.* Journal of the ACM 67(4), Article 21, 2020.
- **[Barrier]** V. Arvind, P. Mukhopadhyay. *Derandomizing the isolation lemma and lower bounds for circuit size.* APPROX-RANDOM 2008, LNCS 5171, pp. 276–289.
- **[Related]** K. Reinhardt, E. Allender. *Making nondeterminism unambiguous.* SIAM Journal on Computing 29(4):1118–1131, 2000.
- **[Related]** E. Allender, K. Reinhardt, S. Zhou. *Isolation, matching, and counting uniform and nonuniform upper bounds.* Journal of Computer and System Sciences 59(2):164–181, 1999.
- **[Related]** M. Agrawal, T. M. Hoang, T. Thierauf. *The polynomially bounded perfect matching problem is in NC².* STACS 2007, LNCS 4393, pp. 489–499.
- **[Related]** M. Agrawal, R. Gurjar, A. Korwar, N. Saxena. *Hitting-sets for ROABP and sum of set-multilinear polynomials.* SIAM Journal on Computing 44(3):669–697, 2015.
- **[Related]** S. Goldwasser, O. Grossman. *Bipartite perfect matching in pseudo-deterministic NC.* ICALP 2017, LIPIcs 80, Article 87.
- **[Survey/Thesis]** R. Gurjar. *Derandomizing PIT for ROABP and Isolation Lemma for Special Graphs.* PhD thesis, IIT Kanpur, 2015.
- **[Exposition]** A. Ta-Shma. *A simple proof of the isolation lemma.* ECCC Technical Report TR15-080, 2015.

## 10. Worked Example / Concrete Special Case

**Instance.** Bipartite $G$: parts $U=\{u_1,u_2,u_3\}$, $V=\{v_1,v_2,v_3\}$, edges forming the $6$-cycle
$$e_1=u_1v_1,\; e_2=u_2v_1,\; e_3=u_2v_2,\; e_4=u_3v_2,\; e_5=u_3v_3,\; e_6=u_1v_3 .$$
Here $m=6$, $n=3$, and $\mathcal{M}(G)=\{M_1,M_2\}$ with $M_1=\{e_1,e_3,e_5\}$, $M_2=\{e_2,e_4,e_6\}$. Cycle space dimension: $m-n_{\text{vert}}+1 = 6-6+1 = 1$, spanned by the single cycle $C=e_1e_2e_3e_4e_5e_6$.

**Isolation condition.** $w$ isolates iff $w(M_1)\ne w(M_2)$, i.e.
$$\mathrm{circ}_w(C) = w(e_1)-w(e_2)+w(e_3)-w(e_4)+w(e_5)-w(e_6) \;\ne\; 0 .$$

**A bad weighting.** $w\equiv 1$ gives $\mathrm{circ}_w(C)=3-3=0$: both matchings weigh $3$, $\det(A_w)=2^3-2^3=0$, and the determinant test *fails to even detect* a matching. This is exactly the cancellation the lemma is designed to break.

**A good weighting.** $w(e_1)=2$, $w(e_i)=1$ otherwise: $\mathrm{circ}_w(C)=2-1+1-1+1-1=1\ne 0$. Then $w(M_1)=4$, $w(M_2)=3$, and
$$\det(A_w)=\pm(2^{4}-2^{3})=\pm 8 = \pm 2^{3},$$
so $W_{\min}=3$ and $M_2$ is recovered by testing, for each edge $e$, whether deleting $e$ raises the minimum weight.

**Two-function isolating family for this instance.** $W=\{w^{(1)},w^{(2)}\}$ with $w^{(1)}\equiv 1$ and $w^{(2)}$ as above isolates $\mathcal{M}(G)$; weights $\le 2$, list length $2$.

**Where the difficulty enters.** Take instead $G'=K_{n,n}$. Its cycle space has dimension $(n^2-2n+1)=(n-1)^2$, and the alternating cycles number $2^{\Theta(n\log n)}$. The naive fix $w(e_i)=2^{\,i}$ isolates *every* family (binary expansions are unique) but needs weights $2^{m}$, so $\det(A_w)$ has $2^{\Theta(n^2)}$-bit entries — outside $\mathrm{NC}$. The MVV lemma says random $w\in\{1,\dots,2m\}^m$ works with probability $\ge 1/2$. The FGT construction handles cycles of length $\le 2^i$ at round $i$ with $\mathrm{poly}(n)$ candidates each, and after $\log n$ rounds the union of minimum-weight matchings shrinks to a single matching — at the cost of $n^{O(\log n)}$ candidates overall. Closing the example: for $K_{n,n}$, no explicit list of $\mathrm{poly}(n)$ weightings with $\mathrm{poly}(n)$ weights is known to isolate $\mathcal{M}(K_{n,n})$ for all *subgraphs* of $K_{n,n}$ — that single missing family is the whole open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*