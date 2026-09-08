---
id: 02-algebra-group-theory/kaplanskys-unit-conjecture
title: "Kaplansky's Unit Conjecture"
topic: 02-algebra-group-theory
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kaplansky's Unit Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kaplanskys-unit-conjecture` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Let $K$ be a field and $G$ a **torsion-free** group. Form the group ring $K[G]$. The unit conjecture asserted:

> Every unit of $K[G]$ is **trivial**, i.e. of the form $\lambda g$ with $\lambda \in K^{\times}$ and $g \in G$.

Equivalently: if $\alpha\beta = 1$ in $K[G]$ then $|\operatorname{supp}\alpha| = |\operatorname{supp}\beta| = 1$.

The conjecture is **false**. Gardam (2021) exhibited $\alpha, \beta \in \mathbb{F}_2[P]$, each with support of size $21$, satisfying $\alpha\beta = 1$, where $P$ is the torsion-free Promislow (Hantzsche–Wendt / Passman fours) group. A complete disproof required exactly this: one field, one torsion-free group, one unit with support of size $> 1$. What remains open is the conjecture over fields of characteristic $0$ (in particular $K = \mathbb{Q}, \mathbb{C}$), and the two weaker companions — the zero-divisor and idempotent conjectures — which are untouched by the counterexample.

## 2. Mathematical Foundations

**Group ring.** For a field $K$ and group $G$,
$$K[G] = \Big\{ \alpha = \sum_{g \in G} \alpha_g\, g \;:\; \alpha_g \in K,\; \alpha_g = 0 \text{ for all but finitely many } g \Big\},$$
with multiplication $(\alpha\beta)_h = \sum_{g \in G} \alpha_g \beta_{g^{-1}h}$. The **support** is $\operatorname{supp}\alpha = \{g : \alpha_g \neq 0\}$. The **augmentation** $\varepsilon : K[G] \to K$, $\varepsilon(\alpha) = \sum_g \alpha_g$, is a ring homomorphism, so any unit has $\varepsilon(\alpha) \neq 0$.

**Why torsion-freeness is required.** If $g \in G$ has order $n \ge 2$, then
$$(1-g)(1 + g + \cdots + g^{n-1}) = 0,$$
producing zero divisors and (for suitable $K$) non-trivial units.

**The Kaplansky hierarchy.** For $G$ torsion-free:
- **Unit:** $\mathcal{U}(K[G]) = K^{\times} \times G$ (false).
- **Zero divisor:** $\alpha\beta = 0 \Rightarrow \alpha = 0$ or $\beta = 0$ (open).
- **Idempotent:** $\alpha^2 = \alpha \Rightarrow \alpha \in \{0,1\}$ (open).

Unit $\Rightarrow$ zero divisor $\Rightarrow$ idempotent, so the falsity of the strongest statement says nothing about the other two.

**Unique product property (UP).** $G$ has UP if for all finite non-empty $A, B \subseteq G$ there exists $g \in AB$ with a unique factorisation $g = ab$, $a \in A$, $b \in B$. If $G$ is UP then $K[G]$ has only trivial units and no zero divisors, since the unique product term cannot cancel: $(\alpha\beta)_g = \alpha_a\beta_b \neq 0$. Ordered groups are UP (Higman 1940); UP groups are torsion-free.

**The Promislow group.**
$$P = \langle a, b \mid a^{-1}b^{2}a = b^{-2},\; b^{-1}a^{2}b = a^{-2} \rangle .$$
$P$ is torsion-free, virtually $\mathbb{Z}^3$, and is the fundamental group of the closed flat Hantzsche–Wendt $3$-manifold. Put $X = a^2$, $Y = b^2$, $Z = (ab)^2$. Then $N = \langle X, Y, Z\rangle \cong \mathbb{Z}^3$ is normal of index $4$, with $P/N \cong (\mathbb{Z}/2)^2$ and conjugation acting by
$$a : (X,Y,Z) \mapsto (X, Y^{-1}, Z^{-1}), \qquad b : (X,Y,Z) \mapsto (X^{-1}, Y, Z^{-1}).$$
Every $\alpha \in K[P]$ decomposes uniquely as
$$\alpha = \alpha_1 + \alpha_a\, a + \alpha_b\, b + \alpha_{ab}\, ab, \qquad \alpha_\ast \in K[N] = K[X^{\pm},Y^{\pm},Z^{\pm}].$$

## 3. History & State of the Art (SOTA)

