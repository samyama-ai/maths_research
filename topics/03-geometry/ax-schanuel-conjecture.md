---
id: 03-geometry/ax-schanuel-conjecture
title: "Ax-Schanuel Conjecture"
topic: 03-geometry
status: partially-solved
first_added: 2026-09
last_reviewed: 2026-09
last_substantive_update: 2026-09
stale_since: ""
provenance: synthesized
---

# Ax-Schanuel Conjecture

> **Topic:** Algebraic & Differential Geometry · **ID:** `03-geometry/ax-schanuel-conjecture` · **Status:** partially-solved

## 1. Problem Statement / Conjecture

The Ax–Schanuel conjecture is the functional-transcendence counterpart of Schanuel's arithmetic conjecture. In its modern geometric form it asserts:

Let $S$ be a smooth connected complex algebraic variety, $\Omega$ a complex analytic space, and $\pi \colon \Omega \to S^{\mathrm{an}}$ a surjective, locally biholomorphic uniformization arising from geometry (the exponential of a semiabelian variety, the uniformization of a Shimura variety, or a period map of a variation of Hodge structure). Let
$$D \;=\; \{(u, \pi(u)) : u \in \Omega\} \;\subset\; \Omega \times S$$
be its graph, viewed inside $X \times S$ for a suitable algebraic $X \supseteq \Omega$ (or with $\Omega$ semialgebraic in a period domain). **Conjecture (Ax–Schanuel).** For every irreducible algebraic subvariety $V \subseteq X \times S$ and every irreducible complex-analytic component $U$ of $V \cap D$ satisfying the *atypicality* inequality
$$\dim U \;>\; \dim V - \dim S,$$
the projection $\mathrm{pr}_S(U)$ is contained in a **proper weakly special subvariety** of $S$.

Equivalently, in differential-algebraic language: unexpected algebraic relations between the coordinates of a point and its uniformizing coordinates occur only for structural (group-theoretic or Hodge-theoretic) reasons. A complete resolution requires either a proof valid for a general class of uniformizations (in particular for non-arithmetic quotients, arbitrary mixed period maps with derivatives, and general algebraic foliations), or a counterexample: an algebraic $V$ with an atypical component whose projection is Zariski-dense in $S$.

The constant-field analogue — **Schanuel's conjecture**: if $\lambda_1,\dots,\lambda_n \in \mathbb{C}$ are linearly independent over $\mathbb{Q}$ then
$$\operatorname{trdeg}_{\mathbb{Q}} \mathbb{Q}\big(\lambda_1,\dots,\lambda_n, e^{\lambda_1},\dots,e^{\lambda_n}\big) \;\ge\; n$$
— remains completely open and is the source of the name.

## 2. Mathematical Foundations

**Differential fields.** A differential field $(K, D)$ is a field with an additive $D \colon K \to K$ satisfying $D(ab) = aDb + bDa$. Its constants are $C_K = \{a : Da = 0\}$. The exponential relation is written differentially: $y \ne 0$ is an *exponential of* $x$ when
$$Dy \;=\; y\, Dx .$$

**Ax's theorem (1971).** Let $(K,D)$ have algebraically closed constant field $C$, and let $x_1,\dots,x_n,y_1,\dots,y_n \in K$ with $y_i \neq 0$ and $D y_i = y_i D x_i$. If $x_1,\dots,x_n$ are linearly independent over $\mathbb{Q}$ modulo $C$, then
$$\operatorname{trdeg}_C\, C(x_1,\dots,x_n,y_1,\dots,y_n) \;\ge\; n + \operatorname{rk}\big(D x_i\big),$$
where $\operatorname{rk}$ is the rank of the matrix of derivatives (rank $1$ for a single derivation with some $Dx_i \ne 0$). This is Schanuel's statement with $\mathbb{Q}$ replaced by $C$ and $\mathbb{C}$ by $K$.

