---
id: 04-topology/mutant-knot-unknotting-number-conjecture
title: "Mutant Knot Unknotting Number Conjecture"
topic: 04-topology
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Mutant Knot Unknotting Number Conjecture

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/mutant-knot-unknotting-number-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Conway mutation replaces a $2$-string tangle in a knot diagram by its image under a $\pi$-rotation about one of three coordinate axes, reglued so the endpoints match.

**Conjecture (folklore; "mutation invariance of unknotting number").** For every knot $K \subset S^3$ and every Conway mutant $K^\tau$ of $K$,
$$u(K) \;=\; u(K^\tau),$$
where $u(\cdot)$ is the unknotting number — the minimum, over all diagrams $D$ of the knot, of the number of crossing changes needed to turn $D$ into a diagram of the unknot.

A **proof** must show that any unknotting sequence of length $n$ for $K$ yields one of length $n$ for $K^\tau$ — equivalently, that $u$ is determined by data preserved under mutation. A **disproof** requires an explicit mutant pair $(K,K^\tau)$ together with a certified upper bound $u(K)\le a$ (an explicit crossing-change sequence) and a certified lower bound $u(K^\tau)\ge a+1$ (an obstruction theorem, not a table lookup).

The expected answer is *no*: the Kinoshita–Terasaka / Conway pair is the standard candidate counterexample. The problem is listed as open here because the lower bound needed for the Conway knot has not been established by a published obstruction. Two weaker statements are also open: whether $|u(K)-u(K^\tau)|$ is bounded by a universal constant, and whether the property $u(K)=1$ is mutation-invariant.

## 2. Mathematical Foundations

**Tangles and mutation.** A *Conway sphere* for $K$ is an embedded $S^2 \subset S^3$ meeting $K$ transversely in $4$ points; it splits $(S^3,K)$ into two $2$-string tangles $(B_1,T_1)$ and $(B_2,T_2)$. Put the $4$ points at $(\pm1,0,0),(0,\pm1,0)$ and let
$$\tau_x,\ \tau_y,\ \tau_z \in \mathrm{SO}(3)$$
be the $\pi$-rotations about the coordinate axes; they generate the Klein group $\mathbb{Z}/2\times\mathbb{Z}/2$ acting on the $4$ marked points. The *mutant* is
$$K^\tau \;=\; (B_1,T_1)\ \cup_{\tau}\ (B_2,T_2),$$
with orientations corrected if necessary. The Conway sphere is *essential* if the $4$-punctured sphere $S^2 \setminus K$ is incompressible and not boundary-parallel in the exterior $E_K = S^3\setminus \nu(K)$.

**Unknotting number.** Equivalently $u(K)$ is the minimum number of double points of a generic homotopy from $K$ to the unknot, and it satisfies
$$u(K)\;\ge\; g_4(K)\;\ge\;\max\Big(|\tau(K)|,\ \tfrac{|s(K)|}{2},\ \tfrac{|\sigma(K)|}{2}\Big),$$
with $g_4$ the smooth slice genus, $\tau$ the Ozsváth–Szabó concordance invariant, $s$ the Rasmussen invariant, $\sigma$ the signature.

**Invariance results.** Mutation preserves the Alexander polynomial $\Delta_K(t)$, the Jones, HOMFLY and Kauffman polynomials (Lickorish–Millett), the signature function, the hyperbolic volume (Ruberman), the homology of the double branched cover $\Sigma_2(K)$ (so $\det K=|\Delta_K(-1)|$ is preserved), $\delta$-graded Khovanov homology over $\mathbb{F}_2$ (Wehrli), odd Khovanov homology (Bloom), and $\delta$-graded knot Floer homology (Zibrowius). Mutation does **not** preserve the Seifert genus ($g(11n42)=2$, $g(11n34)=3$) nor the smooth slice genus (Piccirillo).

**Montesinos trick.** If $u(K)=1$ then $\Sigma_2(K)$ is obtained by $\pm\frac{\det K}{2}$-surgery on a knot in $S^3$. This is the main source of $u\ge 2$ obstructions.

## 3. History & State of the Art (SOTA)

