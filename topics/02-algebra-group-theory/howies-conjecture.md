---
id: 02-algebra-group-theory/howies-conjecture
title: "Howie's Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Howie's Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/howies-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $G$ be a group and let $F = F(x_1,\dots,x_n)$ be free of rank $n$. A **system of $n$ equations in $n$ unknowns over $G$** is a set of words $w_1,\dots,w_n \in G * F$. The system is **solvable over $G$** if there is a group $H$ containing $G$ and elements $h_1,\dots,h_n \in H$ with $w_i(h_1,\dots,h_n) = 1$ for all $i$.

Let $\sigma_j(w_i) \in \mathbb{Z}$ be the exponent sum of $x_j$ in $w_i$, and let $M = (\sigma_j(w_i))_{i,j}$ be the $n \times n$ **exponent-sum matrix**. The system is **non-singular** if $\det M \neq 0$.

> **Conjecture (Howie, 1981).** Every non-singular system of $n$ equations in $n$ unknowns over a torsion-free group is solvable over that group.

The $n = 1$ case is the Kervaire–Laudenbach conjecture; the general statement is usually called the **Kervaire–Laudenbach–Howie conjecture**. The stronger version dropping "torsion-free" (solvability over *every* group) is also open and is often stated alongside it.

A proof must produce, for every torsion-free $G$ and every non-singular $W$, an embedding $G \hookrightarrow H$ realising a solution; equivalently (Section 2) it must show the canonical map $G \to (G*F)/\langle\langle w_1,\dots,w_n\rangle\rangle$ is injective. A disproof requires an explicit torsion-free $G$ and non-singular system whose quotient kills some $g \neq 1$.

## 2. Mathematical Foundations

**Equivalence of the two formulations.** Set
$$G_W \;=\; \big(G * F(x_1,\dots,x_n)\big) \big/ \big\langle\!\big\langle\, w_1,\dots,w_n \,\big\rangle\!\big\rangle .$$
If $\varphi: G \to G_W$ is injective, the images $\bar x_j$ solve the system in $H = G_W$. Conversely a solution in $H \geq G$ factors $G \to G_W \to H$, forcing injectivity. So the conjecture is a **Freiheitssatz** for the relative presentation $\langle G, x_1,\dots,x_n \mid w_1,\dots,w_n\rangle$.

**Topological model.** Let $K_G$ be a $K(G,1)$ with one vertex. Attach $n$ oriented $1$-cells $x_1,\dots,x_n$ and $n$ $2$-cells along the words $w_i$, giving a relative $2$-complex $(K, K_G)$ with
$$\chi(K,K_G) \;=\; -n + n \;=\; 0 .$$
Then $\pi_1(K) = G_W$, and the conjecture asserts $\pi_1(K_G) \to \pi_1(K)$ is injective. The matrix $M$ is exactly the relative boundary map
$$\partial_2 \otimes \mathbb{Z} : H_2(K,K_G) \cong \mathbb{Z}^n \longrightarrow H_1(K_G \cup K^{(1)}, K_G) \cong \mathbb{Z}^n,$$
so non-singularity says $H_2(K, K_G;\mathbb{Q}) = 0$: the added cells do not create rational homology. This is the exact algebraic-topological reason non-singularity is the right hypothesis.

**Necessity of non-singularity.** If $\det M = 0$ the statement fails: over $G = \langle a \rangle * \langle b\rangle \cong \mathbb{Z}/2 * \mathbb{Z}/3$ the equation $x a x^{-1} b^{-1} = 1$ has $\sigma_1 = 0$ and no solution in any overgroup, since conjugate elements have equal order.

**Diagram calculus.** Solvability is refuted only by a *reduced relative spherical diagram*: a van Kampen-type diagram over $(K,K_G)$ whose $2$-cells carry labels $w_i^{\pm1}$, whose corner labels lie in $G$, and no two cells cancel. A complex in which no such diagram exists is **diagrammatically reducible (DR)**; DR $\Rightarrow$ aspherical $\Rightarrow$ Freiheitssatz. Weight tests, curvature distribution, and Klyachko's "car" argument are all devices for excluding such diagrams.

**Local indicability.** $G$ is *locally indicable* if every non-trivial finitely generated subgroup surjects onto $\mathbb{Z}$. Locally indicable $\Rightarrow$ left-orderable (Burns–Hale) $\Rightarrow$ torsion-free; both implications are strict.