**Geometric form for $\mathbb{G}_m^n$.** With $\exp \colon \mathbb{C}^n \to (\mathbb{C}^\times)^n$ and $D = \Gamma_{\exp} \subset \mathbb{C}^n \times (\mathbb{C}^\times)^n$, Ax's theorem says: if $U$ is a component of $V \cap D$ with $\dim U > \dim V - n$, then $\mathrm{pr}(U)$ lies in a coset of a proper subtorus — the weakly special subvarieties of $\mathbb{G}_m^n$ are exactly translates $g\cdot T$ of subtori.

**Weakly special subvarieties.** For $S = \Gamma \backslash \Omega$ a Shimura variety with $\Omega$ a Hermitian symmetric domain, weakly special subvarieties are images of $\Omega' \times \{y\}$ for $\Omega' \times \Omega'' \subseteq \Omega$ a totally geodesic factor. For $Y(1)^n = \mathbb{A}^n$ uniformized by $j\colon \mathbb{H}^n \to \mathbb{C}^n$, they are cut out by conditions $z_i = \gamma z_k$ with $\gamma \in \mathrm{GL}_2^+(\mathbb{Q})$ and $z_l = \text{const}$ — i.e. modular curves $\Phi_N(j(z_i), j(z_k)) = 0$ and constant coordinates.

**Atypicality.** Inside a smooth ambient of dimension $d$, two subvarieties of dimensions $a, b$ meet *typically* in dimension $a + b - d$. Ax–Schanuel is an *atypical intersection* principle: excess intersection with the leaf-space $D$ is never accidental. This places it in the Zilber–Pink circle of conjectures.

**Foliation formulation.** $D$ is a leaf of the algebraic foliation defined by the differential equation satisfied by $\pi$ (e.g. $y' = y$ for $\exp$; the Schwarzian equation $\mathrm{Sch}(z) + R(z)(z')^2 = 0$ for $j$). Ax–Schanuel then reads: leaves of these foliations have no atypical algebraic intersections beyond those forced by the symmetry group of the equation.

## 3. History & State of the Art (SOTA)

- **1960s.** Schanuel formulates his conjecture; it is first published in Lang, *Introduction to Transcendental Numbers* (1966). It implies the Lindemann–Weierstrass theorem, Baker's theorem, and the algebraic independence of $e$ and $\pi$.
- **1971.** James Ax proves the differential-field analogue for $\mathbb{G}_m^n$ (Annals of Math. 93), using formal-group/Kolchin-style arguments; 1972 extends to analytic subgroups of algebraic groups.
- **1998–2008.** Zilber's pseudo-exponentiation programme reformulates Ax–Schanuel model-theoretically; Pila–Zannier introduce the o-minimality/point-counting method for Manin–Mumford.
- **2011–2014.** Pila proves Ax–Lindemann–Weierstrass for $Y(1)^n$ and, with Tsimerman, for $\mathcal{A}_g$; these are the "$V$ algebraic in $\Omega$" special cases.
- **2016.** Pila–Tsimerman, *Ax–Schanuel for the $j$-function* (Duke Math. J. 165) — the first full Ax–Schanuel outside algebraic groups, including the derivatives $j', j''$.
- **2019.** Mok–Pila–Tsimerman prove Ax–Schanuel for all Shimura varieties (Annals 189). Bakker–Tsimerman prove it for arbitrary variations of pure Hodge structure (Invent. Math. 217).
- **2020.** Gao proves the mixed case for universal abelian varieties (Compositio 156); Casale–Freitag–Nagloo prove Ax–Lindemann with derivatives for genus-$0$ Fuchsian groups, including **non-arithmetic** ones (Annals 192).
- **2021–2024.** Chiu extends Ax–Schanuel with derivatives to mixed period mappings; Baldi–Klingler–Ullmo use Ax–Schanuel as the engine for the distribution of the Hodge locus (Invent. Math. 2024).

## 4. Partial Results / Verified Cases

