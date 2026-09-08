---
id: 04-topology/kadomtsev-petviashvili-equation-and-novikov
title: "Kadomtsev-Petviashvili Equation and Novikov"
topic: 04-topology
status: solved-recently
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Kadomtsev–Petviashvili Equation and Novikov's Conjecture (Riemann–Schottky Problem)

> **Topic:** Topology & Knot Theory · **ID:** `04-topology/kadomtsev-petviashvili-equation-and-novikov` · **Status:** solved-recently

## 1. Problem Statement / Conjecture

Novikov's conjecture asks for a characterization of Jacobians of compact Riemann surfaces inside the space of all principally polarized abelian varieties (ppavs) by a *single* nonlinear PDE.

**Conjecture (Novikov, 1970s).** Let $B \in \mathbb{H}_g$ be a symmetric $g\times g$ complex matrix with $\operatorname{Im} B > 0$, and let $(X,\Theta) = (\mathbb{C}^g/(\mathbb{Z}^g + B\mathbb{Z}^g), \Theta)$ be the associated indecomposable ppav with Riemann theta function $\theta(z\mid B)$. Then $(X,\Theta)$ is the Jacobian of a smooth algebraic curve of genus $g$ **if and only if** there exist vectors $U,V,W \in \mathbb{C}^g$ with $U \neq 0$, and a constant $c\in\mathbb{C}$, such that
$$u(x,y,t) \;=\; 2\,\partial_x^2 \log \theta\big(Ux+Vy+Wt+Z \,\big|\, B\big) \;+\; c$$
solves the Kadomtsev–Petviashvili (KP) equation for every $Z \in \mathbb{C}^g$.

The "only if" direction is Krichever's construction (1977) and was known. The conjecture is the **"if"** direction: one equation of the KP hierarchy already cuts out the Jacobian locus $\mathcal{J}_g \subset \mathcal{A}_g$.

A complete proof must show that the finitely many theta-constant identities equivalent to the KP equation force the existence of a curve $\Gamma$ of genus $g$ and an isomorphism $(X,\Theta)\cong (JJ\Gamma,\Theta_\Gamma)$ — with **no** genericity, irreducibility, or non-degeneracy hypothesis on $U$ or on $(X,\Theta)$ beyond indecomposability.

**Status.** Proved by T. Shiota (*Invent. Math.* 1986). Extensions (the Welters trisecant conjecture, the Prym analogue) were settled by Krichever (2006, 2010) and Grushevsky–Krichever (2010). Several sharpened forms — an *effective* Schottky solution in genus $\ge 5$, the full Prym–Schottky problem, and the characterization of degenerate/singular loci — remain open.

## 2. Mathematical Foundations

**KP equation.** In the normalization used throughout the soliton literature,
$$\frac{3}{4}\,\sigma^2 u_{yy} \;=\; \partial_x\!\left(u_t - \tfrac{1}{4}\big(6uu_x + u_{xxx}\big)\right), \qquad \sigma^2 = \pm 1 .$$
Setting $u = 2\partial_x^2\log\tau$ gives the Hirota bilinear form
$$\big(D_x^4 + 3\sigma^2 D_y^2 - 4 D_x D_t + d\big)\,\tau\cdot\tau \;=\; 0,$$
where $D$ are Hirota derivatives, $D_x^m a\cdot b = \partial_s^m\, a(x+s)b(x-s)\big|_{s=0}$, and $d$ is a constant.

**Theta function.** For $B\in\mathbb{H}_g$,
$$\theta(z\mid B) \;=\; \sum_{n\in\mathbb{Z}^g} \exp\!\big(\pi i\, {}^t n B n + 2\pi i\, {}^t n z\big).$$
Substituting $\tau(x,y,t)=\theta(Ux+Vy+Wt+Z)$ into the bilinear form and expanding in the $\mathbb{Z}^g$-Fourier basis converts the PDE into a system of algebraic equations in the theta constants $\theta[\varepsilon](0\mid B)$ and the entries of $U,V,W$ — the **Novikov equations**. So the conjecture is a statement of pure algebraic geometry: these equations define $\overline{\mathcal{J}_g}$ (plus decomposable loci) in $\mathcal{A}_g$.

