---
id: 02-algebra-group-theory/kervaire-laudenbach-conjecture
title: "Kervaire-Laudenbach Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kervaire-Laudenbach Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/kervaire-laudenbach-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a group and let $w \in G * \langle t \rangle$ be a word in the free product of $G$ with an infinite cyclic group $\langle t\rangle$. Write $\sigma(w) \in \mathbb{Z}$ for the **exponent sum** of $t$ in $w$.

**Kervaire–Laudenbach Conjecture.** If $\sigma(w) \neq 0$, then the equation $w = 1$ is *solvable over* $G$: there is a group $H \supseteq G$ and an element $h \in H$ with $w(h) = 1$ in $H$. Equivalently, the natural map
$$G \longrightarrow \frac{G * \langle t \rangle}{\langle\langle w \rangle\rangle}$$
is injective, where $\langle\langle w \rangle\rangle$ is the normal closure of $w$.

A weaker form, usually called the **Kervaire Conjecture**, asserts only non-triviality: if $G \neq 1$ and $\sigma(w) \neq 0$, then $(G*\langle t\rangle)/\langle\langle w\rangle\rangle \neq 1$. The two are known to be equivalent as universal statements over all groups.

A complete proof must handle arbitrary $G$, including groups with torsion and groups that are not residually finite. A disproof requires an explicit pair $(G, w)$ with $\sigma(w)\neq 0$ and a proof that some $g \in G \setminus\{1\}$ dies in the quotient (or that the quotient is trivial).

The hypothesis $\sigma(w)\neq 0$ is necessary: over $G = \mathbb{Z}/6 = \langle c \rangle$, the equation $t^{-1}c^3 t\, c^{-2} = 1$ has $\sigma = 0$ and is unsolvable, since conjugation preserves order and $c^3$ has order $2$ while $c^2$ has order $3$.

## 2. Mathematical Foundations

**Normal form and invariants.** Every $w \in G*\langle t\rangle$ can be written
$$w = g_0 t^{\varepsilon_1} g_1 t^{\varepsilon_2} \cdots t^{\varepsilon_n} g_n, \qquad g_i \in G,\ \varepsilon_i \in \{\pm 1\},$$
with $g_i \neq 1$ for $0 < i < n$. Define
$$\sigma(w) = \sum_{i=1}^{n}\varepsilon_i \quad(\text{exponent sum}), \qquad \ell(w) = n \quad(\text{length, i.e. number of } t\text{-letters}).$$
Both are invariants of the conjugacy class of $w$ up to inversion.

**Relative presentation view.** The quotient $\widehat{G} = (G*\langle t\rangle)/\langle\langle w\rangle\rangle$ is the group with relative presentation $\langle G, t \mid w \rangle$. Its relative 2-complex has one 0-cell, one 1-cell ($t$) and one 2-cell ($w$) attached to the classifying space $K(G,1)$. Injectivity of $G \to \widehat G$ is implied by asphericity of this relative presentation, so the conjecture sits inside the circle of problems around the Whitehead asphericity conjecture. When $G$ is free, injectivity is exactly Magnus' **Freiheitssatz** for one-relator groups (1930), which is a theorem.

**Systems version.** For $w_1,\dots,w_m \in G * F(t_1,\dots,t_m)$ let $M = (\sigma_j(w_i))_{i,j} \in \mathbb{Z}^{m\times m}$ be the exponent-sum matrix. The **generalized Kervaire–Laudenbach conjecture** asserts $G \hookrightarrow (G*F)/\langle\langle w_1,\dots,w_m\rangle\rangle$ whenever $\det M \neq 0$. The case $m=1$ is Section 1.