- **1940.** Graham Higman's thesis and *The units of group-rings* (Proc. LMS) prove triviality of units for right-orderable groups and initiate the study.
- **1957/1970.** Kaplansky circulates the unit, zero-divisor and idempotent problems; they appear in print in *Problems in the theory of rings revisited* (Amer. Math. Monthly, 1970).
- **1977.** Passman's *The Algebraic Structure of Group Rings* codifies UP and diffuseness-style approaches; the conjectures become standard test problems for group-ring theory.
- **1987–1988.** Rips and Segev construct the first torsion-free non-UP group; Promislow gives the small, explicit example $P$ with a $14$-element set violating UP. This removed the only general tool for a positive answer on a large class, but no unit was found in $K[P]$ for over three decades.
- **1988–1998.** Kropholler–Linnell–Moody prove the zero-divisor conjecture for torsion-free elementary amenable groups in characteristic $0$; Linnell's analytic methods (Atiyah-type $L^2$ arguments) extend idempotent results.
- **2000.** Bowditch introduces **diffuse** groups, a checkable strengthening of UP.
- **February 2021.** Gardam announces a non-trivial unit in $\mathbb{F}_2[P]$, found by an exhaustive SAT-solver search over supports inside a bounded region of $P$; published in *Annals of Mathematics* 194 (2021).
- **2021.** Murray produces further counterexamples, including in characteristic $3$, in the same and related groups.
- **2022–2026.** Gardam's survey *Kaplansky's conjectures* frames the residual problems; searches in characteristic $0$ and for zero divisors continue without success.

## 4. Partial Results / Verified Cases

**Where the unit conjecture is a theorem (any field $K$):**
- **Right-orderable groups** (Higman 1940) — includes free groups, free abelian groups, torsion-free nilpotent groups, braid groups, surface groups of genus $\ge 1$.
- **Unique product groups**, and the strictly smaller classes of **two-unique-product** and **diffuse** groups (Bowditch 2000); diffuseness is verifiable for many $3$-manifold groups.
- **Torsion-free groups with a UP-by-orderable structure**, and locally indicable groups (every non-trivial f.g. subgroup surjects onto $\mathbb{Z}$).
- $K[\mathbb{Z}^n] = K[t_1^{\pm},\dots,t_n^{\pm}]$: units are exactly monomials $\lambda t^{\mathbf{v}}$, by a leading-term argument in any total order on $\mathbb{Z}^n$.

**Where it fails:**
- $K$ of characteristic $2$, $G = P$: Gardam's unit, $|\operatorname{supp}| = 21$, verified by direct expansion; the identity holds over $\mathbb{F}_2$ and hence over every field of characteristic $2$.
- Characteristic $3$: Murray (2021), same group.
- Characteristic $0$ (e.g. $\mathbb{Q}$, $\mathbb{C}$): **no counterexample known** — open.

**Related conjectures still verified, not refuted:** $\mathbb{F}_2[P]$ has *no* zero divisors, since $P$ is virtually abelian and hence covered by the Kropholler–Linnell–Moody/Linnell results. The unit counterexample lives in a ring that is a domain.

## 5. Principal Obstacles