- **1957.** Kinoshita and Terasaka construct the knot $11n42$ with $\Delta \equiv 1$.
- **1970.** Conway introduces mutation while enumerating knots; the mutant of $11n42$ is the Conway knot $11n34$. The pair becomes the standard test case for every knot invariant.
- **1985–1987.** Lickorish–Millett prove mutation invariance of the HOMFLY and Kauffman polynomials; Ruberman proves invariance of the simplicial volume. Mutation is thereby established as the principal obstruction to distinguishing knots by quantum and geometric invariants.
- **1993.** Kronheimer–Mrowka prove the Milnor conjecture, giving $u(T_{p,q}) = (p-1)(q-1)/2$ — the template for gauge-theoretic lower bounds on $u$.
- **2003–2010.** $\tau$ (Ozsváth–Szabó) and $s$ (Rasmussen) give $g_4$ lower bounds. Both vanish on knots with $\Delta\equiv1$, hence give nothing for the KT/Conway pair.
- **2005–2006.** Ozsváth–Szabó obstruct $u=1$ using Heegaard Floer $d$-invariants of $\Sigma_2(K)$; Gordon–Luecke classify knots with $u=1$ admitting an essential Conway sphere — the only structural theorem directly linking unknotting number to the mutation apparatus.
- **2020.** Piccirillo shows the Conway knot is not slice, so $g_4(11n34)=1$ while $g_4(11n42)=0$: mutation changes the slice genus. This is the strongest evidence that it changes $u$ as well.
- **2026.** Tables (KnotInfo) record $u(11n42)=1$ and $u(11n34)=3$ *(frontier — verify: the value for the Conway knot rests on tabulated bounds rather than a single published obstruction theorem)*.

## 4. Partial Results / Verified Cases

- **Unknot detection.** $u(K)=0 \iff K$ unknot; mutation preserves the unknot (its only Conway spheres are inessential). So the conjecture holds at $n=0$.
- **Inessential Conway spheres.** If the mutating sphere is compressible or boundary-parallel, $K^\tau = K$ or $K^\tau$ is the mirror/reverse of $K$; since $u(K)=u(\overline K)=u(-K)$, the conjecture holds trivially.
- **Alternating knots.** For $K$ alternating with $u(K)=1$, the classification of unknotting crossings interacts with the Tait flype structure; mutants of alternating knots are alternating with equal $\sigma$, $\det$, and genus, and no alternating mutant pair with distinct unknotting number is known through $16$ crossings.
- **Torus knots.** $u(T_{p,q})=(p-1)(q-1)/2$ (Kronheimer–Mrowka); torus knots admit no essential Conway spheres, so all their mutants are the knots themselves.
- **$u=1$ with essential Conway spheres.** Gordon–Luecke (2006) classify these knots explicitly, constraining where an unknotting crossing can lie relative to the sphere; this settles mutation-invariance of $u$ for the classified families.
- **Signature-detected cases.** Whenever $u(K)=|\sigma(K)|/2$ (e.g. positive braid closures, $2$-bridge knots realizing the signature bound), the value is mutation-invariant because $\sigma$ is.
- **Tables.** Among knots up to $10$ crossings, no mutant pair has differing tabulated unknotting number; the first candidate discrepancy is at $11$ crossings.

## 5. Principal Obstacles

- **Every classical lower bound is itself mutation-invariant.** Bounds from $\Delta_K$, the Jones/HOMFLY polynomials, $\sigma$ and the Levine–Tristram signatures, the linking form on $H_1(\Sigma_2(K))$, and $\delta$-graded Khovanov and knot Floer homology cannot, by construction, separate a mutant pair. Any disproof must use an invariant known to break under mutation — currently only $g_4$-type and $4$-manifold trace invariants.
- **The $\Delta\equiv1$ collapse.** For the KT/Conway pair, $\det=1$, $\sigma=0$, $\tau=0$, $s=0$, and $\Sigma_2(K)$ is an integer homology sphere with $d=0$. Every standard obstruction returns $u\ge 1$ and stops.
- **Gauge theory is not local enough.** Instanton and Heegaard Floer obstructions to $u\le n$ pass through surgery descriptions of $\Sigma_2(K)$ or through slice surfaces in $B^4$; mutation is a modification supported in a ball that leaves these global objects nearly unchanged, so the obstructions degenerate simultaneously on both mutants.
- **Upper bounds are non-constructive from the other side.** Even granting $u(11n42)=1$, transporting an unknotting crossing across the mutation sphere is impossible in general: the crossing change may be forced to occur inside the mutated tangle, where the rotation permutes the strands.
- **No minimal-diagram theorem.** $u$ is not realized in general by a minimal-crossing diagram (Bleiler–Nakanishi), so exhaustive diagram search yields upper bounds only.