**Relevant classes of groups.**
- $G$ is **locally indicable** if every nontrivial finitely generated subgroup surjects onto $\mathbb{Z}$.
- $G$ is **right-orderable** if it admits a total order invariant under right multiplication. Brodskii: locally indicable $\Rightarrow$ right-orderable (converse false, by Bergman's examples).
- $G$ is **residually finite** if $\bigcap \{N \trianglelefteq G : [G:N] < \infty\} = 1$; **locally residually finite** if every f.g. subgroup is.

**Two anchor theorems.**

*Gerstenhaber–Rothaus (1962).* If $G$ is locally residually finite and $\sigma(w)\neq 0$, then $w=1$ is solvable over $G$. Proof idea: embed a finite quotient in $U(n)$; the map $U(n)\to U(n)$, $u \mapsto w(u)$, has nonzero degree because its induced map on $H^{*}(U(n);\mathbb{Q})$ is multiplication by powers of $\sigma(w)$, hence it is surjective and $w(u)=1$ has a unitary solution.

*Klyachko (1993).* If $G$ is torsion-free and $\sigma(w) = \pm 1$ (a **unimodular** equation), then $w = 1$ is solvable over $G$. Proof idea: the "car crash lemma" — on a sphere with finitely many cars driving along closed smooth curves, each traversed with degree $1$ and no car standing still, some two cars collide head-on; applied to a spherical van Kampen diagram over $\langle G,t\mid w\rangle$ this forces a contradiction.

## 3. History & State of the Art (SOTA)

- **1930.** Magnus proves the Freiheitssatz — the free case of the conjecture.
- **1962.** Gerstenhaber and Rothaus prove the locally residually finite case (PNAS), motivated by Kervaire's question. In the same year B. H. Neumann and Levin study solvability of equations over groups; **Levin's conjecture** (every equation over a torsion-free group is solvable, with no exponent-sum hypothesis) is stated.
- **1965.** Kervaire, in work on higher-dimensional knot groups, formulates the non-triviality statement: killing one relator with $\sigma \neq 0$ cannot kill a nontrivial group.
- **1970s.** Laudenbach reaches the same statement from 3-manifold topology (2-spheres in 3-manifolds), giving the conjecture its double name.
- **1980–84.** Brodskii, and independently Howie, prove the conjecture (in the strong Levin form) for **locally indicable** groups, using right-orderability and tower arguments over 2-complexes.
- **1983–91.** Howie settles all equations of length $\ell(w)\le 3$; Edjvet–Howie settle $\ell(w)=4$.
- **1993.** Klyachko's car-crash proof for unimodular equations over torsion-free groups — the largest single advance, since it imposes no residual or indicability hypothesis.
- **1996.** Fenn–Rourke give a clean topological account of Klyachko's method; Gersten's reducible-diagram machinery and Bogley–Pride weight tests provide combinatorial alternatives.
- **2017–18.** Klyachko–Thom introduce homological/topological methods giving new proofs and extensions; Ivanov–Klyachko settle equations of length $\le 6$ over torsion-free groups.

Status: open in general; open even for torsion-free $G$ (where it is a special case of the still-open Levin conjecture); open for specific finitely presented targets such as Higman's group, which is torsion-free but has no nontrivial finite quotients.

## 4. Partial Results / Verified Cases

| Hypothesis on $G$ or $w$ | Result | Source |
|---|---|---|
| $G$ free | Freiheitssatz, conjecture holds | Magnus 1930 |
| $G$ locally residually finite (in particular finite, f.g. linear, free) | Holds for all $\sigma(w)\neq 0$ | Gerstenhaber–Rothaus 1962 |
| $G$ locally indicable | Holds for **all** $w$ with $w \notin G$, no $\sigma$ condition | Brodskii 1984; Howie 1981 |
| $G$ torsion-free, $\sigma(w)=\pm 1$ | Holds | Klyachko 1993 |
| $G$ arbitrary, $\ell(w)\le 3$ | Holds | Howie 1983 |
| $G$ arbitrary, $\ell(w)= 4$ | Holds | Edjvet–Howie 1991 |
| $G$ torsion-free, $\ell(w)\le 6$ | Holds (Levin form) | Ivanov–Klyachko 2018 |
| $w = g_1 t^{n_1}\cdots g_k t^{n_k}$ with all $|n_i|\ge 2$ ("high powers") | Broad families settled | Howie 1980s; Bogley–Pride weight tests |
| Systems, $\det M \neq 0$, $G$ locally residually finite | Holds | Gerstenhaber–Rothaus 1962 |

Quantitatively: the only unrestricted-length results require $G$ torsion-free plus $|\sigma(w)|=1$; the only unrestricted-$G$ results cap the length at $4$; over torsion-free groups the length cap is $6$.

## 5. Principal Obstacles

- **Torsion breaks Klyachko's method.** The car-crash lemma yields, in a minimal spherical diagram, a vertex whose corner labels multiply to an element of $G$ of small order; over a torsion-free group this is immediately a contradiction, but with torsion the configuration is consistent. No replacement for "no nontrivial finite-order elements" is known.
- **Failure of residual finiteness.** Gerstenhaber–Rothaus needs a finite (hence unitary) quotient that still sees the nontrivial element. Groups with no nontrivial finite quotients (Higman's group, infinite simple groups, Thompson-like groups) are invisible to this argument. Metric approximation (sofic/hyperlinear) is the natural weakening, but the analytic degree argument does not transfer without an index/degree theory for approximate unitary solutions.
- **Exponent sums $|\sigma| \ge 2$.** Klyachko's argument is genuinely degree-one: cars must traverse their curves with degree exactly $1$. For $|\sigma|\ge 2$ the corresponding covering-space unfolding loses the collision conclusion.
- **Length induction stalls.** Howie/Edjvet-style curvature and diagram case analysis grows combinatorially: length $5$ and $6$ over torsion-free groups already required hundreds of configurations, and the number of vertex types is not bounded by any known scheme.
- **No asphericity criterion is strong enough.** Weight tests certify asphericity of $\langle G,t\mid w\rangle$ only under curvature hypotheses that fail for short relators with torsion coefficients, and relative asphericity is strictly stronger than the injectivity actually wanted.

## 6. The Gap

Proved: $\{$torsion-free$\} \times \{|\sigma|=1\}$, $\{$any $G\} \times \{\ell \le 4\}$, $\{$torsion-free$\}\times\{\ell\le 6\}$, $\{$locally residually finite or locally indicable$\}\times\{$all $\sigma\neq 0\}$.

Wanted: all $G$, all $w$ with $\sigma(w)\neq 0$.

The boundary is a single missing mechanism: a combinatorial or analytic invariant of a minimal spherical diagram over $\langle G, t \mid w\rangle$ that is (i) insensitive to torsion in the coefficient group and (ii) sensitive to $\sigma(w)\ne 0$ rather than only to $\sigma(w)=\pm1$. Concretely, two crossings would suffice for the general case: pass from degree-$1$ to degree-$\sigma$ curve systems in the car-crash argument, and replace "finite quotient" by "approximate unitary representation" in the Gerstenhaber–Rothaus degree computation.

## 7. Current Research (as of June 2026)

- **Topological/homological methods (Klyachko, Thom, and collaborators; Moscow State University, TU Dresden).** Reformulating solvability via chain complexes attached to relative presentations, seeking degree invariants valid for $|\sigma|\ge 2$.
- **Metric approximation route.** Attempts to run the unitary degree argument for hyperlinear or sofic groups, replacing exact finite quotients by almost-representations into $U(n)$ with the Hilbert–Schmidt metric. *(frontier — verify)* claims that the conjecture holds for all hyperlinear groups should be checked against the exact hypotheses of the cited preprints.
- **Length-by-length extension (Edjvet, Williams, Ivanov; Nottingham, Essex).** Pushing the unrestricted-$G$ bound past $\ell(w)=4$ and the torsion-free bound past $\ell(w)=6$ by computer-assisted curvature distribution.
- **Relative asphericity programme (Bogley, Edjvet, Williams).** Classifying which relative presentations $\langle G,t\mid w\rangle$ are aspherical; each new aspherical family gives injectivity for free.
- **Orderability.** Determining whether right-orderability (weaker than local indicability) already suffices; Bergman's right-orderable non-locally-indicable examples are the test cases.

## 8. Future Work

- Prove the case $|\sigma(w)| = 2$ over torsion-free groups — the first genuinely new degree beyond Klyachko.
- Settle the conjecture for coefficient groups with torsion but no finite quotients; Higman's group and its finite-index-free relatives are the canonical targets.
- Establish or refute: right-orderable $\Rightarrow$ every equation over $G$ is solvable.
- Develop a "torsion-tolerant" car-crash lemma, e.g. by allowing cars to traverse curves with prescribed multiplicities and tracking a weighted collision count.
- Prove the generalized (systems, $\det M\neq 0$) form for torsion-free groups; currently even the unimodular systems case is not fully settled.
- Automate the length induction with formally verified curvature checks, so that $\ell \le 8$ becomes feasible.

## 9. Key References

- **[Foundational]** M. Gerstenhaber and O. S. Rothaus. *The solution of sets of equations in groups.* Proceedings of the National Academy of Sciences USA 48 (1962), 1531–1533.
- **[Foundational]** M. Kervaire. *On higher dimensional knots.* In: Differential and Combinatorial Topology (A Symposium in Honor of Marston Morse), Princeton University Press, 1965, 105–119.
- **[Foundational]** W. Magnus. *Über diskontinuierliche Gruppen mit einer definierenden Relation (Der Freiheitssatz).* Journal für die reine und angewandte Mathematik 163 (1930), 141–165.
- **[Foundational]** S. D. Brodskii. *Equations over groups and groups with one defining relation.* Siberian Mathematical Journal 25 (1984), 235–251.
- **[Foundational]** J. Howie. *On pairs of 2-complexes and systems of equations over groups.* Journal für die reine und angewandte Mathematik 324 (1981), 165–174.
- **[Foundational]** A. A. Klyachko. *A funny property of sphere and equations over groups.* Communications in Algebra 21 (1993), 2555–2575.
- **[Partial results]** J. Howie. *The solution of length three equations over groups.* Proceedings of the Edinburgh Mathematical Society 26 (1983), 89–96.
- **[Partial results]** M. Edjvet and J. Howie. *The solution of length four equations over groups.* Transactions of the American Mathematical Society 326 (1991), 345–369.
- **[SOTA / Recent]** S. V. Ivanov and A. A. Klyachko. *Solving equations of length at most six over torsion-free groups.* Journal of Group Theory 21 (2018), 329–345.
- **[SOTA / Recent]** A. A. Klyachko and A. Thom. *New topological methods to solve equations over groups.* Algebraic & Geometric Topology 17 (2017), 331–353.
- **[Method]** R. Fenn and C. Rourke. *Klyachko's methods and the solution of equations over torsion-free groups.* L'Enseignement Mathématique 42 (1996), 49–74.
- **[Method]** S. M. Gersten. *Reducible diagrams and equations over groups.* In: Essays in Group Theory (S. M. Gersten, ed.), MSRI Publications 8, Springer, 1987, 15–73.
- **[Survey]** V. A. Roman'kov. *Equations over groups.* Groups, Complexity, Cryptology 4 (2012), 191–239.
- **[Survey]** W. A. Bogley, M. Edjvet and G. Williams. *Aspherical relative presentations all over again.* In: Groups St Andrews 2017 in Birmingham, LMS Lecture Note Series 455, Cambridge University Press, 2019, 169–199.
- **[Background]** R. C. Lyndon and P. E. Schupp. *Combinatorial Group Theory.* Springer, 1977 (Chapter on equations over groups and small cancellation).

## 10. Worked Example / Concrete Special Case

Take the smallest group with torsion, $G = \mathbb{Z}/2 = \langle a \mid a^2 \rangle$, and the equation
$$w = t^2 a = 1, \qquad \sigma(w) = 2 \neq 0,\ \ \ell(w) = 2.$$

**Step 1 — form the quotient.**
$$\widehat G = \frac{G * \langle t\rangle}{\langle\langle t^2 a\rangle\rangle} = \langle a, t \mid a^2,\ t^2 a\rangle.$$

**Step 2 — eliminate $a$.** The relator $t^2a$ gives $a = t^{-2}$. Substituting into $a^2$:
$$\widehat G = \langle t \mid t^{-4}\rangle = \langle t \mid t^4 \rangle \cong \mathbb{Z}/4.$$

**Step 3 — check injectivity.** The image of $a$ is $t^{-2}$, which has order $2$ in $\mathbb{Z}/4$. Hence $G = \mathbb{Z}/2 \hookrightarrow \mathbb{Z}/4 = \widehat G$: the conjecture holds here, and the solution is $t = $ a generator of $\mathbb{Z}/4$, with $H = \mathbb{Z}/4 \supseteq G$.

**Step 4 — a second instance, same $G$.** Let $w = atat$, $\sigma(w) = 2$. Then
$$\widehat G = \langle a, t \mid a^2, (at)^2\rangle,$$
generated by the two involutions $x = a$ and $y = at$ with $t = xy$. No further relation ties $xy$ down, so $\widehat G \cong D_\infty = \mathbb{Z}/2 * \mathbb{Z}/2$, in which $a = x \neq 1$. Injectivity again holds.

**Step 5 — why this is not a proof.** Both cases are covered by Gerstenhaber–Rothaus, since $\mathbb{Z}/2$ is finite hence residually finite: map $G$ into $U(1)$ by $a \mapsto -1$ and solve $u^2 = -1$ with $u = i$. Klyachko's theorem, by contrast, does not apply at all — $G$ has torsion, and $\sigma(w)=2$ is not unimodular. Replacing $\mathbb{Z}/2$ by a torsion-bearing group with no nontrivial finite quotients removes both tools simultaneously, and there the equation $t^2a = 1$ is genuinely open. That contrast is the whole content of Sections 5 and 6.

**Step 6 — contrast with $\sigma = 0$.** Over $G=\mathbb{Z}/6=\langle c\rangle$, $w = t^{-1}c^3tc^{-2}$ forces $c^3$ (order $2$) to be conjugate to $c^{2}$ (order $3$) in any overgroup, which is impossible. So $\widehat G$ collapses $G$, showing that the hypothesis $\sigma(w)\neq 0$ cannot be dropped.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*