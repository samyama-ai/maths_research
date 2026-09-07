---
id: 02-algebra-group-theory/lipman-zariski-conjecture
title: "Lipman-Zariski Conjecture"
topic: 02-algebra-group-theory
status: open
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Lipman-Zariski Conjecture

> **Topic:** Algebra & Group Theory · **ID:** `02-algebra-group-theory/lipman-zariski-conjecture` · **Status:** open

## 1. Problem Statement / Conjecture

Let $X$ be a complex algebraic variety (or a reduced complex space, or a reduced excellent scheme over a field $k$ of characteristic $0$). Let $\mathcal{T}_X = \mathcal{H}om_{\mathcal{O}_X}(\Omega^1_X, \mathcal{O}_X)$ be its tangent sheaf, i.e. the sheaf of $k$-derivations of $\mathcal{O}_X$.

**Conjecture (Lipman–Zariski).** If $\mathcal{T}_X$ is a locally free $\mathcal{O}_X$-module, then $X$ is smooth.

Equivalently, in local algebra: let $(R,\mathfrak{m},k)$ be a local ring essentially of finite type over a field $k$ of characteristic $0$, with $k \to R$ giving $R/\mathfrak{m}$ separable. If the derivation module $\operatorname{Der}_k(R)$ is a free $R$-module, then $R$ is regular.

The converse is elementary: if $X$ is smooth, $\Omega^1_X$ and hence $\mathcal{T}_X$ are locally free of rank $\dim X$. A complete proof must show freeness of the *dual* forces regularity; a disproof requires one singular $X$ over a characteristic-$0$ field with $\mathcal{T}_X$ locally free. The statement is **false in characteristic $p>0$**, so any proof must use characteristic-zero-only input (resolution of singularities, Hodge theory, or the minimal model program).

## 2. Mathematical Foundations

Let $A$ be a $k$-algebra. The module of Kähler differentials $\Omega_{A/k}$ represents derivations:
$$\operatorname{Der}_k(A,M) \;\cong\; \operatorname{Hom}_A(\Omega_{A/k}, M),$$
so $\operatorname{Der}_k(A) = \operatorname{Hom}_A(\Omega_{A/k},A) = (\Omega_{A/k})^{*}$.

**Contrast with the Zariski–Nagata / Kunz criterion.** For $R$ local, essentially of finite type over a perfect field of characteristic $0$:
$$\Omega_{R/k} \text{ free} \;\Longleftrightarrow\; R \text{ regular}.$$
The Lipman–Zariski conjecture asks the same with $\Omega$ replaced by its dual. Dualizing loses information: $(\Omega_{R/k})^{*}$ is a second-syzygy (reflexive) module and is insensitive to torsion in $\Omega_{R/k}$, which is precisely where singularity information lives. This is why the two statements are not formally equivalent.

**Reflexive differentials.** For $X$ normal with smooth locus $j: X_{\mathrm{reg}} \hookrightarrow X$, set
$$\Omega^{[p]}_X := \big(\Omega^p_X\big)^{**} = j_*\Omega^p_{X_{\mathrm{reg}}}, \qquad \mathcal{T}_X = \big(\Omega^{[1]}_X\big)^{*}.$$
Freeness of $\mathcal{T}_X$ near a point $x$ means there exist derivations $D_1,\dots,D_n$ ($n=\dim X$) forming an $\mathcal{O}_{X,x}$-basis; equivalently the evaluation map $\mathcal{T}_X \otimes k(x) \to$ (Zariski tangent space) has an $n$-dimensional image spanned by a *global frame*, so $X$ carries a nowhere-vanishing vector field through $x$ in $n$ independent directions.

**Extension theorems** (the modern engine). For $\pi: \widetilde{X}\to X$ a log resolution,
$$\pi_*\Omega^p_{\widetilde{X}} \;\subseteq\; \Omega^{[p]}_X,$$
with equality for all $p$ when $X$ has klt or log canonical singularities (Greb–Kebekus–Kovács–Peternell 2011). Equality for $p=1$ is exactly what converts a free tangent sheaf into a lifting statement on $\widetilde{X}$.

**Discrepancies.** For $\pi$ with exceptional divisors $E_i$, $K_{\widetilde X} = \pi^*K_X + \sum a_i E_i$; $X$ is klt if all $a_i > -1$, log canonical if all $a_i \ge -1$. These classes bound the singularities for which extension theorems are currently available.

## 3. History & State of the Art (SOTA)

