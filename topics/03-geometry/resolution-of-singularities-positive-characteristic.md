---
id: 03-geometry/resolution-of-singularities-positive-characteristic
title: "Resolution of Singularities in Positive Characteristic"
topic: 03-geometry
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Resolution of Singularities in Positive Characteristic

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/resolution-of-singularities-positive-characteristic` · **Status:** open

## 1. Problem Statement / Conjecture

**Conjecture (Resolution of singularities in characteristic $p>0$).** Let $k$ be a field of characteristic $p>0$ and let $X$ be a reduced separated scheme of finite type over $k$. Then there exists a proper birational morphism
$$\pi : \tilde{X} \longrightarrow X$$
with $\tilde{X}$ regular, $\pi$ an isomorphism over the regular locus $X_{\mathrm{reg}}$, and $\pi^{-1}(X_{\mathrm{sing}})$ a simple normal crossings divisor.

Stronger forms, all open in general:

- **Strong/embedded resolution.** If $X \subset W$ with $W$ regular, $\pi$ is a composite of blow-ups along regular centers contained in the successive strict transforms of $X_{\mathrm{sing}}$, and the total transform of $X$ becomes normal crossings.
- **Functorial resolution.** $\pi$ commutes with smooth morphisms and field extensions.
- **Local uniformization (Zariski form).** For every valuation $\nu$ of the function field $K(X)$, some birational model of $X$ is regular at the center of $\nu$.
- **General base.** The statement for reduced quasi-excellent Noetherian schemes (mixed characteristic included).

A complete solution is a proof valid for all $p$ and all dimensions, or a counterexample: a variety over some $\overline{\mathbb{F}}_p$ admitting no proper birational regular model. No expert expects the latter; the difficulty is entirely in method.

## 2. Mathematical Foundations

Let $W$ be a regular excellent scheme, $\mathcal{I} \subset \mathcal{O}_W$ a coherent ideal, and $\xi \in W$ a point with local ring $\mathcal{O}_{W,\xi}$ of maximal ideal $\mathfrak{m}$. The **order** is
$$\operatorname{ord}_\xi(\mathcal{I}) = \max\{ n : \mathcal{I}_\xi \subset \mathfrak{m}^n \}.$$
For $X = V(f) \subset W$ a hypersurface, $\operatorname{mult}_\xi X = \operatorname{ord}_\xi(f)$. Let $b = \max_{\xi} \operatorname{ord}_\xi(\mathcal{I})$ and let $\mathrm{Top}(\mathcal{I}) = \{\xi : \operatorname{ord}_\xi(\mathcal{I}) = b\}$, a closed set. Blowing up a regular center $Z \subset \mathrm{Top}(\mathcal{I})$ with exceptional divisor $E$, the **weak transform** is $\mathcal{I}' = \mathcal{I}\mathcal{O}_{W'} \cdot \mathcal{O}_{W'}(bE)$, and one always has $\operatorname{ord}_{\xi'}(\mathcal{I}') \le b$ for $\xi' \in E$. Resolution amounts to forcing strict decrease of a well-ordered invariant refining $b$.

**Characteristic-zero mechanism.** Write $f = z^b + a_1(x) z^{b-1} + \cdots + a_b(x)$ in Weierstrass form. The **Tschirnhaus substitution** $z \mapsto z - a_1/b$ is legitimate because $b$ is invertible, giving $a_1 = 0$; then $\{z=0\}$ is a **hypersurface of maximal contact**: it contains $\mathrm{Top}(f)$ and this persists under all permissible blow-ups. Descending to it yields the induction on dimension underlying Hironaka's proof, and the residual **coefficient ideal**
$$\mathcal{C}(f) = \sum_{i=1}^{b} \left( a_i \right)^{b!/i}$$
carries the secondary invariant $\operatorname{ord}(\mathcal{C})/b!$. The Hironaka invariant is the lexicographic string
$$\mathrm{inv}(\xi) = \big(b_1, m_1, b_2, m_2, \dots\big) \in \big(\mathbb{Q}_{\ge 0}\big)^{2d},$$
orders and exceptional-multiplicity counters at successive levels, and it drops strictly under blow-up of $\mathrm{Top}(\mathrm{inv})$.

**Characteristic $p$ obstruction.** If $p \mid b$ — the purely inseparable case $f = z^p - g(x)$ is typical — the substitution $z \mapsto z - a_1/b$ is undefined and no hypersurface of maximal contact exists in general (Narasimhan 1983). One replaces it by weaker data: the **characteristic polyhedron** $\Delta(f; x, z) \subset \mathbb{R}^d_{\ge 0}$ of Hironaka, the smallest polyhedron obtained over all admissible coordinate changes, and the **idealistic filtration** / differential saturation of Kawanoue–Matsuki, saturated under the Hasse–Schmidt derivations $D^{(n)}$ (ordinary derivations $\partial^n/n!$ are unavailable since $n!$ may vanish). Hironaka's **polyhedra game**, a combinatorial abstraction of the descent, was solved by Spivakovsky (1983); the char-$p$ variant with restricted moves is where the classical strategy fails.

## 3. History & State of the Art (SOTA)

- **1939–40.** Zariski proves local uniformization for algebraic function fields of characteristic $0$ and resolution for surfaces and $3$-folds over $\mathbb{C}$.
- **1956.** Abhyankar proves local uniformization, hence resolution, for surfaces over any field of characteristic $p>0$ (Ann. of Math. 63).
- **1964.** Hironaka proves resolution in all dimensions in characteristic $0$ (Ann. of Math. 79) — Fields Medal 1970. The proof uses maximal contact and hence excludes $p>0$.
- **1966.** Abhyankar resolves embedded algebraic surfaces and $3$-folds over algebraically closed fields of characteristic $p > 5$.
- **1983.** Spivakovsky solves Hironaka's polyhedra game; Narasimhan produces the char-$2$ example killing maximal contact.
- **1989–2005.** Villamayor, Bierstone–Milman, Encinas–Villamayor, Włodarczyk make characteristic-zero resolution constructive, canonical and functorial.
- **1996.** de Jong: every variety over any field admits an **alteration** (proper, surjective, generically finite of possibly inseparable degree) from a regular variety — the strongest general substitute available.
- **2008–2009.** Cossart–Piltant prove resolution for $3$-folds over **any** field, removing all restrictions on $p$.
- **2009.** Cutkosky gives a shorter proof for $3$-folds when $p > 5$.
- **2017.** Temkin: desingularization by $p$-alterations of degree a power of $p$ (Ann. of Math. 186). Hironaka circulates a claimed general proof; not accepted.
- **2019.** Cossart–Piltant extend to reduced quasi-excellent $3$-dimensional schemes, covering arithmetic $3$-folds over $\mathbb{Z}$.

## 4. Partial Results / Verified Cases

| Case | Status | Source |
|---|---|---|
| $\dim X \le 2$, any field, any $p$ | Solved (incl. embedded, functorial versions by Cossart–Jannsen–Saito) | Abhyankar 1956; Lipman 1978 for excellent surfaces |
| $\dim X = 3$, $k$ alg. closed, $p>5$ | Solved | Abhyankar 1966; Cutkosky 2009 |
| $\dim X = 3$, arbitrary field, all $p$ (incl. $p=2,3,5$) | Solved | Cossart–Piltant 2008, 2009 |
| $\dim X = 3$, reduced quasi-excellent schemes, mixed characteristic | Solved | Cossart–Piltant 2019 |
| $\dim X \ge 4$, any $p$ | **Open** | — |
| Toric, binomial, and monomial varieties, any dimension, any $p$ | Solved (combinatorial subdivision) | Kempf–Knudsen–Mumford–Saint-Donat 1973 |
| Abhyankar valuations (rational rank + transcendence degree $=\dim$) | Local uniformization in any characteristic | Knaf–Kuhlmann 2005 |
| Valuations of rank $1$ on function fields, $\dim \le 3$ | Local uniformization | Cossart–Piltant |
| Alterations, any dimension, any $p$ | Solved | de Jong 1996; Gabber ($\ell'$-alterations); Temkin 2017 ($p$-alterations) |
| Purely inseparable hypersurfaces $z^p = f(x_1,\dots,x_n)$, $n\le 3$ | Solved | Cossart–Piltant, Cutkosky |
| Characteristic $0$, all dimensions, functorial, weighted centers | Solved | Hironaka 1964; Abramovich–Temkin–Włodarczyk 2019–2022 |

## 5. Principal Obstacles

- **No maximal contact.** Narasimhan (1983) exhibits in characteristic $2$ a hypersurface in $\mathbb{A}^4$ whose multiplicity-$2$ locus is a monomial curve contained in **no** regular hypersurface germ. The dimension-reducing induction of Hironaka's proof therefore has no starting point.
- **Failure of Tschirnhaus.** For $f = z^p - g$, $\partial f/\partial z \equiv 0$; the derivative ideal $\mathcal{D}(f)$ loses the $z$-direction entirely, so differential operators cannot distinguish the "vertical" variable.
- **Kangaroo / jumping points.** After a permissible blow-up the *residual* order of the coefficient ideal can **increase** (Moh; Hauser). The natural secondary invariant is not upper semicontinuous along the resolution process, so no obvious well-ordering terminates.
- **Wild ramification.** Purely inseparable field extensions and Artin–Schreier covers $z^p - z = g$ produce singularities with no characteristic-zero analogue; the Galois-theoretic tools used to reduce to normal crossings (tameness, abhyankar's lemma) fail when $p$ divides ramification indices.
- **Non-functoriality.** Every known char-$p$ argument (Abhyankar's, Cossart–Piltant's) chooses coordinates, so the output is not canonical, cannot be glued over non-closed points, and does not descend along smooth morphisms. Cossart–Piltant's $3$-fold proof runs several hundred journal pages with heavy case analysis on $p \le 5$, giving no template for $\dim 4$.
- **Non-existence of maximal-multiplicity resolution.** Even in dimension $3$, one cannot always lower multiplicity by blowing up centers inside the top-multiplicity locus without first performing auxiliary modifications.

## 6. The Gap

Proven: dimension $\le 3$ (all $p$, all excellent bases). Conjectured: all dimensions.

The precise missing step is an **inductive invariant valid when $p \mid \operatorname{mult}$**. In characteristic $0$ the induction is: (i) maximal contact hypersurface $H$, (ii) coefficient ideal $\mathcal{C}$ on $H$, (iii) $\operatorname{ord}(\mathcal{C})$ strictly drops. In characteristic $p$, steps (i) and (iii) both fail. Candidate replacements — elimination algebras (Villamayor), the idealistic filtration with Hasse–Schmidt saturation (Kawanoue–Matsuki), the characteristic polyhedron (Hironaka, Cossart) — all produce an invariant that *can increase* at kangaroo points. What is needed is either a modified invariant with a proof of eventual strict decrease, or a genuinely different scheme (e.g. valuation-theoretic global patching, or a functorial weighted-blow-up formalism) that avoids induction on dimension. Dimension $4$ in characteristic $2$ is the first untouched case.

## 7. Current Research (as of June 2026)

- **Idealistic Filtration Program (IFP).** Kawanoue and Matsuki (Kyoto/Purdue) develop a differentially saturated filtration $\mathcal{R} \subset \mathcal{O}[t]$; they have proved resolution in dimension $3$ within the framework and isolate the exact obstruction as the "monomial case" in higher dimension.
- **Elimination algebras.** Villamayor, Bravo, Benito and the Madrid/Coruña school replace maximal contact by Rees-algebra-theoretic elimination; the surviving invariant ("$H$-order function") controls resolution up to the monomial case in any dimension.
- **Cossart–Jannsen–Saito programme.** A book-length canonical framework for excellent schemes, with functorial embedded resolution of $2$-dimensional schemes and machinery aimed at $3$-folds and beyond.
- **Weighted and stack-theoretic blow-ups.** Abramovich–Temkin–Włodarczyk's weighted resolution gives a dramatically simpler characteristic-zero proof; Abramovich–Quek and Rydh study logarithmic/multi-weighted blow-ups on Artin stacks, with partial char-$p$ statements. *(frontier — verify)*
- **$p$-alterations and inseparable local uniformization.** Temkin (HUJI) proves every variety in char $p$ admits a regular alteration of degree $p^n$; extending this to genuine birational modifications is an active line.
- **Hironaka's 2017 manuscript.** Circulated claim of general resolution in char $p$ via "$\ell$-th ideals"; the community has not verified it and gaps have been reported. *(frontier — verify)*

## 8. Future Work

- Prove resolution for $\dim X = 4$ over $\overline{\mathbb{F}}_p$ — the smallest open case, treated as the benchmark by Hauser and Kollár.
- Find a well-ordered invariant that is **provably** non-increasing at kangaroo points; equivalently, bound the number of consecutive increases of the residual order.
- Solve the char-$p$ analogue of Hironaka's polyhedra game with the restricted moves imposed by $p$-th powers.
- Deduce resolution from local uniformization for **all** valuations plus a quasi-compactness/patching argument on the Riemann–Zariski space; the patching step is itself open in char $p$ beyond dimension $3$.
- Transfer weighted-blow-up functoriality to char $p$: the stack-theoretic centers $(x_1^{w_1},\dots)$ do not require Tschirnhaus, which is why this route is currently the most optimistic.
- Derive the applications that currently need resolution: existence of minimal models, Hodge-theoretic statements, and $\ell$-adic weight arguments in char $p$ (many already recovered from de Jong's alterations).

## 9. Key References

- **[Foundational]** O. Zariski. *Local uniformization on algebraic varieties.* Annals of Mathematics 41 (1940), 852–896.
- **[Foundational]** S. S. Abhyankar. *Local uniformization on algebraic surfaces over ground fields of characteristic $p \ne 0$.* Annals of Mathematics 63 (1956), 491–526.
- **[Foundational]** H. Hironaka. *Resolution of singularities of an algebraic variety over a field of characteristic zero: I, II.* Annals of Mathematics 79 (1964), 109–203 and 205–326.
- **[Foundational]** S. S. Abhyankar. *Resolution of Singularities of Embedded Algebraic Surfaces.* Academic Press, 1966; 2nd enlarged ed., Springer Monographs in Mathematics, 1998.
- **[Obstruction]** R. Narasimhan. *Monomial equimultiple curves in positive characteristic.* Proceedings of the AMS 89 (1983), 402–406.
- **[Foundational]** M. Spivakovsky. *A solution to Hironaka's polyhedra game.* In: Arithmetic and Geometry, Vol. II, Progress in Mathematics 36, Birkhäuser, 1983, 419–432.
- **[Foundational]** A. J. de Jong. *Smoothness, semi-stability and alterations.* Publications Mathématiques de l'IHÉS 83 (1996), 51–93.
- **[SOTA]** V. Cossart, O. Piltant. *Resolution of singularities of threefolds in positive characteristic I.* Journal of Algebra 320 (2008), 1051–1082.
- **[SOTA]** V. Cossart, O. Piltant. *Resolution of singularities of threefolds in positive characteristic II.* Journal of Algebra 321 (2009), 1836–1976.
- **[SOTA]** V. Cossart, O. Piltant. *Resolution of singularities of arithmetical threefolds.* Journal of Algebra 529 (2019), 268–535.
- **[SOTA]** S. D. Cutkosky. *Resolution of singularities for 3-folds in positive characteristic.* American Journal of Mathematics 131 (2009), 59–127.
- **[SOTA]** M. Temkin. *Tame distillation and desingularization by $p$-alterations.* Annals of Mathematics 186 (2017), 97–126.
- **[SOTA]** H. Kawanoue, K. Matsuki. *Toward resolution of singularities over a field of positive characteristic (the idealistic filtration program) Part II.* Publications of RIMS 46 (2010), 359–422.
- **[SOTA]** H. Knaf, F.-V. Kuhlmann. *Abhyankar places admit local uniformization in any characteristic.* Annales Scientifiques de l'ENS 38 (2005), 833–846.
- **[Survey]** H. Hauser. *On the problem of resolution of singularities in positive characteristic (or: a proof we are still waiting for).* Bulletin of the AMS 47 (2010), 1–30.
- **[Survey]** J. Kollár. *Lectures on Resolution of Singularities.* Annals of Mathematics Studies 166, Princeton University Press, 2007.
- **[Survey]** V. Cossart, U. Jannsen, S. Saito. *Desingularization: Invariants and Strategy — Application to Dimension 2.* Lecture Notes in Mathematics 2270, Springer, 2020.
- **[Recent]** D. Abramovich, M. Temkin, J. Włodarczyk. *Functorial embedded resolution via weighted blowings up.* arXiv:1906.07106 (2019).

## 10. Worked Example / Concrete Special Case

Take $k$ algebraically closed with $\operatorname{char} k = 2$ and the surface
$$X = V(f) \subset \mathbb{A}^3_k, \qquad f = z^2 + x^3 + y^3 .$$

**Step 1: the singular locus.** In char $2$, $\partial f/\partial z = 2z = 0$, $\partial f/\partial x = 3x^2 = x^2$, $\partial f/\partial y = y^2$. So $X_{\mathrm{sing}} = \{x=y=z=0\}$, an isolated point of multiplicity $2$. Note $\partial f/\partial z \equiv 0$: the classical Tschirnhaus step $z \mapsto z - a_1/2$ is not merely unnecessary here, it is unavailable — the derivative ideal $\mathcal{D}(f) = (x^2, y^2)$ contains no element of order $1$, hence produces no candidate maximal-contact hypersurface. In char $\ne 2,3$ the same equation is the cone over a smooth plane cubic and is resolved by one blow-up.

**Step 2: blow up the origin.** In the $x$-chart, $x = x$, $y = xy_1$, $z = xz_1$:
$$f \circ \pi = x^2 z_1^2 + x^3 + x^3 y_1^3 = x^2\big(z_1^2 + x(1+y_1^3)\big).$$
The strict transform is $g = z_1^2 + x(1+y_1^3)$.

**Step 3: multiplicity does not drop.** $\partial g/\partial z_1 = 0$, $\partial g/\partial x = 1+y_1^3$, $\partial g/\partial y_1 = 3xy_1^2 = xy_1^2$. Singular points require $y_1^3 = 1$ and $xy_1^2 = 0$, so $x = 0$, $y_1 = \eta$ with $\eta^3 = 1$ (three points, since $\mathbb{F}_4 \subset k$), and then $g = 0$ forces $z_1 = 0$. Setting $y_1 = \eta + u$ and using $3=1$ in char $2$:
$$1 + y_1^3 = 1 + (\eta+u)^3 = \eta^2 u + \eta u^2 + u^3 = u\,(\eta^2 + \eta u + u^2),$$
a unit times $u$. Hence locally $g = z_1^2 + x u \cdot(\text{unit})$, still of multiplicity $2$. One blow-up of the origin has replaced one double point by **three** double points.

**Step 4: what the new points are.** $z_1^2 + xu$ has $\partial_{z_1} = 0$, $\partial_x = u$, $\partial_u = x$, so it is singular at the origin — whereas in characteristic $\ne 2$ the equation $z^2 = xu$ is the ordinary node $A_1$, and $\{z=0\}$ would be a maximal contact hypersurface. This is a *wild* double point: the tangent cone $z_1^2$ is a double plane, and $V(z_1)$ does **not** contain the singular locus of the next chart in general.

**Step 5: resolution.** Blowing up the new origin, $x=x$, $u = xu_1$, $z_1 = xz_2$ gives $x^2 z_2^2 + x^2 u_1 = x^2(z_2^2 + u_1)$, strict transform $z_2^2 + u_1$, which is regular ($\partial/\partial u_1 = 1$). So $X$ is resolved after two blow-ups — but only because $\dim X = 2$, where Abhyankar's theorem guarantees termination.

**What generalizes and what does not.** The mechanism seen here — vanishing $z$-derivative, multiplicity stalling at $p$, singular locus splitting into several points — is exactly the local picture that Abhyankar controls in dimension $2$ using the characteristic polyhedron $\Delta(f;x,y,z)$, whose vertices strictly improve under blow-up. In dimension $\ge 4$ and $p \mid \operatorname{mult}$, the analogous residual invariant can *increase* (Moh's kangaroo points), and no proof of termination is known. That single failure of monotonicity is the whole open problem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*