**Torelli / Schottky setting.** The Torelli map $\mathcal{M}_g \to \mathcal{A}_g$, $\Gamma\mapsto (J\Gamma,\Theta_\Gamma)$, is injective on isomorphism classes and has image of dimension $3g-3$, while $\dim \mathcal{A}_g = g(g+1)/2$. The two agree for $g\le 3$; for $g\ge 4$ the codimension is $\binom{g-2}{2}$. Determining the image is the **Riemann–Schottky problem**.

**Krichever correspondence.** Given a curve $\Gamma$ of genus $g$, a point $p\in\Gamma$, a local parameter $k^{-1}$, and a generic degree-$g$ divisor $D$, the Baker–Akhiezer function
$$\psi(x,y,t;P) \;=\; \frac{\theta\big(A(P)+Ux+Vy+Wt+Z\big)}{\theta\big(A(P)+Z\big)}\, e^{\,kx + k^2 y + k^3 t + \cdots}$$
where $A$ is the Abel map and $U,V,W$ are the $b$-period vectors of the normalized second-kind differentials with poles of order $2,3,4$ at $p$, satisfies
$$\big(\partial_y - \partial_x^2 - u\big)\psi = 0,\qquad \big(\partial_t - \partial_x^3 - \tfrac{3}{2}u\partial_x - w\big)\psi = 0,$$
whose compatibility is exactly KP. Hence every Jacobian yields a KP solution (Krichever 1977; Dubrovin–Matveev–Novikov 1976).

**Trisecant formulation.** The Kummer map $K:X\to \mathbb{P}^{2^g-1}$, $z\mapsto \big(\theta[\varepsilon](2z)\big)_\varepsilon$, sends $X/\pm$ to the Kummer variety $K(X)$. Fay's trisecant identity says $K(J\Gamma)$ carries a $3$-dimensional family of trisecant lines. **Welters' conjecture:** an indecomposable ppav is a Jacobian iff $K(X)$ admits a single trisecant line. The three degenerations of a trisecant (secant-tangent, inflection) correspond respectively to the KP, KdV-type and difference-equation flows; the fully degenerate case (a flex of $K(X)$) is equivalent to Novikov's conjecture.

## 3. History & State of the Art

- **1970.** Kadomtsev and Petviashvili derive the KP equation as a $(2{+}1)$-dimensional correction to KdV for weakly transverse ion-acoustic waves.
- **1974–76.** Its'–Matveev, Dubrovin, Novikov solve finite-gap KdV in theta functions; the survey of Dubrovin–Matveev–Novikov (1976) records Novikov's conjecture.
- **1977.** Krichever's algebro-geometric integration proves the "only if" direction for all $g$.
- **1982–84.** Gunning and Welters give geometric (secant/flex) criteria for Jacobians; Arbarello–De Concini (1984) show that the *whole* KP hierarchy characterizes Jacobians, as does Mulase (1984) via a cohomological/Sato-Grassmannian argument. Segal–Wilson (1985) give the loop-group framework.
- **1986.** **Shiota** proves Novikov's conjecture: one KP equation suffices.
- **1987–98.** Arbarello–De Concini give a second proof; Marini (1998) a geometric proof avoiding some of Shiota's analytic machinery.
- **2006–2010.** Krichever proves Welters' trisecant conjecture, first in the degenerate (flex) form, then in full.
- **2010.** Grushevsky–Krichever characterize Prym varieties by a pair of quadrisecants of the Kummer variety.

## 4. Partial Results / Verified Cases