| Setting | Status | Reference |
|---|---|---|
| $\mathbb{G}_m^n$, all $n$ | **Theorem** | Ax 1971 |
| Semiabelian varieties / analytic subgroups | **Theorem** | Ax 1972; Kirby 2009 |
| $j \colon \mathbb{H}^n \to \mathbb{C}^n$, with $j', j''$ | **Theorem** | Pila–Tsimerman 2016 |
| All Shimura varieties (pure, any dimension) | **Theorem** | Mok–Pila–Tsimerman 2019 |
| Variations of **pure** Hodge structure, any weight | **Theorem** | Bakker–Tsimerman 2019 |
| Universal abelian variety $\mathfrak{A}_g \to \mathcal{A}_g$ (mixed) | **Theorem** | Gao 2020 |
| Genus-$0$ Fuchsian groups, non-arithmetic, Ax–Lindemann with derivatives | **Theorem** | Casale–Freitag–Nagloo 2020 |
| Mixed period mappings with derivatives | **Theorem** (recent) | Chiu 2022–2024 |
| Schanuel's conjecture over $\mathbb{C}$, $n \ge 2$ | **Open** | — |
| Schanuel for $n=1$: $\lambda \ne 0 \Rightarrow \operatorname{trdeg} \ge 1$ | Trivially true (Hermite–Lindemann for algebraic $\lambda$) | — |
| General algebraic foliations / arbitrary ODEs | **Open** | Blázquez-Sanz–Casale–Freitag–Nagloo |

## 5. Principal Obstacles

- **The arithmetic case has no derivation.** Ax's proof differentiates a hypothetical minimal relation. Over $\mathbb{C}$ with $\lambda_i$ constants there is nothing to differentiate; Schanuel's conjecture for $n = 2$ already implies the algebraic independence of $e$ and $\pi$, far beyond current transcendence technology (Nesterenko's theorem gives only $\operatorname{trdeg}_{\mathbb{Q}}\mathbb{Q}(\pi, e^{\pi}, \Gamma(1/4)) = 3$).
- **Loss of group structure.** For $j$ and general period maps there is no algebraic group law, so the formal-group and Kolchin-logarithmic-derivative arguments that carry Ax's proof have no analogue. Proofs instead need o-minimality (definability of $\pi$ on a fundamental domain), volume/monodromy estimates, and — in Mok–Pila–Tsimerman — hyperbolic-analytic input (Mok's rigidity/asymptotic curvature arguments).
- **Definability fails outside arithmetic quotients.** The Peterzil–Starchenko definability of $\pi$ in $\mathbb{R}_{\mathrm{an},\exp}$ relies on a fundamental domain of finite complexity; for a general foliation or a general non-arithmetic uniformization no such tame structure is available.
- **Monodromy control.** The Bakker–Tsimerman and Mok–Pila–Tsimerman proofs need the monodromy of the ambient family to be large (a Zariski-density/Deligne–André normality statement). For arbitrary foliations there is no monodromy group at all, and the Galois-theoretic substitute (the Malgrange groupoid) is hard to compute.
- **Weakly special subvarieties are not defined in general.** For an arbitrary foliation the class of "expected" atypical loci is unknown, so the conjecture cannot even be stated without first solving a classification problem.

## 6. The Gap

Proven: Ax–Schanuel wherever the uniformization is either (a) the exponential of an algebraic group, or (b) an arithmetic/Hodge-theoretic period map admitting a definable fundamental domain and a large monodromy group. Conjectured: the same conclusion for *any* algebraically-defined leaf-space.

The exact barrier has two components:

1. **Structural.** Identify the right notion of "weakly special" for an arbitrary algebraic foliation — conjecturally the invariant subvarieties of the Malgrange groupoid. Without this, the atypicality dichotomy has no target.
2. **Analytic.** Replace definability-plus-point-counting by an intrinsic argument. The known proofs feed a lower bound on $\dim U$ into a counting theorem to produce many monodromy translates of $U$; one then contradicts algebraicity. No proof is known that survives the loss of either the tame fundamental domain or the monodromy.

For the arithmetic Schanuel conjecture the gap is total: no case with $n \ge 2$ and $\lambda_i$ not covered by Baker's theorem is known.

## 7. Current Research (as of June 2026)