- **1960s.** Oscar Zariski raised the question; Joseph Lipman gave the first systematic treatment in *Free derivation modules on algebraic varieties*, Amer. J. Math. **87** (1965). Lipman proved two structural facts in characteristic $0$: (i) freeness of $\operatorname{Der}_k(R)$ implies $R$ is **normal**, reducing the conjecture to normal varieties; (ii) the conjecture holds in **dimension $\le 2$**.
- **1970s.** Scheja–Storch (*Math. Ann.* **197**, 1972) developed the analytic-algebra machinery for derivation modules of localizations, giving the hypersurface/analytic tools. Hochster (*J. Algebra* **47**, 1977) proved the **graded case**: a graded affine algebra over a characteristic-$0$ field with free derivation module is regular.
- **1980s.** Flenner (*Invent. Math.* **94**, 1988) settled the case of **normal isolated singularities in dimension $\ge 3$**, via extendability of differential forms across the singular point. Steenbrink–van Straten (1985) supplied related extension results for isolated hypersurface singularities.
- **2011.** Källström proved the conjecture for **local complete intersections** (*J. Algebra* **337**), using $D$-module and integrability arguments.
- **2014.** Two MMP-flavoured advances: Graf–Kovács proved it for **klt spaces** using an optimal $1$-form extension theorem (*Doc. Math.* **19**); Druel extended it to **log canonical spaces** (*Bull. LMS* **46**) via foliation theory.
- **2017.** Graf, *The Lipman–Zariski conjecture in low dimension* (*Math. Z.*): the conjecture holds for normal complex spaces whose **singular locus has dimension $\le 1$**, hence for **all normal complex threefolds**.
- **2021.** Kebekus–Schnell (*J. Amer. Math. Soc.* **34**) proved extension of holomorphic forms from the regular locus for klt spaces in full generality, strengthening the toolkit but not yet breaking the klt barrier for LZ.

No counterexample is known in characteristic $0$; counterexamples do exist in characteristic $p>0$, where derivation modules can be free on singular rings because $p$-th powers are annihilated by all derivations.

## 4. Partial Results / Verified Cases

The conjecture is a **theorem** in each of the following characteristic-$0$ settings:

| Class | Author, year |
|---|---|
| $\dim X \le 2$ (curves, surfaces) | Lipman, 1965 |
| Freeness $\Rightarrow$ normality (reduction step) | Lipman, 1965 |
| Graded affine algebras (cones, toric, quotient singularities) | Hochster, 1977 |
| Normal isolated singularities, $\dim X \ge 3$ | Flenner, 1988 |
| Local complete intersections (any dimension) | Källström, 2011 |
| klt singularities | Graf–Kovács, 2014 |
| Log canonical singularities | Druel, 2014 |
| $\dim \operatorname{Sing}(X) \le 1$; in particular all normal threefolds | Graf, 2017 |
| Quotient singularities $\mathbb{C}^n/G$, $G$ finite | covered by graded / klt cases |

Also known: the analytic and algebraic formulations agree for varieties, and freeness may be tested at closed points, so the problem is genuinely local.

## 5. Principal Obstacles

- **Duality erases torsion.** $\mathcal{T}_X$ is reflexive and depends only on $X$ in codimension $1$ plus reflexive hull data. Two varieties with very different singularities can have isomorphic tangent sheaves in codimension $2$, so no purely homological invariant of $\mathcal{T}_X$ (depth, Ext-vanishing, Auslander-type rigidity) has been shown to detect regularity.
- **Failure in characteristic $p$.** Any proof must be non-characteristic-free. This rules out standard commutative-algebra techniques that pass through reduction mod $p$ or tight closure, which is otherwise the strongest available machinery for detecting regularity (Kunz, Hochster–Huneke).
- **Extension theorems stop at log canonical.** Graf–Kovács and Druel convert freeness into "reflexive $1$-forms pull back to honest forms on a resolution". That equality $\pi_*\Omega^1_{\widetilde X} = \Omega^{[1]}_X$ is *false* for general normal singularities (e.g. cones over abelian varieties of large degree, non-lc cones), so the arguments collapse outside the MMP-friendly classes.
- **Non-isolated singularities.** Flenner's method integrates over links of an isolated point; with a positive-dimensional singular locus the local topology varies and the vanishing/extension estimates degrade. Graf's dimension-$\le 1$ singular locus result is exactly where induction on strata still terminates.
- **Frames are not integrable.** A free $\mathcal{T}_X$ gives a global frame $D_1,\dots,D_n$, but $[D_i,D_j]$ need not lie in a nice subsheaf; there is no Frobenius theorem to integrate the frame into a local chart, which is what would immediately give smoothness.

## 6. The Gap