- **$g \le 3$:** trivially true — $\mathcal{J}_g = \mathcal{A}_g$ (as $3g-3 = g(g+1)/2$ for $g=3$, with $g=1,2$ likewise), so every indecomposable ppav is a Jacobian and Krichever's construction gives the KP solution.
- **$g=4$:** the Schottky locus is the single Schottky–Igusa modular form $J^{(4)}$ of weight 8 (Igusa 1981: its zero locus in $\mathcal{A}_4$ is $\overline{\mathcal{J}_4}$ plus decomposables). KP-based and modular-form-based descriptions agree here, giving a fully *effective* answer.
- **Whole hierarchy:** Arbarello–De Concini (1984) and Mulase (1984) — a ppav whose theta function solves *all* KP-hierarchy flows is a Jacobian. Weaker hypothesis than Novikov's, proved earlier.
- **KdV reduction:** if $V=0$ (the flow degenerates to KdV), the corresponding statement characterizes hyperelliptic Jacobians (Krichever; Taimanov).
- **Full Novikov statement, all $g$:** Shiota (1986), with an added non-degeneracy assumption on $U$ removed in the same paper's final sections and re-proved cleanly by Arbarello–De Concini (1987) and Marini (1998).
- **Trisecant forms:** Krichever (2006) for the flex/degenerate case; Krichever (2010) for a general trisecant, assuming indecomposability.
- **Prym varieties:** Beauville–Debarre (1986) relate Prym–Schottky to quadrisecants; Grushevsky–Krichever (2010) prove a characterization of Pryms by a pair of quadrisecants, but only within an open subset (Prym–Tyurin/degeneracy issues persist).

## 5. Principal Obstacles

- **From formal to convergent.** The KP equation gives a *formal* pseudo-differential Lax operator; recovering a curve requires that the associated ring of commuting operators be finitely generated over a convergent, not merely formal, base. Shiota's proof needs delicate estimates on the Taylor coefficients of theta along the $U$-flow; naive Fourier or perturbative expansions diverge.
- **Orbit closure.** The linear flow $\{Ux : x\in\mathbb{C}\}$ may be dense in $X$ or may close up to a proper abelian subvariety $X_U \subsetneq X$. In the second case the Krichever-type reconstruction is applied on a lower-dimensional object and the descent back to $X$ fails without extra input. This is precisely the technical hypothesis that made Shiota's argument hardest and that Arbarello–De Concini and Marini re-treated.
- **Non-effectivity.** The proof is existential: it never produces explicit equations for $\overline{\mathcal{J}_g}\subset\mathcal{A}_g$ in terms of theta constants for $g\ge 5$. Eliminating $U,V,W,c$ from the Novikov equations is an elimination-theory problem of astronomical degree.
- **Failure of topological methods.** $\mathcal{J}_g$ and $\mathcal{A}_g$ have the same rational cohomology in low degrees, and the Torelli map is not a cohomological embedding in any useful sense; characteristic-class or surgery-theoretic invariants do not see the locus. The mapping class group action on $\mathbb{H}_g$ is the same $\mathrm{Sp}(2g,\mathbb{Z})$ action that acts on all of $\mathcal{A}_g$.
- **Boundary and singular loci.** For degenerate ppavs (products, or compactified boundary strata), trisecant/KP criteria acquire spurious solutions; controlling these is the main open technical difficulty in the Prym case.

## 6. The Gap

The original conjecture has no gap: Section 4 covers Section 1. The live boundary has moved to three refinements.

1. **Effectivity.** Proven: $\overline{\mathcal{J}_g}$ is the projection of the Novikov variety. Not proven: an explicit finite set of modular forms cutting out $\overline{\mathcal{J}_g}$ in $\mathcal{A}_g$ for any $g\ge 5$. The missing step is an elimination — or a new construction of Schottky-type forms from the KP $\tau$-function.
2. **Prym–Schottky.** Grushevsky–Krichever characterize Pryms among ppavs admitting a *symmetric* pair of quadrisecants and satisfying an openness condition. The gap is the degenerate stratum: whether a single quadrisecant, without genericity, forces a Prym.
3. **Higher-rank / abelian solutions.** Krichever's "abelian solutions" program conjectures that abelian solutions of KP correspond precisely to Jacobians of curves with an appropriate structure; the general case with non-reduced or reducible spectral data is unsettled.

## 7. Current Research (as of June 2026)