- **Hodge loci and atypicality.** Baldi, Klingler, Ullmo (IMJ-PRG, Paris; HU Berlin) use Ax–Schanuel to prove that the Hodge locus of a $\mathbb{Z}$-VHS with large monodromy is algebraic unless the level is $\le 3$ (Invent. Math. 2024). Ongoing extensions to non-reduced and mixed settings. *(frontier — verify)*
- **Mixed and derivative-enhanced Ax–Schanuel.** K. C. T. Chiu's Ax–Schanuel with derivatives for mixed period mappings is being applied to Zilber–Pink for mixed Shimura varieties. *(frontier — verify)*
- **Differential-algebraic approach.** Blázquez-Sanz, Casale, Freitag, Nagloo (Universidad Nacional de Colombia; Rennes; UIC; CUNY) develop a proof strategy through the Malgrange groupoid and strong minimality of the generic fibres of the Schwarzian equation, aiming to remove o-minimality entirely.
- **Model theory / existential closedness.** Aslanyan, Eterović, Kirby (Bristol, UEA, Santiago) study Ax–Schanuel-with-existential-closedness for $j$ and for the Weierstrass $\wp$-function; uniform versions in families are actively pursued.
- **Effectivity.** Making Ax–Schanuel-driven Zilber–Pink bounds effective — via the Pila–Shankar–Tsimerman height machinery used for André–Oort — is a stated goal of several groups.

## 8. Future Work

- Formulate and prove Ax–Schanuel for a general algebraic foliation, with weakly special loci defined by the Malgrange groupoid.
- Prove Ax–Schanuel for uniformizations of non-arithmetic ball quotients and for Painlevé equations, where the Ax–Lindemann case is known but the full graph statement is not.
- Establish "Ax–Schanuel with derivatives" uniformly in algebraic families, a prerequisite for effective Zilber–Pink.
- Deduce further consequences: full Zilber–Pink for $\mathcal{A}_g$, the Zariski-density statements needed for André–Oort in mixed settings.
- On the arithmetic side, prove any nontrivial instance of Schanuel beyond Baker's theorem; Zilber's programme suggests attacking it through the categoricity of pseudo-exponential fields.

## 9. Key References

