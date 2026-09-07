---
id: 08-logic-set-theory/l-space-problem
title: "L Space Problem"
topic: 08-logic-set-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# The L Space Problem

> **Topic:** Mathematical Logic & Set Theory · **ID:** `08-logic-set-theory/l-space-problem` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

An **L space** is a regular topological space that is hereditarily Lindelöf but not separable. The L space problem asks:

> Does ZFC prove that an L space exists?

The dual question — does ZFC prove that an **S space** (regular, hereditarily separable, not Lindelöf) exists? — is the S space problem. Both ask whether the two halves of the metric equivalence "hereditarily Lindelöf $\iff$ hereditarily separable" can be split without extra set-theoretic axioms.

A complete solution is either (a) a ZFC construction of a regular hereditarily Lindelöf non-separable space, or (b) a model of ZFC with no such space. Answer (a) was given by **Justin Tatch Moore in 2006**. The S space problem had the opposite answer: Todorcevic (1989) showed PFA implies no S spaces, and S spaces exist under CH, so their existence is independent. The asymmetry — L spaces in ZFC, S spaces not — is the content of the solution. Several sharpened forms remain open (Sections 6–7).

## 2. Mathematical Foundations

All spaces are regular and $T_1$; regularity is essential, since Hausdorff counterexamples are cheap.

**Definitions.** $X$ is *Lindelöf* if every open cover has a countable subcover; *hereditarily Lindelöf* (HL) if every subspace is, equivalently if every open subspace is Lindelöf. $X$ is *separable* if it has a countable dense subset; *hereditarily separable* (HS) if every subspace is. Cardinal functions:
$$hL(X)=\sup\{L(Y):Y\subseteq X\},\qquad hd(X)=\sup\{d(Y):Y\subseteq X\}.$$
Thus $X$ is an L space iff $hL(X)=\omega<d(X)$, and an S space iff $hd(X)=\omega<L(X)$.

**Separation duality.** $Y\subseteq X$ is *right-separated* if it can be well-ordered as $\{y_\alpha\}$ so that each initial segment is relatively open; *left-separated* if each initial segment is relatively closed. Then
$$hd(X)=\omega \iff X \text{ has no uncountable left-separated subspace},$$
$$hL(X)=\omega \iff X \text{ has no uncountable right-separated subspace}.$$
So an L space is exactly a space with an uncountable left-separated subspace but no uncountable right-separated one. This is why S and L look symmetric and, combinatorially, are not.

**Walks on ordinals.** Fix a *C-sequence* $\langle C_\alpha : \alpha<\omega_1\rangle$ with $C_{\alpha+1}=\{\alpha\}$ and $C_\alpha\subseteq\alpha$ cofinal of order type $\omega$ for limit $\alpha$. The minimal walk from $\beta$ down to $\alpha\le\beta$ is $\beta=\beta_0>\beta_1>\cdots>\beta_k=\alpha$ with $\beta_{i+1}=\min(C_{\beta_i}\setminus\alpha)$. From this one extracts the coherent sequence $e_\alpha:\alpha\to\omega$ of finite-to-one maps with $|\{\xi<\alpha : e_\alpha(\xi)\ne e_\beta(\xi)\}|<\omega$ for $\alpha<\beta$.

**Oscillation.** For finite sets of ordinals $s,t$ define the number of alternations
$$\operatorname{osc}(s,t)=\bigl|\{\xi\in s:\ t\cap[\xi,\ \min(s\setminus(\xi+1)))\neq\emptyset\}\bigr|,$$
i.e. the number of elements of $s$ immediately followed (before the next element of $s$) by an element of $t$. Todorcevic's oscillation theory shows $\operatorname{osc}$ is a strong coloring: on suitable uncountable families of finite sets it attains *every* value in $\omega$ on uncountably many pairs.