## 6. The Gap

Proven: $u$ is constant on mutation classes whenever it equals a mutation-invariant lower bound ($\sigma/2$, $\tau$, $s/2$), and $u=0$ is mutation-invariant. General statement: constancy for all mutant pairs.

The gap is one certified inequality. For the KT/Conway pair, the known facts give $1 \le u(11n34) \le 3$ and $u(11n42)=1$; the missing step is a proof that $u(11n34)\ge 2$. Because $\det(11n34)=1$, this means: show that the integer homology sphere $\Sigma_2(11n34)$ is **not** $\pm\frac12$-surgery on any knot in $S^3$, or find a $4$-dimensional obstruction to unknotting with one crossing change that survives $\tau=s=0$. Conversely, a proof of the conjecture would have to produce a mutation-invariant complete lower bound for $u$ — which would immediately give an algorithmic handle on the unknotting number, a stronger statement than anything currently known.

## 7. Current Research (as of June 2026)

- **Trace-based methods.** Piccirillo's technique — replacing $K$ by a knot with diffeomorphic $0$-trace and computing $s$ there — is being adapted to unknotting number: an unknotting sequence of length $n$ gives a genus-$0$ cobordism with $n$ double points, hence constraints on $n$-trace. Groups at MIT, UT Austin and Georgia Tech pursue this *(frontier — verify)*.
- **Instanton and singular instanton homology.** Kronheimer–Mrowka's $\mathrm{KHI}$ and the $s^\sharp$ invariant detect information invisible to Khovanov/Floer $\delta$-gradings; whether they are mutation-invariant is open and is the sharpest current question *(frontier — verify)*.
- **Immersed-curve and bordered technology.** Zibrowius' peculiar modules explain precisely which parts of knot Floer homology survive mutation; extending the analysis to the $\Upsilon$ and $\nu^+$ families is active.
- **Machine search.** Reinforcement-learning searches for unknotting sequences (following Gukov et al. on the unknotting problem) have raised confidence in the upper bound $u(11n34)\le 3$ but produce no lower bounds.

## 8. Future Work

1. Decide whether $\Sigma_2(11n34)$ arises by half-integer surgery, using Heegaard Floer $d$- and $\nu^+$-obstructions refined for homology spheres.
2. Determine whether $|u(K)-u(K^\tau)|$ is bounded; even $\le 1$ is unknown.
3. Test $u$ against genus-$2$ mutation (Cooper–Lickorish), a larger operation preserving the same polynomial invariants.
4. Build a mutation-sensitive unknotting obstruction from singular instanton homology of the double branched cover.
5. Extend the Gordon–Luecke classification from $u=1$ to $u=2$ for knots with essential Conway spheres.

## 9. Key References

