---
id: 07-combinatorics/hills-conjecture
title: "Hill's Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Hill's Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/hills-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

The **crossing number** $\mathrm{cr}(G)$ of a graph $G$ is the minimum number of pairwise edge crossings over all drawings of $G$ in the plane. Hill's conjecture (also called the Harary–Hill conjecture) asserts that for the complete graph $K_n$,

$$\mathrm{cr}(K_n) \;=\; Z(n) \;:=\; \frac{1}{4}\left\lfloor \frac{n}{2}\right\rfloor \left\lfloor \frac{n-1}{2}\right\rfloor \left\lfloor \frac{n-2}{2}\right\rfloor \left\lfloor \frac{n-3}{2}\right\rfloor .$$

The upper bound $\mathrm{cr}(K_n) \le Z(n)$ is a theorem: explicit drawings achieving $Z(n)$ were given by Anthony Hill and independently by Blažek and Koman. The open content is the **lower bound** $\mathrm{cr}(K_n) \ge Z(n)$ for every $n$.

A complete proof must show that *every* drawing of $K_n$ in the plane (equivalently, on the sphere) has at least $Z(n)$ crossings. A disproof requires a single drawing of some $K_n$ with fewer than $Z(n)$ crossings; by the standard counting recursion this would falsify the conjecture for all larger $n$ as well.

## 2. Mathematical Foundations

**Drawings.** A *drawing* $D$ of a graph $G$ maps vertices to distinct points of $\mathbb{R}^2$ and edges to simple arcs joining their endpoints, containing no other vertex. A *crossing* is a transversal intersection of the relative interiors of two edges. $\mathrm{cr}(D)$ is the number of crossings; $\mathrm{cr}(G) = \min_D \mathrm{cr}(D)$.

**Good drawings.** A drawing is *good* if (i) no two edges cross more than once, (ii) adjacent edges do not cross, (iii) no three edges share a crossing point. Every crossing-minimal drawing may be assumed good, so

$$\mathrm{cr}(K_n) = \min\{\mathrm{cr}(D) : D \text{ a good drawing of } K_n\}.$$

In a good drawing of $K_n$ crossings correspond to 4-element vertex subsets: each $4$-set spans a $K_4$ that is drawn with $0$ or $1$ crossing, so $\mathrm{cr}(D) \le \binom{n}{4}$ and

$$\mathrm{cr}(D) \;=\; \\#\{Q \in \tbinom{[n]}{4} : D[Q] \text{ has a crossing}\}.$$

**Counting recursion.** Each crossing of a drawing of $K_n$ survives in exactly $n-4$ of the $n$ induced sub-drawings of $K_{n-1}$, giving

$$\mathrm{cr}(K_n) \;\ge\; \frac{n}{\,n-4\,}\,\mathrm{cr}(K_{n-1}),$$

and hence that $\mathrm{cr}(K_n)/\binom{n}{4}$ is non-decreasing in $n$, so the limit

$$c \;:=\; \lim_{n\to\infty} \frac{\mathrm{cr}(K_n)}{\binom{n}{4}}$$

exists. Since $Z(n)/\binom{n}{4} \to 3/8$, Hill's conjecture implies (and, by monotonicity, is asymptotically equivalent to) $c = 3/8 = 0.375$.

**Hill's construction (cylindrical drawing).** Place $\lceil n/2 \rceil$ vertices on an outer circle and $\lfloor n/2 \rfloor$ on a concentric inner circle of a cylinder, each set in convex position; draw each circle's internal edges inside its own disc region and the $\lceil n/2\rceil\lfloor n/2\rfloor$ "vertical" edges in the annulus as arcs following a fixed rotational pattern. Counting crossings within each disc and within the annulus yields exactly $Z(n)$.

**Related parameters.** The *rectilinear* crossing number $\overline{\mathrm{cr}}(K_n)$ (straight-line edges) satisfies $\overline{\mathrm{cr}}(K_n) > Z(n)$ for $n \ge 10$, so Hill's conjecture is genuinely about curved drawings. The *$k$-page (book)* crossing number $\nu_k$ and the *cylindrical* crossing number are restricted variants used as testbeds.

## 3. History & State of the Art (SOTA)