- **[Foundational]** J. Ax. *On Schanuel's conjectures.* Annals of Mathematics (2) **93** (1971), 252–268.
- **[Foundational]** J. Ax. *Some topics in differential algebraic geometry I: Analytic subgroups of algebraic groups.* American Journal of Mathematics **94** (1972), 1195–1204. [DOI](https://doi.org/10.2307/2373569)
- **[Foundational]** S. Lang. *Introduction to Transcendental Numbers.* Addison-Wesley, 1966.
- **[SOTA]** J. Pila, J. Tsimerman. *Ax–Schanuel for the $j$-function.* Duke Mathematical Journal **165** (2016), 2587–2605. [DOI](https://doi.org/10.1215/00127094-3620005)
- **[SOTA]** N. Mok, J. Pila, J. Tsimerman. *Ax–Schanuel for Shimura varieties.* Annals of Mathematics **189** (2019), 945–978. [DOI](https://doi.org/10.4007/annals.2019.189.3.7)
- **[SOTA]** B. Bakker, J. Tsimerman. *The Ax–Schanuel conjecture for variations of Hodge structures.* Inventiones mathematicae **217** (2019), 77–94. [DOI](https://doi.org/10.1007/s00222-019-00863-8)
- **[SOTA]** Z. Gao. *Mixed Ax–Schanuel for the universal abelian varieties and some applications.* Compositio Mathematica **156** (2020), 2263–2297. [DOI](https://doi.org/10.1112/s0010437x20007447)
- **[SOTA]** G. Casale, J. Freitag, J. Nagloo. *Ax–Lindemann–Weierstrass with derivatives and the genus 0 Fuchsian groups.* Annals of Mathematics **192** (2020), 721–765. [DOI](https://doi.org/10.4007/annals.2020.192.3.2)
- **[Recent]** G. Baldi, B. Klingler, E. Ullmo. *On the distribution of the Hodge locus.* Inventiones mathematicae **235** (2024), 441–487. [DOI](https://doi.org/10.1007/s00222-023-01226-0)
- **[Related]** J. Kirby. *The theory of the exponential differential equations of semiabelian varieties.* Selecta Mathematica **15** (2009), 445–486. [DOI](https://doi.org/10.1007/s00029-009-0001-7)
- **[Survey]** B. Klingler, E. Ullmo, A. Yafaev. *Bi-algebraic geometry and the André–Oort conjecture.* In *Algebraic Geometry: Salt Lake City 2015*, Proc. Sympos. Pure Math. **97.2**, AMS, 2018.
- **[Survey]** J. Pila. *Point-Counting and the Zilber–Pink Conjecture.* Cambridge Tracts in Mathematics 228, Cambridge University Press, 2022.

## 10. Worked Example / Concrete Special Case

**Claim ($n = 1$ case of Ax's theorem).** Let $(K, D)$ be a differential field with algebraically closed constants $C$, and let $x, y \in K$ with $y \neq 0$ and $Dy = y\,Dx$. If $Dx \neq 0$ then $x$ and $y$ are algebraically independent over $C$, i.e. $\operatorname{trdeg}_C C(x,y) = 2 = n + \operatorname{rk}(Dx)$.

*Proof.* Suppose not. Since $Dx \ne 0$, $x \notin C$, so $x$ is transcendental over $C$ and $y$ is algebraic over $C(x)$. Let
$$P(X,Y) \;=\; Y^d + a_{d-1}(X)Y^{d-1} + \cdots + a_0(X), \qquad a_i \in C(X),$$
be the monic minimal polynomial of $y$ over $C(X)$, of degree $d \ge 1$, so $P(x,y) = 0$.

Apply $D$, writing $a_i' = \frac{d a_i}{dX}$ and using $Dx \ne 0$, $Dy = y\,Dx$:
$$0 = D\big(P(x,y)\big) = Dx\left[\sum_{i=0}^{d} a_i'(x)\,y^{i} \;+\; \sum_{i=0}^{d} i\,a_i(x)\,y^{i}\right],$$
with $a_d = 1$. Dividing by $Dx \neq 0$ gives $Q(x,y) = 0$ where
$$Q(X,Y) \;=\; \sum_{i=0}^{d} \big(a_i'(X) + i\,a_i(X)\big) Y^{i}.$$
The coefficient of $Y^d$ in $Q$ is $a_d' + d\,a_d = 0 + d = d \neq 0$, so $\deg_Y Q = d$. Then $Q - d\,P$ vanishes at $(x,y)$ and has $Y$-degree $< d$; minimality of $P$ forces $Q = d\,P$. Comparing coefficients:
$$a_i' + i\,a_i \;=\; d\,a_i \quad \Longrightarrow \quad a_i' \;=\; (d - i)\,a_i \qquad (0 \le i < d).$$

Write $a_i = p/q$ in lowest terms with $p,q \in C[X]$. The relation $a_i' = c\, a_i$ with $c = d - i \ge 1$ a nonzero constant has no nonzero solution in $C(X)$: comparing degrees, if $a_i \in C[X]\setminus\{0\}$ then $\deg a_i' = \deg a_i - 1 < \deg a_i = \deg(c\,a_i)$; in general the only solutions of $u' = cu$ in a field of rational functions are $u = 0$ (the exponential $e^{cX}$ is not rational). Hence $a_i = 0$ for all $i < d$, so $P = Y^d$ and $y^d = 0$, contradicting $y \neq 0$. $\square$

**Reading it as atypical intersection.** Take $V \subset \mathbb{C} \times \mathbb{C}^\times$ an irreducible curve, $\dim V = 1$, $\dim S = 1$. A component $U$ of $V \cap \Gamma_{\exp}$ is atypical when $\dim U > 1 - 1 = 0$, i.e. $U$ is a curve, i.e. $V \subseteq \Gamma_{\exp}$ — an algebraic relation $P(x, e^x) = 0$. The proof above rules this out unless $x$ is constant, and constancy is exactly containment in the proper weakly special subvariety $\{pt\}$. Concretely: there is no nonzero polynomial $P$ with $P(z, e^z) \equiv 0$ on $\mathbb{C}$, the functional Hermite–Lindemann theorem.

---
*Part of the [Maths Research catalog](../../README.md). Schema: [TEMPLATE.md](../../TEMPLATE.md).*