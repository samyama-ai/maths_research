---
id: 07-combinatorics/alon-tarsi-conjecture
title: "Alon-Tarsi Conjecture"
topic: 07-combinatorics
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Alon-Tarsi Conjecture

> **Topic:** Combinatorics & Graph Theory · **ID:** `07-combinatorics/alon-tarsi-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $\mathcal{L}_n$ be the set of Latin squares of order $n$ on symbol set $[n]=\{1,\dots,n\}$. Each $L\in\mathcal{L}_n$ has $n$ rows and $n$ columns, each of which is a permutation of $[n]$. Define the **sign** of $L$ as
$$\varepsilon(L)\;=\;\prod_{i=1}^{n}\operatorname{sgn}(r_i)\;\cdot\;\prod_{j=1}^{n}\operatorname{sgn}(c_j),$$
where $r_i$ is the $i$-th row read as a permutation and $c_j$ the $j$-th column. Call $L$ **even** if $\varepsilon(L)=+1$ and **odd** otherwise, and set
$$\Delta(n)\;=\;\operatorname{els}(n)-\operatorname{ols}(n)\;=\;\sum_{L\in\mathcal{L}_n}\varepsilon(L).$$

**Conjecture (Alon–Tarsi, 1992).** For every **even** $n$,
$$\Delta(n)\neq 0 .$$

The restriction to even $n$ is necessary: for odd $n$ a parity-reversing involution forces $\Delta(n)=0$ (Section 10). A complete resolution requires either a proof of non-vanishing for all even $n$, or an explicit even $n$ with $\operatorname{els}(n)=\operatorname{ols}(n)$. Note the asymmetry of difficulty: a disproof needs an exact signed count of a set of size $|\mathcal{L}_{26}|\approx 10^{360}$, so a counterexample would itself have to be structural, not computational.

## 2. Mathematical Foundations

**Graph-orientation origin.** For a digraph $D$, a spanning sub-digraph is *Eulerian* if $d^+(v)=d^-(v)$ at every vertex. Let $EE(D)$ and $EO(D)$ count Eulerian sub-digraphs with an even, resp. odd, number of edges.

**Theorem (Alon–Tarsi 1992).** If $D$ is an orientation of $G$ with $EE(D)\neq EO(D)$, then $G$ is $f$-choosable for $f(v)=d^+_D(v)+1$.

The proof is the archetype of the **Combinatorial Nullstellensatz** (Alon 1999): the graph polynomial $f_G=\prod_{ij\in E, i<j}(x_i-x_j)$ has the coefficient of $\prod_v x_v^{d^+_D(v)}$ equal to $\pm(EE(D)-EO(D))$, and a nonzero coefficient certifies a non-vanishing assignment, i.e. a proper colouring from arbitrary lists.

**Latin square formulation.** Applying this to $G=K_{n,n}$ with the $d$-regular orientation converts the Eulerian count into the signed Latin-square count $\Delta(n)$. Equivalently, in terms of the $n\times n$ generic matrix $X=(x_{ij})$:
$$[\,x_{11}x_{12}\cdots x_{nn}\,]\;\det(X)^{\,n}\;=\;\pm\,\Delta(n),$$
the sign depending only on $n$. Reason: a monomial in $\det(X)^n$ using every cell exactly once selects $n$ pairwise disjoint permutation matrices, i.e. a Latin square, and the product of the permutation signs is the Latin square's parity invariant. Hence

$$\textbf{AT}(n)\iff \det(X)^n \text{ has a nonzero squarefree-monomial coefficient.}$$

This is Huang–Rota's "straightening coefficient" form and Onn's determinantal identity; Zappa reformulated it via the Cayley $\Omega$-process applied to the determinant tensor.

**Implications.**
- AT for even $n$ $\Rightarrow$ **Dinitz conjecture** for $n$ (list edge-colouring of $K_{n,n}$ with lists of size $n$) — later proved for all $n$ by Galvin (1995) via kernel-perfect orientations, independently of AT.
- AT for $n$ $\Rightarrow$ **Rota's basis conjecture** in dimension $n$ over characteristic-$0$ fields (Huang–Rota 1994; Onn 1997).
- AT is connected to plethysm: Kumar–Landsberg (2015) express $\Delta(n)$ as an integral $\int_{SU(n)}$ and link non-vanishing to the Hadamard–Howe/Foulkes problem.

**Parity structure.** Rows, columns and symbols each carry a sign, $\operatorname{rsgn}$, $\operatorname{csgn}$, $\operatorname{ssgn}$; conjugation of a Latin square permutes them, so $\varepsilon$ is only *partially* invariant under the six conjugates, a fact exploited (and shown to be limiting) by Kotlar and by Stones–Wanless.

## 3. History & State of the Art (SOTA)

- **1992** — Alon and Tarsi, *Colorings and orientations of graphs* (Combinatorica), introduce the Eulerian-subgraph criterion and state the even-order Latin square conjecture as the missing ingredient for Dinitz.
- **1994** — Huang and Rota prove AT$(n)$ implies Rota's basis conjecture in dimension $n$, converting a colouring question into a matroid/invariant-theory question.
- **1995** — Galvin proves the Dinitz conjecture directly; AT survives as the deeper, still-open statement.
- **1997** — Drisko proves AT for $n=p+1$, $p$ an odd prime, by computing $\Delta(p+1)$ modulo $p$ using a $\mathbb{F}_p$-action on Latin squares with few fixed points.
- **1997** — Onn gives a two-page determinantal proof of the AT $\Rightarrow$ Rota implication; Zappa relates $\Delta(n)$ to Cayley's $\Omega$-process and formulates strengthenings.
- **1999** — Alon's *Combinatorial Nullstellensatz* survey canonises the method AT grew out of.
- **2010/2011** — Glynn proves AT for $n=p-1$, $p$ an odd prime, again via a mod-$p$ argument, and deduces Rota's conjecture in those dimensions.
- **2012** — Stones and Wanless, *How not to prove the Alon–Tarsi conjecture*, show that several natural congruence/involution strategies provably cannot work.
- **2017** — Alpoge proves square-root cancellation for the signed sum, quantifying how delicate non-vanishing is.
- **2020** — Grytczuk and Zhu push the *Alon–Tarsi number* of graphs: planar graphs minus a matching have $AT\le 4$.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $n$ odd | $\Delta(n)=0$ (theorem, explains the even hypothesis) | folklore/Alon–Tarsi 1992 |
| $n=2$ | $\Delta(2)=2$ | direct (Section 10) |
| $n=p+1$, $p$ odd prime | $\Delta(n)\not\equiv 0 \pmod p$ | Drisko 1997 |
| $n=p-1$, $p$ odd prime | $\Delta(n)\not\equiv 0 \pmod p$ | Glynn 2011 |
| all even $n\le 24$ | covered by the two prime results | — |
| $n\le 8$ (roughly) | direct/orbit-assisted enumeration of $\mathcal{L}_n$ | Kotlar 2012 and predecessors |

Combining $p\pm1$: $4=3+1=5-1$, $6=5+1=7-1$, $8=7+1$, $10=11-1$, $12=11+1$, $14=13+1$, $16=17-1$, $18=17+1$, $20=19+1$, $22=23-1$, $24=23+1$. The **smallest open case is $n=26$**, since neither $25$ nor $27$ is prime. The next open orders are $34, 46, 50, 56, \dots$ — the even integers not adjacent to a prime, a set of positive density by standard prime-gap heuristics. So the known cases, though infinite, have density $0$ among even orders unless twin-type conjectures are invoked.

Related but distinct: the graph-theoretic **Alon–Tarsi number** $AT(G)$ (least $k$ with an orientation of max outdegree $k-1$ and $EE\neq EO$) satisfies $AT(G)\le 5$ for planar $G$ and $\le 4$ for planar minus a matching (Grytczuk–Zhu 2020).

## 5. Principal Obstacles

- **Massive cancellation.** Alpoge (2017) proved square-root-type cancellation: $|\Delta(n)|$ is vanishingly small relative to $|\mathcal{L}_n|\approx (n!)^{2n}/n^{n^2}$. Any argument that bounds $\Delta(n)$ by controlling error terms of size $\sqrt{|\mathcal{L}_n|}$ is hopeless — the target is below the noise floor.
- **No positivity.** There is no known bijective or injective map from odd to even Latin squares with controlled defect. Unlike permanent/determinant positivity results, $\Delta(n)$ is a genuinely signed quantity with no manifestly positive combinatorial model.
- **Congruence methods stall.** Both proven families work by finding a prime $p$ with a $p$-group acting on $\mathcal{L}_n$ whose fixed points are countable and whose signed total is nonzero mod $p$. For general even $n$ no prime is available with the right relation to $n$; Stones–Wanless (2012) show that broad families of such congruence and involution schemes provably return $0$ and therefore cannot decide the conjecture.
- **Representation-theoretic route is itself open.** The Kumar–Landsberg translation into $SU(n)$ integrals / Hadamard–Howe coefficients replaces one non-vanishing problem by another (plethysm positivity) of comparable difficulty; no direction of the equivalence is currently the easy one.
- **Nullstellensatz is one-way.** The Combinatorial Nullstellensatz certifies colourability from a nonzero coefficient but gives no tool for proving a coefficient nonzero. Since Galvin settled Dinitz by other means, there is no external combinatorial theorem that would force $\Delta(n)\neq 0$.

## 6. The Gap

Proven: $\Delta(n)\neq 0$ whenever $n\pm 1$ is prime, via mod-$p$ non-vanishing. Conjectured: $\Delta(n)\neq0$ for **all** even $n$.

The precise missing step is a *characteristic-free* certificate. Every existing proof produces a prime $p$ and shows $\Delta(n)\not\equiv0\pmod p$; the choice of $p$ is dictated by $n\pm1$ being prime, which is an arithmetic accident unrelated to the combinatorics. Crossing the gap requires one of:
1. an algebraic group action on $\mathcal{L}_n$, defined for every even $n$, whose fixed-point set has a computable signed count that is provably nonzero;
2. a lower bound $|\Delta(n)|\ge g(n)>0$ from the determinant-power coefficient, e.g. via a degeneration or a representation-theoretic multiplicity that is visibly positive;
3. a structural decomposition $\mathcal{L}_n = \mathcal{P}\sqcup \mathcal{Q}$ with a sign-reversing involution on $\mathcal{Q}$ and $\mathcal{P}$ of provably nonzero signed weight.

None of the three is known even conditionally for $n=26$.

## 7. Current Research (as of June 2026)

- **Invariant theory / GCT.** Landsberg's circle continues to develop the Alon–Tarsi ↔ Hadamard–Howe ↔ Foulkes web; the working hypothesis is that a proof of stability for Hadamard–Howe coefficients would transfer. *(frontier — verify)*
- **Latin square parity and autotopisms.** Wanless, Stones, Kotlar and collaborators refine congruences for $\Delta(n)$ modulo small primes and classify which symmetry groups can contribute; the emphasis since 2012 has been on *ruling out* method families as much as proving cases.
- **Rota's basis conjecture.** Bucić–Kwan–Pokrovskiy–Sudakov's "halfway" theorem (IMRN 2020) shows $(1/2-o(1))n$ disjoint transversal bases exist, bypassing AT entirely; this weakens the incentive to prove AT for Rota's sake but sharpens the question of what AT alone encodes.
- **Alon–Tarsi numbers of graphs.** Zhu, Grytczuk, Kaul and Mudrock have made the graph-side invariant a research programme in its own right (planar bounds, online list colouring, $AT$ vs. list chromatic number), which keeps the Eulerian-subgraph machinery active.
- **Computation.** No published exact value of $\Delta(26)$ exists; the enumeration is far beyond current reach, and no serious claim of a randomized estimate with provable sign has appeared. *(frontier — verify)*

## 8. Future Work

- Find a proof for $n=2^k$, where the abundance of $2$-group actions on $\mathcal{L}_n$ suggests a mod-$2$ argument; success would give the first infinite family not tied to primality of $n\pm1$.
- Establish multiplicativity: prove $\Delta(mn)\neq0$ follows from $\Delta(m)\neq0$ and $\Delta(n)\neq0$ (via products of Latin squares). This is a stated hope of several authors and would immediately extend the covered set.
- Prove a $p$-adic valuation formula $v_p(\Delta(n))$ for a family of primes $p$, converting the ad hoc mod-$p$ computations into a theory.
- Settle the sharpened form conjectured by Zappa and by Drisko relating $\Delta(n)$ to $\left(\frac{n}{2}\right)!$-type factors; even a plausible closed form would give a target for asymptotic methods.
- Resolve the Hadamard–Howe/Foulkes non-vanishing statement equivalent to AT in the Kumar–Landsberg dictionary.

## 9. Key References

- **[Foundational]** N. Alon and M. Tarsi. *Colorings and orientations of graphs.* Combinatorica **12** (1992), 125–134.
- **[Foundational]** R. Huang and G.-C. Rota. *On the relations of various conjectures on Latin squares and straightening coefficients.* Discrete Mathematics **128** (1994), 225–236.
- **[Key result]** A. A. Drisko. *On the number of even and odd Latin squares of order $p+1$.* Advances in Mathematics **128** (1997), 20–35.
- **[Key result]** D. G. Glynn. *The conjectures of Alon–Tarsi and Rota in dimension prime minus one.* Advances in Applied Mathematics **46** (2011), 148–156.
- **[Foundational]** S. Onn. *A colorful determinantal identity, a conjecture of Rota, and Latin squares.* American Mathematical Monthly **104** (1997), 156–159.
- **[Foundational]** P. Zappa. *The Cayley determinant of the determinant tensor and the Alon–Tarsi conjecture.* Advances in Applied Mathematics **19** (1997), 31–44.
- **[Related]** F. Galvin. *The list chromatic index of a bipartite multigraph.* Journal of Combinatorial Theory, Series B **63** (1995), 153–158.
- **[Method]** N. Alon. *Combinatorial Nullstellensatz.* Combinatorics, Probability and Computing **8** (1999), 7–29.
- **[SOTA]** L. Alpoge. *Square-root cancellation for the signs of Latin squares.* Combinatorica **37** (2017), 137–142.
- **[SOTA]** S. Kumar and J. M. Landsberg. *Connections between conjectures of Alon–Tarsi, Hadamard–Howe, and integrals over the special unitary group.* Discrete Mathematics **338** (2015), 1232–1238.
- **[Survey / negative results]** D. S. Stones and I. M. Wanless. *How not to prove the Alon–Tarsi conjecture.* Nagoya Mathematical Journal **205** (2012), 1–24.
- **[Related]** D. Kotlar. *Parity types, cycle structures and autotopisms of Latin squares.* Electronic Journal of Combinatorics **19**(3) (2012), #P10.
- **[Recent]** J. Grytczuk and X. Zhu. *The Alon–Tarsi number of planar graphs minus a matching.* Journal of Combinatorial Theory, Series B **145** (2020), 511–520.
- **[Recent]** M. Bucić, M. Kwan, A. Pokrovskiy, B. Sudakov. *Halfway to Rota's basis conjecture.* International Mathematics Research Notices, 2020.

## 10. Worked Example / Concrete Special Case

**(a) Odd $n$ gives $\Delta(n)=0$.** Let $\tau$ swap rows $1$ and $2$ of $L$. The multiset of row permutations is unchanged, so $\prod_i\operatorname{sgn}(r_i)$ is unchanged. Each column, read as a permutation from row-index to symbol, is pre-composed with the transposition $(1\,2)$, so each of the $n$ column signs flips:
$$\prod_j \operatorname{sgn}(c_j) \;\longmapsto\; (-1)^n \prod_j \operatorname{sgn}(c_j).$$
For $n$ odd this is $-1$, so $\varepsilon(\tau L)=-\varepsilon(L)$: a fixed-point-free sign-reversing involution, hence $\operatorname{els}(n)=\operatorname{ols}(n)$. For $n$ even the factor is $+1$ and the argument collapses — precisely why the conjecture is stated for even $n$.

**(b) $n=2$ computed exactly.** $\mathcal{L}_2=\{L_1,L_2\}$ with
$$L_1=\begin{pmatrix}1&2\\2&1\end{pmatrix},\qquad L_2=\begin{pmatrix}2&1\\1&2\end{pmatrix}.$$
For $L_1$: rows are $\mathrm{id}$ and $(1\,2)$, so $\prod\operatorname{sgn}(r_i)=(+1)(-1)=-1$; columns likewise give $-1$. Hence $\varepsilon(L_1)=(-1)(-1)=+1$. By the same computation $\varepsilon(L_2)=+1$. So
$$\operatorname{els}(2)=2,\quad \operatorname{ols}(2)=0,\quad \Delta(2)=2\neq0 .$$

**(c) Cross-check via the determinant.** With $X=\begin{pmatrix}a&b\\c&d\end{pmatrix}$,
$$\det(X)^2=(ad-bc)^2=a^2d^2-2abcd+b^2c^2 .$$
The coefficient of the squarefree monomial $abcd$ is $-2$, matching $\pm\Delta(2)=\pm2$ and confirming the identity of Section 2. For $n=26$ the same coefficient extraction is a sum over roughly $10^{360}$ terms of size $\pm1$ whose total is conjectured — but not known — to avoid zero.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*