- **1960.** Richard Guy publishes the problem and the value $Z(n)$ in *A combinatorial problem* (Nabla, Bull. Malayan Math. Soc.), attributing the extremal drawings to Anthony Hill.
- **1963.** Harary and Hill, *On the number of crossings in a complete graph* (Proc. Edinburgh Math. Soc.), state the conjecture $\mathrm{cr}(K_n)=Z(n)$.
- **1964.** Blažek and Koman give an independent construction attaining $Z(n)$.
- **1972.** Guy verifies $\mathrm{cr}(K_n)=Z(n)$ for $n \le 10$.
- **1976.** Kleitman's parity theorem: for odd $n$, all good drawings of $K_n$ have crossing numbers of the same parity. This converts even-$n$ information into odd-$n$ information and vice versa.
- **2007.** Pan and Richter prove $\mathrm{cr}(K_{11}) = 100$ by exhaustive generation of good drawings; with the counting recursion this gives $\mathrm{cr}(K_{12}) = 150$.
- **2006–07.** Semidefinite programming (de Klerk, Maharry, Pasechnik, Richter, Salazar; de Klerk, Pasechnik, Schrijver) gives the first strong asymptotic lower bound, $c \ge 0.8594 \cdot \tfrac38$.
- **2013–14.** Ábrego, Aichholzer, Fernández-Merchant, Ramos, Salazar prove the conjecture exactly for **2-page drawings** and for **shellable drawings**, a class containing the cylindrical and $x$-monotone drawings.
- **2015–18.** McQuillan–Pan–Richter, then the *bishellable drawings* paper, establish $\mathrm{cr}(K_{13}) \ge 219$ (vs. $Z(13)=225$).
- **2019.** Balogh, Lidický and Salazar, *Closing in on Hill's conjecture*, use flag algebras to push the asymptotic ratio to $\mathrm{cr}(K_n) \ge (0.985 + o(1))\,Z(n)$ — the current SOTA general bound.

## 4. Partial Results / Verified Cases

- **Exact small cases.** $\mathrm{cr}(K_n) = Z(n)$ is proven for all $n \le 12$: $Z(5)=1$, $Z(6)=3$, $Z(7)=9$, $Z(8)=18$, $Z(9)=36$, $Z(10)=60$ (Guy), $Z(11)=100$, $Z(12)=150$ (Pan–Richter, computer-assisted).
- **$n = 13$.** Open. Known: $219 \le \mathrm{cr}(K_{13}) \le 225 = Z(13)$. By Kleitman parity and the recursion, $\mathrm{cr}(K_{13}) \in \{219, 221, 223, 225\}$ (odd-$n$ parity fixes the residue class); settling $n=13$ would give $n=14$ for free.
- **2-page crossing number.** $\nu_2(K_n) = Z(n)$ for all $n$ (Ábrego–Aichholzer–Fernández-Merchant–Ramos–Salazar, 2013). Equivalently, Hill's conjecture holds for all $x$-monotone (cylindrical book) drawings.
- **Shellable and bishellable drawings.** If a good drawing of $K_n$ is $s$-shellable with $s \ge \lfloor n/2 \rfloor$, it has at least $Z(n)$ crossings; the bishellable extension covers a strictly larger class and reproves $\mathrm{cr}(K_{13}) \ge 219$. Mutzel and Oettershagen (2018) extend this to *seq-shellable* drawings.
- **Cylindrical drawings.** The cylindrical crossing number of $K_n$ equals $Z(n)$.
- **Asymptotic bound.** $\liminf_n \mathrm{cr}(K_n)/Z(n) \ge 0.985$ (flag algebras). The gap to $1$ is $\le 1.5\%$ asymptotically.
- **Rectilinear analogue.** For straight-line drawings the answer is *not* $Z(n)$: $\overline{\mathrm{cr}}(K_n)/\binom{n}{4} \to q^\ast$ with $0.379972 \le q^\ast \le 0.380488$, strictly above $3/8$.

## 5. Principal Obstacles