Proven: LZ for $X$ normal with (a) $\dim X\le 3$, or (b) $\dim\operatorname{Sing} X \le 1$, or (c) $X$ log canonical, or (d) $X$ lci, or (e) $X$ graded, or (f) $X$ with isolated singularities.

Missing: a normal complex variety $X$ with $\dim X \ge 4$, singular locus of dimension $\ge 2$, and singularities **worse than log canonical** — e.g. a cone over a smooth projective variety with $-K$ not sufficiently positive, or a non-normal-crossings degeneration with non-lc centres. For such $X$ no version of the extension theorem
$$\pi_*\Omega^1_{\widetilde X} \;=\; \Omega^{[1]}_X$$
is known, and it genuinely fails. The precise step to cross: show that a **nowhere-vanishing frame of $\mathcal{T}_X$ by itself forces discrepancies $a_i \ge -1$** (i.e. freeness implies log canonicity), or find a substitute for the extension theorem that only uses the existence of $n$ independent global derivations. Either direction closes the gap; a counterexample would require constructing a non-lc singularity whose derivation module is free — currently no construction technique produces free derivation modules on non-lc germs.

## 7. Current Research (as of June 2026)

- **Bayreuth / Freiburg school (Graf, Kebekus, and collaborators).** Continued work on extension theorems for $1$-forms beyond klt, using Hodge modules and the Kebekus–Schnell machinery. The target is a "weak extension" statement adequate for LZ under freeness assumptions alone. *(frontier — verify)*
- **Foliation-theoretic route (Druel, Spicer, and the birational foliated MMP).** A free tangent sheaf is a rank-$n$ foliation with trivial determinant; recent progress on the MMP for foliations gives adjunction and canonical-bundle formulas that may be applied to non-lc bases. *(frontier — verify)*
- **$D$-module and Lie-algebroid approaches (Källström and successors).** Studying $\operatorname{Der}_k(R)$ as a Lie–Rinehart algebra: freeness plus integrability constraints on $[D_i,D_j]$ used to force the associated graded ring to be polynomial.
- **Characteristic-$p$ boundary.** Explicit study of which char-$p$ counterexamples lift, to identify the exact char-$0$ ingredient any proof must use (resolution vs. Hodge theory).
- **Computational search.** Macaulay2/Singular experiments computing $\operatorname{Der}$ of non-lc cones and determinantal singularities, checking minimal-generator counts against rank; no free examples found.

## 8. Future Work

1. **Prove "free $\Rightarrow$ log canonical".** This single implication, combined with Druel (2014), settles the conjecture completely. Suggested route: study the Rees/blow-up algebra generated by the frame and bound the discrepancy of exceptional divisors by the order of vanishing of $D_1\wedge\cdots\wedge D_n$.
2. **Codimension induction.** Extend Graf's $\dim\operatorname{Sing} X\le 1$ argument to $\dim\operatorname{Sing} X \le 2$ by cutting with general hyperplanes and controlling how freeness of $\mathcal{T}$ behaves under restriction — currently $\mathcal{T}_{X\cap H} \ne \mathcal{T}_X|_H$ in general.
3. **Non-normal and analytic cases.** Establish the reduced (non-normal) complex-space version uniformly; Lipman's normality reduction is algebraic and its analytic analogue for arbitrary complex spaces is not fully documented.
4. **Positive characteristic.** Formulate a corrected statement using Hasse–Schmidt (divided-power) derivations, where freeness of the full Hasse–Schmidt derivation module plausibly does characterize regularity.
5. **Search for counterexamples** among quotients of non-lc cones by finite groups and among Schubert-type determinantal varieties in dimension $\ge 4$.

## 9. Key References