- **[Foundational]** J. H. Conway. *An enumeration of knots and links, and some of their algebraic properties.* In "Computational Problems in Abstract Algebra", Pergamon Press, 1970, 329–358.
- **[Foundational]** S. Kinoshita, H. Terasaka. *On unions of knots.* Osaka Mathematical Journal 9 (1957), 131–153.
- **[Foundational]** W. B. R. Lickorish, K. C. Millett. *A polynomial invariant of oriented links.* Topology 26 (1987), 107–141.
- **[Foundational]** D. Ruberman. *Mutation and volumes of knots in $S^3$.* Inventiones Mathematicae 90 (1987), 189–215.
- **[Foundational]** P. Kronheimer, T. Mrowka. *Gauge theory for embedded surfaces, I.* Topology 32 (1993), 773–826.
- **[SOTA]** L. Piccirillo. *The Conway knot is not slice.* Annals of Mathematics 191 (2020), 581–591.
- **[SOTA]** C. McA. Gordon, J. Luecke. *Knots with unknotting number one and essential Conway spheres.* Algebraic & Geometric Topology 6 (2006), 2051–2116.
- **[SOTA]** P. Ozsváth, Z. Szabó. *Knots with unknotting number one and Heegaard Floer homology.* Topology 44 (2005), 705–745.
- **[SOTA]** J. Rasmussen. *Khovanov homology and the slice genus.* Inventiones Mathematicae 182 (2010), 419–447.
- **[SOTA]** S. Wehrli. *Mutation invariance of Khovanov homology over $\mathbb{F}_2$.* Quantum Topology 1 (2010), 111–128.
- **[SOTA]** J. M. Bloom. *Odd Khovanov homology is mutation invariant.* Mathematical Research Letters 17 (2010), 1–10.
- **[SOTA]** C. Zibrowius. *On symmetries of peculiar modules; or, $\delta$-graded knot Floer homology is mutation invariant.* Preprint, 2019.
- **[Recent]** A. Moore, L. Starkston. *Genus-two mutant knots with the same dimension in knot Floer and Khovanov homology.* Algebraic & Geometric Topology 15 (2015), 43–63.
- **[Recent]** A. Stoimenow. *Polynomial values, the linking form and unknotting numbers.* Mathematical Research Letters 11 (2004), 755–769.
- **[Survey]** R. Kirby (ed.). *Problems in Low-Dimensional Topology.* AMS/IP Studies in Advanced Mathematics 2.2, 1997.
- **[Survey]** C. Livingston, A. H. Moore. *KnotInfo: Table of Knot Invariants.* Online database, accessed 2026.

## 10. Worked Example / Concrete Special Case

**The pair.** Let $K_{\mathrm{KT}} = 11n42$ (Kinoshita–Terasaka) and $K_C = 11n34$ (Conway). They differ by a single mutation: both are built from the same two $2$-tangles $T_1, T_2$ across an essential Conway sphere $S$, with $K_C = (B_1,T_1)\cup_{\tau_y}(B_2,T_2)$.

**Shared data (all mutation-invariant).**

| invariant | value |
|---|---|
| $\Delta_K(t)$ | $1$ |
| $\det K = \|\Delta_K(-1)\|$ | $1$ |
| $\sigma(K)$, all Levine–Tristram $\sigma_\omega$ | $0$ |
| Jones, HOMFLY, Kauffman | identical |
| $\tau$, $s$ | $0$, $0$ |
| hyperbolic volume | equal (Ruberman) |

**Data that differs.** Seifert genus $g(K_{\mathrm{KT}})=2$, $g(K_C)=3$. Slice genus $g_4(K_{\mathrm{KT}})=0$ (the KT knot is slice), $g_4(K_C)=1$ (Piccirillo).

**Bounding $u$.**

*Upper bounds.* An explicit sequence of $3$ crossing changes in the standard $11$-crossing diagram unknots $K_C$, so $u(K_C)\le 3$. A single crossing change in the KT diagram yields the unknot, so $u(K_{\mathrm{KT}})=1$ (it cannot be $0$).

*Lower bounds for $K_C$.* Every standard obstruction collapses:
$$u(K_C)\ \ge\ g_4(K_C)=1,\qquad \tfrac{|s|}{2}=0,\qquad |\tau|=0,\qquad \tfrac{|\sigma|}{2}=0 .$$
The Alexander-polynomial criterion for $u=1$ is vacuous since $\Delta\equiv1$. Applying the Montesinos trick: $\det K_C = 1$, so if $u(K_C)=1$ then the integer homology sphere $\Sigma_2(K_C)$ is $\pm\frac12$-surgery on some knot $J\subset S^3$. The Ozsváth–Szabó $d$-invariant obstruction reads $d(\Sigma_2(K_C))=0$ — which is exactly what a $\pm\frac12$-surgery on a homologically trivial knot can produce. The obstruction returns no contradiction.

**Where it stalls.** We have $1\le u(K_C)\le 3$ and $u(K_{\mathrm{KT}})=1$. If $u(K_C)\ge 2$, mutation changes the unknotting number and the conjecture is false. Proving $u(K_C)\ge 2$ requires either showing $\Sigma_2(11n34)$ is not half-integer surgery on a knot in $S^3$, or a new $4$-dimensional obstruction that does not vanish when $\tau=s=0$. That single inequality is the whole content of Section 6.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*