**Moore's space (outline).** Fix an irrational $\theta$, a sequence $\langle x_\alpha:\alpha<\omega_1\rangle$ of finite subsets of $\omega_1$ derived from the walk data, and set
$$w_\alpha(\xi)=\exp\bigl(2\pi i\,\theta\cdot \operatorname{osc}(x_\xi,x_\alpha)\bigr)\in\mathbb{T},\qquad \xi<\alpha,$$
extended by $1$ elsewhere, so $w_\alpha\in\mathbb{T}^{\omega_1}$. The space is $L=\{w_\alpha:\alpha<\omega_1\}$ in the product topology. Non-separability follows from unboundedness of $\operatorname{osc}$; hereditary Lindelöfness follows from the fact that on any uncountable set of indices the values $\operatorname{osc}$ realizes, pushed through $\theta$, are **equidistributed** in $\mathbb{T}$ by Weyl's theorem, so every point of a would-be right-separated sequence is already in the closure of its predecessors.

## 3. History & State of the Art (SOTA)

- **1920s.** Souslin's problem (1920) and the Sierpiński–Kuratowski school raise the question of which metric-space equivalences survive in general regular spaces.
- **1968.** Hajnal and Juhász construct, under CH, a first countable S space and a first countable L space, showing consistency of both.
- **1971.** Solovay and Tennenbaum force $\mathrm{MA}+\neg\mathrm{CH}$, killing Souslin lines — a Souslin continuum is simultaneously an S space and an L space, so this removed the classical source of both.
- **1970s–80s.** A large "S and L" industry: Kunen, Tall, Rudin, Fedorchuk (a compact hereditarily separable S space from $\diamondsuit$, 1977), Szentmiklóssy ($\mathrm{MA}+\neg\mathrm{CH}$ implies no compact S spaces). Roitman's *Basic S and L* (1984) is the standard survey of this period.
- **1989.** Todorcevic proves in *Partition Problems in Topology* that PFA implies there are no S spaces. The S space problem is thereby settled as independent.
- **2006.** Moore, *A solution to the L space problem* (JAMS 19): a ZFC L space, built from oscillations of minimal walks plus Weyl equidistribution. Same machinery underlies his five-element basis theorem for uncountable linear orders (Annals, 2006).
- **Since 2006.** Work moves to *strengthened* L spaces: compact, group-valued, strong (all finite powers HL), and to the L-analogues of the Todorcevic partition calculus. Todorcevic's *Walks on Ordinals and Their Characteristics* (2007) is the reference text for the technology.

## 4. Partial Results / Verified Cases

| Setting | Status |
|---|---|
| ZFC, general regular spaces | **Solved (Moore 2006):** an L space exists outright |
| $\diamondsuit$ / $\neg$SH | A Souslin continuum is a **compact, first countable, ccc** L space |
| CH | First countable L spaces (Hajnal–Juhász 1968); also L groups |
| $\mathrm{MA}+\neg\mathrm{CH}$ | No Souslin lines, hence no ccc compact L space of that type; L spaces still exist (Moore) |
| PFA | **No S spaces** (Todorcevic 1989), but L spaces exist — full asymmetry |
| Compact Hausdorff | Consistently yes (Souslin); ZFC existence of a compact L space **open**, tied to Fremlin's problem on perfectly normal compacta |
| Topological groups | Consistently yes (CH); ZFC existence of an L *group* **open** |
| Linearly ordered spaces (LOTS) | Fully classified: a LOTS is an L space iff it is ccc and non-separable, i.e. iff it is a Souslin line |
| Metrizable, second countable, or $\sigma$-compact metric | No L space: HL $\iff$ separable |

## 5. Principal Obstacles

Why the problem stood from 1968 to 2006:

- **Forcing symmetry misled.** Every technique that removed S spaces (MA, PFA, iterated ccc/proper forcing with side conditions) was expected by duality to remove L spaces too. Todorcevic's PFA argument uses that an uncountable *right*-separated space yields an uncountable set of finite sets with a specific partition property destroyed by proper forcing; the mirrored argument for left-separated spaces simply fails — the left-separated case has no such forcing-fragile trace.
- **Consistency proofs cannot exist.** Any attempt to force "no L spaces" was doomed; the obstruction was invisible because the ZFC object is not built from any classical cardinal-arithmetic or tree structure. Neither Souslin trees, gaps, nor Luzin sets survive under MA, so the natural inventory of $\omega_1$-objects was empty.
- **Elementary submodel and reflection arguments stall.** Standard countable-elementary-submodel closing-off shows an HL space is "locally small", but gives no dense countable set: density is not a reflecting property at $\omega_1$ in the way Lindelöfness is.
- **The needed coloring is not a partition relation.** What works is not $\omega_1\not\to[\omega_1]^2_{\omega}$ in raw form but the finer statement that $\operatorname{osc}$ realizes *all* values on any uncountable family of finite sets, combined with an *analytic* input (equidistribution of $\{n\theta\}$ mod 1). Purely combinatorial colorings give non-separability but destroy hereditary Lindelöfness; the irrational rotation is what makes the two compatible.