## 3. History & State of the Art (SOTA)

- **1962.** Gerstenhaber and Rothaus prove that non-singular systems over *locally residually finite* groups are solvable, by a degree argument in the compact Lie group $U(m)$: non-singularity forces the associated map $U(m)^n \to U(m)^n$ to have non-zero degree, so $1$ is in its image. This yields the first evidence for the conjecture in all $n$. Levin, the same year, shows every equation with only positive occurrences of the unknowns is solvable over any group.
- **1960s.** Kervaire and Laudenbach, motivated by higher-dimensional knot groups, ask the $n=1$ case: if $G \neq 1$ then $\langle G, t \mid w \rangle \neq 1$.
- **1981.** Howie, in *On pairs of 2-complexes and systems of equations over groups* (Crelle 324), proves the full statement for **locally indicable** $G$, using towers of covering spaces (a Papakyriakopoulos-style tower argument adapted to $2$-complexes), and conjectures the torsion-free case.
- **1983–1991.** Length-based attacks on single equations over *arbitrary* groups: length $\leq 3$ (Howie), length $\leq 4$ (Edjvet–Howie).
- **1993.** Klyachko's *funny property of the sphere* settles $n=1$ for all torsion-free $G$ — the single largest advance. Fenn–Rourke (1996) recast the argument in terms of car-crash diagrams and vector fields on $S^2$.
- **2017.** Klyachko and Thom replace compactness in the Gerstenhaber–Rothaus argument by metric ultraproducts of unitary groups, proving non-singular systems solvable over **hyperlinear** groups — a class containing every group not known to be a counterexample to soficity.

## 4. Partial Results / Verified Cases

| Case | Result | Source |
|---|---|---|
| $G$ locally indicable, all $n \geq 1$ | Solvable | Howie 1981 (also Brodskii 1984, $n=1$) |
| $G$ locally residually finite, all $n$ | Solvable | Gerstenhaber–Rothaus 1962 |
| $G$ hyperlinear (incl. sofic, amenable, residually finite, LEF), all $n$ | Solvable | Klyachko–Thom 2017 |
| $G$ torsion-free, $n = 1$ | Solvable | Klyachko 1993 |
| $G$ arbitrary, $n=1$, $|w| \leq 3$ | Solvable | Howie 1983 |
| $G$ arbitrary, $n=1$, $|w| \leq 4$ | Solvable | Edjvet–Howie 1991 |
| $G$ arbitrary, $w$ positive in the unknowns | Solvable | Levin 1962 |
| $G$ arbitrary, $n=1$, $|w| \leq 6$ | Solvable *(frontier — verify attribution)* | Ivanov–Klyachko, ca. 2000 |
| Staggered systems over free $G$ | Aspherical, hence solvable | Howie 1983; Gersten 1987 |

The genuinely open region is: $n \geq 2$, $G$ torsion-free but neither locally indicable nor hyperlinear. No candidate counterexample is known for any $n$.

## 5. Principal Obstacles

- **The tower argument needs an indicable subgroup.** Howie's induction peels off a subgroup mapping onto $\mathbb{Z}$ to reduce the exponent sums. Torsion-freeness gives no such quotient: Higman's group $\langle a,b,c,d \mid a^b = a^2,\, b^c = b^2,\, c^d = c^2,\, d^a = d^2\rangle$ is torsion-free, infinite, and perfect, so it is locally indicable nowhere. Every extension of the tower method stalls exactly at such groups.
- **Klyachko's method is intrinsically one-dimensional.** The car-crash argument places a car on the boundary of each $2$-cell of a reduced spherical diagram and uses the Euler characteristic of $S^2$ to force a collision; the counting works because all $2$-cells are labelled by *one* word with *one* exponent sum. With $n \geq 2$ distinct words the collision bookkeeping has no known weighting that reproduces $\chi(S^2)=2$; determinant non-singularity is a global linear-algebra condition that no local curvature distribution has yet been made to see.
- **Degree theory needs an approximating compact group.** Gerstenhaber–Rothaus and Klyachko–Thom both require $G$ to embed in a (limit of) unitary group(s) so that a Brouwer/Fuglede–Kadison degree can be computed. For a group with no finitary or hyperlinear approximation the map $H^n \to H^n$ has no degree, and there is no known replacement invariant.
- **Asphericity is unavailable.** The natural route — show $(K,K_G)$ is DR or aspherical — is blocked because non-singular relative complexes are not DR in general, and the Whitehead asphericity conjecture, which would imply the $n=1$ case, is itself open.
- **Torsion genuinely breaks small-cancellation control.** In the version without the torsion-free hypothesis, relative diagrams over $G$ with finite-order coefficients admit low-curvature cells that defeat every known weight test, which is why the length-based results stop near $|w| = 6$.