- **The only positive tool was combinatorial.** Every proof of unit-triviality goes through some form of "a support product term survives cancellation" (UP, orderability, diffuseness). Once $G$ is known to be non-UP, there is no replacement mechanism: no invariant separates trivial from non-trivial units in a non-UP torsion-free group.
- **Non-UP does not imply a counterexample.** Promislow's $14$-element set gives cancellation *potential*; converting it into an actual unit requires a global algebraic identity across all four cosets of $N$ simultaneously. Thirty-three years separated the two.
- **Search space explosion.** Gardam's method — encode "$\alpha\beta = 1$ with supports in a fixed finite window $S \subseteq P$" as a Boolean satisfiability instance — scales as $2^{|S|}$ in the worst case and only works over small finite fields, where coefficients are Boolean-encodable. Over $\mathbb{Q}$ the coefficients are unbounded rationals and the problem is no longer finite; SAT/SMT encodings lose completeness.
- **Characteristic $0$ has extra rigidity.** Analytic methods (trace conjectures, $L^2$-Betti numbers, Kaplansky's trace being an integer) constrain idempotents in $\mathbb{C}[G]$ but say almost nothing about units, since a unit need not be an idempotent or a projection. No analytic obstruction to non-trivial units is known, and no construction exploits characteristic $0$ either.
- **Zero divisors are strictly harder.** A unit is one equation $\alpha\beta = 1$; a zero divisor needs $\alpha\beta = 0$ with both non-zero, which the same SAT searches have failed to find in every group and field tried.

## 6. The Gap

Proven: units are trivial for UP/diffuse/orderable torsion-free groups, all fields. Refuted: characteristic $2$ and $3$ over $P$. The gap has two precise edges.

1. **Characteristic $0$.** Does there exist a torsion-free $G$ and a field $K$ with $\operatorname{char} K = 0$ such that $K[G]$ has a non-trivial unit? Gardam's identity does not lift: reducing his $\mathbb{F}_2$ coefficients to $\{0,1\} \subseteq \mathbb{Z}$ produces $\alpha\beta \equiv 1 \pmod 2$ but not $\alpha\beta = 1$; the carry terms do not vanish. Crossing this gap needs either a lift construction (a $p$-adic or deformation argument turning a mod-$p$ unit into a characteristic-$0$ one) or a characteristic-$0$-specific search over a group where $\mathbb{Z}$-coefficient bounds can be imposed.
2. **The remaining conjectures.** The step from "non-trivial unit" to "zero divisor" is exactly the step from $\alpha\beta = 1$ to $\alpha\beta = 0$ with $\alpha,\beta \ne 0$. Since $P$ is virtually abelian, its group ring is a domain, so *any* counterexample to the zero-divisor conjecture must come from a group outside the elementary amenable class — a place where no computational search is currently feasible.

## 7. Current Research (as of June 2026)

- **Extending the characteristic range.** After Murray's characteristic-$3$ examples, work continues on whether non-trivial units exist in $\mathbb{F}_p[P]$ for all primes $p$, and on classifying the units found so far up to the symmetries of $P$ *(frontier — verify)*.
- **SAT/SMT for group-theoretic decision problems.** Gardam's *Solving semidecidable problems in group theory* programme (Bonn / Max Planck Institute for Mathematics) treats support-bounded equations in group rings as constraint-satisfaction problems; the same pipeline is being aimed at zero divisors and at non-UP sets in hyperbolic-like groups.
- **Non-UP groups from small cancellation.** Gruber–Martin–Steenbock-style constructions supply lacunary hyperbolic torsion-free non-UP groups; whether their group rings contain non-trivial units is being probed, but the groups are infinitely presented and resist exhaustive search *(frontier — verify)*.
- **Diffuseness computations.** Groups of flat and hyperbolic $3$-manifolds are being certified diffuse or not (Kielak, Linton, and collaborators), sharpening the boundary of the positive theory.
- **Analytic/$L^2$ side.** Linnell-style methods and the Atiyah-conjecture circle remain the main hope for the *idempotent* conjecture over $\mathbb{C}$; nothing there transfers to units.

## 8. Future Work

- Search for a unit in $\mathbb{Z}[P]$ or $\mathbb{Q}[P]$ with bounded coefficient height, using integer programming rather than SAT — a negative result at a given height bound would itself be informative.
- Develop a lifting theory: conditions under which a unit in $\mathbb{F}_p[G]$ deforms to a unit in $\mathbb{Z}_p[G]$ (obstruction theory for the reduction map $\mathcal{U}(\mathbb{Z}_p[G]) \to \mathcal{U}(\mathbb{F}_p[G])$).
- Determine the group generated by the non-trivial units of $\mathbb{F}_2[P]$ and whether it is finitely generated — currently unknown.
- Attack the zero-divisor conjecture for torsion-free groups that are *not* elementary amenable and *not* UP; this is the smallest class where a counterexample could live.
- Settle the unit conjecture for hyperbolic torsion-free groups, where no non-UP example is known.

## 9. Key References

- **[Foundational]** G. Higman. *The units of group-rings.* Proceedings of the London Mathematical Society (2) 46, 231–248, 1940.
- **[Foundational]** I. Kaplansky. *Problems in the theory of rings revisited.* The American Mathematical Monthly 77(5), 445–454, 1970. [DOI](https://doi.org/10.2307/2317376)
- **[Foundational]** D. S. Passman. *The Algebraic Structure of Group Rings.* Wiley-Interscience, 1977.
- **[Foundational]** E. Rips, Y. Segev. *Torsion-free group without unique product property.* Journal of Algebra 108(1), 116–126, 1987. [DOI](https://doi.org/10.1016/0021-8693(87)90125-6)
- **[Foundational]** S. D. Promislow. *A simple example of a torsion-free, non-unique product group.* Bulletin of the London Mathematical Society 20(4), 302–304, 1988. [DOI](https://doi.org/10.1112/blms/20.4.302)
- **[SOTA / Recent]** G. Gardam. *A counterexample to the unit conjecture for group rings.* Annals of Mathematics 194(3), 967–979, 2021. (arXiv:2102.11818). [DOI](https://doi.org/10.4007/annals.2021.194.3.9)
- **[SOTA / Recent]** A. G. Murray. *More counterexamples to Kaplansky's unit conjecture.* arXiv preprint arXiv:2106.02147, 2021.
- **[Survey]** G. Gardam. *Kaplansky's conjectures.* arXiv preprint arXiv:2210.16600, 2022 (European Congress of Mathematics proceedings).
- **[Structural]** B. H. Bowditch. *A variation on the unique product property.* Journal of the London Mathematical Society 62(3), 813–826, 2000. [DOI](https://doi.org/10.1112/s0024610700001307)
- **[Structural]** P. H. Kropholler, P. A. Linnell, J. A. Moody. *Applications of a new K-theoretic theorem to soluble group rings.* Proceedings of the American Mathematical Society 104(3), 675–684, 1988. [DOI](https://doi.org/10.2307/2046771)

## 10. Worked Example / Concrete Special Case

**(a) Torsion is fatal; the leading-term proof for $\mathbb{Z}$.** Take $G = \mathbb{Z}/3 = \langle t \rangle$ over $\mathbb{F}_2$. Then
$$(1+t)(1+t+t^2) = 1 + t + t^2 + t + t^2 + t^3 = 1 + t^3 = 1 + 1 = 0,$$
a zero divisor, and $(1+t+t^2)^2 = 1+t^2+t^4 = 1+t+t^2$, a non-trivial idempotent. Torsion-freeness is exactly what blocks this.

Now $G = \mathbb{Z} = \langle t\rangle$, so $K[G] = K[t, t^{-1}]$. If $\alpha = \sum_{i=m}^{M} \alpha_i t^i$ with $\alpha_m, \alpha_M \neq 0$ and $\beta = \sum_{j=n}^{N}\beta_j t^j$ with $\beta_n, \beta_N \neq 0$, then the coefficient of $t^{m+n}$ in $\alpha\beta$ is $\alpha_m\beta_n \neq 0$ and that of $t^{M+N}$ is $\alpha_M\beta_N \neq 0$. If $\alpha\beta = 1$ then $m+n = M+N = 0$, forcing $m = M$ and $n = N$: both supports are singletons. This is the whole UP argument in miniature — one product term cannot cancel.

**(b) Why the argument dies in $P$.** In $P = \langle a,b\rangle$ with $X=a^2,\,Y=b^2,\,Z=(ab)^2$, there is no order for which the leading term is unambiguous: conjugation by $a$ inverts $Y$ and $Z$, so any "largest element" is moved below itself. Concretely, Promislow's $14$-element set $S \subseteq P$ has the property that **every** element of $S\cdot S$ is hit at least twice, so every coefficient of a product supported on $S$ can cancel. Later work found still smaller non-unique-product sets in $P$.

**(c) The shape of Gardam's unit.** Write $\alpha = \alpha_1 + \alpha_a a + \alpha_b b + \alpha_{ab}\,ab$ with each $\alpha_\ast \in \mathbb{F}_2[X^{\pm},Y^{\pm},Z^{\pm}]$. Because $a^2 = X$, $b^2 = Y$, $(ab)^2 = Z$ and conjugation acts by the sign matrices above, the equation $\alpha\beta = 1$ becomes a system of four Laurent-polynomial equations, e.g. the coset-$1$ component reads
$$\alpha_1\beta_1 + \alpha_a\, {}^{a}\beta_a\, X + \alpha_b\, {}^{b}\beta_b\, Y + \alpha_{ab}\, {}^{ab}\beta_{ab}\, Z = 1,$$
where ${}^{g}\gamma$ denotes the twist of $\gamma$ by the sign action of $g$, and the other three components must vanish. Gardam fixed a finite window of monomials, encoded these four $\mathbb{F}_2$-equations as a Boolean satisfiability instance (each coefficient one variable, each monomial one XOR clause) and let a SAT solver search. The solution has $|\operatorname{supp}\alpha| = |\operatorname{supp}\beta| = 21$ and, once written down, is verified by finite expansion — $441$ products reduced by the relations of $P$, with all terms but the identity cancelling in pairs over $\mathbb{F}_2$. Since $\varepsilon(\alpha) = 21 \bmod 2 = 1$, the augmentation obstruction is satisfied, as it must be.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*