- **[Foundational]** J. Lipman. *Free derivation modules on algebraic varieties.* American Journal of Mathematics **87** (1965), 874–898.
- **[Foundational]** G. Scheja, U. Storch. *Differentielle Eigenschaften der Lokalisierungen analytischer Algebren.* Mathematische Annalen **197** (1972), 137–170.
- **[Foundational]** M. Hochster. *The Zariski–Lipman conjecture in the graded case.* Journal of Algebra **47** (1977), 411–424.
- **[Classical]** H. Flenner. *Extendability of differential forms on non-isolated singularities.* Inventiones Mathematicae **94** (1988), 317–326.
- **[Classical]** J. Steenbrink, D. van Straten. *Extendability of holomorphic differential forms near isolated hypersurface singularities.* Abhandlungen aus dem Mathematischen Seminar der Universität Hamburg **55** (1985), 97–110.
- **[SOTA]** R. Källström. *The Zariski–Lipman conjecture for complete intersections.* Journal of Algebra **337** (2011), 169–180.
- **[SOTA]** P. Graf, S. J. Kovács. *An optimal extension theorem for 1-forms and the Lipman–Zariski conjecture.* Documenta Mathematica **19** (2014), 815–830.
- **[SOTA]** S. Druel. *The Zariski–Lipman conjecture for log canonical spaces.* Bulletin of the London Mathematical Society **46** (2014).
- **[SOTA]** P. Graf. *The Lipman–Zariski conjecture in low dimension.* Mathematische Zeitschrift (2017).
- **[Toolkit]** D. Greb, S. Kebekus, S. J. Kovács, T. Peternell. *Differential forms on log canonical spaces.* Publications Mathématiques de l'IHÉS **114** (2011), 87–169.
- **[Toolkit]** S. Kebekus, C. Schnell. *Extending holomorphic forms from the regular locus of a complex space to a resolution of singularities.* Journal of the American Mathematical Society **34** (2021), 315–368.
- **[Background]** E. Kunz. *Kähler Differentials.* Vieweg, Advanced Lectures in Mathematics, 1986.

## 10. Worked Example / Concrete Special Case

**The quadric cone $A_1$ surface singularity.** Let
$$X = V(xy - z^2) \subset \mathbb{C}^3, \qquad R = \mathbb{C}[x,y,z]/(xy-z^2).$$
$X$ is normal, $\dim X = 2$, singular exactly at the origin. Verify directly that $\mathcal{T}_X$ is *not* free, as the conjecture demands.

**Step 1 — presentation via the quotient.** $X \cong \mathbb{C}^2/\{\pm 1\}$ under $u,v \mapsto (x,y,z) = (u^2, v^2, uv)$, since $x y = u^2v^2 = z^2$ and the invariant ring is $\mathbb{C}[u^2,uv,v^2]$.

**Step 2 — compute derivations.** Because the quotient map is étale outside the origin and $\mathcal{T}_X$ is reflexive,
$$\operatorname{Der}_{\mathbb{C}}(R) \;=\; \operatorname{Der}_{\mathbb{C}}(\mathbb{C}[u,v])^{\mathbb{Z}/2}.$$
Write $D = f\partial_u + g\partial_v$. Invariance under $(u,v)\mapsto(-u,-v)$ forces $f,g$ to be **odd** polynomials. The odd part of $\mathbb{C}[u,v]$ is generated over the even part $R$ by $u$ and $v$. Hence
$$\operatorname{Der}_{\mathbb{C}}(R) \;=\; R\!\cdot\! u\partial_u \;+\; R\!\cdot\! v\partial_u \;+\; R\!\cdot\! u\partial_v \;+\; R\!\cdot\! v\partial_v .$$

**Step 3 — rank versus minimal generators.** The module has rank $2$ (generic rank $=\dim X$). But at the maximal ideal $\mathfrak{m}=(x,y,z)$ the four generators are minimal: modulo $\mathfrak{m}$, the odd part $\{u,v\}$ is a $2$-dimensional space, and each of the two "slots" $\partial_u,\partial_v$ contributes independently, giving
$$\dim_{\mathbb{C}} \operatorname{Der}_{\mathbb{C}}(R)\otimes_R R/\mathfrak{m} = 4 \;>\; 2 = \operatorname{rank}.$$
A free module of rank $2$ would need exactly $2$ minimal generators. So $\mathcal{T}_X$ is not free — consistent with the conjecture.

**Step 4 — the same in coordinates on $X$.** With $q = xy-z^2$, $q_x=y,\;q_y=x,\;q_z=-2z$, the derivations preserving $(q)$ include the Euler field $E = x\partial_x+y\partial_y+z\partial_z$ (with $E(q)=2q$) and the three "Hamiltonian" fields
$$D_{xy} = y\partial_y - x\partial_x, \quad D_{xz} = y\partial_z + 2z\partial_x, \quad D_{yz} = x\partial_z + 2z\partial_y,$$
each annihilating $q$. These four span $\mathcal{T}_X$; the syzygies among them are generated by relations of degree $1$ (e.g. $x\,D_{xz} + z\,(D_{xy}-E)\equiv 0 \bmod (q)$ up to normalization), confirming rank $2$ with $4$ generators.

**What the example shows.** Here $X$ is a graded cone with an isolated singularity and a quotient singularity — three separate proven cases (Hochster, Flenner, klt) apply, and all agree. The open problem is precisely that no known argument covers the analogue when $X$ is $4$-dimensional, has a $2$-dimensional singular locus, and is not log canonical, where the passage from "$4 > 2$ generators" to a general obstruction has no available proof mechanism.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*