- **No topological invariant forces the bound.** Euler's formula gives only $\mathrm{cr}(G) \ge e - 3v + 6$, which for $K_n$ yields $\Theta(n^2)$ — hopelessly weak against $Z(n) = \Theta(n^4)$. The bisection-width and embedding methods that work for bounded-degree graphs are lossy by constant factors precisely of the size in dispute.
- **The counting recursion loses exactly the needed constant.** $\mathrm{cr}(K_n) \ge \frac{n}{n-4}\mathrm{cr}(K_{n-1})$ is tight for the ratio $\mathrm{cr}/\binom n4$ and therefore can never *increase* the asymptotic constant; it only propagates exact small values. Any proof must inject new information at unbounded $n$.
- **Combinatorial explosion of good drawings.** Good drawings of $K_n$ are classified by rotation systems; the number of realizable rotation systems grows super-exponentially. Exhaustive search reached $n=11$ in 2007 and has not been pushed past $n=12$–$13$ despite two decades of hardware gains.
- **Non-realizability of abstract rotation systems.** Many combinatorial candidates that would beat $Z(n)$ are *not* realizable as drawings, but deciding realizability is itself hard, so search-based lower bounds must certify a large space of pseudo-configurations.
- **SDP/flag-algebra saturation.** The Lasserre/flag-algebra hierarchy expresses $c$ as a limit of finite semidefinite programs on $k$-vertex sub-drawing densities. The program size grows like the number of good drawings of $K_k$; level $k=8$–$9$ already produces the $0.985$ bound and further levels are computationally out of reach. There is also no evidence the hierarchy converges to $3/8$ at any finite level.
- **The extremal structure is not unique.** $K_n$ has many essentially different optimal drawings (Hill's cylindrical, 2-page, and others), so stability/uniqueness arguments — the usual route from an asymptotic bound to an exact one — have no rigid target to lock onto.

## 6. The Gap

Proven: exact equality for $n \le 12$; equality for structurally restricted drawing classes (2-page, shellable, bishellable, seq-shellable, cylindrical); the asymptotic inequality $\mathrm{cr}(K_n) \ge 0.985\,Z(n)$.

Conjectured: equality for *all* $n$ and *all* good drawings.

The precise barrier: every known exact proof either (a) enumerates drawings, which fails past $n \approx 13$, or (b) assumes a *shelling order* — a sequence of vertices whose removal leaves each remaining vertex "on the outside" of the residual drawing. The missing step is a proof that an arbitrary good drawing of $K_n$ either admits enough shellability to run the induction, or else carries a compensating surplus of crossings. Closing the residual $1.5\%$ asymptotic gap is a second, independent gap: it requires a lower-bound certificate on 4-set crossing densities that is not a finite-level flag-algebra sum-of-squares.

## 7. Current Research (as of June 2026)

- **Extending shellability.** The Ábrego–Fernández-Merchant school (CSU Northridge), with Aichholzer (TU Graz), Richter (Waterloo), Salazar (UASLP) and Mutzel (Bonn), continues to enlarge the drawing classes for which $Z(n)$ is provable — seq-shellable and "$k$-edge"-based generalizations. The stated target is a dichotomy covering all good drawings.
- **$k$-edge and generalized-configuration methods.** Lower bounds via the number of $(\le k)$-edges convert Hill's conjecture into an extremal question about halving-line-like quantities in pseudo-configurations; this is the technique that resolved the 2-page case.
- **Flag algebras at higher levels.** Lidický (Iowa State) and collaborators continue to push semidefinite relaxations; incremental improvements past $0.985$ are reported but the exact value $1$ appears unreachable by this route alone. *(frontier — verify)*
- **Computer search for $n = 13$.** SAT/ILP encodings of realizable rotation systems aimed at deciding whether $\mathrm{cr}(K_{13}) = 225$ remain active; no verified resolution has been published. *(frontier — verify)*
- **Related surfaces.** Crossing numbers of $K_n$ on the torus and projective plane, and the "convex/pseudolinear" variants, are studied as sources of transferable structure.

## 8. Future Work

- Prove that every good drawing of $K_n$ contains a vertex whose removal preserves a shelling-type invariant — reducing the general case to the bishellable case.
- Develop a stability theorem for near-optimal drawings: show that any drawing with $(1+\varepsilon)Z(n)$ crossings is structurally close to a cylindrical or 2-page drawing, then upgrade the $0.985$ bound to equality.
- Resolve $n = 13$ (and hence $14$) by certified exhaustive search over realizable rotation systems; this is the most concrete finite target.
- Find a non-SDP analytic certificate for the density $3/8$, e.g. via a limit object ("crossing-graphon") for drawings of $K_n$.
- Clarify the relationship with the Zarankiewicz conjecture for $\mathrm{cr}(K_{m,n})$, which is open in the same asymptotic regime and shares the SDP bound $0.8594$.

## 9. Key References

- **[Foundational]** R. K. Guy. *A combinatorial problem.* Nabla (Bulletin of the Malayan Mathematical Society) 7 (1960), 68–72.
- **[Foundational]** F. Harary, A. Hill. *On the number of crossings in a complete graph.* Proceedings of the Edinburgh Mathematical Society 13 (1963), 333–338.
- **[Foundational]** J. Blažek, M. Koman. *A minimal problem concerning complete plane graphs.* In: Theory of Graphs and its Applications, Czechoslovak Academy of Sciences, 1964, 113–117.
- **[Foundational]** D. J. Kleitman. *A note on the parity of the number of crossings of a graph.* Journal of Combinatorial Theory, Series B 21 (1976), 88–89.
- **[Exact values]** S. Pan, R. B. Richter. *The crossing number of $K_{11}$ is 100.* Journal of Graph Theory 56 (2007), 128–134.
- **[SOTA]** B. M. Ábrego, O. Aichholzer, S. Fernández-Merchant, P. Ramos, G. Salazar. *The 2-page crossing number of $K_n$.* Discrete & Computational Geometry 49 (2013), 747–777.
- **[SOTA]** B. M. Ábrego, O. Aichholzer, S. Fernández-Merchant, P. Ramos, G. Salazar. *Shellable drawings and the cylindrical crossing number of $K_n$.* Discrete & Computational Geometry 52 (2014), 743–753.
- **[SOTA]** B. M. Ábrego, O. Aichholzer, S. Fernández-Merchant, D. McQuillan, B. Mohar, P. Mutzel, P. Ramos, R. B. Richter, G. Salazar. *Bishellable drawings of $K_n$.* SIAM Journal on Discrete Mathematics 32 (2018), 2482–2492.
- **[SOTA / Recent]** J. Balogh, B. Lidický, G. Salazar. *Closing in on Hill's conjecture.* SIAM Journal on Discrete Mathematics 33 (2019), 1261–1276.
- **[SOTA]** E. de Klerk, J. Maharry, D. V. Pasechnik, R. B. Richter, G. Salazar. *Improved bounds for the crossing numbers of $K_{m,n}$ and $K_n$.* SIAM Journal on Discrete Mathematics 20 (2006), 189–202.
- **[SOTA]** D. McQuillan, S. Pan, R. B. Richter. *On the crossing number of $K_{13}$.* Journal of Combinatorial Theory, Series B 115 (2015), 224–235.
- **[Survey]** L. Beineke, R. Wilson. *The early history of the brick factory problem.* The Mathematical Intelligencer 32 (2010), 41–48.
- **[Survey]** M. Schaefer. *Crossing Numbers of Graphs.* CRC Press, 2018.
- **[Related]** P. Mutzel, L. Oettershagen. *The crossing number of seq-shellable drawings of complete graphs.* IWOCA 2018, Lecture Notes in Computer Science 10979, Springer, 2018, 273–284.

## 10. Worked Example / Concrete Special Case

**Claim: $\mathrm{cr}(K_6) = 3 = Z(6)$.**

*Value of $Z$.* $Z(6) = \frac14 \lfloor 6/2\rfloor \lfloor 5/2\rfloor \lfloor 4/2\rfloor \lfloor 3/2\rfloor = \frac14 \cdot 3 \cdot 2 \cdot 2 \cdot 1 = 3$.

*Step 1: $\mathrm{cr}(K_5) = 1$.* $K_5$ has $v=5$, $e=10$. A planar simple graph satisfies $e \le 3v - 6 = 9 < 10$, so $K_5$ is non-planar and $\mathrm{cr}(K_5) \ge 1$. Draw four vertices as a convex quadrilateral with both diagonals (one crossing) and place the fifth vertex in an outer face joined to all four without further crossings: $\mathrm{cr}(K_5) = 1$.

*Step 2: lower bound by counting.* Take any good drawing $D$ of $K_6$. For each vertex $v$, deleting $v$ leaves a drawing of $K_5$, which has at least $1$ crossing. There are $6$ such sub-drawings. Each crossing of $D$ involves $4$ distinct vertices, hence survives in exactly $6-4 = 2$ of the sub-drawings. Double counting:

$$2\,\mathrm{cr}(D) \;=\; \sum_{v} \mathrm{cr}(D - v) \;\ge\; 6 \cdot \mathrm{cr}(K_5) \;=\; 6 \quad\Longrightarrow\quad \mathrm{cr}(D) \ge 3 .$$

*Step 3: upper bound by Hill's construction.* Take $n = 6$: three vertices $a_1,a_2,a_3$ on an outer circle, three vertices $b_1,b_2,b_3$ on an inner circle. Each triple spans a triangle drawn crossing-free in its own disc region ($0$ crossings inside each circle, since $Z$-style triangles are planar). The $9$ edges $a_ib_j$ are routed in the annulus; the rotationally symmetric routing produces exactly $3$ crossings among them. Total: $3$.

Hence $3 \le \mathrm{cr}(K_6) \le 3$.

*Why this stops working.* Iterating Step 2 gives $\mathrm{cr}(K_7) \ge \tfrac{7}{3}\cdot 3 = 7$, but $Z(7) = 9$. The recursion already loses $2$ crossings at $n=7$, and the loss grows: this is exactly the obstacle described in Section 5 — the counting bound cannot by itself raise the asymptotic density above the value fed into it, so every additional exact value has required genuinely new input (Kleitman parity for $n=7,9$, exhaustive search for $n=11$, shellability arguments for $n=13$).

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*