## 6. The Gap

Two gaps, in different directions.

1. **Class gap ($n = 1$ already closed, $n \geq 2$ open).** For $n=1$ the passage from *locally indicable* (Howie/Brodskii) to *torsion-free* (Klyachko) was crossed by a new combinatorial invariant on spherical diagrams. For $n \geq 2$ the corresponding step is unmade: what is required is a curvature or counting argument on reduced spherical diagrams over $n$ relator classes that consumes the hypothesis $\det M \neq 0$ rather than merely $\sigma \neq 0$ for one relator.
2. **Approximation gap.** Klyachko–Thom settle all $n$ for hyperlinear groups. Since no group is known to be non-hyperlinear, the conjecture is "true for every group anyone can exhibit". Closing the gap therefore means either proving every group is hyperlinear (Connes-embedding-flavoured, and now known false in the operator-algebraic form MIP*=RE addresses) or producing a solvability argument free of any finite-dimensional approximation.

## 7. Current Research (as of June 2026)

- **Moscow (Klyachko and collaborators).** Continued refinement of car-crash/diagram techniques toward two-equation systems and toward equations over groups with torsion; the target is a non-singular $2 \times 2$ system over an arbitrary torsion-free group. *(frontier — verify)*
- **Dresden (Thom's group) and operator-algebraic approaches.** After the collapse of the Connes embedding problem, the status of "every group is hyperlinear" is the live question; work by Thom and coauthors on universal solvability of group equations pushes the Gerstenhaber–Rothaus degree method into ultraproduct and sofic settings, and asks which weakened approximation properties still support a degree. *(frontier — verify)*
- **Nottingham / Heriot-Watt tradition (Edjvet, Howie's students).** Curvature-distribution proofs of asphericity for specific relative presentations, extending the length-based hierarchy for single equations past length six.
- **Whitehead-asphericity school (Bogley, Harlander, Rosebrock).** Work on DR complexes, weight tests and labelled oriented trees; positive results there transfer to the $n=1$ case of this conjecture.
- **Orderability.** Refinements of Burns–Hale and locally indicable/left-orderable separation, aiming to enlarge Howie's 1981 theorem to left-orderable or diffusely orderable groups.

## 8. Future Work

- Find a weight test on relative spherical diagrams whose total curvature bound depends on $\det M$, not on individual exponent sums — the single most-cited desideratum for the $n \geq 2$ case.
- Reduce systems to single equations: given a non-singular $n \times n$ system, produce an equivalent non-singular equation over an overgroup. No such reduction is known, and a proof that none exists would itself be informative.
- Prove the conjecture for left-orderable, or for diffuse, torsion-free groups, extending Howie 1981 past local indicability.
- Settle the $n = 1$ case over groups **with** torsion beyond bounded length; the length-$\leq 6$ frontier has resisted extension for over two decades.
- Determine whether Howie's tower method admits a relative/acylindrical version applicable to torsion-free hyperbolic and acylindrically hyperbolic groups.

## 9. Key References

- **[Foundational]** M. Gerstenhaber and O. S. Rothaus. *The solution of sets of equations in groups.* Proceedings of the National Academy of Sciences USA 48 (1962), 1531–1533.
- **[Foundational]** F. Levin. *Solutions of equations over groups.* Bulletin of the American Mathematical Society 68 (1962), 603–604. [DOI](https://doi.org/10.1090/s0002-9904-1962-10868-4)
- **[Foundational]** J. Howie. *On pairs of 2-complexes and systems of equations over groups.* Journal für die reine und angewandte Mathematik 324 (1981), 165–174. [DOI](https://doi.org/10.1515/crll.1981.324.165)
- **[Foundational]** S. D. Brodskii. *Equations over groups and groups with one defining relation.* Siberian Mathematical Journal 25 (1984), 235–251. [DOI](https://doi.org/10.1007/bf00971461)
- **[Key advance]** A. A. Klyachko. *A funny property of sphere and equations over groups.* Communications in Algebra 21 (1993), 2555–2575. [DOI](https://doi.org/10.1080/00927879308824692)
- **[Key advance]** R. Fenn and C. Rourke. *Klyachko's methods and the solution of equations over torsion-free groups.* L'Enseignement Mathématique (2) 42 (1996), 49–74.
- **[Partial results]** J. Howie. *The solution of length three equations over groups.* Proceedings of the Edinburgh Mathematical Society 26 (1983), 89–96. [DOI](https://doi.org/10.1017/s0013091500028108)
- **[Partial results]** M. Edjvet and J. Howie. *The solution of length four equations over groups.* Transactions of the American Mathematical Society 326 (1991), 345–369. [DOI](https://doi.org/10.2307/2001867)
- **[SOTA / Recent]** A. Klyachko and A. Thom. *New topological methods to solve equations over groups.* Algebraic & Geometric Topology 17 (2017), 331–353. [DOI](https://doi.org/10.2140/agt.2017.17.331)
- **[Survey]** S. M. Gersten. *Reducible diagrams and equations over groups.* In: Essays in Group Theory (ed. S. M. Gersten), MSRI Publications 8, Springer, 1987, 15–73. [DOI](https://doi.org/10.1007/978-1-4613-9586-7_2)
- **[Survey]** W. A. Bogley. *J. H. C. Whitehead's asphericity question.* In: Two-Dimensional Homotopy and Combinatorial Group Theory, LMS Lecture Note Series 197, Cambridge University Press, 1993, 309–334. [DOI](https://doi.org/10.1017/cbo9780511629358.012)
- **[Context]** J. Howie. *Some remarks on a problem of J. H. C. Whitehead.* Topology 22 (1983), 475–485. [DOI](https://doi.org/10.1016/0040-9383(83)90038-1)

## 10. Worked Example / Concrete Special Case

Take the $2 \times 2$ system over a group $G$ with distinguished elements $a, b \in G$:
$$w_1 = x^2 y a^{-1}, \qquad w_2 = x y^3 b^{-1}.$$

**Step 1 — non-singularity.** Exponent sums: $\sigma_x(w_1) = 2$, $\sigma_y(w_1) = 1$, $\sigma_x(w_2) = 1$, $\sigma_y(w_2) = 3$. So
$$M = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}, \qquad \det M = 5 \neq 0 .$$
The system is non-singular, so Howie's conjecture predicts $G \hookrightarrow G_W = \langle G, x, y \mid x^2 y = a,\ x y^3 = b\rangle$ for every torsion-free $G$.

**Step 2 — the abelian shadow.** Let $G = \mathbb{Z} = \langle c \rangle$, $a = c^{\alpha}$, $b = c^{\beta}$. Inside the divisible overgroup $H = \mathbb{Q}$ the system becomes linear: $2u + v = \alpha$, $u + 3v = \beta$, with unique solution
$$u = \frac{3\alpha - \beta}{5}, \qquad v = \frac{2\beta - \alpha}{5}.$$
Solvable exactly because $\det M = 5 \neq 0$; had $M$ been singular with inconsistent right-hand side, no overgroup would help. This is the finite-dimensional shadow of the Gerstenhaber–Rothaus degree argument.

**Step 3 — the general case by known theorems.** If $G$ is locally indicable (free groups, free products of torsion-free abelian groups, torsion-free one-relator groups by Brodskii), Howie 1981 gives a solution. If $G$ is residually finite or merely hyperlinear, Klyachko–Thom 2017 gives one. For $G$ torsion-free, perfect and non-hyperlinear — no such group is known to exist — the instance is open.

**Step 4 — why torsion-freeness is not obviously needed here but is elsewhere.** Replace the system by the single singular equation $x a x^{-1} b^{-1} = 1$ with $a$ of order $2$ and $b$ of order $3$. Then $M = (0)$, and any solution would conjugate $a$ to $b$, forcing $2 = 3$. Non-singularity is thus not a technical convenience but the exact homological condition $H_2(K,K_G;\mathbb{Q}) = 0$ from Section 2.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*