## 6. The Gap

The bare existence question has no gap left: Moore's space is a ZFC theorem. The remaining gaps are structural strengthenings, each of which fails to follow from the 2006 construction because $L=\{w_\alpha\}$ is neither compact, nor a group, nor closed under products:

1. **Compact L space.** Is there, in ZFC, a compact Hausdorff hereditarily Lindelöf non-separable space? Equivalently (up to known reductions) a perfectly normal compactum that is not separable. Moore's space has no compact-like closure property, and its closure in $\mathbb{T}^{\omega_1}$ is separable.
2. **L group.** Is there a ZFC hereditarily Lindelöf non-separable topological group? The group generated by $\{w_\alpha\}$ collapses the oscillation data by multiplying characters, destroying the equidistribution argument.
3. **Strong L space.** Is there a space all of whose finite powers are hereditarily Lindelöf and which is not separable? Powers of $\operatorname{osc}$-based spaces require simultaneous control of $\operatorname{osc}$ on $n$-tuples, which the oscillation theorem does not deliver uniformly. *(frontier — verify)*

## 7. Current Research (as of June 2026)

- **Walks-on-ordinals technology.** Todorcevic's programme (Toronto, Paris VII, Belgrade IMS) continues to mine $\rho$-functions, $\operatorname{osc}$, and coherent sequences for ZFC objects at $\omega_1$; the L space is the flagship application, alongside the five-element basis theorem.
- **Compact case.** Groups working on Fremlin's perfectly normal compactum problem and on the consistency of "every perfectly normal compactum is separable" (relatives of the Kunen–Tall and Eisworth–Nyikos programmes) treat the compact L space as the target. No ZFC example is known. *(frontier — verify)*
- **Higher cardinals.** L spaces at $\omega_2$ and above — whether the oscillation machinery lifts past $\omega_1$ — depends on the existence of coherent sequences at successors of regulars and interacts with square principles and large cardinals.
- **Functional-analytic offshoots.** The same oscillation family gives ZFC examples of non-separable Banach-space and topological-group phenomena (Kalenda-style Corson/Rosenthal compacta questions), keeping the construction in circulation outside pure topology. *(frontier — verify)*

## 8. Future Work

- Determine whether "there is no compact L space" is consistent; a natural test is whether PFA (or PFA plus a supercompact-level axiom) implies every perfectly normal compactum is separable.
- Isolate the exact combinatorial principle equivalent to the existence of an L group; candidate reductions run through $\rho$-functions with subadditivity.
- Push the oscillation theorem to $n$-tuples to settle the strong L space question.
- Reverse-mathematically calibrate Moore's construction: which fragment of ZFC (which instance of $\operatorname{osc}$-unboundedness plus Weyl) is actually consumed.
- Extend the S/L asymmetry to other dual cardinal-function pairs (spread vs. cellularity, tightness vs. character) to find further ZFC-decidable cases.

## 9. Key References