- **Effective Schottky forms.** Work descending from Grushevsky's slope/modular-form techniques seeks explicit equations in $g=5$; candidate forms exist but a proof that they cut out exactly $\overline{\mathcal{J}_5}$ is not available. *(frontier — verify)*
- **Tropical and non-archimedean analogues.** Tropical Schottky problem (Chan, Melody–Viviani, Kudo–Zhang directions): characterizing tropical Jacobians among tropical ppavs; the KP/theta machinery has partial tropical counterparts. *(frontier — verify)*
- **Real and integrable-systems side.** Kodama–Williams' totally non-negative Grassmannian classification of real regular KP solitons, and its extension to degenerate spectral curves, continues to generate a combinatorial picture of the "boundary" of the Jacobian picture.
- **Prym and Prym–Tyurin degenerations** (Krichever's school, HSE/Columbia; Grushevsky at Stony Brook).
- **Difference/discrete versions.** Characterizations via discrete Schrödinger equations and the Hirota difference equation (Krichever–Zabrodin), aimed at the quadrisecant statements.

## 8. Future Work

- Extract *computable* invariants from Shiota's proof: bound the degree of the elimination ideal for the Novikov equations in fixed $g$, then attempt $g=5$ with Gröbner/numerical algebraic geometry.
- Settle the single-quadrisecant Prym conjecture without genericity, which would complete the trisecant program one level up.
- Give a purely geometric proof of Shiota's theorem intrinsic to $\mathcal{A}_g$ — Marini's argument is a step; a proof using only the geometry of $\Theta$ and its singularities (as in Andreotti–Mayer, $\dim\operatorname{Sing}\Theta \ge g-4$) would connect two historically separate approaches.
- Develop the analogous characterization for Jacobians in positive characteristic, where the Sato Grassmannian arguments partly survive but theta-function analysis does not.

## 9. Key References

- **[Foundational]** B. B. Kadomtsev, V. I. Petviashvili. *On the stability of solitary waves in weakly dispersing media.* Soviet Physics Doklady **15** (1970), 539–541.
- **[Foundational]** B. A. Dubrovin, V. B. Matveev, S. P. Novikov. *Non-linear equations of Korteweg–de Vries type, finite-zone linear operators, and Abelian varieties.* Russian Mathematical Surveys **31**(1) (1976), 59–146. [DOI](https://doi.org/10.1070/rm1976v031n01abeh001446)
- **[Foundational]** I. M. Krichever. *Methods of algebraic geometry in the theory of non-linear equations.* Russian Mathematical Surveys **32**(6) (1977), 185–213. [DOI](https://doi.org/10.1070/rm1977v032n06abeh003862)
- **[Foundational]** E. Arbarello, C. De Concini. *On a set of equations characterizing Riemann matrices.* Annals of Mathematics **120** (1984), 119–140. [DOI](https://doi.org/10.2307/2007073)
- **[Foundational]** M. Mulase. *Cohomological structure in soliton equations and Jacobian varieties.* Journal of Differential Geometry **19** (1984), 403–430. [DOI](https://doi.org/10.4310/jdg/1214438685)
- **[Foundational]** G. E. Welters. *A criterion for Jacobi varieties.* Annals of Mathematics **120** (1984), 497–504. [DOI](https://doi.org/10.2307/1971084)
- **[Resolution]** T. Shiota. *Characterization of Jacobian varieties in terms of soliton equations.* Inventiones Mathematicae **83** (1986), 333–382. [DOI](https://doi.org/10.1007/bf01388967)
- **[Resolution]** E. Arbarello, C. De Concini. *Another proof of a conjecture of S. P. Novikov on periods of abelian integrals on Riemann surfaces.* Duke Mathematical Journal **54** (1987), 163–178. [DOI](https://doi.org/10.1215/s0012-7094-87-05412-3)
- **[SOTA / Recent]** I. Krichever. *Characterizing Jacobians via trisecants of the Kummer variety.* Annals of Mathematics **172** (2010), 485–516. [DOI](https://doi.org/10.4007/annals.2010.172.485)
- **[SOTA / Recent]** S. Grushevsky, I. Krichever. *Integrable discrete Schrödinger equations and a characterization of Prym varieties by a pair of quadrisecants.* Duke Mathematical Journal **152** (2010), 317–371. [DOI](https://doi.org/10.1215/00127094-2010-014)
- **[Related]** A. Beauville, O. Debarre. *Une relation entre deux approches du problème de Schottky.* Inventiones Mathematicae **86** (1986), 195–207. [DOI](https://doi.org/10.1007/bf01391500)
- **[Related]** G. Segal, G. Wilson. *Loop groups and equations of KdV type.* Publications Mathématiques de l'IHÉS **61** (1985), 5–65. [DOI](https://doi.org/10.1007/bf02698802)
- **[Related]** M. Marini. *A geometrical proof of Shiota's theorem on a conjecture of S. P. Novikov.* Compositio Mathematica **111** (1998), 305–322. [DOI](https://doi.org/10.1023/a:1000310019510)
- **[Survey]** S. Grushevsky. *The Schottky problem.* In *Current Developments in Algebraic Geometry*, MSRI Publications **59**, Cambridge University Press, 2012, 129–164. [DOI](https://doi.org/10.1017/9781139032766.007)
- **[Survey]** O. Debarre. *The Schottky problem: an update.* In *Complex Algebraic Geometry*, MSRI Publications **28**, Cambridge University Press, 1995, 57–64. [DOI](https://doi.org/10.1017/9781009701877.005)
- **[Book]** D. Mumford. *Tata Lectures on Theta II.* Birkhäuser, 1984 (reprint 2007, with Arbarello's appendix surveying the Schottky problem).

## 10. Worked Example / Concrete Special Case

**Genus 1: the elliptic KP (KdV) solution.**

Take $g=1$, $B=\tau \in \mathbb{H}_1$, $X=\mathbb{C}/(\mathbb{Z}+\tau\mathbb{Z})$. Every such $X$ *is* a Jacobian (of itself), so Novikov's criterion must be satisfiable. Construct the solution explicitly.

Let $\wp$ be the Weierstrass function of the lattice $\Lambda=\mathbb{Z}+\tau\mathbb{Z}$, satisfying
$$\wp'' = 6\wp^2 - \tfrac{1}{2}g_2 .$$
Set $\xi = x - ct$ and try $u = 2\wp(\xi) + a$ in the KdV equation $u_t = 6uu_x - u_{xxx}$ (the $y$-independent reduction of KP). Then

- $u_t = -c\,u_\xi = -2c\,\wp'(\xi)$,
- $u_{xxx} = 2\wp'''(\xi) = 2\cdot 12\wp\wp' = 24\wp\wp'$,
- $6uu_x = 6(2\wp+a)(2\wp') = 24\wp\wp' + 12a\wp'$.

So $6uu_x - u_{xxx} = 12a\,\wp'$, and matching with $u_t=-2c\wp'$ gives
$$a = -\frac{c}{6}, \qquad u(x,t) = 2\wp\!\left(x-ct\right) - \frac{c}{6}.$$
This is $y$-independent, so $u_{yy}=0$ and it solves the full KP equation with $V=0$.

**Theta form.** Using $\wp(z) = -\partial_z^2 \log\theta_1(z\mid\tau) + \eta$ for a lattice constant $\eta$, we get
$$u(x,y,t) = 2\,\partial_x^2 \log \theta\big(Ux+Vy+Wt+Z\big) + c',\qquad U=1,\; V=0,\; W=-c,$$
exactly the form required in Section 1 (the additive constant absorbs $\eta$ and $-c/6$).

**What the conjecture adds.** For $g=1$ this is vacuous: the Novikov equations impose no condition, because $\dim\mathcal{A}_1 = \dim\mathcal{M}_1 = 1$. The same is true for $g=2,3$. At $g=4$ the condition becomes a genuine hypersurface: $\dim\mathcal{A}_4 = 10$, $\dim\mathcal{J}_4 = 9$, and eliminating $(U,V,W,c)$ from the Novikov equations recovers — up to decomposable ppavs — the vanishing of Schottky's degree-16 polynomial in the theta constants,
$$J^{(4)}\big(\theta[\varepsilon](0\mid B)\big) = 0 .$$
Shiota's theorem is the statement that this pattern continues for every $g$: the existence of one KP solution of theta form is exactly the condition of being a Jacobian, even though no explicit polynomial like $J^{(4)}$ is known for $g\ge 5$.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*