- **[Foundational]** A. Hajnal and I. Juhász. *On hereditarily $\alpha$-Lindelöf and hereditarily $\alpha$-separable spaces.* Annales Universitatis Scientiarum Budapestinensis, Sectio Mathematica, 11 (1968), 115–124.
- **[Foundational]** R. M. Solovay and S. Tennenbaum. *Iterated Cohen extensions and Souslin's problem.* Annals of Mathematics 94 (1971), 201–245.
- **[Foundational]** S. Todorcevic. *Partition Problems in Topology.* Contemporary Mathematics, vol. 84, American Mathematical Society, 1989.
- **[SOTA]** J. T. Moore. *A solution to the L space problem.* Journal of the American Mathematical Society 19 (2006), 717–736.
- **[SOTA]** J. T. Moore. *A five element basis for the uncountable linear orders.* Annals of Mathematics 163 (2006), 669–688.
- **[Technique]** S. Todorcevic. *Walks on Ordinals and Their Characteristics.* Progress in Mathematics 263, Birkhäuser, 2007.
- **[Technique]** S. Todorcevic. *Oscillations of sets of integers.* Advances in Applied Mathematics 20 (1998), 220–252.
- **[Survey]** J. Roitman. *Basic S and L.* In: K. Kunen and J. E. Vaughan (eds.), *Handbook of Set-Theoretic Topology*, North-Holland, 1984, 295–326.
- **[Survey]** I. Juhász. *Cardinal Functions in Topology — Ten Years Later.* Mathematical Centre Tracts 123, Amsterdam, 1980.
- **[Related]** V. V. Fedorchuk. *A compact space having the cardinality of the continuum with no convergent sequences.* Mathematical Proceedings of the Cambridge Philosophical Society 81 (1977), 177–181.

## 10. Worked Example / Concrete Special Case

**(a) A Souslin line is an L space.** Let $S$ be a Souslin continuum: a compact, connected, linearly ordered space that is ccc (every family of pairwise disjoint open intervals is countable) but not separable.

*Claim: $S$ is hereditarily Lindelöf.* Let $U\subseteq S$ be open, and suppose an open cover $\mathcal{V}$ of $U$ has no countable subcover. Refine $\mathcal V$ to open intervals. Build recursively intervals $I_\alpha\in\mathcal V$, $\alpha<\omega_1$, with $I_\alpha\not\subseteq\bigcup_{\beta<\alpha}I_\beta$; pick $p_\alpha\in I_\alpha\setminus\bigcup_{\beta<\alpha}I_\beta$ and an interval $J_\alpha\ni p_\alpha$ with $J_\alpha\subseteq I_\alpha$ and $J_\alpha\cap\{p_\beta:\beta<\alpha\}=\emptyset$ (possible since the $p_\beta$ enumerated so far miss a neighbourhood of $p_\alpha$ by regularity of the order topology on a first countable, non-separable LOTS). Shrinking, one extracts an uncountable pairwise disjoint family, contradicting ccc. Hence $hL(S)=\omega$; since $d(S)>\omega$, $S$ is an L space — and compact.

But $\mathrm{MA}_{\omega_1}$ implies no Souslin line exists (Solovay–Tennenbaum), so this example is **not** a ZFC construction. That is precisely the gap Moore closed.

**(b) Computing $\operatorname{osc}$.** Take $s=\{1,4,5,9\}$, $t=\{2,6,7,12\}$. For each $\xi\in s$ check whether $t$ meets the interval up to the next element of $s$:

| $\xi\in s$ | next elt. of $s$ | interval | $t\cap$ interval | counts? |
|---|---|---|---|---|
| 1 | 4 | $[1,4)$ | $\{2\}$ | yes |
| 4 | 5 | $[4,5)$ | $\emptyset$ | no |
| 5 | 9 | $[5,9)$ | $\{6,7\}$ | yes |
| 9 | — | — | — | no |

So $\operatorname{osc}(s,t)=2$. In Moore's space this makes the coordinate $w_\alpha(\xi)=e^{2\pi i\cdot 2\theta}$ for the corresponding pair. The oscillation theorem says that along any uncountable $A\subseteq\omega_1$ the integers $\operatorname{osc}(x_\xi,x_\alpha)$ take **all** values $n\in\omega$; Weyl's equidistribution theorem then says $\{e^{2\pi i n\theta}:n\in\omega\}$ is dense in $\mathbb{T}$ for irrational $\theta$. Consequently no $w_\alpha$ can be separated from the earlier $w_\beta$'s in any single coordinate — killing uncountable right-separated subspaces (hereditary Lindelöfness) — while the same unboundedness spreads the $w_\alpha$ far enough apart that no countable subfamily is dense (non-separability). The tension between these two demands is the whole difficulty, and the irrational rotation is what resolves it.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*